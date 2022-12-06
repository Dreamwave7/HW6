
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

current_path = Path("C:\\test_sorted")  # використвую такий шлях, бо через sys.argv  не виходить, при виклику файла в терминали видаэ помылку,що його не иснуе


RUSS_SYMB = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
ENG_SYMB = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","_", "_")
TRANS = {}
for c, t in zip(RUSS_SYMB, ENG_SYMB):
    TRANS[ord(c)] = t
    TRANS[ord(c



def unpack_arch(archive_path):  #розпакування архиву
    shutil.unpack_archive(archive_path, f"{current_path}\\archives")


def create_folder(folder):    #створення папок для сортування
    for name in name_extensions.keys():
        if os.path.exists(f"{folder}\\{name}"):
            continue
        else:
            os.mkdir(f"{folder}\\{name}")

def bypass_files(path_folder):  #прохид по папкам и файлам
    for item in path_folder.glob("**/*"):
        if item.is_file():
            sort_file(item)
        if item.is_dir():
            if os.path.getsize(item) == 0:
                shutil.rmtree(item)
            if item.name in name_extensions:
                continue


def sort_file(file):     #сортуваня файлив
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




















































