

""" 这是一个打印列表中所有数据模块"""

def print_all(list_obj,isindent=False,indent=0):
	""" list_obj参数是一个复杂的列表，这个列表是个多重嵌套的列表，
	输出每一个数据到屏幕上，各数据项占一行,isindent 表示是否要缩进 indent 表示要缩进的数量 默认为0"""
	for each in list_obj:
		if isinstance(each,list):
			print_all(each,isindent,indent+1)
		else:
			if isindent:
				for i in range(indent):
					print('\t',end='')
			print(each)



if __name__ == '__main__':
	names = ["a","b",[1,4,['kali','kanon']]]
	print_all(names,True)

