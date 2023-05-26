import os
import shutil


audios = ["wav", "mp3"]
compressed = ["zip"]
documents = ["pdf", "xlsx", "docx", "ppt"]
images = ["png", "jpg", "JPG"]
misc = ["exe", "txt", "ttf", "ini", "msi", "iso", "vbox-extpack"]
videos = ["mkv", "mp4", "MOV"]

# Change 'User' to your device name without ''
downloads_path = r"C:\Users\'User'\Downloads"
list_of_files = os.listdir(downloads_path)

if "Audios" not in list_of_files:
    os.mkdir(fr"{downloads_path}\Audios")
if "Compressed" not in list_of_files:
    os.mkdir(fr"{downloads_path}\Compressed")
if "Documents" not in list_of_files:
    os.mkdir(fr"{downloads_path}\Documents")
if "Images" not in list_of_files:
    os.mkdir(fr"{downloads_path}\Images")
if "Misc" not in list_of_files:
    os.mkdir(fr"{downloads_path}\Misc")
if "Videos" not in list_of_files:
    os.mkdir(fr"{downloads_path}\Videos")

# File Extension Checkers
# Uncomment this code to check the extension of your files
# extensions = []
# for file in list_of_files:
#     # print(file)
#     extension = file.split('.')
#     if len(extension) == 1:
#         continue

#     if extension[-1] not in extensions:
#         extensions.append(extension[-1])

# print(extensions)


# Comment this code if you want to check the extension of your files first
for file in list_of_files:
    extension = file.split('.')
    if len(extension) == 1:
        continue

    if extension[-1] in audios:
        shutil.move(fr"{downloads_path}\{file}",
                    fr"{downloads_path}\Audios\{file}")
    elif extension[-1] in compressed:
        shutil.move(fr"{downloads_path}\{file}",
                    fr"{downloads_path}\Compressed\{file}")
    elif extension[-1] in documents:
        shutil.move(fr"{downloads_path}\{file}",
                    fr"{downloads_path}\Documents\{file}")
    elif extension[-1] in images:
        shutil.move(fr"{downloads_path}\{file}",
                    fr"{downloads_path}\Images\{file}")
    elif extension[-1] in misc:
        shutil.move(fr"{downloads_path}\{file}",
                    fr"{downloads_path}\Misc\{file}")
    elif extension[-1] in videos:
        shutil.move(fr"{downloads_path}\{file}",
                    fr"{downloads_path}\Videos\{file}")
