"""Build the front page for 19 November 2026 and render it to entry.png.

The page is one 1024x1024 sheet of newsprint: a masthead, three lead stories
drawn in flat colour, nine more with a small drawing each, a world map with a
pin on every story, and the rest of the day's news in two columns.

    python3 tools/build_page.py

writes entry.html, renders it with headless Chrome and leaves entry.png at the
repository root. assets/map.png comes from tools/make_map.py.
"""
import os
import subprocess
import sys

from PIL import Image

import stories

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HTML = os.path.join(ROOT, "entry.html")
PNG = os.path.join(ROOT, "entry.png")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

INK = "#15171c"
PAPER = "#f7f3e9"
RULE = "#15171c"
MUTED = "#5b5f68"
ACCENT = "#a8232e"

REGION_COLOR = {
    "Asia": "#a8232e",
    "Middle East": "#c2641c",
    "Europe": "#5b3a8e",
    "Africa": "#10705a",
    "United States": "#1b5e93",
    "Americas": "#1b5e93",
    "Global": "#3f434b",
    "South America": "#1b7a6b",
    "Oceania": "#2b6fa8",
    "Culture": "#8a2b5f",
    "Arts": "#8a2b5f",
}


def esc(text):
    return (
        text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )


def art_summit(w, h):
    def flag(x, kind):
        fw, fh = w * 0.20, h * 0.30
        y = h * 0.14
        parts = []
        if kind == "us":
            for i in range(7):
                parts.append(
                    f'<rect x="{x:.1f}" y="{y + i * fh / 7:.1f}" width="{fw:.1f}" '
                    f'height="{fh / 7:.1f}" fill="#b3202a"/>'
                )
            parts.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{fw * 0.42:.1f}" '
                f'height="{fh * 0.55:.1f}" fill="#1c3f77"/>'
            )
        elif kind == "cn":
            parts.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{fw:.1f}" height="{fh:.1f}" fill="#d02a1f"/>'
            )
            parts.append(
                f'<path d="M{x + fw * 0.18:.1f} {y + fh * 0.16:.1f} l{fw * 0.11:.1f} '
                f'{fh * 0.13:.1f} l{-fw * 0.03:.1f} {fh * 0.16:.1f} l{-fh * 0.12:.1f} '
                f'{-fh * 0.05:.1f} l{fh * 0.12:.1f} {fh * 0.05:.1f} '
                f'{-fh * 0.12:.1f} {fh * 0.05:.1f} z" fill="#ffd24a"/>'
            )
        else:
            parts.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{fw:.1f}" height="{fh:.1f}" fill="#ffffff"/>'
            )
            parts.append(
                f'<rect x="{x:.1f}" y="{y + fh / 3:.1f}" width="{fw:.1f}" height="{fh / 3:.1f}" fill="#1f4e9c"/>'
            )
            parts.append(
                f'<rect x="{x:.1f}" y="{y + 2 * fh / 3:.1f}" width="{fw:.1f}" height="{fh / 3:.1f}" fill="#c8323c"/>'
            )
        parts.append(
            f'<circle cx="{x + fw / 2:.1f}" cy="{y + fh:.1f}" r="{w * 0.012:.1f}" fill="#2b2b2b"/>'
        )
        parts.append(
            f'<rect x="{x + fw / 2 - 1:.1f}" y="{y + fh:.1f}" width="2" height="{h * 0.16:.1f}" fill="#2b2b2b"/>'
        )
        return "".join(parts)

    skyline = []
    x = w * 0.04
    while x < w * 0.96:
        bw = w * 0.055
        bh = h * (0.12 + 0.05 * ((int(x) // 7) % 3))
        skyline.append(
            f'<rect x="{x:.1f}" y="{h * 0.86 - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="#d9d2c0"/>'
        )
        x += bw + w * 0.012
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#eef3f6"/>'
        + "".join(skyline)
        + flag(w * 0.16, "us")
        + flag(w * 0.40, "cn")
        + flag(w * 0.64, "ru")
        + f'<rect x="0" y="{h * 0.86:.1f}" width="{w}" height="{h * 0.14:.1f}" fill="#c8bda6"/>'
        + f'<rect x="{w * 0.30:.1f}" y="{h * 0.795:.1f}" width="{w * 0.40:.1f}" height="{h * 0.07:.1f}" fill="#a8232e"/>'
        + f'<text x="{w * 0.5:.1f}" y="{h * 0.845:.1f}" font-family="Arial" font-size="{h * 0.052:.1f}" '
        f'font-weight="700" fill="#f7f3e9" text-anchor="middle" letter-spacing="1">APEC</text>'
    )
    return body


def art_gaza(w, h):
    blocks = []
    x = w * 0.02
    i = 0
    while x < w * 0.98:
        bw = w * 0.085
        bh = h * (0.18 + 0.10 * (i % 4))
        blocks.append(
            f'<rect x="{x:.1f}" y="{h * 0.80 - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="#8d8375"/>'
        )
        for wy in range(2):
            for wx in range(2):
                blocks.append(
                    f'<rect x="{x + bw * (0.22 + 0.42 * wx):.1f}" y="{h * 0.80 - bh + bh * (0.25 + 0.4 * wy):.1f}" '
                    f'width="{bw * 0.16:.1f}" height="{bh * 0.14:.1f}" fill="#f4d9a0"/>'
                )
        x += bw + w * 0.015
        i += 1
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#e7c98f"/>'
        f'<circle cx="{w * 0.80:.1f}" cy="{h * 0.22:.1f}" r="{h * 0.10:.1f}" fill="#f6e3b6"/>'
        + "".join(blocks)
        + f'<ellipse cx="{w * 0.30:.1f}" cy="{h * 0.55:.1f}" rx="{w * 0.20:.1f}" ry="{h * 0.16:.1f}" fill="#d9c3a3" opacity="0.75"/>'
        + f'<ellipse cx="{w * 0.62:.1f}" cy="{h * 0.46:.1f}" rx="{w * 0.14:.1f}" ry="{h * 0.12:.1f}" fill="#e0cdaf" opacity="0.6"/>'
        + f'<rect x="0" y="{h * 0.80:.1f}" width="{w}" height="{h * 0.20:.1f}" fill="#b9a98d"/>'
        + f'<path d="M0 {h * 0.86:.1f} L{w * 0.25:.1f} {h * 0.79:.1f} L{w * 0.55:.1f} {h * 0.87:.1f} '
        f'L{w * 0.80:.1f} {h * 0.81:.1f} L{w} {h * 0.88:.1f} L{w} {h} L0 {h} z" fill="#a9977a"/>'
    )
    return body


def art_ipo(w, h):
    bars = ""
    heights = [0.24, 0.38, 0.32, 0.55, 0.68, 0.86]
    for i, bh in enumerate(heights):
        bw = w * 0.095
        x = w * 0.10 + i * w * 0.135
        bars += (
            f'<rect x="{x:.1f}" y="{h * (0.86 - bh):.1f}" width="{bw:.1f}" height="{h * bh:.1f}" fill="#2f6f9f"/>'
        )
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#0f2740"/>'
        f'<path d="M0 {h * 0.86:.1f} L{w} {h * 0.86:.1f}" stroke="#3c6c96" stroke-width="1.5"/>'
        + bars
        + f'<path d="M{w * 0.09:.1f} {h * 0.56:.1f} L{w * 0.28:.1f} {h * 0.42:.1f} L{w * 0.45:.1f} '
        f'{h * 0.50:.1f} L{w * 0.62:.1f} {h * 0.26:.1f} L{w * 0.84:.1f} {h * 0.12:.1f}" fill="none" '
        f'stroke="#f2c14e" stroke-width="{w * 0.012:.1f}" stroke-linecap="round"/>'
        + f'<path d="M{w * 0.86:.1f} {h * 0.10:.1f} l-{w * 0.02:.1f} {h * 0.13:.1f} l-{w * 0.13:.1f} '
        f'-{h * 0.03:.1f} z" fill="#f2c14e"/>'
        + f'<circle cx="{w * 0.86:.1f}" cy="{h * 0.30:.1f}" r="{w * 0.085:.1f}" fill="#f2c14e" opacity="0.18"/>'
        + f'<text x="{w * 0.86:.1f}" y="{h * 0.345:.1f}" font-family="Georgia" font-size="{w * 0.10:.1f}" '
        f'font-weight="700" fill="#f2c14e" text-anchor="middle">$</text>'
    )
    return body


def art_bridge(w, h):
    deck_y = h * 0.62
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#cfe0ea"/>'
        f'<rect x="0" y="{h * 0.74:.1f}" width="{w}" height="{h * 0.26:.1f}" fill="#3f6f8f"/>'
        f'<path d="M0 {h * 0.74:.1f} L{w} {h * 0.74:.1f}" stroke="#2f5876" stroke-width="1.2"/>'
        f'<rect x="{w * 0.12:.1f}" y="{deck_y - h * 0.30:.1f}" width="{w * 0.035:.1f}" height="{h * 0.30:.1f}" fill="#5d5a54"/>'
        f'<rect x="{w * 0.66:.1f}" y="{deck_y - h * 0.30:.1f}" width="{w * 0.035:.1f}" height="{h * 0.30:.1f}" fill="#5d5a54"/>'
        f'<rect x="{w * 0.03:.1f}" y="{deck_y:.1f}" width="{w * 0.43:.1f}" height="{h * 0.06:.1f}" fill="#6d6a62"/>'
        f'<rect x="{w * 0.54:.1f}" y="{deck_y:.1f}" width="{w * 0.43:.1f}" height="{h * 0.06:.1f}" fill="#6d6a62"/>'
        f'<path d="M{w * 0.46:.1f} {deck_y - h * 0.02:.1f} l{w * 0.04:.1f} {-h * 0.16:.1f} '
        f'l{w * 0.03:.1f} {h * 0.10:.1f} l{w * 0.04:.1f} {-h * 0.12:.1f} l{w * 0.03:.1f} {h * 0.18:.1f} z" fill="#c25b23"/>'
        f'<ellipse cx="{w * 0.50:.1f}" cy="{deck_y - h * 0.28:.1f}" rx="{w * 0.10:.1f}" ry="{h * 0.10:.1f}" fill="#9c9a95" opacity="0.7"/>'
        f'<ellipse cx="{w * 0.56:.1f}" cy="{deck_y - h * 0.34:.1f}" rx="{w * 0.07:.1f}" ry="{h * 0.07:.1f}" fill="#b9b7b2" opacity="0.6"/>'
    )
    return body


def art_game(w, h):
    sky = ""
    for i in range(12):
        bw = w * 0.06
        x = i * bw + w * 0.01
        bh = h * (0.18 + 0.16 * ((i * 5) % 3))
        sky += (
            f'<rect x="{x:.1f}" y="{h * 0.72 - bh:.1f}" width="{bw * 0.86:.1f}" height="{bh:.1f}" fill="#241f3a"/>'
            f'<rect x="{x + bw * 0.2:.1f}" y="{h * 0.72 - bh + bh * 0.3:.1f}" width="{bw * 0.2:.1f}" '
            f'height="{bh * 0.12:.1f}" fill="#ff6ec7"/>'
        )
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#2b1d4d"/>'
        f'<circle cx="{w * 0.80:.1f}" cy="{h * 0.22:.1f}" r="{h * 0.11:.1f}" fill="#ff7bd0"/>'
        + sky
        + f'<rect x="0" y="{h * 0.72:.1f}" width="{w}" height="{h * 0.28:.1f}" fill="#191233"/>'
        + f'<rect x="{w * 0.18:.1f}" y="{h * 0.44:.1f}" width="{w * 0.64:.1f}" height="{h * 0.22:.1f}" rx="{h * 0.10:.1f}" fill="#e8e4f2"/>'
        + f'<circle cx="{w * 0.33:.1f}" cy="{h * 0.55:.1f}" r="{h * 0.030:.1f}" fill="#3b2f5c"/>'
        + f'<circle cx="{w * 0.67:.1f}" cy="{h * 0.55:.1f}" r="{h * 0.030:.1f}" fill="#3b2f5c"/>'
        + f'<rect x="{w * 0.44:.1f}" y="{h * 0.51:.1f}" width="{w * 0.12:.1f}" height="{h * 0.035:.1f}" rx="{h * 0.015:.1f}" fill="#3b2f5c"/>'
        + f'<rect x="{w * 0.40:.1f}" y="{h * 0.575:.1f}" width="{w * 0.20:.1f}" height="{h * 0.028:.1f}" rx="{h * 0.012:.1f}" fill="#3b2f5c"/>'
    )
    return body


def art_podium(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#dfe8f2"/>'
        f'<path d="M{w * 0.5:.1f} {h * 0.18:.1f} a{w * 0.14:.1f} {h * 0.14:.1f} 0 0 1 {w * 0.14:.1f} {h * 0.16:.1f} '
        f'h-{w * 0.28:.1f} z" fill="#f4f1e8"/>'
        f'<rect x="{w * 0.30:.1f}" y="{h * 0.36:.1f}" width="{w * 0.40:.1f}" height="{h * 0.30:.1f}" fill="#f4f1e8"/>'
        f'<rect x="{w * 0.22:.1f}" y="{h * 0.66:.1f}" width="{w * 0.56:.1f}" height="{h * 0.07:.1f}" fill="#e2ddd0"/>'
        f'<rect x="{w * 0.16:.1f}" y="{h * 0.73:.1f}" width="{w * 0.68:.1f}" height="{h * 0.07:.1f}" fill="#d3cdbd"/>'
        f'<rect x="{w * 0.10:.1f}" y="{h * 0.80:.1f}" width="{w * 0.80:.1f}" height="{h * 0.07:.1f}" fill="#c2bba8"/>'
        f'<rect x="{w * 0.24:.1f}" y="{h * 0.60:.1f}" width="{w * 0.52:.1f}" height="{h * 0.035:.1f}" fill="#a8232e"/>'
    )
    return body


def art_coins(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#eef3e6"/>'
        f'<ellipse cx="{w * 0.30:.1f}" cy="{h * 0.72:.1f}" rx="{w * 0.16:.1f}" ry="{h * 0.06:.1f}" fill="#c9a227"/>'
        f'<ellipse cx="{w * 0.30:.1f}" cy="{h * 0.62:.1f}" rx="{w * 0.16:.1f}" ry="{h * 0.06:.1f}" fill="#e0b93a"/>'
        f'<ellipse cx="{w * 0.30:.1f}" cy="{h * 0.52:.1f}" rx="{w * 0.16:.1f}" ry="{h * 0.06:.1f}" fill="#f0d066"/>'
        f'<text x="{w * 0.30:.1f}" y="{h * 0.56:.1f}" font-family="Georgia" font-size="{w * 0.16:.1f}" '
        f'font-weight="700" fill="#8a6d16" text-anchor="middle">€</text>'
        f'<path d="M{w * 0.62:.1f} {h * 0.86:.1f} L{w * 0.62:.1f} {h * 0.30:.1f}" stroke="#7a8b3f" stroke-width="{w * 0.015:.1f}"/>'
        f'<path d="M{w * 0.62:.1f} {h * 0.42:.1f} q{w * 0.12:.1f} {-h * 0.10:.1f} {w * 0.16:.1f} {h * 0.02:.1f}" '
        f'fill="none" stroke="#7a8b3f" stroke-width="{w * 0.012:.1f}"/>'
        f'<path d="M{w * 0.62:.1f} {h * 0.55:.1f} q{w * 0.12:.1f} {-h * 0.10:.1f} {w * 0.16:.1f} {h * 0.02:.1f}" '
        f'fill="none" stroke="#7a8b3f" stroke-width="{w * 0.012:.1f}"/>'
        f'<path d="M{w * 0.62:.1f} {h * 0.68:.1f} q{w * 0.12:.1f} {-h * 0.10:.1f} {w * 0.16:.1f} {h * 0.02:.1f}" '
        f'fill="none" stroke="#7a8b3f" stroke-width="{w * 0.012:.1f}"/>'
    )
    return body


def art_palette(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#f3ece2"/>'
        f'<path d="M{w * 0.18:.1f} {h * 0.62:.1f} a{w * 0.28:.1f} {h * 0.28:.1f} 1 1 1 {w * 0.46:.1f} '
        f'{-h * 0.34:.1f} a{w * 0.20:.1f} {h * 0.16:.1f} 0 0 0 {-w * 0.36:.1f} {h * 0.06:.1f} '
        f'a{w * 0.26:.1f} {h * 0.24:.1f} 0 0 1 {-w * 0.10:.1f} {h * 0.28:.1f} z" fill="#e3c98f"/>'
        f'<circle cx="{w * 0.30:.1f}" cy="{h * 0.48:.1f}" r="{w * 0.055:.1f}" fill="#a8232e"/>'
        f'<circle cx="{w * 0.42:.1f}" cy="{h * 0.38:.1f}" r="{w * 0.05:.1f}" fill="#1b5e93"/>'
        f'<circle cx="{w * 0.54:.1f}" cy="{h * 0.44:.1f}" r="{w * 0.045:.1f}" fill="#e0b93a"/>'
        f'<circle cx="{w * 0.38:.1f}" cy="{h * 0.60:.1f}" r="{w * 0.04:.1f}" fill="#1d7a5f"/>'
        f'<rect x="{w * 0.60:.1f}" y="{h * 0.30:.1f}" width="{w * 0.05:.1f}" height="{h * 0.42:.1f}" '
        f'transform="rotate(28 {w * 0.62:.1f} {h * 0.51:.1f})" fill="#8a5a2b"/>'
        f'<path d="M{w * 0.66:.1f} {h * 0.26:.1f} l{w * 0.10:.1f} {-h * 0.10:.1f} l{w * 0.03:.1f} {h * 0.07:.1f} '
        f'l{-w * 0.06:.1f} {h * 0.08:.1f} z" fill="#2b2b2b"/>'
    )
    return body


def art_siren(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#dfe6ee"/>'
        f'<rect x="0" y="{h * 0.70:.1f}" width="{w}" height="{h * 0.30:.1f}" fill="#8b9099"/>'
        f'<rect x="{w * 0.12:.1f}" y="{h * 0.44:.1f}" width="{w * 0.62:.1f}" height="{h * 0.26:.1f}" fill="#f2f4f7"/>'
        f'<rect x="{w * 0.74:.1f}" y="{h * 0.50:.1f}" width="{w * 0.14:.1f}" height="{h * 0.20:.1f}" fill="#dde3ea"/>'
        f'<circle cx="{w * 0.80:.1f}" cy="{h * 0.70:.1f}" r="{h * 0.05:.1f}" fill="#2f3338"/>'
        f'<rect x="{w * 0.30:.1f}" y="{h * 0.30:.1f}" width="{w * 0.26:.1f}" height="{h * 0.14:.1f}" rx="{h * 0.02:.1f}" fill="#2f3338"/>'
        f'<rect x="{w * 0.31:.1f}" y="{h * 0.31:.1f}" width="{w * 0.12:.1f}" height="{h * 0.06:.1f}" fill="#d33a3a"/>'
        f'<rect x="{w * 0.44:.1f}" y="{h * 0.31:.1f}" width="{w * 0.11:.1f}" height="{h * 0.06:.1f}" fill="#3a6ad0"/>'
        f'<path d="M{w * 0.28:.1f} {h * 0.30:.1f} l{w * 0.06:.1f} {-h * 0.12:.1f} l{w * 0.20:.1f} {h * 0.12:.1f} z" fill="#d33a3a" opacity="0.45"/>'
        f'<path d="M{w * 0.52:.1f} {h * 0.30:.1f} l{w * 0.06:.1f} {-h * 0.12:.1f} l{w * 0.20:.1f} {h * 0.12:.1f} z" fill="#3a6ad0" opacity="0.45"/>'
    )
    return body


def art_flame(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#f6e2c4"/>'
        f'<rect x="{w * 0.20:.1f}" y="{h * 0.52:.1f}" width="{w * 0.60:.1f}" height="{h * 0.48:.1f}" fill="#b5673a"/>'
        + "".join(
            f'<rect x="{w * (0.24 + 0.12 * i):.1f}" y="{h * 0.60:.1f}" width="{w * 0.08:.1f}" height="{h * 0.12:.1f}" fill="#f2d6a8"/>'
            for i in range(4)
        )
        + f'<path d="M{w * 0.44:.1f} {h * 0.52:.1f} q{w * 0.02:.1f} {-h * 0.22:.1f} {w * 0.08:.1f} {-h * 0.28:.1f} '
        f'q{w * 0.02:.1f} {h * 0.16:.1f} {w * 0.07:.1f} {h * 0.28:.1f} z" fill="#e2761f"/>'
        + f'<path d="M{w * 0.53:.1f} {h * 0.52:.1f} q{w * 0.05:.1f} {-h * 0.18:.1f} {w * 0.11:.1f} {-h * 0.24:.1f} '
        f'q{-w * 0.02:.1f} {h * 0.14:.1f} {w * 0.02:.1f} {h * 0.24:.1f} z" fill="#f2a01f"/>'
        + f'<ellipse cx="{w * 0.56:.1f}" cy="{h * 0.20:.1f}" rx="{w * 0.16:.1f}" ry="{h * 0.12:.1f}" fill="#b9b3aa" opacity="0.65"/>'
        + f'<ellipse cx="{w * 0.66:.1f}" cy="{h * 0.12:.1f}" rx="{w * 0.10:.1f}" ry="{h * 0.07:.1f}" fill="#c9c3ba" opacity="0.5"/>'
    )
    return body


def art_children(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#e7eef0"/>'
        f'<circle cx="{w * 0.30:.1f}" cy="{h * 0.32:.1f}" r="{h * 0.11:.1f}" fill="#d9a066"/>'
        f'<path d="M{w * 0.30:.1f} {h * 0.43:.1f} q-{w * 0.14:.1f} {h * 0.05:.1f} -{w * 0.13:.1f} {h * 0.30:.1f} '
        f'h{w * 0.26:.1f} q{w * 0.01:.1f} -{h * 0.25:.1f} {-w * 0.13:.1f} {-h * 0.30:.1f} z" fill="#2f6f9f"/>'
        f'<circle cx="{w * 0.62:.1f}" cy="{h * 0.27:.1f}" r="{h * 0.10:.1f}" fill="#b98757"/>'
        f'<path d="M{w * 0.62:.1f} {h * 0.37:.1f} q-{w * 0.13:.1f} {h * 0.05:.1f} {-w * 0.12:.1f} {h * 0.30:.1f} '
        f'h{w * 0.24:.1f} q{w * 0.01:.1f} -{h * 0.26:.1f} {-w * 0.12:.1f} {-h * 0.30:.1f} z" fill="#a8232e"/>'
        f'<path d="M{w * 0.18:.1f} {h * 0.14:.1f} q{w * 0.32:.1f} {-h * 0.14:.1f} {w * 0.64:.1f} {h * 0.02:.1f}" fill="none" '
        f'stroke="#1d7a5f" stroke-width="{w * 0.018:.1f}" stroke-linecap="round"/>'
        f'<circle cx="{w * 0.86:.1f}" cy="{h * 0.62:.1f}" r="{h * 0.09:.1f}" fill="#e8c07a" opacity="0.7"/>'
    )
    return body


def art_accord(w, h):
    body = (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#eef1f6"/>'
        f'<path d="M{w * 0.08:.1f} {h * 0.55:.1f} l{w * 0.22:.1f} {-h * 0.10:.1f} l{w * 0.10:.1f} {h * 0.08:.1f} '
        f'l{-w * 0.10:.1f} {h * 0.06:.1f} l{w * 0.16:.1f} {h * 0.12:.1f} z" fill="#1b5e93"/>'
        f'<path d="M{w * 0.92:.1f} {h * 0.55:.1f} l{-w * 0.22:.1f} {-h * 0.10:.1f} l{-w * 0.10:.1f} {h * 0.08:.1f} '
        f'l{w * 0.10:.1f} {h * 0.06:.1f} l{-w * 0.16:.1f} {h * 0.12:.1f} z" fill="#a8232e"/>'
        f'<circle cx="{w * 0.50:.1f}" cy="{h * 0.46:.1f}" r="{h * 0.10:.1f}" fill="#f4f1e8" stroke="#c9c2b2" stroke-width="1.5"/>'
        f'<text x="{w * 0.5:.1f}" y="{h * 0.52:.1f}" font-family="Arial" font-size="{w * 0.09:.1f}" font-weight="700" '
        f'fill="#a8232e" text-anchor="middle">+</text>'
        f'<path d="M{w * 0.46:.1f} {h * 0.30:.1f} l{w * 0.04:.1f} {-h * 0.10:.1f} l{w * 0.04:.1f} {h * 0.10:.1f} z" fill="#f2c14e"/>'
        f'<circle cx="{w * 0.44:.1f}" cy="{h * 0.24:.1f}" r="{h * 0.022:.1f}" fill="#f2c14e"/>'
        f'<circle cx="{w * 0.56:.1f}" cy="{h * 0.24:.1f}" r="{h * 0.022:.1f}" fill="#f2c14e"/>'
    )
    return body


ART = {
    "summit": art_summit,
    "gaza": art_gaza,
    "ipo": art_ipo,
    "bridge": art_bridge,
    "game": art_game,
    "podium": art_podium,
    "coins": art_coins,
    "palette": art_palette,
    "siren": art_siren,
    "flame": art_flame,
    "children": art_children,
    "accord": art_accord,
}


def wrap(text, max_chars):
    """Greedy word wrap: returns the lines a reader would see."""
    lines = []
    current = ""
    for word in text.split():
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= max_chars:
            current = f"{current} {word}"
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def lines_svg(x, y, lines, size, family, fill, weight="400", line_height=None, extra=""):
    """One <text> per line, so nothing overflows the column."""
    step = line_height or size * 1.25
    out = []
    for index, line in enumerate(lines):
        out.append(
            f'<text x="{x}" y="{y + index * step:.1f}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{extra}>{esc(line)}</text>'
        )
    return "".join(out)


def svg(w, h, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'preserveAspectRatio="none">{body}</svg>'
    )


def hero_block(story, x, y, width):
    art_h = 118
    color = REGION_COLOR.get(story["region"], "#3f434b")
    headline = lines_svg(
        0,
        art_h + 44,
        wrap(story["headline"], 30),
        24,
        "Didot, Georgia, serif",
        INK,
        weight="700",
        line_height=28,
    )
    deck = lines_svg(
        0,
        art_h + 44 + 28 * len(wrap(story["headline"], 30)) + 8,
        wrap(story["deck"], 52),
        12.5,
        "Georgia, serif",
        "#3d4149",
        line_height=16,
    )
    return f"""
    <g transform="translate({x},{y})">
      <rect x="0" y="0" width="{width}" height="{art_h}" fill="#e9e3d4"/>
      {svg(width, art_h, ART[story['art']](width, art_h))}
      <rect x="0" y="0" width="{width}" height="{art_h}" fill="none" stroke="#cfc7b4" stroke-width="1"/>
      <circle cx="16" cy="{art_h + 15}" r="11" fill="{color}"/>
      <text x="16" y="{art_h + 20}" font-family="Arial" font-size="13" font-weight="700"
            fill="#f7f3e9" text-anchor="middle">{story['no']}</text>
      <text x="34" y="{art_h + 19}" font-family="Arial" font-size="11" font-weight="700"
            fill="{color}" letter-spacing="1.1">{story['region'].upper()} · {story['beat'].upper()}</text>
      {headline}
      {deck}
    </g>"""


def card_block(story, x, y, width):
    color = REGION_COLOR.get(story["region"], "#3f434b")
    art = 42
    text_x = art + 10
    headline_lines = wrap(story["headline"], 38)
    headline = lines_svg(
        text_x,
        28,
        headline_lines,
        13.5,
        "Georgia, serif",
        INK,
        weight="700",
        line_height=16,
    )
    deck = lines_svg(
        text_x,
        28 + 16 * len(headline_lines) + 4,
        wrap(story["deck"], 54),
        10.5,
        "Georgia, serif",
        "#4a4e57",
        line_height=13,
    )
    return f"""
    <g transform="translate({x},{y})">
      <rect x="0" y="0" width="{art}" height="{art}" fill="#e9e3d4"/>
      {svg(art, art, ART[story['art']](art, art))}
      <circle cx="{art + 9}" cy="10" r="9" fill="{color}"/>
      <text x="{art + 9}" y="14" font-family="Arial" font-size="11" font-weight="700"
            fill="#f7f3e9" text-anchor="middle">{story['no']}</text>
      <text x="{art + 22}" y="14" font-family="Arial" font-size="8.5" font-weight="700"
            fill="{color}" letter-spacing="0.7">{story['region'].upper()} · {story['beat'].upper()}</text>
      {headline}
      {deck}
    </g>"""


SHORT_REGION = {
    "Middle East": "M. EAST",
    "South America": "S. AMERICA",
    "Americas": "AMERICAS",
    "United States": "AMERICAS",
    "Oceania": "OCEANIA",
}


def also_block(items, x, y, width):
    rows = []
    line_h = 19
    for index, (region, text) in enumerate(items):
        color = REGION_COLOR.get(region, "#3f434b")
        label = SHORT_REGION.get(region, region.upper())
        rows.append(
            f'<text x="0" y="{index * line_h}" font-family="Arial" font-size="9" font-weight="700" '
            f'fill="{color}">{esc(label)}:</text>'
            f'<text x="62" y="{index * line_h}" font-family="Georgia, serif" font-size="11" '
            f'fill="{INK}">{esc(text)}</text>'
        )
    return (
        f'<g transform="translate({x},{y})">' + "".join(rows) + "</g>"
    )


def legend_block(x, y):
    pins = stories.HEROES + stories.CARDS
    rows = []
    for index, story in enumerate(pins):
        col = index // 4
        row = index % 4
        y_row = y + row * 11
        rows.append(
            f'<circle cx="{x + col * 112}" cy="{y_row}" r="6.5" fill="#a8232e"/>'
            f'<text x="{x + col * 112}" y="{y_row + 3.3}" font-family="Arial" font-size="8.5" '
            f'font-weight="700" fill="#ffffff" text-anchor="middle">{story["no"]}</text>'
            f'<text x="{x + col * 112 + 11}" y="{y_row + 3.3}" font-family="Georgia, serif" '
            f'font-size="10" fill="{INK}">{esc(story["place"])}</text>'
        )
    return "".join(rows)


def build_html():
    heroes = []
    for index, story in enumerate(stories.HEROES):
        heroes.append(hero_block(story, 18 + index * 330, 166, 320))
    cards = []
    for index, story in enumerate(stories.CARDS):
        col = index % 3
        row = index // 3
        cards.append(card_block(story, 18 + col * 330, 478 + row * 77, 320))
    also = stories.ALSO
    left = also[: len(also) // 2]
    right = also[len(also) // 2 :]
    total = 12 + len(also)
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>The World on {stories.DAY['date_long']}</title>
<style>
  html, body {{ margin: 0; padding: 0; width: 1024px; height: 1024px; background: {PAPER}; }}
  svg {{ display: block; }}
</style></head>
<body>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <rect x="0" y="0" width="1024" height="1024" fill="{PAPER}"/>
  <rect x="0" y="0" width="1024" height="32" fill="#14233c"/>
  <text x="18" y="21" font-family="Arial" font-size="11" font-weight="700" fill="#f2e9d6"
        letter-spacing="2.2">{stories.DAY['edition']}</text>
  <text x="1006" y="21" text-anchor="end" font-family="Arial" font-size="11" font-weight="700"
        fill="#f2e9d6" letter-spacing="1.6">{total} STORIES · 6 CONTINENTS · ONE DAY</text>

  <text x="18" y="58" font-family="Arial" font-size="10.5" font-weight="700" fill="{ACCENT}"
        letter-spacing="1.8">THE WORLD'S NEWS IN ONE PICTURE</text>
  <text x="18" y="112" font-family="Didot, Georgia, serif" font-size="56" font-weight="700"
        fill="{INK}">{stories.DAY['date_long']}</text>
  <text x="18" y="140" font-family="Georgia, serif" font-size="15" font-style="italic"
        fill="#4a4e57">{esc(stories.DAY['deck'])}</text>
  <rect x="18" y="152" width="988" height="2.5" fill="{RULE}"/>
  <rect x="18" y="157" width="988" height="0.8" fill="{RULE}" opacity="0.5"/>

  {''.join(heroes)}

  <rect x="18" y="466" width="988" height="1.4" fill="{RULE}"/>
  {''.join(cards)}

  <rect x="18" y="708" width="988" height="1.4" fill="{RULE}"/>

  <text x="18" y="730" font-family="Arial" font-size="12" font-weight="700" fill="{INK}"
        letter-spacing="1.6">WHERE IT HAPPENED</text>
  <rect x="18" y="738" width="336" height="168" fill="#eef1f3"/>
  <image href="assets/map.png" x="18" y="738" width="336" height="168" preserveAspectRatio="none"/>
  <rect x="18" y="738" width="336" height="168" fill="none" stroke="#cfc7b4" stroke-width="1"/>
  <text x="18" y="923" font-family="Georgia, serif" font-size="10" fill="#6a6e77">
    Every number marks the place a story on this page happened.</text>
  {legend_block(18, 937)}

  <rect x="366" y="738" width="0.8" height="212" fill="{RULE}" opacity="0.35"/>

  <text x="382" y="730" font-family="Arial" font-size="12" font-weight="700" fill="{INK}"
        letter-spacing="1.6">ALSO ON THURSDAY</text>
  {also_block(left, 382, 754, 300)}
  <rect x="688" y="738" width="0.8" height="212" fill="{RULE}" opacity="0.35"/>
  {also_block(right, 704, 754, 300)}

  <rect x="18" y="980" width="988" height="1" fill="{RULE}" opacity="0.6"/>
  <text x="18" y="998" font-family="Georgia, serif" font-size="9.5" fill="#6a6e77">{esc(stories.SOURCES)}</text>
</svg>
</body></html>
"""


def render(html_path, png_path):
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--default-background-color=00000000",
            "--window-size=1024,1024",
            f"--screenshot={png_path}",
            f"file://{html_path}",
        ],
        check=True,
        capture_output=True,
    )


def main():
    html = build_html()
    with open(HTML, "w") as handle:
        handle.write(html)
    render(HTML, PNG)
    image = Image.open(PNG)
    print("rendered", image.size, os.path.getsize(PNG), "bytes")
    if os.path.getsize(PNG) > 1048576:
        image = image.convert("P", palette=Image.ADAPTIVE, colors=200)
        image.save(PNG, optimize=True)
        print("re-encoded", os.path.getsize(PNG), "bytes")
    if image.size != (1024, 1024):
        sys.exit(f"wrong size {image.size}")


if __name__ == "__main__":
    main()
