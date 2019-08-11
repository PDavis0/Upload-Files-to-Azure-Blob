from azure.storage.blob import BlockBlobService
import time  
from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler
from os import listdir
from os.path import isfile, join
import sys
import glob
import os


#returns list of files in directory given
def getFilesInDirectory(path_to_directory):
    list = [f for f in glob.glob("*.png")]
    print (list)
    return list

    #returns uploaded_files. (~files_uploaded) UNION files_in_directory
def uploadFilesNotUploaded(files_in_directory,files_uploaded,path_to_directory):
    for file in files_in_directory:
        if file not in files_uploaded:
            #upload file
            save_image_to_azure(file,path_to_directory)
            files_uploaded.append(file)
    return files_uploaded

def save_image_to_azure(local_file_name,full_path_to_file):
    # Create the BlockBlobService object, which points to the Blob service in your storage account
    block_blob_service = BlockBlobService(account_name='gencharacters', account_key='uYSYgQmYY9bZD/YISsxLM9l2fyTxsMrwR8B5R/tnf/USS9b9nf7mDZlftXE+Q/988hpJqrEML0INFJXsbeCHrg==')
    block_blob_service.create_blob_from_path('generatedcharacters', local_file_name, full_path_to_file + '\\'+local_file_name)
        
    # get_blob_to_text
    #block_blob_service.get_blob_to_bytes('container-name','blob-name')

    # create-blob-from-text
    #block_blob_service.create_blob_from_text('container-name','local-file-name','content-to-be-added-to-file')





#argument [1] passed is taking the path to the file directory.    
if __name__ == '__main__':
    #w = Watcher()
    #w.run()

    directory_path = local_path=os.path.abspath(os.path.curdir)
    uploaded_files = []
    try:
        while(True):
            files_in_directory = getFilesInDirectory(directory_path)
            uploaded_files = uploadFilesNotUploaded(files_in_directory, uploaded_files, directory_path)
    except KeyboardInterrupt:
        print("User ended program.")
        pass
    


