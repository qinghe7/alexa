import os,time,threading
import logs,volume
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD) #物理引脚编码
#GPIO.setwarnings(False)
#GPIO.setup(24, GPIO.OUT)

play_ok = 'music_messy/prompt/as_you_wish.wav'
play_go = 'music_messy/prompt/end.wav'
play_back = 'music_messy/prompt/start.wav'
play_read_temper = 'music_messy/prompt/read_temper.wav'

def light_on(action):
	print(action)
	#GPIO.output(24, 1)
	print('\033[1;32m 已经开灯啦 \033[0m')
	volume.play_prompt(play_ok)
	return 'ok'

def light_off(action):
	print(action)
	#GPIO.output(24, 0)
	print('\033[1;32m 已经关灯啦 \033[0m')
	volume.play_prompt(play_ok)
	return 'ok'
	
def temperature():
	volume.play_prompt(play_read_temper)
	text = '当前温度为25度'
	return text

def setTimeOut_down():
	time.sleep(10)
	#GPIO.output(23, 0)
	print('\033[1;32m 已经关灯啦 \033[0m')

def SE(bool):
	if bool == 0:
		volume.play_prompt(play_back)
		print('       Messy，祝你有个愉快的一天！')
		logs.suc('i_said:我回来了')
	elif bool == 1:
		volume.play_prompt(play_go)
		print('       将在五分钟后切断相应设备电源并开启监控模式，晚安！')
		logs.suc('i_said:我走了')
		#t = threading.Thread(target=setTimeOut_down)
		#t.start()
