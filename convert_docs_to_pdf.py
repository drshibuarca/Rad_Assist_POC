"""
Convert Markdown documentation to PDF with proper styling
Note: Mermaid diagrams will be shown as code blocks in PDF
For full diagram rendering, use a browser-based PDF export
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import os

# Paths
docs_dir = Path(
    r"c:\Users\Dr Shibu\OneDrive\Desktop\Git hub\Rad_Assist\Radiology Assistant\docs"
)
artifacts_dir = Path(
    r"C:\Users\Dr Shibu\.gemini\antigravity\brain\afc8f3ce-1c4d-42f2-ab3a-2eabf790a2de"
)

# Source markdown file
markdown_file = artifacts_dir / "technical_documentation.md"
output_pdf = docs_dir / "Radiology_Assistant_Technical_Documentation.pdf"

# Ensure docs directory exists
docs_dir.mkdir(exist_ok=True)

print(f"Reading markdown from: {markdown_file}")

# Read markdown content
with open(markdown_file, "r", encoding="utf-8") as f:
    md_content = f.read()

print(f"Converting markdown to HTML...")

# Convert markdown to HTML with extensions
html_content = markdown.markdown(
    md_content,
    extensions=[
        "extra",  # Tables, fenced code blocks
        "codehilite",  # Syntax highlighting
        "toc",  # Table of contents
        "sane_lists",  # Better list handling
        "nl2br",  # Newline to break
    ],
)

# Create full HTML document with CSS styling
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Radiology Assistant - Technical Documentation</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
            @bottom-center {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 10pt;
                color: #666;
            }}
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
        }}
        
        h1 {{
            color: #2563eb;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 10px;
            margin-top: 30px;
            page-break-before: always;
        }}
        
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        
        h2 {{
            color: #1e40af;
            border-bottom: 2px solid #93c5fd;
            padding-bottom: 8px;
            margin-top: 25px;
        }}
        
        h3 {{
            color: #1e3a8a;
            margin-top: 20px;
        }}
        
        h4 {{
            color: #1e293b;
            margin-top: 15px;
        }}
        
        code {{
            background-color: #f1f5f9;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
            color: #c7254e;
        }}
        
        pre {{
            background-color: #1e293b;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        
        pre code {{
            background-color: transparent;
            color: #e2e8f0;
            padding: 0;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            page-break-inside: avoid;
        }}
        
        th {{
            background-color: #2563eb;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            border: 1px solid #e2e8f0;
            padding: 10px;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8fafc;
        }}
        
        blockquote {{
            border-left: 4px solid #2563eb;
            padding-left: 15px;
            margin-left: 0;
            color: #64748b;
            font-style: italic;
        }}
        
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 5px 0;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #e2e8f0;
            margin: 30px 0;
        }}
        
        .mermaid-note {{
            background-color: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            margin: 15px 0;
            page-break-inside: avoid;
        }}
        
        .mermaid-note::before {{
            content: "📊 Mermaid Diagram:";
            font-weight: bold;
            display: block;
            margin-bottom: 10px;
            color: #b45309;
        }}
        
        a {{
            color: #2563eb;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        /* Cover page */
        .cover-page {{
            text-align: center;
            padding-top: 150px;
            page-break-after: always;
        }}
        
        .cover-title {{
            font-size: 36pt;
            color: #1e40af;
            margin-bottom: 20px;
        }}
        
        .cover-subtitle {{
            font-size: 18pt;
            color: #64748b;
            margin-bottom: 40px;
        }}
        
        .cover-version {{
            font-size: 14pt;
            color: #94a3b8;
        }}
    </style>
</head>
<body>
    <div class="cover-page">
        <div class="cover-title">Radiology Assistant</div>
        <div class="cover-subtitle">Comprehensive Technical Documentation</div>
        <div class="cover-version">Version 2.0 | December 2024</div>
    </div>
    {html_content}
</body>
</html>
"""

print(f"Generating PDF...")

# Convert HTML to PDF
HTML(string=full_html).write_pdf(output_pdf)

print(f"✅ PDF generated successfully!")
print(f"📄 Output: {output_pdf}")
print(f"📊 File size: {output_pdf.stat().st_size / 1024:.1f} KB")
print()
print("Note: Mermaid diagrams are shown as code blocks in PDF.")
print(
    "For interactive diagrams, view the original Markdown file in a Mermaid-compatible viewer."
)
