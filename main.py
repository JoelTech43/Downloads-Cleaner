import os
from datetime import datetime
from config import *

def setup():
    for folder in PROGRAM_FOLDERS:
        full_path = os.path.join(DIRECTORY, folder)
        if not os.path.exists(full_path):
            os.mkdir(full_path)

# def days_since_last_use(full_path):
#     file_stat = os.stat(full_path)
#     last_mod = datetime.fromtimestamp(file_stat.st_mtime)
#     last_acc = datetime.fromtimestamp(file_stat.st_atime)
#     current_time = datetime.now()
#     if last_mod < last_acc: #use whichever of last_mod and last_acc are most recent
#         time_since_last_use = current_time-last_acc
#     else:
#         time_since_last_use = current_time-last_mod

#     days_since_last_use = time_since_last_use.days
#     return days_since_last_use

def run_search():
    files_to_move = []
    dirs_to_move = []
    for name in os.listdir(DIRECTORY):
        file_path = os.path.join(DIRECTORY, name)
        if os.path.isfile(file_path):
            # if days_since_last_use(file_path) >= 1:
            files_to_move.append(name)
        elif os.path.isdir(file_path):
            if name not in PROGRAM_FOLDERS:
                dirs_to_move.append(name)
    return files_to_move, dirs_to_move

def move_files(files_to_move):
    for file in files_to_move:
        ext = os.path.splitext(file)[1]
        dest = ""
        match ext.lower():
            case ".jpg" | ".png" | ".jpeg" | ".svg" | ".avi" | ".3gp" | ".mkv" | ".m4a" | ".ogg" | ".mp3" | ".mp4":
                dest = os.path.join(DIRECTORY, "Media_Files")
            case ".zip" | ".rar" | ".7zip":
                dest = os.path.join(DIRECTORY, "Compressed_Files")
            case ".3mf" | ".stp" | ".stl" | ".obj" | ".step":
                dest = os.path.join(DIRECTORY, "3D_Files")
            case ".doc" | ".dot" | ".wbk" | ".docx" | ".docm" | ".dotx" | ".dotm" | ".xls" | ".xlt" | ".xlm" | ".xlsx" | ".xlsm" | ".xltx" | ".xltm" | ".xlsb" | ".xls" | ".xlam" | ".xlw" | ".ppt" | ".pot" | ".pps" | ".ppa" | ".pptx" | ".pptm" | ".potx" | ".potm" | ".ppsx" | ".ppsm" | ".sldx" | ".sldm" | ".accda" | ".accdb" | ".accde" | ".accdr" | ".accdt" | ".accdu" | ".one" | ".ecf" | ".pub":
                dest = os.path.join(DIRECTORY, "Microsoft_Files")
            case ".exe" | ".msi":
                dest = os.path.join(DIRECTORY, "Executable_Files")
            case "pdf":
                dest = os.path.join(DIRECTORY, "PDF_Files")
            case _:
                dest = os.path.join(DIRECTORY, "Misc_Files")
        old_path = os.path.join(DIRECTORY, file)
        new_path = os.path.join(dest, file)
        os.rename(old_path, new_path)

def move_subdirectories(dirs_to_move):
    for dir in dirs_to_move:
        old_path = os.path.join(DIRECTORY, dir)
        new_path = os.path.join(DIRECTORY, "Subdirectories", dir)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    setup()
    files_to_move, dirs_to_move = run_search()
    move_files(files_to_move)
    move_subdirectories(dirs_to_move)