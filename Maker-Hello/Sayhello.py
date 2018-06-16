import get_arcsoft
import gethello
import time
import cv2

cache = '1' 
while(1):
	people =get_arcsoft.getPeople()  #从虹软获取识别的到的人
	print(people)
	if people == -1:
		print("This is a mistake in face detection")
		continue
	name = gethello.getname(people)		#获取到该人对应目录下问好文件
	time.sleep(0.5)
	if name != None and name != cache:
		gethello.sayhello(name)		#向这个人问好
		f = open('log.txt','a')	 	#在问好以后，将这个人的姓名和当前时间存入log文件
		t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		f.write('%s %s \n'%(t1,name))			
		f.close()
	k = cv2.waitKey(1) & 0xFF 
	if k == 27:
		break
	cache = name
	

	