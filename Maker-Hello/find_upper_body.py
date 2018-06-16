#coding = utf-8
# from this program,we wish to get the upper body of a  person ,then save this img
#这个程序可以从摄像头中获取上半部人体信息，并且进一步的识别出人脸，同时将其保存起来。
import face_recognition
import matplotlib.pyplot as plt
import time
import cv2

def converToRGB(img):
	return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cap = cv2.VideoCapture('http://192.168.1.100:8080/video')#获取视频串流
cap = cv2.VideoCapture(0)#获取视频串流

# haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')#Harr分类器
# haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器
haar_face_cascade = cv2.CascadeClassifier('./classifier/haarcascade_upperbody.xml')  #经过多番测试，发现只有这一个上半身检测的分类器在距离较远时依然管用。

def save_face(filepath):
    face_locations = face_recognition.face_locations(filepath)
    # print(face_locations)
    top, right, bottom, left = face_locations[0]
    cv2.imwrite('test.jpg',filepath[top:bottom,left:right])


def get_face():

    while(1):    # get a frame   
        ret, test = cap.read()    # show a frame     
        # gray_img = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
        faces=haar_face_cascade.detectMultiScale(test,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100) )#通过harr识别器识别人脸

        if len(faces) > 0 :
            for (x,y,w,h) in faces:
                cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
            save_face(test[y:y+h,x:x+w])

   
            return True
      
        cv2.imshow("capture",test)
        k = cv2.waitKey(1) & 0xFF 

        if k == 27:
            break

cv2.destroyAllWindows() 
# print(get_face())


