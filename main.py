from pathlib import Path

import os

img_directory = "img"

directories = ["img", "pdf_documents","compressed_files","music", "videos", "sheets", "txt_documents"]

# img - .jpg .png .jpeg .gif .jfif .tiff .tif .heic .jpe .bmp .dip .dcm .dng .eps .exr .heif .ico .nef .psd .raw .tga .webp .xcf
# pdf_documents .pdf_documents
# compressed_files: .zip .rar .7z .tar .cab .bzip2 .arj 


#todo

# check list of the directories insied of the existing folder, if directory is already created ask user for changeing the name of directory or for skipping renaming. 


def test_destination_directory(self):
    self.assertTrue(Path('path').exists())

for i in directories:
    path = Path(i).resolve()
    path.mkdir(exist_ok = True)
