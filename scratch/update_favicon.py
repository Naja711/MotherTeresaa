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

target = '<link rel="icon" href="data:;base64,iVBORw0KGgo=">'
replacement = '<link rel="icon" type="image/jpg" href="assets/images/school_logo.jpg">'

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(target, replacement)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"File {file} not found")
