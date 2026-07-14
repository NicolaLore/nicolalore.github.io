#!/usr/bin/env python3
"""Build the GitHub Pages site from the HTML fragments in pages/."""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent
PAGES = {
    "index.html": ("Lorè Lab | Host–Pathogen Interactions", "home", "home.html"),
    "research.html": ("Research | Lorè Lab", "", "research.html"),
    "people.html": ("People | Lorè Lab", "", "people.html"),
    "publications.html": ("Publications | Lorè Lab", "", "publications.html"),
    "resources.html": ("Resources | Lorè Lab", "", "resources.html"),
    "join.html": ("Join us | Lorè Lab", "", "join.html"),
    "contact.html": ("Contact | Lorè Lab", "", "contact.html"),
}

HEADER = '''
<div class="progress" aria-hidden="true"><span></span></div>
<header class="site-header">
  <div class="shell header-inner">
    <a class="brand" href="index.html#home" aria-label="Lorè Lab home">
      <img src="assets/img/logo.svg" alt="" width="46" height="46">
      <span><strong>Lorè Lab</strong><small>Host–Pathogen Interactions</small></span>
    </a>
    <button class="menu" type="button" aria-expanded="false" aria-controls="navigation">
      <span class="sr-only">Open navigation</span><span></span><span></span><span></span>
    </button>
    <nav id="navigation" class="nav" aria-label="Primary navigation">
      <a href="index.html#home" data-nav="home">Home</a>
      <a href="index.html#research" data-nav="research">Research</a>
      <a href="index.html#approaches" data-nav="approaches">Approaches</a>
      <a href="index.html#people" data-nav="people">People</a>
      <a href="index.html#publications" data-nav="publications">Publications</a>
      <a href="index.html#join" data-nav="join">Join us</a>
      <a href="index.html#contact" data-nav="contact">Contact</a>
      <a class="detail" href="research.html">Detailed pages</a>
    </nav>
  </div>
</header>
'''

FOOTER = '''
<footer class="site-footer">
  <div class="shell footer-main">
    <div>
      <a class="footer-brand" href="index.html#home">Lorè Lab</a>
      <p>Respiratory infections, host–pathogen interactions, non-tuberculous mycobacteria and spatial transcriptomics.</p>
    </div>
    <div><h2>Explore</h2><a href="research.html">Research</a><a href="people.html">People</a><a href="publications.html">Publications</a><a href="resources.html">Resources</a><a href="join.html">Join us</a><a href="contact.html">Contact</a></div>
    <div><h2>Connect</h2><a href="https://github.com/NicolaLore">GitHub</a><a href="#">ORCID</a><a href="mailto:replace-with-your-institutional-email@example.org">Email</a></div>
  </div>
  <div class="shell footer-bottom"><span>© <span data-year></span> Nicola Ivan Lorè</span><span>Hosted with GitHub Pages</span></div>
</footer>
<button class="top" type="button" aria-label="Back to top">↑</button>
'''

TEMPLATE = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="Academic research website focused on respiratory infections, host–pathogen interactions and spatial transcriptomics.">
  <meta name="theme-color" content="#10232d">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/site.css">
  <script src="assets/js/site.js" defer></script>
</head>
<body class="{body_class}">
<a class="skip-link" href="#main-content">Skip to content</a>
{header}
<main id="main-content">{content}</main>
{footer}
</body>
</html>
'''

def build() -> None:
    for output, (title, body_class, fragment) in PAGES.items():
        content = (ROOT / "pages" / fragment).read_text(encoding="utf-8")
        page = TEMPLATE.format(
            title=html.escape(title), body_class=body_class,
            header=HEADER, content=content, footer=FOOTER
        )
        (ROOT / output).write_text(page, encoding="utf-8")
        print(f"Created {output}")

if __name__ == "__main__":
    build()
