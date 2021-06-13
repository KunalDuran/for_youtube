import face_recognition
import pickle


## Loading Image outside the function to save time at the time of prediction
kunal_image = face_recognition.load_image_file("static/images/kunal.png")
kunal_face_encoding = face_recognition.face_encodings(kunal_image)[0]

mom_image = face_recognition.load_image_file("static/images/kunal.jpg")
mom_face_encoding = face_recognition.face_encodings(mom_image)[0]

# Load a second sample picture and learn how to recognize it.
kaku_image = face_recognition.load_image_file("static/images/kunal.jpg")
kaku_face_encoding = face_recognition.face_encodings(kaku_image)[0]

pingu_image = face_recognition.load_image_file("static/images/kunal.jpg")
pingu_face_encoding = face_recognition.face_encodings(pingu_image)[0]

arvind_image = face_recognition.load_image_file("static/images/kunal.jpeg")
arvind_face_encoding = face_recognition.face_encodings(arvind_image)[0]


all_encodings = {'Kunal': kunal_face_encoding,
                    'Mom': mom_face_encoding,
                    'Kaku': kaku_face_encoding,
                    'Pingu': pingu_face_encoding,
                    'Arvind': arvind_face_encoding
}

pickle.dump(all_encodings, open('all_encoding.pkl', 'wb'))