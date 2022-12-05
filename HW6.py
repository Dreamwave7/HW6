
from pathlib import Path
import shutil
import os
import sys


name_extensions = {
    "images" : ('.jpeg', '.png', '.jpg', 'svg'),
    "video" : ('.avi', '.mp4', '.mov', '.mkv'),
    "documents" : ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "music" : ('.mp3', '.ogg', '.wav', '.amr'),
    "archives" : ('.zip', '.gz', '.tar')
}

current_path = Path("C:\\test_sorted")

def create_folder(folder):    #створення папок для сортування
    for name in name_extensions.keys():
        if os.path.exists(f"{folder}\\{name}"):
            continue
        else:
            os.mkdir(f"{folder}\\{name}")

def bypass_files(path_folder):
    for item in path_folder.glob("**/*"):
        if item.is_file():
            sort_file(item)
        if item.is_dir():
            if os.path.getsize(item) == 0:
                shutil.rmtree(item)
            if item.name in name_extensions:
                continue


def sort_file(file):
    if file.suffix in name_extensions["images"]:
        shutil.move(file, f"{current_path}\\images")
    if file.suffix in name_extensions["video"]:
        shutil.move(file, f"{current_path}\\video")
    if file.suffix in name_extensions["documents"]:
        shutil.move(file, f"{current_path}\\documents")
    if file.suffix in name_extensions["music"]:
        shutil.move(file, f"{current_path}\\music")
    if file.suffix in name_extensions["archives"]:
        shutil.move(file, f"{current_path}\\archives")


#create_folder(current_path)


bypass_files(current_path)




















































    # shutil.make_archive("images","zip","C:/test_sorted")
    # current_direct = Path(directory)
    # for file in current_direct.iterdir():
    #     if file.suffix in images:
    #         pass
    #     if file.suffix in video:
    #         moving = os.path.join(r"C:\test_sorted\video", file)
    #     if file.suffix in documents:
    #         archive_name = shutil.make_archive('backup', 'zip', '//test_sorted')
    #     if file.suffix in music:
    #         print ("1 music file")
    #     if file.suffix in archives:
    #         print ("1 archive")
    #

# print(sort_function())