"""Stamps the cursive "Brodysoptics." watermark in the lower right corner of every photo.

Runs on GitHub while the site is being published (see .github/workflows/deploy.yml),
so only the copies on the website get the watermark. The photos in the repo stay clean.

Skips: the hero photo (the big banner at the top), videos, and anything that isn't a photo.

Run it yourself on a folder to preview:  python .github/watermark/watermark.py some-folder
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

TEXT = "Brodysoptics."
FONT = os.path.join(os.path.dirname(__file__), "HerrVonMuellerhoff-Regular.ttf")
PHOTO = (".jpg", ".jpeg", ".png", ".webp")
WIDTH = 0.26    # watermark width, as a share of the photo's shorter side
OPACITY = 175   # 0-255. White text, a little see-through
MARGIN = 0.03   # gap from the bottom and right edges, as a share of the photo's shorter side


def stamp(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)  # bake in phone rotation so the text lands at the real bottom
    w, h = img.size

    # size the font so the text is WIDTH of the shorter side
    size = 100
    font = ImageFont.truetype(FONT, size)
    tw = font.getbbox(TEXT)[2]
    size = max(12, int(size * WIDTH * min(w, h) / tw))
    font = ImageFont.truetype(FONT, size)
    left, top, right, bottom = font.getbbox(TEXT)
    gap = MARGIN * min(w, h)
    x = w - gap - right    # lower right corner
    y = h - gap - bottom

    # soft dark shadow underneath so it still shows up on bright photos
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((x, y), TEXT, font=font, fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(max(1, size // 25)))
    mark = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(mark).text((x, y), TEXT, font=font, fill=(255, 255, 255, OPACITY))

    out = Image.alpha_composite(Image.alpha_composite(img.convert("RGBA"), shadow), mark)
    ext = os.path.splitext(path)[1].lower()
    if ext in (".jpg", ".jpeg"):
        out.convert("RGB").save(path, quality=86, optimize=True, progressive=True)
    elif ext == ".png":
        out.save(path, optimize=True)
    else:
        out.save(path, quality=86)


def main(folder):
    done = 0
    for root, _, files in os.walk(folder):
        for f in files:
            if not f.lower().endswith(PHOTO):
                continue
            if root == folder and f.lower().startswith("hero"):
                continue  # the big banner photo stays clean
            stamp(os.path.join(root, f))
            done += 1
    print(done, "photos watermarked")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "photos")
