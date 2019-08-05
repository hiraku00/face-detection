import os
import cv2

HAAR_FILE = "./haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(HAAR_FILE)

IN_PATH = './input/'
OUT_PATH = './output/'

def get_file(dir_path):
    file_names = os.listdir(dir_path)
    return file_names

images = get_file(IN_PATH)

for i in images:

    # read image
    img = cv2.imread(IN_PATH + i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # face detection
    face = face_cascade.detectMultiScale(gray)

    # cut out the face area
    for x,y,w,h in face:
        face_cut = img[y:y+h, x:x+w]
    # wrap in red frame
    for x,y,w,h in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imwrite(OUT_PATH + '{}_face_cut.jpg'.format(i.replace('.jpg', '')), face_cut)
    cv2.imwrite(OUT_PATH + '{}_face_rectangle.jpg'.format(i.replace('.jpg', '')), img)
