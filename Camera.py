from tracemalloc import Snapshot
import cv2
import dropbox
import time
import random
start_time=0
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name= "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token = 'sl.BGdXwNnxnH2T6DWpHkY_quWxoLHw9WdsgBGQzdpMQINaRvYjIOAnkzrXz_oDrM-y_nMuC6T-11g7pi8IMabwj5hCGEZjfoUOf-alr8CsbEJ3_lfoMesf8KUAdYHEBEH5HLSrliAXk3Q'
    file = img_name
    file_from = file 
    file_to = '/text/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded succesfully")

def main():
    while(True):
        if((time.time() - start_time)>=5):
            name = take_snapshot()
            upload_files(name)

main()