import cv2 as cv


image = cv.imread('kunal.png')


def face_detector_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
    return faces_rect


faces_rect = face_detector_image(image)

for x,y,w,h in faces_rect:
    cv.rectangle(image, (x,y), (x+w, y+h), (0,255,0), thickness=2)


cv.imwrite('detected.jpg', image)
'''
capture = cv.VideoCapture('test_vid.mp4')


while True:
    isTrue, frame = capture.read()
    faces_rect = face_detector_image(frame)
    
    for x,y,w,h in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        cv.destroyAllWindows()
        break

capture.release()'''
