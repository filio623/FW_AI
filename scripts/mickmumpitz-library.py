#!/usr/bin/env python3
"""Sort Mickmumpitz Patreon downloads into a per-video library and write its index.

Inputs are a Patreon post manifest (JSON captured from the post API) and a YouTube
video list (TSV). Each post is matched to a video by its embedded YouTube link, by
an explicit override, or by sharing a publish date with a video post. Downloaded
files are matched to attachments by exact name and byte size, then moved into
<library>/<group>/<free|advanced>/. Runs as a dry run unless --apply is given.
Folders listed in <library>/_meta/removed_*.txt were pruned on purpose: nothing is
filed into them and the index marks their files as removed.
"""

import argparse
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

# Posts tied to a video by title rather than by an embed or a shared date.
POST_VIDEO_OVERRIDES = {
    "86637347": "-rfNOBGIiyk",  # Workflow Sheet #1, Turn your AI images into CG movies
    "87140285": "nTLuH-uRaZ8",  # NEW VIDEO: Generate entire movies with AI
    "87188990": "nTLuH-uRaZ8",  # Workflow Sheet #2
    "89199693": "PFybvdKH8hc",  # Workflow Sheet #3, 3D short films from 2D images
    "93011334": "mwWS8DyG_HU",  # Project files, AI music videos
    "93821351": "SHbY-6Vy53g",  # Bonus tutorial, 3D movie character workflow
    "98157565": "kTdIbU_guNQ",  # Free workflow, lip sync
    "98718056": "efxYEbF793c",  # Free workflow, any style
    "98818966": "efxYEbF793c",
    "98819681": "efxYEbF793c",
    "98832164": "efxYEbF793c",
    "112221865": "L0mhlsg8KyY",  # Project files, set extensions (posted a day after)
    "112224131": "L0mhlsg8KyY",
    "154405015": "o5ZqrVNoeiI",  # 3D model texturing guides (posted a day before)
    "154406422": "o5ZqrVNoeiI",
    "154406935": "o5ZqrVNoeiI",
}

ADVANCED_RE = re.compile(
    r"ADVANCED|AVANCED|WORLFLOWS|EXAMPLE FILES|PROJECT FILES|EXCLUSIVE|BETA|BONUS|SHEET|EARLY ACCESS",
    re.IGNORECASE,
)
YT_ID_RE = re.compile(r"(?:youtu\.be/|v=)([\w-]{11})")


def slug(text, limit=48):
    text = re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", text)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text[:limit].rstrip("-") or "untitled"


def load_videos(path):
    videos = {}
    lines = Path(path).read_text().splitlines()
    for line in lines[1:]:
        vid, duration, title, age = line.split("\t")
        videos[vid] = {"id": vid, "duration": duration, "title": title, "age": age}
    return videos


def group_posts(posts, videos):
    """Return {group_key: {"video": id or None, "date": str, "title": str, "posts": [...]}}."""
    post_video = {}
    for p in posts:
        m = YT_ID_RE.search(p.get("embed_url") or "")
        if m:
            post_video[p["post_id"]] = m.group(1)
    post_video.update(POST_VIDEO_OVERRIDES)

    video_dates = defaultdict(set)
    for p in posts:
        if p["post_id"] in post_video:
            video_dates[p["published"][:10]].add(post_video[p["post_id"]])

    groups = {}
    for p in sorted(posts, key=lambda p: p["published"]):
        date = p["published"][:10]
        vid = post_video.get(p["post_id"])
        if not vid and len(video_dates[date]) == 1:
            vid = next(iter(video_dates[date]))
        if vid:
            key = f"video:{vid}"
            if key not in groups:
                title = videos.get(vid, {}).get("title") or p["title"]
                groups[key] = {"video": vid, "date": date, "title": title, "posts": []}
            groups[key]["date"] = min(groups[key]["date"], date)
        else:
            key = f"post:{p['post_id']}"
            groups[key] = {"video": None, "date": date, "title": p["title"], "posts": []}
        groups[key]["posts"].append(p)

    for g in groups.values():
        name = f"{g['date']}_{slug(g['title'])}"
        if g["video"]:
            name += f"__{g['video']}"
            g["folder"] = name
        else:
            g["folder"] = f"_patreon-only/{name}__p{g['posts'][0]['post_id']}"
    return groups


def kind(post):
    return "advanced" if ADVANCED_RE.search(post["title"]) else "free"


def plan_files(groups):
    """Assign each unique attachment (name + size) to one destination folder."""
    placed = {}
    for g in sorted(groups.values(), key=lambda g: g["date"]):
        for p in sorted(g["posts"], key=lambda p: (kind(p) != "free", p["published"])):
            for a in p["attachments"]:
                k = (a["file_name"], a["size_bytes"])
                if k not in placed:
                    placed[k] = f"{g['folder']}/{kind(p)}/{a['file_name']}"
    return placed


def find_source(name, size, sources):
    stem, dot, ext = name.rpartition(".")
    pattern = re.compile(re.escape(stem) + r"( \(\d+\))?" + re.escape(dot + ext) + "$")
    for src in sources:
        for f in src.iterdir():
            if f.is_file() and pattern.match(f.name) and f.stat().st_size == size:
                return f
    return None


def human(n):
    for unit, div in (("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if n >= div:
            return f"{n / div:.1f} {unit}"
    return f"{n} B"


def load_removed(library):
    removed = []
    for f in sorted((library / "_meta").glob("removed_*.txt")):
        removed += [line.strip() + "/" for line in f.read_text().splitlines() if line.strip()]
    return removed


def write_index(path, groups, videos, placed, library, removed):
    lines = [
        "# Mickmumpitz Workflow Library Index",
        "",
        "Generated by `scripts/mickmumpitz-library.py`. Paths are relative to the library root.",
        "Files marked removed were pruned as obsolete; their folders are listed in `_meta/removed_*.txt`.",
        "",
    ]
    linked = set()
    for g in sorted(groups.values(), key=lambda g: g["date"], reverse=True):
        if g["video"]:
            linked.add(g["video"])
            head = f"## {g['date']} · {g['title']}"
            yt = f"https://youtu.be/{g['video']}"
        else:
            head = f"## {g['date']} · {g['title']} (Patreon only)"
            yt = None
        lines += [head, ""]
        if yt:
            lines.append(f"- YouTube: [{g['video']}]({yt})")
        for p in sorted(g["posts"], key=lambda p: p["published"]):
            lines.append(f"- Patreon ({kind(p)}): [{p['title'].strip()}]({p['url']})")
            for a in p["attachments"]:
                rel = placed[(a["file_name"], a["size_bytes"])]
                if (library / rel).exists():
                    mark = ""
                elif rel.startswith(tuple(removed)):
                    mark = " — removed as obsolete"
                else:
                    mark = " — not downloaded"
                lines.append(f"  - `{rel}` ({human(a['size_bytes'])}){mark}")
        lines.append("")
    unlinked = [v for v in videos.values() if v["id"] not in linked]
    if unlinked:
        lines += ["## Videos With No Patreon Files", ""]
        for v in unlinked:
            lines.append(f"- [{v['title']}](https://youtu.be/{v['id']}) · {v['duration']} · {v['age']} ago")
        lines.append("")
    path.write_text("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--videos", required=True)
    ap.add_argument("--library", required=True)
    ap.add_argument("--source", action="append", default=[], help="folder to pull downloads from")
    ap.add_argument("--apply", action="store_true", help="move files; default is a dry run")
    args = ap.parse_args()

    posts = json.loads(Path(args.manifest).read_text())["posts"]
    videos = load_videos(args.videos)
    library = Path(args.library)
    sources = [Path(s) for s in args.source]

    groups = group_posts(posts, videos)
    placed = plan_files(groups)
    removed = load_removed(library)

    moved = present = missing = 0
    for (name, size), rel in sorted(placed.items(), key=lambda kv: kv[1]):
        dest = library / rel
        if dest.exists():
            present += 1
            continue
        if rel.startswith(tuple(removed)):
            continue
        src = find_source(name, size, sources)
        if not src:
            missing += 1
            continue
        print(f"{'move' if args.apply else 'would move'}: {src} -> {rel}")
        if args.apply:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), dest)
        moved += 1

    if args.apply:
        write_index(library / "INDEX.md", groups, videos, placed, library, removed)
    print(f"groups={len(groups)} files={len(placed)} moved={moved} already={present} missing={missing}")


if __name__ == "__main__":
    main()
