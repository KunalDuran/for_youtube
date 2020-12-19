import cv2 as cv
import face_recognition


im = face_recognition.load_image_file('kunal.png')
box = face_recognition.face_locations(im)
for top, right, bottom, left in box:
    cv.rectangle(im, (left, top), (right, bottom), (0,255,0),2)
cv.imwrite('detected.jpg', cv.cvtColor(im, cv.COLOR_BGR2RGB))


