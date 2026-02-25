#!/usr/bin/env python3
"""
Scrapling - Web Scraping Tool
https://github.com/D4Vinci/Scrapling

Usage:
    source ~/.openclaw/workspace/.venv/bin/activate
    python3 ~/zaltyko-os/scripts/scrapling_tool.py <url> [css_selector]

Examples:
    python3 ~/zaltyko-os/scripts/scrapling_tool.py "https://example.com" "title"
    python3 ~/zaltyko-os/scripts/scrapling_tool.py "https://example.com" "h1"
"""
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from scrapling import Fetcher

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    url = sys.argv[1]
    selector = sys.argv[2] if len(sys.argv) > 2 else None
    
    f = Fetcher()
    resp = f.get(url, verify=False)
    
    print(f"Status: {resp.status}")
    print(f"URL: {resp.url}")
    print("---")
    
    if selector:
        elements = resp.css(selector)
        print(f"Found {len(elements)} elements matching '{selector}':")
        for i, el in enumerate(elements[:10]):
            try:
                text = el.text.strip()[:100]
                print(f"  [{i+1}] {text}")
            except:
                pass
    else:
        try:
            print(f"Title: {resp.css('title').first.text}")
        except:
            pass
        try:
            print(f"H1: {resp.css('h1').first.text}")
        except:
            pass

if __name__ == "__main__":
    main()
