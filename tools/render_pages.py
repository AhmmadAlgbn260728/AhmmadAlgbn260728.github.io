"""Render every page of a PDF to JPEGs for the portfolio's document viewer.

Usage:  python tools/render_pages.py projects/my-project.pdf docs/my-project
Needs:  pip install pypdfium2 pillow
"""
import pathlib
import sys

import pypdfium2 as pdfium

WIDTH = 1400  # pixels per page image

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
pdf = pdfium.PdfDocument(str(src))
for i, page in enumerate(pdf, start=1):
    w, _ = page.get_size()
    img = page.render(scale=WIDTH / w).to_pil().convert("RGB")
    img.save(out / f"{i}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print(f"{out / f'{i}.jpg'}  {img.width}x{img.height}")
