import os

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

target = 'href="styles.css?v=13"'
replacement = 'href="styles.css?v=14"'

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(target, replacement)
        
        # In case some have no version or different version
        if new_content == content:
             # Try a more general match
             import re
             new_content = re.sub(r'href="styles\.css(\?v=\d+)?"', 'href="styles.css?v=14"', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"File {file} not found")
