import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os

# Source folder paths.
DOWNLOAD_PATH = r'C:\Users\malsh\Downloads'
DESKTOP_PATH = r'C:\Users\malsh\OneDrive\Desktop'

# Destination folder paths.
ASSIGNMENTS_PATH = r'C:\Users\malsh\OneDrive\Desktop\Assignments'
IMAGES_PATH = r'C:\Users\malsh\OneDrive\Desktop\Images'
PDF_PATH = r'C:\Users\malsh\OneDrive\Desktop\PDFs'


def move_files(source_path, event):
    """
    This method moves files downloaded to downloads folder or placed in desktop into general folders
    based on their filetype and or filename. Ex/ Any file of type avif added to desktop will
    be immediately redirected to the images' folder.

    :param source_path: The path of the directory which will have its contents sorted.
    :param event: Represents a filesystem event which may trigger a file moving event.
    :return:
    """
    for file in os.listdir(source_path):

        source_file_path = os.path.join(source_path, file)
        assignments_destination_file_path = os.path.join(ASSIGNMENTS_PATH, file)
        images_destination_file_path = os.path.join(IMAGES_PATH, file)
        pdf_destination_file_path = os.path.join(PDF_PATH, file)

        # Directs files to their appropriate folder
        if "assn" in file:
            shutil.move(source_file_path, assignments_destination_file_path)

        elif file.endswith(("jpg", "png", "avif", "webp")):
            shutil.move(source_file_path, images_destination_file_path)

        elif file.endswith("pdf"):
            shutil.move(source_file_path, pdf_destination_file_path)


class FileMover(FileSystemEventHandler):

    def on_created(self, event):
        """
        Waits 20 seconds upon triggering of the event and then moves files which need to be moved.

        :param event:
        :return:
        """
        time.sleep(20)
        move_files(DOWNLOAD_PATH, event)
        move_files(DESKTOP_PATH, event)


"""
This code mostly belongs to the watchdog repository on gitHub.
There were edits made to fit this program's desired functionality.
Full citation in README file.
"""
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = DOWNLOAD_PATH         # Path to downloads folder. Used to trigger file moving event.
    path1 = DESKTOP_PATH         # Path to desktop. Used to trigger file moving event.
    event_handler = FileMover()  # FileMover() method set to event_handler
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)   # Observes downloads folder
    observer.schedule(event_handler, path1, recursive=True)  # Observes desktop
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
