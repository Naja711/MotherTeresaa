import os
import re

files = [
    "bursar.html",
    "establishment.html",
    "gallery.html",
    "index.html",
    "mission.html",
    "motto.html",
    "principal.html",
    "vision.html"
]

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace any version of styles.css?v=X with v=15
        new_content = re.sub(r'href="styles\.css(\?v=\d+)?"', 'href="styles.css?v=15"', content)

        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"No match found in {file}")
    else:
        print(f"File {file} not found")
