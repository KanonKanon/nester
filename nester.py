

""" 这是一个打印列表中所有数据的方法"""

def print_all(list_obj，indent = False,level =0, fileoutput = sys.stdout):
	""" 参数是一个复杂的列表，这个列表是个多重嵌套的列表"""
	for each in list_obj:
		if isinstance(each,list):
			print_all(each,indent,level+1,fileoutput)
		else:
			if indent:
				for tab_stop in range(level):
					print("/t",end='',file = fileoutput)
				print(each,fileoutput)

