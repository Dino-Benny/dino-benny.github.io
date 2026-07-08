# dinobenny.com

Website for The Adventures of Dino and Benny. Built with Jekyll, which GitHub Pages
runs natively: push to the default branch and GitHub builds and publishes the site
automatically in a minute or two. No local tooling required.

## How to add a new book (no AI assistance needed)

1. Copy an existing file in `_books/` (say `a-parisian-adventure.md`) to a new name.
   The filename becomes the web address: `_books/a-new-york-adventure.md` publishes at
   `dinobenny.com/books/a-new-york-adventure.html`.
2. Edit the fields at the top (title, number, location, cover filenames, descriptions,
   the one-line hooks) and replace the two blurb paragraphs below the `---` line.
3. Make the two cover images. With Pillow installed, this one command resizes and
   embeds the brand metadata:
   `python3 tools/process_cover.py path/to/cover_front.png newyork`
4. Commit and push. The home page grid, the book page, the cross-links on other book
   pages, and the sitemap all update themselves.

To add per-format buy links later, add any of `buy_url`, `kindle_url`,
`paperback_url`, `hardcover_url` to a book's front matter. Without them, buttons fall
back to the series link in `_config.yml`.

## Site-wide settings

Edit `_config.yml` for the contact email and the Amazon series link. The copyright
year in the footer updates itself.

## Folder map

```
_config.yml           Site settings (email, Amazon link, collections)
_books/               One markdown file per book = one page per book
_layouts/             Page skeletons (default.html wraps everything; book.html renders a book)
_includes/            Shared head/header/footer used by the layouts
index.html            Home page (hero, auto-generated book grid, series pitch)
printables.html       Free printables + mailing list call to action
about.html            Series story and contact
404.html              Friendly not-found page
style.css             All styles; palette locked to the series character sheet
images/               Web-optimized covers, character art, favicons, OG banner
images/_incoming/     Full-res generated masters (gitignored, never published)
files/                Downloadable printables (coloring pack PDF)
tools/                process_cover.py (resize + brand metadata), never published
CNAME, robots.txt     Domain and crawler config; sitemap.xml is generated automatically
```

## Previewing changes

Easiest: push to GitHub and check the live site a minute later. For local preview,
install Ruby and run `bundle install` then `bundle exec jekyll serve` in this folder,
then open http://localhost:4000. Plain double-clicking the HTML files no longer works,
since pages are assembled by Jekyll at build time.

## Custom domain (one-time setup)

1. GitHub: repo Settings → Pages → Custom domain → enter `dinobenny.com` (the CNAME file here already matches).
2. Porkbun: DNS for dinobenny.com → add four A records for `@` (hostname blank):
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Porkbun: add a CNAME record, host `www`, answer `dino-benny.github.io`.
4. Back in GitHub Pages settings, tick "Enforce HTTPS" once the certificate is issued (can take up to 24 hours).

## Email forward (one-time setup)

Porkbun → Domain Management → dinobenny.com → Email Forwarding: create `hello`
forwarding to your personal address. Free, up to 20 addresses.

## Wiring the mailing list

When you create the mailing list account (MailerLite free tier or similar): make an
embedded signup form there, then in `printables.html` replace the button under the
`<!-- MAILERLITE -->` comment with the provider's embed snippet.

## Metadata policy

Every image and PDF here is re-encoded before publishing: that strips tool-provenance
metadata (C2PA and similar) and embeds
"The Adventures of Dino and Benny - dinobenny.com" as Author/Copyright/Description.
`tools/process_cover.py` does this for covers; ask Claude to process other new images
the same way.
