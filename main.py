#Importing Libraries

import numpy as np
import cv2
import tkinter as tk
import tkinter.messagebox  
import face_recognition
import ctypes
import time
from capture import captureimg

# Input Image
input_image = face_recognition.load_image_file(r'C:\Projects\PythonSecurityShutdown/Sample.jpg')
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

# Input Image Face Locations and Encoding
faceLoc = face_recognition.face_locations(input_image)
encode_input = face_recognition.face_encodings(input_image)
for face_Loc in faceLoc :
    y11, x22, y22, x11 = face_Loc

# WebCam Access 
cap =  cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	faceLoc_out = face_recognition.face_locations(frame)
	encode_output = face_recognition.face_encodings(frame, faceLoc_out)
	for face_Loc1 in faceLoc_out:
		yo1, xo2, yo2, xo1 = face_Loc1
	# cv2.rectangle(frame, (xo1,yo1), (xo2,yo2),(255,255,0),1)
	# cv2.imshow("out_image", frame)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	cap.release()
	# 	cv2.destroyAllWindows()
	for encode_face, face_location in zip(encode_output, faceLoc_out):
		matches = face_recognition.compare_faces(encode_face, encode_input)
		faceDis = face_recognition.face_distance(encode_input, encode_face)
		matchIndex = np.nanargmin(faceDis)
		if not matches[matchIndex]:
			# GUI
			root = tkinter.Tk()
			root.title("Warning!!")
			root.geometry('400x200')
			root.config(bg='#345')

			def lock():
				ctypes.windll.user32.LockWorkStation()				# Lock the entire workstation 
				# captureimg()
				root.destroy()

			my_label = tkinter.Label(root, text="Owner is not present.Locking the workstation in 5 seconds!")
			my_label.pack(pady=20)
			my_label.after(5000, lock)
			#root.destroy()
			root.mainloop()

