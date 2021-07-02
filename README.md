# Quick start
First download face landmark predictor:
```
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

bunzip2 /content/shape_predictor_68_face_landmarks.dat.bz2
```
## For single image

Change path of the source image and destination images in file image_swap.py

```
img = cv2.imread("data/messi.jpg") # source image
img2 = cv2.imread("data/ronaldo.jpg") # destination image
```

run `python3 image_swap.py`

Source image
![ronaldo](data/messi.jpg "Ronaldo")

Destination image
![messi](data/ronaldo.jpg "Ronaldo")

Result image
![ronaldo](images/results.png "Ronaldo")


## For video

change the path of the image whose face you want to swap with your face in line 15 `realtime.py`
```
img = cv2.imread("data/suzy.jpg")
```
after that run `python3 realtime.py`
