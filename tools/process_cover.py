#!/usr/bin/env python3
"""Prepare a book cover for the website.

Takes a full-size cover image, makes the two web sizes, strips all existing
metadata (including AI-tool provenance), and embeds the brand string.

Usage:
    python3 tools/process_cover.py path/to/cover_front.png newyork

That writes images/cover-newyork.jpg (800x1200) and images/cover-newyork-sm.jpg
(400x600). Requires Pillow:  pip install Pillow

Run it from the _website folder.
"""
import sys
from PIL import Image

BRAND = "The Adventures of Dino and Benny - dinobenny.com"

def brand_exif():
    e = Image.Exif()
    e[315] = BRAND      # Artist
    e[33432] = BRAND    # Copyright
    e[270] = BRAND      # ImageDescription
    return e.tobytes()

def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src, slug = sys.argv[1], sys.argv[2]
    im = Image.open(src).convert('RGB')
    for size, suffix in [((800, 1200), ''), ((400, 600), '-sm')]:
        out = f'images/cover-{slug}{suffix}.jpg'
        copy = im.resize(size, Image.LANCZOS)
        copy.info = {}
        copy.save(out, quality=85, optimize=True, exif=brand_exif())
        print('wrote', out)

if __name__ == '__main__':
    main()
