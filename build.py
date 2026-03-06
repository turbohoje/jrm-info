#!/usr/bin/env python3
"""
build.py — Resume build script

Reads resume.md (with YAML front matter) and generates:
  - index.html   : SEO-optimised web page with JSON-LD structured data
  - <pdf_filename>: Print-ready PDF via WeasyPrint

Usage:
    python build.py              # build both HTML and PDF
    python build.py --html       # HTML only
    python build.py --pdf        # PDF only

Edit the YAML front matter in resume.md to control all formatting,
contact info, SEO keywords, analytics, and output settings.
"""

import argparse
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Dependency check with helpful errors
# ---------------------------------------------------------------------------
try:
    import frontmatter
except ImportError:
    print("ERROR: python-frontmatter not installed.  Run: pip install -r requirements.txt")
    sys.exit(1)

try:
    import markdown as md_lib
except ImportError:
    print("ERROR: markdown not installed.  Run: pip install -r requirements.txt")
    sys.exit(1)

BASE_DIR = Path(__file__).parent


# ---------------------------------------------------------------------------
# Load and parse resume.md
# ---------------------------------------------------------------------------

def load_resume() -> tuple[dict, str]:
    """Return (config_dict, content_as_html)."""
    resume_path = BASE_DIR / "resume.md"
    if not resume_path.exists():
        print(f"ERROR: {resume_path} not found.")
        sys.exit(1)

    post = frontmatter.load(str(resume_path))
    config = dict(post.metadata)

    md = md_lib.Markdown(
        extensions=["tables", "sane_lists"],
        output_format="html",
    )
    content_html = md.convert(post.content)
    return config, content_html


# ---------------------------------------------------------------------------
# schema.org JSON-LD
# ---------------------------------------------------------------------------

def build_jsonld(cfg: dict) -> dict:
    meta = cfg.get("meta", {})
    seo  = cfg.get("seo",  {})
    keywords = seo.get("keywords", [])

    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": meta.get("name", ""),
        "url": meta.get("website_url", ""),
        "email": meta.get("email", ""),
        "telephone": meta.get("phone", ""),
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Denver",
            "addressRegion": "CO",
            "addressCountry": "US",
        },
        "sameAs": [
            meta.get("linkedin_url", ""),
            meta.get("website_url", ""),
        ],
        "jobTitle": "Technical Lead Manager",
        "worksFor": {
            "@type": "Organization",
            "name": "AppOmni",
        },
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": "University of Colorado at Boulder"},
            {"@type": "CollegeOrUniversity", "name": "Regis University Denver"},
        ],
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "name": "Master of Data Engineering"},
            {"@type": "EducationalOccupationalCredential", "name": "Bachelor of Computer Science"},
            {"@type": "EducationalOccupationalCredential", "name": "Project Management Professional"},
            {"@type": "EducationalOccupationalCredential", "name": "Certified Scrum Master"},
        ],
        "knowsAbout": keywords,
        "description": seo.get("description", ""),
    }


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

def web_css(cfg: dict) -> str:
    w = cfg.get("web", {})
    font   = w.get("font_family", "Arial, sans-serif")
    width  = w.get("max_width", "820px")
    accent = w.get("color_accent", "#0055aa")
    hdr_bg = w.get("color_header_bg", "#f8f8f8")

    return f"""
    * {{ box-sizing: border-box; }}
    body {{
      font-family: {font};
      margin: 0; padding: 0;
      background: #fff; color: #000;
      line-height: 1.6;
    }}
    header {{
      position: sticky; top: 0;
      background: {hdr_bg};
      padding: 0.7rem 1rem;
      text-align: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      z-index: 1000;
    }}
    header a {{ text-decoration: none; font-weight: bold; color: #000; }}
    header a:hover {{ text-decoration: underline; }}
    .container {{ padding: 1rem 2rem; max-width: {width}; margin: 0 auto; }}
    h1 {{ margin: 0.75rem 0 0.1rem; font-size: 2rem; }}
    h2 {{
      margin: 1.5rem 0 0.3rem;
      font-size: 1.1rem;
      border-bottom: 1px solid #ddd;
      padding-bottom: 0.2rem;
      color: {accent};
    }}
    h3 {{ margin: 1rem 0 0; font-size: 1rem; }}
    h4 {{ margin: 0.5rem 0 0; font-size: 0.95rem; color: #444; font-style: italic; font-weight: normal; }}
    .contact-info {{
      color: #555; margin: 0.2rem 0 0.8rem;
      font-size: 0.93rem;
    }}
    .contact-info a {{ color: inherit; text-decoration: none; }}
    .contact-info a:hover {{ text-decoration: underline; }}
    p {{ margin: 0.4rem 0; }}
    ul {{ padding-left: 1.3rem; margin: 0.25rem 0 0.1rem; }}
    li {{ margin-bottom: 0.15rem; }}
    table {{
      width: 100%; border-collapse: collapse;
      font-size: 0.88rem; margin-top: 0.4rem;
    }}
    td, th {{ padding: 0.3rem 0.5rem; text-align: left; vertical-align: top; }}
    tr:nth-child(odd) td {{ background: #f9f9f9; }}
    .footer-note {{ color: #aaa; font-size: 0.78rem; text-align: right; margin-top: 2rem; }}
    @media (max-width: 600px) {{
      .container {{ padding: 1rem; }}
      h1 {{ font-size: 1.6rem; }}
    }}
    """


def pdf_css(cfg: dict) -> str:
    p = cfg.get("pdf", {})
    font        = p.get("font_family",   "Arial, sans-serif")
    size_body   = p.get("font_size_body","9.5pt")
    size_h1     = p.get("font_size_h1",  "18pt")
    size_h2     = p.get("font_size_h2",  "11pt")
    size_h3     = p.get("font_size_h3",  "10pt")
    margin_t    = p.get("margin_top",    "0.45in")
    margin_b    = p.get("margin_bottom", "0.45in")
    margin_l    = p.get("margin_left",   "0.55in")
    margin_r    = p.get("margin_right",  "0.55in")
    lh          = p.get("line_height",   "1.4")
    accent      = p.get("color_accent",  "#0066cc")
    color_text  = p.get("color_text",    "#000000")
    page_size   = p.get("page_size",     "letter")

    return f"""
    @page {{
      size: {page_size};
      margin: {margin_t} {margin_r} {margin_b} {margin_l};
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: {font};
      font-size: {size_body};
      color: {color_text};
      line-height: {lh};
      margin: 0; padding: 0;
    }}
    h1 {{
      font-size: {size_h1};
      margin: 0 0 1pt;
      color: {accent};
    }}
    h2 {{
      font-size: {size_h2};
      margin: 5pt 0 1pt;
      border-bottom: 0.5pt solid #999;
      padding-bottom: 1pt;
      color: {accent};
      page-break-after: avoid;
    }}
    h3 {{
      font-size: {size_h3};
      margin: 4pt 0 0;
      page-break-after: avoid;
    }}
    h4 {{
      font-size: {size_h3};
      margin: 2pt 0 0;
      font-style: italic;
      font-weight: normal;
      page-break-after: avoid;
    }}
    .contact-info {{
      font-size: {size_body};
      margin: 1pt 0 3pt;
      color: #333;
    }}
    .contact-info a {{ color: inherit; text-decoration: none; }}
    p {{ margin: 0 0 1pt; }}
    ul {{
      margin: 0 0 2pt;
      padding-left: 11pt;
      page-break-inside: avoid;
    }}
    li {{ margin-bottom: 0; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: {size_body};
      margin-top: 2pt;
    }}
    td {{ padding: 1pt 4pt; vertical-align: top; }}
    tr:nth-child(odd) td {{ background: #f5f5f5; }}
    .footer-note {{ display: none; }}
    """


# ---------------------------------------------------------------------------
# Contact info HTML fragment
# ---------------------------------------------------------------------------

def contact_line_html(meta: dict) -> str:
    parts = []
    phone   = meta.get("phone")
    email   = meta.get("email")
    loc     = meta.get("location")
    web_url = meta.get("website_url", "#")
    web_dsp = meta.get("website_display")
    li_url  = meta.get("linkedin_url", "#")
    li_dsp  = meta.get("linkedin_display")

    sep = " &nbsp;|&nbsp; "

    if phone:
        tel = phone.replace(".", "").replace(" ", "")
        parts.append(f'<a href="tel:{tel}">{phone}</a>')
    if email:
        parts.append(f'<a href="mailto:{email}">{email}</a>')
    if loc:
        parts.append(loc)
    if web_dsp:
        parts.append(f'<a href="{web_url}" rel="noopener noreferrer">{web_dsp}</a>')
    if li_dsp:
        parts.append(f'<a href="{li_url}" rel="noopener noreferrer">{li_dsp}</a>')

    return sep.join(parts)


# ---------------------------------------------------------------------------
# Full HTML document builder
# ---------------------------------------------------------------------------

def build_html(cfg: dict, content_html: str, for_pdf: bool = False) -> str:
    meta         = cfg.get("meta", {})
    seo          = cfg.get("seo",  {})
    analytics    = cfg.get("analytics", {})
    ga_tag       = analytics.get("google_tag", "")

    page_title   = seo.get("page_title",   meta.get("name", "Resume"))
    description  = seo.get("description", "").replace("\n", " ").strip()
    keywords     = ", ".join(seo.get("keywords", []))
    og_image     = seo.get("og_image", "")
    name         = meta.get("name", "")
    pdf_filename = meta.get("pdf_filename", "resume.pdf")
    last_updated = meta.get("last_updated", "")
    website_url  = meta.get("website_url", "")

    jsonld_str   = json.dumps(build_jsonld(cfg), indent=2, ensure_ascii=False)
    contact_html = contact_line_html(meta)
    css          = pdf_css(cfg) if for_pdf else web_css(cfg)

    # ---- Inject contact line immediately after the first </h1> ----
    processed = content_html.replace(
        "</h1>",
        f'</h1>\n<p class="contact-info">{contact_html}</p>',
        1,
    )

    # ---- Google Analytics (web only) ----
    ga_block = ""
    if ga_tag and not for_pdf:
        ga_block = f"""
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga_tag}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{ga_tag}');
</script>"""

    # ---- Sticky download header (web only) ----
    header_block = ""
    if not for_pdf:
        header_block = f"""
  <header>
    <a href="{pdf_filename}" download>Download PDF Resume</a>
  </header>"""

    # ---- OG image tag ----
    og_image_tag = f'  <meta property="og:image" content="{og_image}">' if og_image else ""

    # ---- Canonical (web only) ----
    canonical_tag = ""
    if not for_pdf and website_url:
        canonical_tag = f'  <link rel="canonical" href="{website_url}">'

    # ---- Footer note ----
    footer = ""
    if last_updated:
        footer = f'<p class="footer-note">Last updated: {last_updated}</p>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="{name}">
  <meta name="robots" content="index, follow">
{canonical_tag}
  <!-- Open Graph -->
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="profile">
  <meta property="og:url" content="{website_url}">
{og_image_tag}
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{page_title}">
  <meta name="twitter:description" content="{description}">
  <!-- schema.org structured data -->
  <script type="application/ld+json">
{jsonld_str}
  </script>
{ga_block}
  <style>
{css}
  </style>
</head>
<body>
{header_block}
  <div class="container">
{processed}
{footer}
  </div>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def generate_html(cfg: dict, content_html: str) -> None:
    html = build_html(cfg, content_html, for_pdf=False)
    out  = BASE_DIR / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"  [HTML] Written: {out}")


def generate_pdf(cfg: dict, content_html: str) -> None:
    try:
        from weasyprint import HTML
    except ImportError:
        print(
            "ERROR: weasyprint is not installed.\n"
            "  macOS:  brew install weasyprint   (or: pip install weasyprint)\n"
            "  Linux:  pip install weasyprint\n"
            "  Docs:   https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
        )
        sys.exit(1)

    meta         = cfg.get("meta", {})
    pdf_filename = meta.get("pdf_filename", "justin-meyer-resume.pdf")
    out          = BASE_DIR / pdf_filename

    print_html = build_html(cfg, content_html, for_pdf=True)
    HTML(string=print_html, base_url=str(BASE_DIR)).write_pdf(str(out))

    # Page count feedback (requires weasyprint >= 53)
    try:
        from weasyprint import HTML as WP
        doc = WP(string=print_html, base_url=str(BASE_DIR)).render()
        pages = len(doc.pages)
        note = f" ({pages} page{'s' if pages != 1 else ''})"
        if pages > 2:
            note += "  ← WARNING: exceeds 2-page target; reduce font_size_body or margins in resume.md"
    except Exception:
        note = ""

    print(f"  [PDF]  Written: {out}{note}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build resume HTML and PDF from resume.md"
    )
    parser.add_argument("--html", action="store_true", help="Generate index.html only")
    parser.add_argument("--pdf",  action="store_true", help="Generate PDF only")
    args = parser.parse_args()

    do_html = not args.pdf   # default both; --pdf skips HTML
    do_pdf  = not args.html  # default both; --html skips PDF

    print("Reading resume.md …")
    cfg, content_html = load_resume()

    if do_html:
        generate_html(cfg, content_html)

    if do_pdf:
        print("Rendering PDF …")
        generate_pdf(cfg, content_html)

    print("Done.")


if __name__ == "__main__":
    main()
