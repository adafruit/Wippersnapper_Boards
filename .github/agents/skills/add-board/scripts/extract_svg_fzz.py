#!/usr/bin/env python3
"""Extract the breadboard SVG from a Fritzing .fzpz or .fzz archive.

A .fzpz (part) or .fzz (project) file is a ZIP archive that contains SVG
files for different views.  This script finds the breadboard SVG
(filename matching svg.breadboard.*.svg), copies it to the same directory
as ``image.svg``, and deletes the original archive.

Usage:
    python3 extract_svg_fzz.py <path/to/file.fzpz>
"""
import fnmatch
import pathlib
import sys
import zipfile

BREADBOARD_PATTERN = "svg.breadboard.*.svg"

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/file.fzpz|.fzz>")
        sys.exit(1)

    src = pathlib.Path(sys.argv[1])

    if not src.exists():
        print(f"Error: file not found: {src}")
        sys.exit(1)

    if src.suffix.lower() not in (".fzpz", ".fzz"):
        print(f"Error: expected a .fzpz or .fzz file, got '{src.suffix}'")
        sys.exit(1)

    try:
        zf = zipfile.ZipFile(src)
    except zipfile.BadZipFile:
        print(f"Error: {src} is not a valid ZIP archive")
        sys.exit(1)

    with zf:
        matches = [
            name for name in zf.namelist()
            if fnmatch.fnmatch(name.lower(), BREADBOARD_PATTERN)
        ]

        if not matches:
            print(f"Error: no breadboard SVG found in {src}")
            print(f"  Archive contents: {zf.namelist()}")
            sys.exit(1)

        if len(matches) > 1:
            print(f"Warning: multiple breadboard SVGs found, using first: {matches[0]}")

        svg_data = zf.read(matches[0])

    dest = src.parent / "image.svg"
    dest.write_bytes(svg_data)

    src.unlink()
    print(f"Extracted {matches[0]} -> {dest}")


if __name__ == "__main__":
    main()
