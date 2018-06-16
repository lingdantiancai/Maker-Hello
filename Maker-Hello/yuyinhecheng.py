
from aip import AipSpeech

import time
import os
import sys
import playsound

""" 你的 APPID AK SK """
APP_ID = '10871708'
API_KEY = 'tBfFR8sl20yVlhqE66StMKwQ'
SECRET_KEY = 'uPzuzWsKfdazHMr35Snku4GgWccu3TZ1'

path = ' '
def hecheng(name,rank,text,type):
	if type == 'sayhello':
		path = 'Hello-audio/sayhello/%s/hello%s.mp3'%(name,rank)#这里是存入sayhello的语音，需要传入name和等级两个参数
	if type == 'opendoor':
		path = 'Hello-audio/opendoor/%s%s.mp3'%(name,rank)  #开门的语音设置，只需要传入name：授权开门，或者不开这两个参数
	if type == 'equipment':
		path = 'Hello-audio/equipment/%s%s.mp3'%(name,rank)		
	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

	result = client.synthesis('%s'%(text),'zh',1,{
		'vol':6,
		'per':4,

		})
	if not isinstance(result, dict):
	    with open(path, 'wb') as f:
	        f.write(result)
	return path


path = hecheng('stranger',1,'很抱歉，我不认识你，毕竟我还是一个牙牙学语的婴儿，如果你想让我向你问好，那么请你来我们创客空间进行注册。','sayhello')#sayhello语音加入
# path = hecheng('qualified',1,'尊敬的会员，非常高兴再次见到您，您具有进入的资格，请进！','opendoor')#opendoor语音加入
# path = hecheng('qualified',1,'嗯，尊贵的会员，您具有使用这台机器的资格，请您在使用过程中注意安全，使用完毕后及时关闭电源。祝您使用顺利。','equipment')#opendoor语音加入
#在这里传入要添加语音的文件夹和等级

playsound.playsound(path,True)
print(path)





# #调用系统播放器
# os.system('E:/face-FD&FR\makerHello\OpenCV-Face-detection\Hello-audio\gaoyuyu/hello2.mp3')
# os.system(r'Hello-audio/auido.mp3')
# 'E:/face-FD&FR\makerHello\OpenCV-Face-detection\Hello-audio\gaoyuyu'


#pygame播放
# pygame.mixer.init(frequency=15500,size=-16,channels=4) 
# print(123123)
# print('Play music......')
# pingmu = pygame.display.set_mode([500,365])
# pygame.mixer.music.load(r'E:/face-FD&FR/makerHello/OpenCV-Face-detection/Hello-audio/gaoyuyu/hello2.mp3')  
# # pygame.mixer.music.load(r'woyaoni.mp3')
# pygame.mixer.music.play()  
# while pygame.mixer.music.get_busy(): 
# 	pygame.time.Clock().tick(10)



