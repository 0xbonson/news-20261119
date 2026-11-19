"""Draw the world map the front page uses, with a numbered pin for each story.

Land comes from Natural Earth 110m admin-0 countries (public domain), fetched
once and cached beside this script; the repository keeps only the rendered
PNG. Run from the repository root:

    python3 tools/make_map.py
"""
import json
import math
import os
import urllib.request

from PIL import Image, ImageDraw, ImageFont

import stories

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(HERE, ".cache")
GEO = os.path.join(CACHE, "ne_110m_admin_0_countries.geojson")
OUT = os.path.join(ROOT, "assets", "map.png")

W, H = 660, 330
OCEAN = (233, 238, 240)
LAND = (226, 218, 199)
COAST = (203, 192, 168)
PIN = (176, 38, 46)
PIN_RING = (255, 255, 255)
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def project(lon, lat):
    return (lon + 180.0) / 360.0 * W, (90.0 - lat) / 180.0 * H


def load_geojson():
    if not os.path.exists(GEO):
        os.makedirs(CACHE, exist_ok=True)
        url = (
            "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master"
            "/geojson/ne_110m_admin_0_countries.geojson"
        )
        urllib.request.urlretrieve(url, GEO)
    with open(GEO) as handle:
        return json.load(handle)


def rings(geometry):
    kind = geometry["type"]
    if kind == "Polygon":
        return [geometry["coordinates"]]
    if kind == "MultiPolygon":
        return geometry["coordinates"]
    return []


def main():
    geo = load_geojson()
    image = Image.new("RGB", (W, H), OCEAN)
    draw = ImageDraw.Draw(image)

    for feature in geo["features"]:
        for polygon in rings(feature["geometry"]):
            for ring in polygon:
                points = [project(lon, lat) for lon, lat in ring]
                if len(points) < 3:
                    continue
                draw.polygon(points, fill=LAND, outline=COAST)

    font = ImageFont.truetype(FONT_PATH, 13)
    for story in stories.HEROES + stories.CARDS:
        lat, lon = story["pin"]
        x, y = project(lon, lat)
        if not (0 <= x < W and 0 <= y < H):
            continue
        draw.ellipse(
            [x - 11, y - 11, x + 11, y + 11], fill=PIN_RING, outline=PIN, width=2
        )
        draw.ellipse([x - 8, y - 8, x + 8, y + 8], fill=PIN)
        label = str(story["no"])
        box = draw.textbbox((0, 0), label, font=font)
        draw.text(
            (x - (box[2] - box[0]) / 2, y - (box[3] - box[1]) / 2 - 1),
            label,
            font=font,
            fill=(255, 255, 255),
        )

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    image.save(OUT, optimize=True)
    print("wrote", OUT, image.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
