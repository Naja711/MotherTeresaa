import os
import re

def check_images():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    image_files = [f for f in os.listdir('.') if f.lower().endswith(('.jpeg', '.jpg', '.png', '.gif', '.webp'))]
    
    print(f"Found {len(html_files)} HTML files and {len(image_files)} image files.\n")
    
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
                # On Windows os.path.exists is case-insensitive, so we use listdir
                if src in os.listdir('.'):
                    print(f"  [OK] {src}")
                else:
                    # Check if it exists with a different case
                    exists_ci = any(f.lower() == src.lower() for f in os.listdir('.'))
                    if exists_ci:
                        actual = [f for f in os.listdir('.') if f.lower() == src.lower()][0]
                        print(f"  [WRONG CASE] {src} (Found as: {actual})")
                    else:
                        print(f"  [MISSING] {src}")

if __name__ == "__main__":
    check_images()
