# downloads-folder-organizer
This Python script organizes files in downloads folder based on their file extensions. It categorizes the files into different folders such as "Audios," "Compressed," "Documents," "Images," "Misc," and "Videos" for easy file management.

## Usage
1. Update the downloads_path variable with the path to your target directory. Make sure to replace 'User' with your actual device name without the quotes.
2. Run the script.
 ```py
 python folder_organizer.py
 ```
3. The script will create the necessary folders if they don't already exist in the specified directory.
4. The script will move the files into their respective folders based on their file extensions.
    + Files with audio extensions (wav, mp3) will be moved to the "Audios" folder.
    + Files with compressed extensions (zip) will be moved to the "Compressed" folder.
    + Files with document extensions (pdf, xlsx, docx, ppt) will be moved to the "Documents" folder.
    + Files with image extensions (png, jpg, JPG) will be moved to the "Images" folder.
    + Files with miscellaneous extensions (exe, txt, ttf, ini, msi, iso, vbox-extpack) will be moved to the "Misc" folder.
    + Files with video extensions (mkv, mp4, MOV) will be moved to the "Videos" folder.

Note: If you want to check the extensions of your files before organizing them, you can uncomment the code section mentioned in the script. It will print the unique extensions found in your files. Comment out the subsequent code block that moves the files to organize them.

## Customization
+ If you want to add or remove file extensions for a specific category, modify the respective list in the script (audios, compressed, documents, images, misc, videos).
+ If you want to organize files into different folders or change the folder names, you can update the mkdir and move paths accordingly in the script.
