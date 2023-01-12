import shutil
from pathlib import Path
# A simple python script which copies files from a directory to a single folder

# source of the directory from which files will be copied
source_path = Path(r"D:\Folder\Folder Name ")
# the target path where files are copied
target_path = Path(r"C:\Folder\Folder Name")
if (source_path.exists() and target_path.exists()):
    # set the file type here , .mp4 in this case
    py_files = [p for p in source_path.rglob("*.mp4")]
    for file in py_files:
        shutil.copy(file, target_path)
else:
    print("Please re-check your source and distination paths.")

print("All the files are copied to the distination folder")
