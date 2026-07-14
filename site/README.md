# Lorè Lab — GitHub Pages scrolling website

This is a hybrid academic website inspired by the general structure of modern laboratory websites:

- a long home page with smooth scrolling sections;
- separate pages for Research, People, Publications, Resources, Join us and Contact;
- sticky responsive navigation;
- active section highlighting;
- reveal-on-scroll animations;
- scroll progress bar and back-to-top button;
- no external framework or paid service.

## Publish on GitHub Pages

1. Create a public repository named exactly `nicolalore.github.io`.
2. Upload all files and folders from this package to the repository root.
3. Open `Settings → Pages`.
4. Select `Deploy from a branch`, branch `main`, folder `/(root)`.
5. The site will be published at `https://nicolalore.github.io/`.

## Edit the site

The page content is stored in `pages/`:

- `pages/home.html`
- `pages/research.html`
- `pages/people.html`
- `pages/publications.html`
- `pages/resources.html`
- `pages/join.html`
- `pages/contact.html`

After editing a fragment, run:

```bash
python3 build_site.py
```

This regenerates the public HTML files in the project root.

## Replace images

Put your images in `assets/img/`. For example, replace:

```html
<img src="assets/img/nicola-placeholder.svg" alt="Nicola Ivan Lorè">
```

with:

```html
<img src="assets/img/nicola-lore.jpg" alt="Nicola Ivan Lorè">
```

Recommended sizes:

- portrait: about 1000 × 1200 px;
- team photos: at least 1200 px wide;
- research images: landscape, at least 1600 × 1000 px;
- hero image: about 2000 × 1200 px.

## Replace placeholders

Search all files for:

- `replace-with-your-institutional-email`
- `Add ORCID`
- `Replace with`
- `Full name`
- `href="#"`

## Change scrolling behaviour

The home page uses gentle proximity snapping. To disable it, remove this rule from `assets/css/site.css`:

```css
body.home main { scroll-snap-type: y proximity; }
```

Smooth scrolling will remain active.

## Test locally

Run:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Important

GitHub Pages is public. Do not upload patient-identifiable images, confidential unpublished data, private contact information, or copyrighted journal figures without permission.
