import time
import cv2
import face_recognition
import numpy as np
import os
# 通过这个程序，可以将一个文件夹中的图像中人脸全部识别，出来同时，只保存人脸区域位置

def find_face(filepath):
	unknow_face = face_recognition.load_image_file(filepath)
	face_locations = face_recognition.face_locations(unknow_face)
	return face_locations 


for filename in os.listdir(r'./face'):
	filepath = './face/%s'%(filename)
	face_locations  = find_face(filepath)

	img = cv2.imread(filepath)
	top, right, bottom, left = face_locations[0]
	print(face_locations)
	cv2.imwrite('%s.jpg'%(filename[:-4]),img[top:bottom,left:right])


	# img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

	cv2.imshow('test',img[top:bottom,left:right])
	cv2.waitKey(300)
cv2.destroyAllWindows()