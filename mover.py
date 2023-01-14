import os
import shutil
from pathlib import Path


def search_and_move(root_dir, file_extension, destination_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_extension):
                src_file = os.path.join(subdir, file)
                dst_file = os.path.join(destination_dir, file)
                shutil.move(src_file, dst_file)


# source of the directory form which you want to move files
src = r'D:\Frond End\Frond End Development'
# the destination folder to which you want to move the files to
des = r'D:\Frond End\Frond End Development'
root_dir = Path(src)
# file extension to be copied
file_extension = '.mp4'
destination_dir = Path(des)
if (root_dir.exists() and destination_dir.exists()):
    search_and_move(root_dir, file_extension, destination_dir)
    print("All files moved successfully!")
else:
    print("Either source or destination directory does not exits!")
