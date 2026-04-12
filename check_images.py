import os
import re

def check_images():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    img_tag_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
    
    for html_file in html_files:
        print(f"Checking {html_file}...")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = img_tag_pattern.findall(content)
            for src in matches:
                # Skip external URLs
                if src.startswith(('http', 'https', 'data:')):
                    continue
                
                # Check if file exists (case-sensitive)
                # Normalize path separators for Windows/Linux
                normalized_path = src.replace('/', os.sep)
                
                if os.path.exists(normalized_path):
                    print(f"  [OK] {src}")
                else:
                    print(f"  [MISSING] {src}")

if __name__ == "__main__":
    check_images()
