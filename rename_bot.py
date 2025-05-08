import os           

def rename_files(folder_path,prefix):
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    for index, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{index}{file_ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")
        
folder = "D:/porto/FolderFoto"  # Ganti dengan path folder kamu
prefix = "Foto_Banner"
rename_files(folder, prefix)
        
