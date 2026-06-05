import os
import hashlib

# function to calculate file hash
def get_file_hash(file_path):
    hash_obj = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                hash_obj.update(chunk)
    except Exception:
        print(f"Error reading: {file_path}")
        return None
    return hash_obj.hexdigest()

# function to find duplicate files
def find_duplicates(folder_path):
    hash_map = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash is None:
                continue
            if file_hash in hash_map:
                hash_map[file_hash].append(file_path)
            else:
                hash_map[file_hash] = [file_path]

    found = False
    for file_list in hash_map.values():
        if len(file_list) > 1:
            if not found:
                print("\nDuplicate files found:\n")
                found = True
            for i, file in enumerate(file_list):
                print(f"{i+1}. {file}")
            print()

            # Ask user if they want to delete duplicates (keep first file)
            choice = input("Delete duplicates and keep the first file? (y/n): ")
            if choice.lower() == 'y':
                for dup_file in file_list[1:]:
                    try:
                        os.remove(dup_file)
                        print(f"Deleted: {dup_file}")
                    except Exception as e:
                        print(f"Error deleting {dup_file}: {e}")

    if not found:
        print("No duplicates found.")

# run the script
folder = input("Enter folder path: ")
find_duplicates(folder)
