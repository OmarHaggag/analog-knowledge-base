#!/usr/bin/env python3
"""
Web Crawler for Analog Devices Electronics Course
This script fetches the Table of Contents (TOC), extracts chapter links,
and downloads the raw HTML for each chapter.
"""

import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ==========================================
# Configuration & Constants
# ==========================================
BASE_URL = "https://wiki.analog.com"
TOC_URL = "https://wiki.analog.com/university/courses/electronics/text/electronics-toc"
OUTPUT_DIR = os.path.join("data", "raw_html")

# The specific path all valid chapter links should contain
VALID_LINK_PATH = "/university/courses/electronics/text/"

def setup_directories():
    """Ensure the output directory exists before saving files."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"[*] Ensured output directory exists: {OUTPUT_DIR}")

def get_chapter_links(toc_url: str) -> list:
    """
    Fetches the TOC page and extracts all relevant chapter links.
    """
    print(f"[*] Fetching Table of Contents: {toc_url}")
    try:
        response = requests.get(toc_url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching TOC: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    chapter_links = []

    # Find all anchor tags (links)
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        # Filter: We only want links that belong to the course text
        # and we want to exclude the TOC page itself to avoid an infinite loop
        if VALID_LINK_PATH in href and "electronics-toc" not in href:
            # Resolve relative URLs (e.g., /university/...) to absolute URLs
            full_url = urljoin(BASE_URL, href)
            
            # Avoid duplicates
            if full_url not in chapter_links:
                chapter_links.append(full_url)

    print(f"[*] Found {len(chapter_links)} chapter links.")
    return chapter_links

def download_page(url: str, index: int):
    """
    Downloads a single HTML page and saves it to the output directory.
    """
    try:
        print(f"[*] Downloading ({index}): {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract the last part of the URL to use as a filename
        # e.g., 'chapter-1' from '.../text/chapter-1'
        page_name = url.split('/')[-1]
        if not page_name:
            page_name = f"page_{index}"
            
        filename = f"{index:02d}_{page_name}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(response.text)
            
        print(f"[+] Saved: {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Failed to download {url}: {e}")

def main():
    setup_directories()
    
    # Step 1: Get all links from the TOC
    links = get_chapter_links(TOC_URL)
    
    if not links:
        print("[!] No links found. Exiting.")
        return

    # Step 2: Loop through links and download them
    print("\n[*] Starting download process...")
    for i, link in enumerate(links, start=1):
        download_page(link, i)
        
        # Be polite to the server, wait 1 second between requests
        time.sleep(1)
        
    print("\n[+] Crawling completed successfully!")

if __name__ == "__main__":
    main()