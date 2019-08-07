# To Do
- Scraping Google image search results and downloading image data with ['py_scrayping'](https://github.com/hiraku00/py_scrayping).
- This time, I would like to download the image data of person, make the face part of the person recognized by OpenCV, and create the face image data.

# Summary
1. Preparing cascade files
2. Preparing image files
3. Face recognition & file output

# Operating Environment
- macOS Catalina 10.15 beta
- anaconda 4.6.14
- Python 3.6.8
- opencv 3.4.2

# 1. Preparing cascade files
- In my case, an environment is constructed with anaconda, so "haarcascade_frontalface_default.xml" is in "anaconda3/pkgs/.../ haarcascades/". (Try searching with Finder etc.)
- I copied it and stored it in the same directory as the executable.
- If you don't have the file, download it from [GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades).

```python:1.Preparing cascade files
import os
import cv2

HAAR_FILE = "./haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(HAAR_FILE)
```

# 2. Preparing image files
- Create a folder(input/output) to store the input source file and output destination file, and store multiple image data (.jpg) in the input source.

```python:2.Preparing image files
IN_PATH = './input/'
OUT_PATH = './output/'

def get_file(dir_path):
    file_names = os.listdir(dir_path)
    return file_names

images = get_file(IN_PATH)
```

# 3. Face recognition & file output
- Read image data(imread)
- Convert image to grayscale for easy detection(cvtColor)
- Use cascade read in '1.' to perform face recognition  
  The return value of detectMultiScale is the following list
  - x coordinate
  - y coordinate
  - width
  - height
- Extract the face range or enclose the range in red frame (OpenCV imread is BGR order) and output each file
- 'rectangle' draws a rectangle.
  - rectangle (image, upper left coordinates, lower right coordinates, color, line thickness)


```python:3.Face recognition & file output
for i in images:

    # read image
    img = cv2.imread(IN_PATH + i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # face detection
    face = face_cascade.detectMultiScale(gray)

    # get face area
    for x,y,w,h in face:
        face_cut = img[y:y+h, x:x+w]
    # wrap in red frame
    for x,y,w,h in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imwrite(OUT_PATH + '{}_face_cut.jpg'.format(i.replace('.jpg', '')), face_cut)
    cv2.imwrite(OUT_PATH + '{}_face_rectangle.jpg'.format(i.replace('.jpg', '')), img)
```

# Result
-Image data before/after is as follows.

### 【Before】  
#### 1. 001.jpg
![001.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/8a47f7f5-481b-435c-f64a-ed6f19ccacd8.jpeg)

#### 2. 002.jpg
![002.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/d482f683-7d37-52d7-c202-044b16dabc2d.jpeg)

#### 3. 003.jpg
![003.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/7308e02a-d730-21ab-4a9c-774d79c5026f.jpeg)


### 【After】
#### 1.
#### 001_face_cut.jpg
![001_face_cut.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/11ab9bf7-4e1d-a463-b0bd-f5200caf988a.jpeg)
#### 001_face_rectangle.jpg
![001_face_rectangle.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/376dbac8-8291-0d50-a155-f95581093072.jpeg)

#### 2.
#### 002_face_cut.jpg
![002_face_cut.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/987241a7-8446-bbc9-5f28-3c1526172e13.jpeg)
#### 002_face_rectangle.jpg
![002_face_rectangle.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/f5656d45-e97c-ce88-559c-2ec329454d8b.jpeg)

#### 3.
#### 003_face_cut.jpg
![003_face_cut.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/94ad96c0-f37a-3c99-43b1-e15cfb9c9054.jpeg)
#### 003_face_rectangle.jpg
![003_face_rectangle.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/f541162a-0b03-c96c-f287-5704f97c08f8.jpeg)

# In Japanese
- [Qiita](XXXX)
