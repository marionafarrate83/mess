import os
import shutil
import datetime, time
from datetime import datetime, date
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tinytag import TinyTag



class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "/home/mario/Documents/automation/mess"
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            #time.sleep(10)
            for root, dirs, files in os.walk("/home/mario/Documents/automation/mess", topdown=False):
                for name in files:
                    nombre = os.path.join(root, name)
                    esfile = os.path.isfile(nombre)
                    dm = datetime.strptime(time.ctime(os.path.getmtime(nombre)),"%a %b %d %H:%M:%S %Y")
                    a, b, c, d, e, f, g, h, i = dm.timetuple()
                    if name.lower().startswith(('._','.')):
                        os.remove(nombre)
                        print("archivo chafa borrado")
                    elif nombre.lower().endswith(('.png', '.jpg', '.jpeg','.ico','.avi','.bmp','.3gp','.mp4','.mov','.mpg','.gif','.m4v')):
                        dest_folder = "/home/mario/Documents/photo_archive/" + str(a) + "/" + str(b)
                        new_file_name = "/home/mario/Documents/photo_archive/" + str(a) + "/" + str(b) + "/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    elif nombre.lower().endswith(('.xls', '.xlsx','.csv')):
                        dest_folder = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/excel"
                        new_file_name = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/excel/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    elif nombre.lower().endswith(('.pdf')):
                        dest_folder = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/pdf"
                        new_file_name = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/pdf/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    elif nombre.lower().endswith(('.doc', '.docx','.txt','.dot')):
                        dest_folder = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/word"
                        new_file_name = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/word/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    elif nombre.lower().endswith(('.ppt', '.pptx','.vsd','.pps')):
                        dest_folder = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/powerpoint"
                        new_file_name = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/powerpoint/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    elif nombre.lower().endswith(('.zip', '.7z','.rar','.tar')):
                        dest_folder = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/zip"
                        new_file_name = "/home/mario/Documents/Archive/" + str(a) + "/" + str(b) + "/zip/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    elif nombre.lower().endswith(('.mp3','.ogg','.flac','.m4a')):
                        tag = TinyTag.get(nombre)
                        artista = tag.artist
                        album = tag.album
                        if artista is None:
                            artista = "desconocido"
                        elif album is None:
                            album = "desconocido"
                        folder_to = str(artista) + "_" + str(album)
                        dest_folder = "/home/mario/Music/" + folder_to + "/"
                        new_file_name = "/home/mario/Music/"+ folder_to + "/" +name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                    else:
                        dest_folder = "/home/mario/Documents/LostFound/"
                        new_file_name = "/home/mario/Documents/LostFound/" + name
                        if os.path.isdir(dest_folder):
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                        else:
                            os.makedirs(dest_folder)
                            shutil.move(nombre, new_file_name)
                            print("moviendo: " + new_file_name)
                for name in dirs:
                    folder = os.path.join(root, name)
                    print(folder)
                    if os.path.exists(folder) and os.path.isdir(folder):
                        if not os.listdir(folder):
                            print(f"Borrando directorio vacio {folder}.")
                            os.rmdir(folder)
                        else:
                            print(f"Directorio {folder} no vacio.")
                    else:
                        print(f"El directorio {folder} no existe.")
        elif event.event_type == 'modified':
            print("Watchdog received modified event - % s." % event.src_path)

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
