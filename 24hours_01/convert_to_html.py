#!/usr/bin/env python3
"""
MD -> Interactive HTML Report Converter (v2)
- Sidebar TOC with scroll spy
- In-page search with highlight
- Dark mode toggle
- SVG charts for 00_종합비교 (inline, no external deps)
- All resources inline (works offline / air-gapped)
- Cross-report navigation via sidebar dropdown
- .md links auto-converted to .html links
"""

import re
import markdown
from pathlib import Path

REPORTS_DIR = Path(__file__).parent / "reports"
OUTPUT_DIR = Path(__file__).parent / "output" / "html"

REPORT_FILES = [
    ("00_종합비교_요약.md", "종합 비교 요약", "chart"),
    ("01_KRX_한국거래소.md", "KRX 한국거래소", "kr"),
    ("02_NYSE_뉴욕증권거래소.md", "NYSE 뉴욕증권거래소", "us"),
    ("03_NASDAQ_나스닥.md", "NASDAQ 나스닥", "us"),
    ("04_24X_Exchange.md", "24X Exchange", "us"),
    ("05_CME_Group.md", "CME Group", "us"),
    ("06_DTCC_청산결제.md", "DTCC 청산결제", "us"),
    ("07_LSE_런던증권거래소.md", "LSE 런던증권거래소", "eu"),
    ("08_JPX_도쿄증권거래소.md", "JPX 도쿄증권거래소", "jp"),
    ("09_Blue_Ocean_ATS.md", "Blue Ocean ATS", "us"),
    ("10_유럽거래소_Eurex_Euronext.md", "유럽거래소 Eurex/Euronext", "eu"),
]

ICON_MAP = {"chart": "&#128202;", "kr": "&#127472;&#127479;", "us": "&#127482;&#127480;",
            "eu": "&#127466;&#127482;", "jp": "&#127471;&#127477;"}


def slugify(text):
    """Create a URL-safe slug from heading text."""
    text = re.sub(r'[^\w\s가-힣-]', '', text)
    text = re.sub(r'\s+', '-', text.strip())
    return text.lower()


def convert_md_to_html(md_text, is_summary=False):
    """Convert markdown to HTML. Fix internal .md links to .html."""
    extensions = ['tables', 'fenced_code', 'sane_lists']
    html = markdown.markdown(md_text, extensions=extensions)

    # Convert .md links to .html links
    html = re.sub(r'href="([^"]*?)\.md"', r'href="\1.html"', html)

    # Add IDs to headings for anchor navigation
    def add_heading_id(match):
        tag = match.group(1)
        content = match.group(2)
        slug = slugify(re.sub(r'<[^>]+>', '', content))
        return f'<{tag} id="{slug}">{content}</{tag}>'

    html = re.sub(r'<(h[1-4])>(.*?)</\1>', add_heading_id, html)

    return html


def get_chart_html():
    """Generate inline SVG charts for the summary report."""
    return """
<div id="charts-container" style="margin:30px 0;">
  <h2 id="visual-charts" style="color:var(--accent);margin-bottom:20px;">거래시간 시각화 비교</h2>

  <!-- Trading Hours Bar Chart -->
  <div style="background:var(--sidebar-bg);border:1px solid var(--border);border-radius:12px;padding:25px;margin-bottom:25px;">
    <h3 style="margin-bottom:15px;font-size:16px;">거래소별 일일 운영시간 (시간)</h3>
    <svg viewBox="0 0 700 320" style="width:100%;max-width:700px;">
      <!-- Grid lines -->
      <line x1="120" y1="30" x2="120" y2="280" stroke="var(--border)" stroke-width="1"/>
      <line x1="120" y1="280" x2="680" y2="280" stroke="var(--border)" stroke-width="1"/>
      <!-- Y axis labels & grid -->
      <text x="115" y="280" text-anchor="end" fill="var(--text)" font-size="11">0</text>
      <text x="115" y="230" text-anchor="end" fill="var(--text)" font-size="11">6</text>
      <line x1="120" y1="230" x2="680" y2="230" stroke="var(--border)" stroke-width="0.5" stroke-dasharray="4"/>
      <text x="115" y="180" text-anchor="end" fill="var(--text)" font-size="11">12</text>
      <line x1="120" y1="180" x2="680" y2="180" stroke="var(--border)" stroke-width="0.5" stroke-dasharray="4"/>
      <text x="115" y="130" text-anchor="end" fill="var(--text)" font-size="11">18</text>
      <line x1="120" y1="130" x2="680" y2="130" stroke="var(--border)" stroke-width="0.5" stroke-dasharray="4"/>
      <text x="115" y="80" text-anchor="end" fill="var(--text)" font-size="11">24</text>
      <line x1="120" y1="80" x2="680" y2="80" stroke="var(--border)" stroke-width="0.5" stroke-dasharray="4"/>

      <!-- Bars: height = hours * (200/24) from y=280 -->
      <!-- KRX: 10h -->
      <rect x="135" y="197" width="45" height="83" rx="4" fill="#0066cc"/>
      <text x="157" y="192" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">10h</text>
      <text x="157" y="300" text-anchor="middle" fill="var(--text)" font-size="10">KRX</text>

      <!-- NYSE Arca: 23h -->
      <rect x="200" y="89" width="45" height="191" rx="4" fill="#2196F3"/>
      <text x="222" y="84" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">23h</text>
      <text x="222" y="300" text-anchor="middle" fill="var(--text)" font-size="10">NYSE</text>

      <!-- NASDAQ: 23h -->
      <rect x="265" y="89" width="45" height="191" rx="4" fill="#42A5F5"/>
      <text x="287" y="84" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">23h</text>
      <text x="287" y="300" text-anchor="middle" fill="var(--text)" font-size="10">NASDAQ</text>

      <!-- 24X: 23h -->
      <rect x="330" y="89" width="45" height="191" rx="4" fill="#64B5F6"/>
      <text x="352" y="84" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">23h</text>
      <text x="352" y="300" text-anchor="middle" fill="var(--text)" font-size="10">24X</text>

      <!-- CME: 23h -->
      <rect x="395" y="89" width="45" height="191" rx="4" fill="#90CAF9"/>
      <text x="417" y="84" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">23h</text>
      <text x="417" y="300" text-anchor="middle" fill="var(--text)" font-size="10">CME</text>

      <!-- LSE: 8.5h -->
      <rect x="460" y="209" width="45" height="71" rx="4" fill="#FF9800"/>
      <text x="482" y="204" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">8.5h</text>
      <text x="482" y="300" text-anchor="middle" fill="var(--text)" font-size="10">LSE</text>

      <!-- TSE: 5.5h -->
      <rect x="525" y="234" width="45" height="46" rx="4" fill="#F44336"/>
      <text x="547" y="229" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">5.5h</text>
      <text x="547" y="300" text-anchor="middle" fill="var(--text)" font-size="10">TSE</text>

      <!-- Xetra: 14.5h (with retail) -->
      <rect x="590" y="159" width="45" height="121" rx="4" fill="#4CAF50"/>
      <text x="612" y="154" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">14.5h</text>
      <text x="612" y="300" text-anchor="middle" fill="var(--text)" font-size="10">Xetra</text>
    </svg>
  </div>

  <!-- Latency Comparison -->
  <div style="background:var(--sidebar-bg);border:1px solid var(--border);border-radius:12px;padding:25px;margin-bottom:25px;">
    <h3 style="margin-bottom:15px;font-size:16px;">매칭엔진 레이턴시 비교 (microseconds)</h3>
    <svg viewBox="0 0 700 220" style="width:100%;max-width:700px;">
      <line x1="180" y1="190" x2="680" y2="190" stroke="var(--border)" stroke-width="1"/>
      <!-- KRX EXTURE 3.0: 50us -->
      <text x="175" y="35" text-anchor="end" fill="var(--text)" font-size="11">KRX (EXTURE 3.0)</text>
      <rect x="180" y="25" width="198" height="22" rx="4" fill="#0066cc"/>
      <text x="383" y="40" fill="var(--text)" font-size="11" font-weight="bold"> 50 us</text>

      <!-- NASDAQ: <100us -->
      <text x="175" y="65" text-anchor="end" fill="var(--text)" font-size="11">NASDAQ</text>
      <rect x="180" y="55" width="396" height="22" rx="4" fill="#42A5F5"/>
      <text x="581" y="70" fill="var(--text)" font-size="11" font-weight="bold"> &lt;100 us</text>

      <!-- LSE Millennium: 126us -->
      <text x="175" y="95" text-anchor="end" fill="var(--text)" font-size="11">LSE (Millennium)</text>
      <rect x="180" y="85" width="500" height="22" rx="4" fill="#FF9800"/>
      <text x="685" y="100" fill="var(--text)" font-size="11" font-weight="bold"> 126 us</text>

      <!-- Xetra T7: <10us -->
      <text x="175" y="125" text-anchor="end" fill="var(--text)" font-size="11">Xetra (T7)</text>
      <rect x="180" y="115" width="40" height="22" rx="4" fill="#4CAF50"/>
      <text x="225" y="130" fill="var(--text)" font-size="11" font-weight="bold"> &lt;10 us</text>

      <!-- NYSE, 24X, CME: microsecond-level -->
      <text x="175" y="155" text-anchor="end" fill="var(--text)" font-size="11">NYSE/24X/CME</text>
      <rect x="180" y="145" width="100" height="22" rx="4" fill="#9E9E9E"/>
      <text x="285" y="160" fill="var(--text)" font-size="11"> us급 (비공개)</text>

      <text x="180" y="185" fill="var(--text)" font-size="10" opacity="0.6">* 낮을수록 빠름. 비공개 거래소는 추정치 표시.</text>
    </svg>
  </div>

  <!-- Settlement Cycle Timeline -->
  <div style="background:var(--sidebar-bg);border:1px solid var(--border);border-radius:12px;padding:25px;margin-bottom:25px;">
    <h3 style="margin-bottom:15px;font-size:16px;">글로벌 결제 주기(T+N) 전환 타임라인</h3>
    <svg viewBox="0 0 700 160" style="width:100%;max-width:700px;">
      <!-- Timeline axis -->
      <line x1="50" y1="80" x2="670" y2="80" stroke="var(--border)" stroke-width="2"/>
      <!-- 2024 -->
      <circle cx="150" cy="80" r="8" fill="#2196F3"/>
      <text x="150" y="65" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">2024.5</text>
      <text x="150" y="110" text-anchor="middle" fill="var(--text)" font-size="10">US/CA T+1</text>
      <!-- 2026 -->
      <circle cx="350" cy="80" r="8" fill="#0066cc"/>
      <text x="350" y="65" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">2026.3</text>
      <text x="350" y="110" text-anchor="middle" fill="var(--text)" font-size="10">KRX T+1</text>
      <text x="350" y="125" text-anchor="middle" fill="var(--text)" font-size="9" opacity="0.7">공식 추진 발표</text>
      <!-- 2027 -->
      <circle cx="550" cy="80" r="8" fill="#4CAF50"/>
      <text x="550" y="65" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">2027.10</text>
      <text x="550" y="110" text-anchor="middle" fill="var(--text)" font-size="10">EU/UK T+1</text>
      <!-- Labels -->
      <text x="50" y="150" fill="var(--text)" font-size="10" opacity="0.6">* KRX 구체적 시행일은 워킹그룹 논의 중</text>
    </svg>
  </div>
</div>
"""


def build_report_select_html(current_filename):
    """Build the report navigation dropdown for sidebar."""
    options = []
    for fname, title, icon_key in REPORT_FILES:
        html_name = fname.replace('.md', '.html')
        selected = ' selected' if fname == current_filename else ''
        icon = ICON_MAP.get(icon_key, '')
        options.append(f'<option value="{html_name}"{selected}>{icon} {title}</option>')
    return '\n'.join(options)


def generate_individual_html(filename, title, md_content):
    """Generate an individual HTML file for each report."""
    is_summary = filename.startswith("00_")
    html_content = convert_md_to_html(md_content, is_summary)

    report_select = build_report_select_html(filename)

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 24시간 거래 체제 분석 리포트</title>
    <style>
        :root {{
            --bg: #ffffff; --text: #1a1a2e; --sidebar-bg: #f8f9fa; --border: #dee2e6;
            --accent: #0066cc; --accent-light: #e7f1ff; --table-header: #0066cc;
            --table-header-text: #ffffff; --table-border: #d0d7de; --code-bg: #f6f8fa;
            --highlight: #fff3cd; --hover-bg: #e9ecef;
        }}
        [data-theme="dark"] {{
            --bg: #0f0f1a; --text: #d8d8e8; --sidebar-bg: #161625; --border: #2a2a45;
            --accent: #4da6ff; --accent-light: #1a2a4a; --table-header: #1e3a5f;
            --table-header-text: #e0e8f0; --table-border: #2a3a4a; --code-bg: #1e2a3a;
            --highlight: #3a3520; --hover-bg: #1e1e35;
        }}
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Malgun Gothic', 'Segoe UI', sans-serif;
            background: var(--bg); color: var(--text); line-height: 1.75;
        }}

        /* Sidebar */
        .sidebar {{
            width: 280px; position: fixed; top: 0; left: 0; height: 100vh;
            background: var(--sidebar-bg); border-right: 1px solid var(--border);
            overflow-y: auto; z-index: 100; transition: transform 0.25s ease;
            display: flex; flex-direction: column;
        }}
        .sidebar.collapsed {{ transform: translateX(-280px); }}
        .sidebar-header {{ padding: 16px 16px 12px; border-bottom: 1px solid var(--border); }}
        .sidebar-header h2 {{ font-size: 13px; color: var(--accent); letter-spacing: 0.5px; text-transform: uppercase; }}
        .sidebar-header select {{
            width: 100%; margin-top: 8px; padding: 7px 8px; border: 1px solid var(--border);
            border-radius: 6px; font-size: 12px; background: var(--bg); color: var(--text); cursor: pointer;
        }}
        .toc {{ flex: 1; overflow-y: auto; padding: 8px 0; }}
        .toc a {{
            display: block; padding: 5px 16px; color: var(--text); text-decoration: none;
            font-size: 12.5px; border-left: 3px solid transparent; transition: all 0.15s;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        }}
        .toc a:hover {{ background: var(--hover-bg); }}
        .toc a.active {{ border-left-color: var(--accent); color: var(--accent); font-weight: 600; background: var(--accent-light); }}
        .toc a.depth-3 {{ padding-left: 30px; font-size: 11.5px; opacity: 0.85; }}
        .toc a.depth-4 {{ padding-left: 44px; font-size: 11px; opacity: 0.7; }}

        /* Top bar */
        .topbar {{
            position: fixed; top: 0; right: 0; left: 280px; height: 48px;
            background: var(--bg); border-bottom: 1px solid var(--border);
            display: flex; align-items: center; padding: 0 20px; gap: 10px; z-index: 90;
            transition: left 0.25s ease;
        }}
        .topbar.expanded {{ left: 0; }}
        .topbar button {{
            padding: 6px 12px; border: 1px solid var(--border); border-radius: 6px;
            background: var(--sidebar-bg); color: var(--text); cursor: pointer; font-size: 13px;
            white-space: nowrap;
        }}
        .topbar button:hover {{ background: var(--hover-bg); }}
        .topbar input {{
            flex: 1; max-width: 350px; padding: 6px 12px; border: 1px solid var(--border);
            border-radius: 6px; font-size: 12px; background: var(--sidebar-bg); color: var(--text);
        }}
        .search-count {{ font-size: 11px; color: var(--accent); min-width: 50px; }}

        /* Main content */
        main {{
            margin-left: 280px; padding: 68px 50px 60px;
            transition: margin-left 0.25s ease;
        }}
        main.expanded {{ margin-left: 0; }}
        h1 {{ font-size: 26px; margin: 25px 0 18px; padding-bottom: 8px; border-bottom: 2px solid var(--accent); }}
        h2 {{ font-size: 20px; margin: 28px 0 14px; color: var(--accent); }}
        h3 {{ font-size: 16px; margin: 22px 0 10px; }}
        h4 {{ font-size: 14px; margin: 18px 0 8px; }}
        p {{ margin: 8px 0; }}
        a {{ color: var(--accent); }}

        /* Tables - responsive */
        .table-wrap {{
            overflow-x: auto; margin: 14px 0; border-radius: 8px;
            border: 1px solid var(--table-border);
            -webkit-overflow-scrolling: touch;
            max-width: 100%;
        }}
        table {{ border-collapse: collapse; font-size: 12.5px; width: max-content; min-width: 100%; }}
        th {{ background: var(--table-header); color: var(--table-header-text); font-weight: 600;
              padding: 9px 10px; text-align: left; border: 1px solid var(--table-border);
              position: sticky; top: 0; white-space: nowrap; }}
        td {{ padding: 8px 10px; border: 1px solid var(--table-border); word-break: keep-all; }}
        tr:nth-child(even) {{ background: var(--sidebar-bg); }}
        tr:hover {{ background: var(--accent-light); }}
        /* First column sticky on wide tables */
        th:first-child, td:first-child {{ position: sticky; left: 0; z-index: 1; background: inherit; }}
        th:first-child {{ z-index: 2; }}
        tr:nth-child(odd) td:first-child {{ background: var(--bg); }}
        tr:nth-child(even) td:first-child {{ background: var(--sidebar-bg); }}
        tr:hover td:first-child {{ background: var(--accent-light); }}
        th:first-child {{ background: var(--table-header); }}

        code {{ background: var(--code-bg); padding: 1px 5px; border-radius: 3px; font-size: 12px; }}
        blockquote {{
            border-left: 4px solid var(--accent); padding: 10px 18px; margin: 14px 0;
            background: var(--accent-light); border-radius: 0 8px 8px 0; font-size: 13px;
        }}
        ul, ol {{ padding-left: 22px; margin: 8px 0; }}
        li {{ margin: 4px 0; }}
        hr {{ border: none; border-top: 1px solid var(--border); margin: 25px 0; }}
        mark {{ background: #ffe066; padding: 0 3px; border-radius: 2px; }}
        strong {{ color: var(--accent); }}

        @media (max-width: 768px) {{
            .sidebar {{ transform: translateX(-280px); }}
            .sidebar.mobile-show {{ transform: translateX(0); }}
            main {{ margin-left: 0 !important; padding: 60px 12px 40px; }}
            .topbar {{ left: 0 !important; }}
            table {{ font-size: 11px; }}
            th, td {{ padding: 6px 7px; }}
            h1 {{ font-size: 20px; }}
            h2 {{ font-size: 17px; }}
            h3 {{ font-size: 14px; }}
        }}
        @media (max-width: 480px) {{
            main {{ padding: 56px 8px 30px; }}
            table {{ font-size: 10px; }}
            th, td {{ padding: 5px 5px; }}
            .topbar input {{ max-width: 150px; }}
        }}
        @media print {{
            .sidebar, .topbar {{ display: none !important; }}
            main {{ margin: 0 !important; padding: 10px !important; max-width: 100%; }}
            .table-wrap {{ overflow: visible; }}
            table {{ min-width: 0; }}
        }}
    </style>
</head>
<body>
    <nav class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <h2>24H Trading Report</h2>
            <select onchange="if(this.value)location.href=this.value">
                {report_select}
            </select>
        </div>
        <div class="toc" id="toc"></div>
    </nav>

    <div class="topbar" id="topbar">
        <button id="toggleBtn" onclick="toggleSidebar()" title="Toggle sidebar">&#9776;</button>
        <input type="text" id="searchInput" placeholder="Search..." oninput="doSearch(this.value)">
        <span class="search-count" id="searchCount"></span>
        <button onclick="toggleTheme()" title="Toggle dark mode">&#9681;</button>
        <button onclick="window.print()" title="Print">&#128424;</button>
    </div>

    <main id="main">
        {html_content}
    </main>

    <script>
    (function() {{
        // --- Wrap tables ---
        document.querySelectorAll('main table').forEach(t => {{
            if (!t.parentElement.classList.contains('table-wrap')) {{
                const w = document.createElement('div');
                w.className = 'table-wrap';
                t.parentNode.insertBefore(w, t);
                w.appendChild(t);
            }}
        }});

        // --- Build TOC ---
        const toc = document.getElementById('toc');
        const headings = document.querySelectorAll('main h1, main h2, main h3');
        const tocLinks = [];
        headings.forEach(h => {{
            const a = document.createElement('a');
            a.href = '#' + h.id;
            a.textContent = h.textContent;
            a.dataset.id = h.id;
            const depth = parseInt(h.tagName[1]);
            if (depth >= 3) a.classList.add('depth-' + depth);
            toc.appendChild(a);
            tocLinks.push({{ el: h, link: a }});
        }});

        // --- Scroll spy ---
        let ticking = false;
        function updateActive() {{
            const scrollY = window.scrollY + 100;
            let current = tocLinks[0];
            for (const item of tocLinks) {{
                if (item.el.offsetTop <= scrollY) current = item;
            }}
            tocLinks.forEach(i => i.link.classList.remove('active'));
            if (current) {{
                current.link.classList.add('active');
                current.link.scrollIntoView({{ block: 'nearest' }});
            }}
            ticking = false;
        }}
        window.addEventListener('scroll', () => {{
            if (!ticking) {{ requestAnimationFrame(updateActive); ticking = true; }}
        }});
        updateActive();

        // --- Smooth scroll for TOC links ---
        toc.addEventListener('click', e => {{
            if (e.target.tagName === 'A') {{
                e.preventDefault();
                const target = document.getElementById(e.target.dataset.id);
                if (target) target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                history.replaceState(null, '', e.target.href);
            }}
        }});

        // --- Smooth scroll for in-content anchor links ---
        document.querySelectorAll('main a[href^="#"]').forEach(a => {{
            a.addEventListener('click', e => {{
                const id = decodeURIComponent(a.getAttribute('href').slice(1));
                const target = document.getElementById(id);
                if (target) {{
                    e.preventDefault();
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
    }})();

    // --- Sidebar toggle ---
    function toggleSidebar() {{
        const sb = document.getElementById('sidebar');
        const main = document.getElementById('main');
        const tb = document.getElementById('topbar');
        sb.classList.toggle('collapsed');
        main.classList.toggle('expanded');
        tb.classList.toggle('expanded');
    }}

    // --- Search ---
    let searchTimeout;
    function doSearch(q) {{
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => _search(q), 200);
    }}
    function _search(query) {{
        const main = document.getElementById('main');
        // Remove old marks
        main.querySelectorAll('mark[data-search]').forEach(m => {{
            const parent = m.parentNode;
            parent.replaceChild(document.createTextNode(m.textContent), m);
            parent.normalize();
        }});
        const countEl = document.getElementById('searchCount');
        if (!query || query.length < 2) {{ countEl.textContent = ''; return; }}
        const regex = new RegExp(query.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
        const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
        const nodes = [];
        while (walker.nextNode()) {{
            if (walker.currentNode.parentElement.tagName !== 'SCRIPT' &&
                regex.test(walker.currentNode.textContent)) {{
                nodes.push(walker.currentNode);
                regex.lastIndex = 0;
            }}
        }}
        let count = 0;
        nodes.forEach(node => {{
            const frag = document.createDocumentFragment();
            let last = 0;
            regex.lastIndex = 0;
            let m;
            while ((m = regex.exec(node.textContent)) !== null) {{
                frag.appendChild(document.createTextNode(node.textContent.slice(last, m.index)));
                const mark = document.createElement('mark');
                mark.setAttribute('data-search', '');
                mark.textContent = m[0];
                frag.appendChild(mark);
                last = regex.lastIndex;
                count++;
            }}
            frag.appendChild(document.createTextNode(node.textContent.slice(last)));
            node.parentNode.replaceChild(frag, node);
        }});
        countEl.textContent = count > 0 ? count + '건' : '0건';
        const first = main.querySelector('mark[data-search]');
        if (first) first.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    }}

    // --- Theme ---
    function toggleTheme() {{
        const d = document.body.dataset.theme === 'dark' ? '' : 'dark';
        document.body.dataset.theme = d;
        try {{ localStorage.setItem('theme', d); }} catch(e) {{}}
    }}
    try {{ if (localStorage.getItem('theme') === 'dark') document.body.dataset.theme = 'dark'; }} catch(e) {{}}
    </script>
</body>
</html>"""
    return html


def generate_index_html():
    """Generate an index page linking all reports."""
    cards = ""
    for filename, title, icon_key in REPORT_FILES:
        html_file = filename.replace('.md', '.html')
        icon = ICON_MAP.get(icon_key, '&#128200;')
        highlight = ' style="grid-column:1/-1;background:var(--accent);color:#fff;border-color:var(--accent);"' if filename.startswith("00_") else ''
        cards += f'        <a href="{html_file}" class="card"{highlight}><span class="icon">{icon}</span><span class="title">{title}</span></a>\n'

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>24시간 거래 체제 비교 분석 리포트</title>
    <style>
        :root {{ --bg:#f0f2f5; --card-bg:#fff; --text:#1a1a2e; --accent:#0066cc; --border:#dee2e6; }}
        [data-theme="dark"] {{ --bg:#0f0f1a; --card-bg:#161625; --text:#d8d8e8; --accent:#4da6ff; --border:#2a2a45; }}
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ font-family:-apple-system,BlinkMacSystemFont,'Malgun Gothic',sans-serif; background:var(--bg); color:var(--text); min-height:100vh; }}
        .header {{ text-align:center; padding:60px 20px 40px; }}
        .header h1 {{ font-size:30px; margin-bottom:10px; }}
        .header p {{ font-size:14px; opacity:0.7; }}
        .header .meta {{ font-size:11px; margin-top:12px; opacity:0.5; }}
        .theme-btn {{ position:fixed; top:12px; right:12px; padding:7px 12px; border:1px solid var(--border);
            border-radius:6px; background:var(--card-bg); color:var(--text); cursor:pointer; font-size:13px; }}
        .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:16px;
            max-width:1100px; margin:0 auto; padding:0 24px 50px; }}
        .card {{ display:flex; align-items:center; gap:14px; padding:18px 22px; background:var(--card-bg);
            border:1px solid var(--border); border-radius:10px; text-decoration:none; color:var(--text);
            transition:transform 0.2s,box-shadow 0.2s; }}
        .card:hover {{ transform:translateY(-2px); box-shadow:0 6px 20px rgba(0,0,0,0.08); }}
        .icon {{ font-size:24px; }} .title {{ font-size:14px; font-weight:600; }}
    </style>
</head>
<body>
    <button class="theme-btn" onclick="toggleTheme()">&#9681; Theme</button>
    <div class="header">
        <h1>24시간 거래 체제 비교 분석</h1>
        <p>KRX vs 글로벌 주요 거래소 - 제도, 시스템, 청산결제 종합 리포트</p>
        <div class="meta">2026.03 | EXTURE 3.0 | 11 Reports</div>
    </div>
    <div class="grid">
{cards}    </div>
    <script>
        function toggleTheme() {{
            const d = document.body.dataset.theme === 'dark' ? '' : 'dark';
            document.body.dataset.theme = d;
            try {{ localStorage.setItem('theme', d); }} catch(e) {{}}
        }}
        try {{ if (localStorage.getItem('theme') === 'dark') document.body.dataset.theme = 'dark'; }} catch(e) {{}}
    </script>
</body>
</html>"""


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename, title, _ in REPORT_FILES:
        md_path = REPORTS_DIR / filename
        if not md_path.exists():
            print(f"  [SKIP] {filename}")
            continue
        md_content = md_path.read_text(encoding='utf-8')
        html = generate_individual_html(filename, title, md_content)
        out_path = OUTPUT_DIR / filename.replace('.md', '.html')
        out_path.write_text(html, encoding='utf-8')
        print(f"  [OK] {out_path.name}")

    index = generate_index_html()
    (OUTPUT_DIR / "index.html").write_text(index, encoding='utf-8')
    print(f"  [OK] index.html")
    print(f"\n  Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
