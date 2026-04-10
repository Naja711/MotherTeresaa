import os
import re

def update_html():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Pattern to match school image N .jpeg with any number of spaces or encode
    # But since we know the exact format, we can be specific
    
    for html_file in html_files:
        print(f"Updating {html_file}...")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace "school image" with "school_image"
        # We handle case 19 specially if needed, but the simple replace might catch it
        new_content = content.replace('school image', 'school_image')
        
        # Handle the special case for image 19 if it was school_image19jpeg.jpeg
        new_content = new_content.replace('school_image19jpeg.jpeg', 'school_image19.jpeg')
        
        if content != new_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  [UPDATED] {html_file}")
        else:
            print(f"  [NO CHANGE] {html_file}")

if __name__ == "__main__":
    update_html()
