import os

def rename_files():
    files = os.listdir('.')
    mapping = {}
    
    for f in files:
        if f.startswith('school image'):
            new_name = f.replace(' ', '_')
            if '19jpeg' in new_name:
                new_name = new_name.replace('19jpeg', '19')
            
            if f != new_name:
                mapping[f] = new_name
    
    for old, new in mapping.items():
        print(f"Renaming: '{old}' -> '{new}'")
        try:
            os.rename(old, new)
        except Exception as e:
            print(f"Error renaming {old}: {e}")

if __name__ == "__main__":
    rename_files()
