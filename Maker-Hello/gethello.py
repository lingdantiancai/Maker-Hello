import os
import playsound

hello_list = []

dic={0:'gaoyuyu',1:'lixiangyu',2:'chixiaoyu',9:'stranger',-1:"mistake"}
def getname(id):
	try :
		return dic[id]
	except:
		print('the man is not register ')
	

def sayhello(name):#这里进行的是问好程序
	if name == None:
		namepath = 'Hello-audio/sayhello/stranger'
	else: 
		namepath = 'Hello-audio/sayhello/%s/'%(name)
	for file in os.listdir(namepath):
		hello_list.append(file)
		rank = file[-5:-4]
		print(file,rank)
	playsound.playsound(namepath+hello_list[-1])
	if int(hello_list[-1][-5:-4]) > 1:
		print('delete this item')
		os.remove(namepath+hello_list[-1])



def opendoor(type):#不同的等级类别，播放不同的提示语音
	if type == "qualified":
		namepath = 'Hello-audio/opendoor/qualified1.mp3'#通过开门
	elif type == 'unqualified' : 
		namepath = 'Hello-audio/opendoor/unqualified1.mp3'#没有权限开门
	elif type == 'notreal':
		namepath = 'Hello-audio/opendoor/unqualified2.mp3'#不是一张真正的人脸
	elif type == 'tip':
		namepath = 'Hello-audio/opendoor/tip1.mp3'
	elif type == 'VoiceTip':
		namepath = 'Hello-audio/opendoor/VoiceTip1.mp3'
	elif type == 'VoiceNot':
		namepath = 'Hello-audio/opendoor/VoiceNot1.mp3'
	elif type == 'Success':
		namepath = 'Hello-audio/opendoor/Success1.mp3'
	playsound.playsound(namepath)

def equipment(type):
	if type == "qualified":	
		namepath = 'Hello-audio/equipment/qualified1.mp3'#可以使用机器
	elif type == 'unqualified' : 
		namepath = 'Hello-audio/equipment/unqualified1.mp3'#不可以使用机器
	elif type == 'broken':
		namepath = 'Hello-audio/equipment/unqualified2.mp3'#机器坏掉了
	# elif type == 'tip':
	# 	namepath = 'Hello-audio/equipment/tip1.mp3'
	playsound.playsound(namepath)	

# sayhello('gaoyuyu')#
#向函数传入一个姓名，则便会播放该姓名下的最高等级语音
# print(hello_list)
# opendoor('qualified')



# path = hecheng('gaoyuyu',2,'你好啊，好久不见')#在这里传入要添加语音的文件夹和等级
# playsound.playsound(path,True)