from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "C:\\Users\\chotu\\Downloads"
dest_dir_Zip = "C:\\Users\\chotu\\Downloads\\Zip"
dest_dir_Application= "C:\\Users\\chotu\\Downloads\\Application startups"
dest_dir_video = "C:\\Users\\chotu\\Downloads\\Videos"
dest_dir_image = "C:\\Users\\chotu\\Downloads\\Images"
dest_dir_documents = "C:\\Users\\chotu\\Downloads\\Documents"
dest_dir_Programs = "C:\\Users\\chotu\\Downloads\\Programs files"

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

Zip_extensions = [".zip",".ZIP"]

Application_extensions = [".exe", ".EXE"]

Programs_extentions = [".ipynb", ".py"]

document_extensions = [".doc", ".docx", ".odt", ".csv"
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_Program_files(entry, name)
                self.check_Application_files(entry, name)
                self.check_Zip_files(entry, name)
                
    def check_Program_files(self, entry, name):  # * Checks all Video Files
        for Programs_extensions in Programs_extensions:
            if name.endswith(Programs_extensions) or name.endswith(Programs_extensions.upper()):
                move_file(dest_dir_Programs, entry, name)
                logging.info(f"Moved Program file: {name}")
                
    def check_Application_files(self, entry, name):  # * Checks all Video Files
        for Application_extension in Application_extension:
            if name.endswith(Application_extension) or name.endswith(Application_extension.upper()):
                move_file(dest_dir_Application, entry, name)
                logging.info(f"Moved video file: {name}")
                
    def check_Zip_files(self, entry, name):  # * Checks all Video Files
        for Zip_extensions in Zip_extensions:
            if name.endswith(Zip_extensions) or name.endswith(Zip_extensions.upper()):
                move_file(dest_dir_Zip, entry, name)
                logging.info(f"Moved video file: {name}")
                

    def check_video_files(self, entry, name):  # * Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")


# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()