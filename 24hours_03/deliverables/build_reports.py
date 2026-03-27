#!/usr/bin/env python3
"""
KRX 24시간 거래 프로젝트 - 리포트 빌드 파이프라인 v2
md → html (오프라인/반응형/Mermaid/사이드바 TOC) → docx (pandoc)
"""

import sys
import argparse
import subprocess
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).parent
MD_DIR = BASE_DIR / "md"
HTML_DIR = BASE_DIR / "html"
DOCX_DIR = BASE_DIR / "docx"
ASSETS_DIR = BASE_DIR / "assets"
CSS_FILE = ASSETS_DIR / "style.css"
MERMAID_JS = ASSETS_DIR / "mermaid.min.js"

REPORT_INFO = {
    "00_종합비교_요약": ("KRX 24시간 거래 도입 전략: 글로벌 비교 종합 분석", "마스터 종합 리포트 — 15+ 차원 비교 매트릭스, 로드맵, 규정 개정안"),
    "01_NYSE_Arca_22시간_분석": ("NYSE Arca 22시간 거래 체제 분석", "Pillar 아키텍처, 22시간 세션, GTC 지속성, DTCC 연계"),
    "02_NASDAQ_23_5_분석": ("NASDAQ 23/5 글로벌 거래 생태계 분석", "이분화 세션, Genium INET, Night Session 제한, GTC 폐지"),
    "03_24X_National_Exchange_분석": ("24X National Exchange 23/5 거래 체제 분석", "MEMX Aeron, 24X Price Bands, 옥션 부재 연속 매칭"),
    "04_CME_Globex_24시간_분석": ("CME Globex 24시간 거래 인프라 분석", "60초 리셋, Follow-the-Sun, GC2 신용통제, iLink 3"),
    "05_DTCC_24_5_청산결제_분석": ("DTCC 24/5 청산결제 로드맵 분석", "UTC 24/5, FIX Tag 715, CCP 보증 확장, Good Night 프로토콜"),
    "06_TSE_JPX_JSCC_분석": ("TSE-JPX 및 JSCC 거래·청산 인프라 분석", "ARROWHEAD 4.0, Itayose 종가 옥션, 아시아 비교"),
    "07_KRX_규정_분석": ("KRX 유가증권시장 규정 분석 및 24시간 전환 규정 개정안", "업무규정/시행세칙 분석, EXTURE 3.0, 규정 개정 로드맵"),
}


def slugify(text):
    """Generate a URL-friendly slug that preserves Korean characters."""
    text = text.strip().lower()
    text = re.sub(r'[^\w\s가-힣-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def remove_manual_toc(md_text):
    """Remove the manual '## 목차' section from markdown."""
    pattern = r'^## 목차\s*\n(.*?\n)*?(?=^---|\n^## |\Z)'
    cleaned = re.sub(pattern, '', md_text, flags=re.MULTILINE)
    return cleaned


def md_to_html_with_ids(md_text):
    """Convert markdown to HTML with proper Korean-friendly heading IDs."""
    import markdown

    md_text = remove_manual_toc(md_text)

    extensions = [
        "tables",
        "fenced_code",
        "attr_list",
        "def_list",
        "footnotes",
    ]
    html = markdown.markdown(md_text, extensions=extensions, output_format="html5")

    # Assign stable IDs to headings
    seen_slugs = {}

    def assign_id(match):
        tag = match.group(1)
        attrs = match.group(2) or ""
        content = match.group(3)
        # Strip HTML tags from content for slug
        plain = re.sub(r'<[^>]+>', '', content)
        slug = slugify(plain)
        if not slug:
            slug = "section"
        if slug in seen_slugs:
            seen_slugs[slug] += 1
            slug = f"{slug}-{seen_slugs[slug]}"
        else:
            seen_slugs[slug] = 0
        # Keep existing id if present
        if 'id="' in attrs:
            return match.group(0)
        return f'<{tag}{attrs} id="{slug}">{content}</{tag}>'

    html = re.sub(
        r'<(h[1-6])([^>]*)>(.*?)</\1>',
        assign_id,
        html,
        flags=re.DOTALL,
    )
    return html


def process_mermaid_blocks(html_content):
    """Convert fenced mermaid code blocks to <div class='mermaid'>."""
    pattern = r'<pre><code class="language-mermaid">(.*?)</code></pre>'

    def replace_mermaid(match):
        code = match.group(1)
        for old, new in [("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                         ("&quot;", '"'), ("&#x27;", "'"), ("&#39;", "'")]:
            code = code.replace(old, new)
        return f'<div class="mermaid">\n{code}\n</div>'

    return re.sub(pattern, replace_mermaid, html_content, flags=re.DOTALL)


def get_sidebar_css():
    """Return CSS for sidebar TOC layout."""
    return """
/* === Sidebar TOC Layout === */
body {
    margin: 0;
    padding: 0;
}

.page-wrapper {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 280px;
    min-width: 280px;
    background: #f8fafc;
    border-right: 1px solid var(--border);
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 100;
    transition: transform 0.3s ease;
}

.sidebar-header {
    padding: 1.2rem 1rem;
    border-bottom: 1px solid var(--border);
    background: var(--primary);
    color: #fff;
}

.sidebar-header h2 {
    color: #fff;
    font-size: 0.85rem;
    margin: 0;
    border: none;
    line-height: 1.4;
    font-weight: 600;
}

.sidebar-header a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    font-size: 0.75rem;
    display: block;
    margin-top: 0.4rem;
}

.sidebar-header a:hover { color: #fff; }

.toc-nav {
    padding: 0.8rem 0;
}

.toc-nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.toc-nav li {
    margin: 0;
}

.toc-nav a {
    display: block;
    padding: 0.35rem 1rem;
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.8rem;
    line-height: 1.4;
    border-left: 3px solid transparent;
    transition: all 0.15s ease;
}

.toc-nav a:hover {
    background: #edf2f7;
    color: var(--primary);
}

.toc-nav a.active {
    background: #ebf4ff;
    color: var(--primary);
    border-left-color: var(--primary);
    font-weight: 600;
}

.toc-nav .toc-h3 a {
    padding-left: 2rem;
    font-size: 0.75rem;
    color: #718096;
}

.toc-nav .toc-h3 a:hover,
.toc-nav .toc-h3 a.active {
    color: var(--primary-light);
}

/* Main content */
.main-content {
    margin-left: 280px;
    flex: 1;
    min-width: 0;
}

.main-content .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 2.5rem;
}

/* Mobile toggle */
.sidebar-toggle {
    display: none;
    position: fixed;
    bottom: 1.5rem;
    left: 1.5rem;
    z-index: 200;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--primary);
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 1.3rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.3);
    line-height: 48px;
    text-align: center;
}

/* Responsive */
@media (max-width: 1024px) {
    .sidebar {
        transform: translateX(-100%);
    }
    .sidebar.open {
        transform: translateX(0);
        box-shadow: 4px 0 24px rgba(0,0,0,0.15);
    }
    .main-content {
        margin-left: 0;
    }
    .sidebar-toggle {
        display: block;
    }
    .main-content .container {
        padding: 1.5rem 1rem;
    }
}

@media print {
    .sidebar, .sidebar-toggle { display: none !important; }
    .main-content { margin-left: 0 !important; }
}

/* Table wrapper for horizontal scroll */
.table-wrapper {
    overflow-x: auto;
    margin: 1.5em 0;
    -webkit-overflow-scrolling: touch;
}

.table-wrapper table {
    display: table;
    min-width: 600px;
}

/* Report index cards in appendix */
.report-index-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.report-index-card {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    background: var(--bg-alt);
    transition: box-shadow 0.2s;
}

.report-index-card:hover {
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}

.report-index-card h4 {
    margin: 0 0 0.3rem;
    font-size: 0.95rem;
    color: var(--primary);
}

.report-index-card p {
    margin: 0 0 0.6rem;
    font-size: 0.8rem;
    color: var(--text-secondary);
}

.report-index-card .card-links a {
    display: inline-block;
    margin-right: 1rem;
    font-size: 0.85rem;
    text-decoration: none;
    color: var(--primary-light);
    padding: 0.2rem 0.5rem;
    border: 1px solid var(--border);
    border-radius: 4px;
}

.report-index-card .card-links a:hover {
    background: var(--primary);
    color: #fff;
    border-color: var(--primary);
}
"""


def get_toc_js():
    """Return JavaScript for auto-generating sidebar TOC and scroll spy."""
    return """
(function() {
    var sidebar = document.getElementById('sidebar-toc');
    if (!sidebar) return;

    var content = document.querySelector('.main-content');
    if (!content) return;

    var headings = content.querySelectorAll('h2, h3');
    if (headings.length === 0) return;

    var ul = document.createElement('ul');

    headings.forEach(function(h) {
        if (!h.id) return;
        var li = document.createElement('li');
        li.className = 'toc-' + h.tagName.toLowerCase();
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        a.setAttribute('data-target', h.id);
        li.appendChild(a);
        ul.appendChild(li);
    });

    sidebar.appendChild(ul);

    // Scroll spy
    var tocLinks = sidebar.querySelectorAll('a[data-target]');
    var headingEls = Array.from(headings).filter(function(h) { return h.id; });

    function onScroll() {
        var scrollPos = window.scrollY + 100;
        var current = null;
        headingEls.forEach(function(h) {
            if (h.offsetTop <= scrollPos) current = h.id;
        });
        tocLinks.forEach(function(a) {
            if (a.getAttribute('data-target') === current) {
                a.classList.add('active');
            } else {
                a.classList.remove('active');
            }
        });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Smooth scroll on click
    tocLinks.forEach(function(a) {
        a.addEventListener('click', function(e) {
            e.preventDefault();
            var target = document.getElementById(a.getAttribute('data-target'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                history.replaceState(null, null, '#' + a.getAttribute('data-target'));
            }
            // Close sidebar on mobile
            if (window.innerWidth <= 1024) {
                document.querySelector('.sidebar').classList.remove('open');
            }
        });
    });

    // Mobile toggle
    var toggle = document.querySelector('.sidebar-toggle');
    if (toggle) {
        toggle.addEventListener('click', function() {
            document.querySelector('.sidebar').classList.toggle('open');
        });
    }
})();
"""


def wrap_tables(html):
    """Wrap <table> elements in a scrollable div."""
    return re.sub(
        r'(<table\b)',
        r'<div class="table-wrapper">\1',
        html,
    ).replace('</table>', '</table></div>')


def generate_html(md_file, base_css, sidebar_css, toc_js, mermaid_js):
    """Generate complete HTML with sidebar TOC."""
    md_text = md_file.read_text(encoding="utf-8")

    title_match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else md_file.stem

    body_html = md_to_html_with_ids(md_text)
    body_html = process_mermaid_blocks(body_html)
    body_html = wrap_tables(body_html)

    stem = md_file.stem
    info = REPORT_INFO.get(stem)
    sidebar_title = info[0] if info else title

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{base_css}
{sidebar_css}
    </style>
</head>
<body>
    <div class="page-wrapper">
        <nav class="sidebar">
            <div class="sidebar-header">
                <h2>{sidebar_title}</h2>
                <a href="index.html">&larr; 리포트 목록</a>
            </div>
            <div class="toc-nav" id="sidebar-toc">
            </div>
        </nav>

        <main class="main-content">
            <div class="container">
{body_html}
            </div>
        </main>
    </div>

    <button class="sidebar-toggle" aria-label="Toggle sidebar">&#9776;</button>

    <script>
{mermaid_js}
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            if (typeof mermaid !== 'undefined') {{
                mermaid.initialize({{
                    startOnLoad: true,
                    theme: 'default',
                    securityLevel: 'loose',
                    fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif'
                }});
            }}
        }});
    </script>
    <script>
{toc_js}
    </script>
</body>
</html>"""


def generate_index_html(md_files, base_css):
    """Generate index.html with report cards."""
    cards = []
    for md_file in sorted(md_files):
        stem = md_file.stem
        info = REPORT_INFO.get(stem, (stem, ""))
        title, desc = info
        is_master = stem.startswith("00_")
        cls = "report-index-card master-card" if is_master else "report-index-card"

        cards.append(f"""
            <div class="{cls}">
                <h4><a href="{stem}.html">{title}</a></h4>
                <p>{desc}</p>
                <div class="card-links">
                    <a href="{stem}.html">HTML</a>
                    <a href="../docx/{stem}.docx">DOCX</a>
                </div>
            </div>""")

    cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KRX 24시간 거래 도입 전략 - 리포트 인덱스</title>
    <style>
{base_css}

body {{ background: #f0f4f8; }}

.index-page {{
    max-width: 960px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
}}

.index-header {{
    text-align: center;
    padding: 2.5rem 0;
    margin-bottom: 2rem;
}}

.index-header h1 {{
    font-size: 2.2rem;
    color: var(--primary);
    border: none;
    margin: 0 0 0.3rem;
}}

.index-header .subtitle {{
    color: var(--text-secondary);
    font-size: 1.1rem;
}}

.index-header .date {{
    color: #a0aec0;
    font-size: 0.85rem;
    margin-top: 0.5rem;
}}

.master-card {{
    border: 2px solid var(--primary) !important;
    background: linear-gradient(135deg, #ebf4ff, #f0f7ff) !important;
    grid-column: 1 / -1;
}}

.master-card h4 {{ font-size: 1.1rem !important; }}

.report-index-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1rem;
}}

.report-index-card {{
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    background: #fff;
    transition: box-shadow 0.2s, transform 0.15s;
}}

.report-index-card:hover {{
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}}

.report-index-card h4 {{
    margin: 0 0 0.3rem;
    font-size: 0.95rem;
    color: var(--primary);
}}

.report-index-card h4 a {{
    text-decoration: none;
    color: inherit;
}}

.report-index-card h4 a:hover {{ color: var(--accent); }}

.report-index-card p {{
    margin: 0 0 0.7rem;
    font-size: 0.82rem;
    color: var(--text-secondary);
    line-height: 1.5;
}}

.card-links a {{
    display: inline-block;
    margin-right: 0.8rem;
    padding: 0.25rem 0.7rem;
    font-size: 0.8rem;
    text-decoration: none;
    color: var(--primary-light);
    border: 1px solid var(--border);
    border-radius: 4px;
    transition: all 0.15s;
}}

.card-links a:hover {{
    background: var(--primary);
    color: #fff;
    border-color: var(--primary);
}}

.footer {{
    text-align: center;
    color: #a0aec0;
    font-size: 0.8rem;
    margin-top: 2.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
}}
    </style>
</head>
<body>
    <div class="index-page">
        <div class="index-header">
            <h1>KRX 24시간 거래 도입 전략</h1>
            <div class="subtitle">글로벌 비교 분석 리포트 시리즈</div>
            <div class="date">2026년 3월 27일</div>
        </div>

        <div class="report-index-grid">
{cards_html}
        </div>

        <div class="footer">
            EXTURE 3.0 기반 &middot; KRX 12시간 거래 2026.09.14 &middot; KRX 24시간 거래 2027.12 목표
        </div>
    </div>
</body>
</html>"""


def convert_to_docx(md_file, docx_file):
    """Convert MD directly to DOCX using pandoc (avoids sidebar HTML issues)."""
    try:
        result = subprocess.run(
            [
                "pandoc",
                str(md_file),
                "-f", "markdown",
                "-t", "docx",
                "-o", str(docx_file),
                "--wrap=none",
                "--toc",
                "--toc-depth=3",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print(f"  [ERROR] pandoc: {result.stderr[:200]}")
            return False
        return True
    except FileNotFoundError:
        print("  [ERROR] pandoc not found")
        return False
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] pandoc timed out")
        return False


def main():
    parser = argparse.ArgumentParser(description="KRX 리포트 빌드 v2")
    parser.add_argument("--html-only", action="store_true")
    parser.add_argument("--docx-only", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if not any([args.html_only, args.docx_only, args.all]):
        args.all = True

    HTML_DIR.mkdir(parents=True, exist_ok=True)
    DOCX_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(MD_DIR.glob("*.md"))
    if not md_files:
        print("[ERROR] No .md files found")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files")

    base_css = CSS_FILE.read_text(encoding="utf-8") if CSS_FILE.exists() else ""
    sidebar_css = get_sidebar_css()
    toc_js = get_toc_js()
    mermaid_js = MERMAID_JS.read_text(encoding="utf-8") if MERMAID_JS.exists() else ""

    if args.html_only or args.all:
        print("\n=== Generating HTML (sidebar TOC) ===")
        for md_file in md_files:
            print(f"  {md_file.name}")
            try:
                html = generate_html(md_file, base_css, sidebar_css, toc_js, mermaid_js)
                out = HTML_DIR / (md_file.stem + ".html")
                out.write_text(html, encoding="utf-8")
                print(f"    -> {out.name} ({out.stat().st_size / 1024:.0f} KB)")
            except Exception as e:
                print(f"    [ERROR] {e}")

        print("  index.html")
        try:
            idx = generate_index_html(md_files, base_css)
            out = HTML_DIR / "index.html"
            out.write_text(idx, encoding="utf-8")
            print(f"    -> index.html ({out.stat().st_size / 1024:.0f} KB)")
        except Exception as e:
            print(f"    [ERROR] {e}")

    if args.docx_only or args.all:
        print("\n=== Generating DOCX (from MD via pandoc) ===")
        for md_file in md_files:
            docx_file = DOCX_DIR / (md_file.stem + ".docx")
            print(f"  {md_file.stem}.docx")
            if convert_to_docx(md_file, docx_file):
                print(f"    -> {docx_file.name} ({docx_file.stat().st_size / 1024:.0f} KB)")

    html_count = len(list(HTML_DIR.glob("*.html")))
    docx_count = len(list(DOCX_DIR.glob("*.docx")))
    print(f"\n=== Build Complete ===")
    print(f"  HTML: {html_count} files")
    print(f"  DOCX: {docx_count} files")


if __name__ == "__main__":
    main()
