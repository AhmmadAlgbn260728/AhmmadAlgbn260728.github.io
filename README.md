# Ahmmad Algbn · Portfolio

Live site: https://ahmmadalgbn260728.github.io

## Featured projects
The big project cards (the SDG 13 dashboard and the VIKI presentation) are written by hand in `index.html`.
To add one, copy an `<article class="proj">` block and change the text.
If the project also has a GitHub repository, put the repository name in `data-repo="…"`. That stops it from showing up a second time under "More on GitHub".

## Project documents (PDF viewer)
"View dashboard" and "View slides" open the document as page images inside the site, so they also work on phones.

- The PDFs are in `projects/`. "Download PDF" links point there.
- One image per page is in `docs/<name>/1.jpg`, `2.jpg`, …
- Each document is a `<template id="doc-…">` near the bottom of `index.html`. It lists the page images and the PDF to download.

To add a new document, or after replacing a PDF, render its pages again:

```
pip install pypdfium2 pillow
python tools/render_pages.py projects/my-project.pdf docs/my-project
```

Then copy a `<template>` block, point it at the new images, and give the button `data-doc="…"` with the template's name.

## More on GitHub (automatic)
Smaller projects load from GitHub on their own. Nothing in `index.html` needs to change.

1. Put the project in a **public** GitHub repository.
2. Fill in the repository's **description** (the "About" box on the repository page). Only repositories with a description appear.
3. Optional: add **topics** such as `python` or `pandas`. They show as tags on the card.
4. Optional: add a screenshot named `preview.png` (16:9) to the root of the repository. It becomes the card image.
5. Optional: put a demo link in the repository's **Website** field. It becomes a "Live demo" button.

The six most recently updated repositories are shown. Forks and archived repositories are skipped.

## Update the CV or photo
Replace `Ahmmad_Algbn_CV.pdf` or `photo.jpg` with a new file using the same name.

## Edit text
All text is in `index.html`. Search for the sentence you want to change.
