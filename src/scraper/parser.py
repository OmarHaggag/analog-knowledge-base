"""
HTML to Markdown Parser for Analog Devices Course.
This script reads raw HTML files, extracts the core educational content 
(removing menus, footers, etc.), and converts it to clean Markdown.
"""

import os
import glob
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ==========================================
# Configuration & Constants
# ==========================================
INPUT_DIR = os.path.join("data", "raw_html")
OUTPUT_DIR = os.path.join("data", "markdown")

def setup_directories():
    """Ensure the output directory exists before saving files."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"[*] Ensured output directory exists: {OUTPUT_DIR}")

def clean_html(html_content: str) -> str:
    """
    Parses HTML and removes unnecessary elements like navigation, 
    footers, and scripts to isolate the main educational content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Remove inherently noisy tags (scripts, styles, menus)
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    # 2. Extract the main content.
    # Analog Devices uses DokuWiki, which usually wraps content in these specific divs.
    main_content = soup.find('div', id='dokuwiki__content')
    
    if not main_content:
        main_content = soup.find('div', class_='page')
        
    # Fallback if the structure is different: use the body
    if not main_content:
        main_content = soup.find('body')

    # Return the HTML string of just the relevant part
    return str(main_content) if main_content else str(soup)

def process_files():
    """Reads HTML files, converts them to Markdown, and saves them."""
    # Find all HTML files in the input directory, sorted alphabetically
    html_files = sorted(glob.glob(os.path.join(INPUT_DIR, "*.html")))
    
    if not html_files:
        print("[!] No HTML files found. Did the crawler run successfully?")
        return

    print(f"[*] Found {len(html_files)} HTML files to process.\n")

    for filepath in html_files:
        filename = os.path.basename(filepath)
        # Create the new filename by replacing .html with .md
        md_filename = filename.replace(".html", ".md")
        md_filepath = os.path.join(OUTPUT_DIR, md_filename)

        print(f"[*] Converting: {filename} -> {md_filename}")

        with open(filepath, 'r', encoding='utf-8') as f:
            raw_html = f.read()

        # Step 1: Clean the HTML
        cleaned_html = clean_html(raw_html)

        # Step 2: Convert to Markdown
        # heading_style="ATX" ensures we get '#' instead of underlined headings, better for LLMs
        markdown_content = md(cleaned_html, heading_style="ATX")

        # Step 3: Save to the markdown directory
        with open(md_filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

def main():
    setup_directories()
    process_files()
    print("\n[+] Parsing and Markdown conversion completed successfully!")

if __name__ == "__main__":
    main()