# CLAUDE.md — Session 5: Build & Quality Assurance

## ROLE
You are the build engineer and final QA reviewer.
Convert all Korean .md files to HTML and DOCX. Run final quality checks.

## TASKS

### Task 1 — HTML Generation
For each file in deliverables/md/:
- Convert to fully offline, responsive HTML
- Embed Mermaid charts (no external CDN dependency)
- Include clickable TOC per report
- Consistent CSS styling across all reports

### Task 2 — DOCX Generation
For each file in deliverables/md/:
- Convert to .docx with proper heading hierarchy
- Tables must render correctly with borders
- Korean text encoding verified (UTF-8)

### Task 3 — Master Index
Create deliverables/index.html:
- Landing page linking to all HTML reports and DOCX downloads
- Display summary: exchanges covered, total sources, completion date

### Task 4 — Final QA Checklist
□ All 10 HTML files render correctly?
□ All 10 DOCX files open correctly?
□ All internal links in index.html functional?
□ No empty or placeholder sections in any report?
□ Mermaid charts visible without internet?
□ Source bibliography complete and linked?
□ research_gaps.md included as appendix?
□ No non-functional UI elements (remove stray sidebar links)?
