from azure.storage.blob import BlockBlobService
import time  
from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler
from os import listdir
from os.path import isfile, join
import sys


'''
class Watcher:
    DIRECTORY_TO_WATCH = sys.argv[1]

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print "Received created event - %s." % event.src_path

'''


if __name__ == '__main__':
    #w = Watcher()
    #w.run()

    directory_path = sys.argv[1]
    user_stop_script = False
    uploaded_files = []

    try:
        while(not user_stop_script):
            files_in_directory = getFilesInDirectory(directory_path)
            uploaded_files = uploadFilesNotUploaded(files_in_directory, uploaded_files, directory_path)
    except KeyboardInterrupt:
        pass
    print("User ended program.")
  

#returns list of files in directory given
def getFilesInDirectory(path_to_directory):
    return [f for f in listdir(path_to_directory) if isfile(join(mpath_to_directoryypath, f))]

#returns uploaded_files. (~files_uploaded) UNION files_in_directory
def uploadFilesNotUploaded(files_in_directory,files_uploaded,path_to_directory):
    for file in files_in_directory:
        if file not in files_uploaded:
            #upload file
            save_image_to_azure(str(file),path_to_directory)
            files_uploaded.append(str(file))
    return files_uploaded

def save_image_to_azure(local_file_name,full_path_to_file):
    # Create the BlockBlobService object, which points to the Blob service in your storage account
    block_blob_service = BlockBlobService(account_name='gencharacters', account_key='xxx')
    
    block_blob_service.create_blob_from_path('gencharacters', local_file_name, full_path_to_file)
        
    # get_blob_to_text
    #block_blob_service.get_blob_to_bytes('container-name','blob-name')

    # create-blob-from-text
    #block_blob_service.create_blob_from_text('container-name','local-file-name','content-to-be-added-to-file')


'''
FILE WILL RUN SEPERATELY THAN GIMP AND BE A FILE_LISTENER


while(true):
    look for new files (have a list of the file names)
    if new file 

    upload to the cloud and change the logging .txt. file on the cloud 
        (requires read, then write)
    
        reloop / break when key user types "s" ??

'''