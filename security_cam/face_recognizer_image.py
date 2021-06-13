import face_recognition
import cv2
import numpy as np
from gtts import gTTS
import pickle
from playsound import playsound
import os


def speak(audio):
    tts = gTTS(text=audio, lang='en')
    mp3_file = 'aud.mp3'
    tts.save(mp3_file)
    playsound(mp3_file, True)
    os.remove(mp3_file)


encodingz = pickle.load(open('all_encoding.pkl', 'rb'))

kunal_face_encoding = encodingz['Kunal']
mom_face_encoding = encodingz['Mom']
kaku_face_encoding = encodingz['Kaku']
pingu_face_encoding = encodingz['Pingu']
arvind_face_encoding = encodingz['Arvind']


def image_rec(image):

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        kunal_face_encoding,pingu_face_encoding, kaku_face_encoding, 
        mom_face_encoding, arvind_face_encoding
    ]
    known_face_names = [
        "Kunal Duran", "Rahul Tak", "Kaku Tak", "Kamlesh", "Arvind"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []


    if type(image) == np.ndarray:
        frame = cv2.imdecode(image, flags=1)
    else:
        frame = cv2.imread(image)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)

    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_name = ""
    for face_encoding in face_encodings:
        # See if the face is a match
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            face_name = name

    # print(face_names)
    if len(face_name) > 0:
        speak(f"Happy to see you respected {face_name} Welcome to Duranz Palace")
        for (top, right, bottom, left), name in zip(face_locations, face_names):

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, face_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Writing to the resulting image
        cv2.imwrite('detected.jpg', frame)
    else:
        speak(f"Sorry I Did not recognise you, Please try again or contact Mister Duran")
    
