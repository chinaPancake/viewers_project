from pathlib import Path
extensions = {
    '.jpg': 'images',
    '.png': 'images',
    '.jpeg': 'images',
    '.jfif':'images',
    '.gif': 'gifs',
    '.pdf': 'pdf_documents',
    '.txt': 'text',
    '.docx': 'documents',
    # Add more extensions and directories as needed
}

src_dir = Path.cwd()

for file in src_dir.glob("*"):
    if file.is_file():
        ext = file.suffix.lower()
        if ext in extensions:
            dest_dir = Path(extensions[ext])
            dest_dir.mkdir(exist_ok=True)

            new_path = dest_dir / file.name
            file.rename(new_path)

# img - .jpg .png .jpeg .gif .jfif .tiff .tif .heic .jpe .bmp .dip .dcm .dng .eps .exr .heif .ico .nef .psd .raw .tga .webp .xcf
# pdf_documents .pdf_documents
# compressed_files: .zip .rar .7z .tar .cab .bzip2 .arj 

#todo

# check list of the directories insied of the existing folder, if directory is already created ask user for changeing the name of directory or for skipping renaming. 


