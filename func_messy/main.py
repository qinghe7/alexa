import time
import household
import tuling
import volume
import yuyinhecheng
import yuyinshibie
import logs
import isKeyword

# 时间
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# 提示音频与对话音频的文件路径
init_prompt = '/home/pi/alexa/music_messy/prompt/how_can_i_help.wav'
none_prompt = '/home/pi/alexa/music_messy/prompt/please_speak.wav'
play_shibie_failed = '/home/pi/alexa/music_messy/prompt/shibie_failed.wav'
play_hecheng_failed = '/home/pi/alexa/music_messy/prompt/hecheng_failed.wav'
i_said = '/home/pi/alexa/music_messy/said/i_said.mp3'
alexa_said = '/home/pi/alexa/music_messy/said/alexa_said.mp3'


def main(p,detector):
	detector.terminate()
	print('\033[1;32m     识别成功，随便说说吧! \033[0m')
	# 播放提示语
	volume.play_prompt_not_loop(init_prompt)
	# 录音
	print('      开始录音啦!')
	volume_in = volume.volume(p)
	# 语音识别
	#print('       开始语音识别啦!')
	i_said_json = yuyinshibie.baidu(i_said)
	#print('百度识别后返回json文件')
	# 判断是否识别成功(这里我本来想直接用变量的，但不知道为什么第二个if的赋值赋不出来，就先用数组代替)
	shibie_suc = []
	if int(i_said_json['err_no']) == 0:
		shibie_suc.append('1')
	if len(shibie_suc) == 1 or len(shibie_suc) == 2:
		# 判断有无声源输入
		if len(shibie_suc) == 1:
			i_said_text = i_said_json['result'][0]
			#打印语音识别的结果
			print('\033[1;32m*****语音识别结果为：',i_said_text)
		if i_said_text == '':
				volume.play_prompt(none_prompt)
		else:
			keyword = isKeyword.main_1(i_said_text)
			#print('return = keyword是返回值，为bool类型，可不打印')
			hecheng_keyword = isKeyword.main_2(i_said_text)
			# 判断是否包含控制家具关键字
			#print('已经判断结束是否包含控制家具关键字')
            #如果不是家具关键字，将i_said_text传送给图灵机器人
			if keyword == 1 and hecheng_keyword==1:
				alexa_said_text = tuling.robot(i_said_text)
				print('      %s' % alexa_said_text)
				# 把我和alexa的对话记录到日志
				logs.suc('i_said%s\n    alexa_said:%s' % (i_said_text,alexa_said_text))				
				# 语音合成阶段的错误处理
				hecheng = yuyinhecheng.baidu(alexa_said_text)
				if hecheng == 1:
					volume.play_prompt(alexa_said)
				else:
					logs.yuyin_err('语音合成发生了错误，以下是具体信息:\n%s' % hecheng)
					volume.play_prompt(play_hecheng_failed)
	else:
		logs.yuyin_err('语音识别发生了错误，以下是具体信息:\n%s' % i_said_json)
		volume.play_prompt(play_shibie_failed)
