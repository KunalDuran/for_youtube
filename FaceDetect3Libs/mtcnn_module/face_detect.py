import cv2 as cv
import mtcnn


detector = mtcnn.MTCNN()


image = cv.imread('kunal.png')
face = detector.detect_faces(image)
for box in face:
    box = box['box']
    cv.rectangle(image, (box[0],box[1]),(box[0]+box[2],box[1]+box[3]), (0,255,0),2)
cv.imwrite('Detected.jpg', image)
