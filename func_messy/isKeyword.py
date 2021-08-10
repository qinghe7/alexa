import os,time
import volume
import household
import yuyinhecheng

# 固定关键词提示语
keywords = {
	'开灯':'household.light_on("请求开灯")',
	'关灯':'household.light_off("请求关灯")',
	'我走了':'household.SE(1)',
	'我回来了':'household.SE(0)',
}

# 需要进行语音合成的关键词
hecheng_keywords = ['几点','温度']
hecheng_music = 'music_messy/said/alexa_said.mp3'

def main_1(text):		
	for i in keywords:
		if text.find(i) != -1:
			#eval()把字符串变成可执行的函数
			#print('执行开关灯操作')
			eval(keywords[i])
			return False
	return True

def main_2(text):
	# 返回自定义的时间（图灵的回复太长了！！！）
	#print('main_2执行')
	if text.find(hecheng_keywords[0]) != -1:
		print('找到几点温度关键词')
		now_time = time.strftime('%H点%M分', time.localtime(time.time()))
		print('准备输出时间')
		yuyinhecheng.baidu(now_time)
		volume.play_prompt(hecheng_music)
		print('已经报完当前时间')
	# 返回温度读数
	elif text.find(hecheng_keywords[1]) != -1:
		temper = household.temperature()
		yuyinhecheng.baidu(temper)
		print(temper)
		volume.play_prompt(hecheng_music)
	else:
		return True