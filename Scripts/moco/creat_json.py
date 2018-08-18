#coding=utf-8
import json
import os
import xlrd
import re
from xlrd import open_workbook
def GetDataFromTable(file_name):
  file_d = open_workbook(file_name)
  # 获得第一个页签对象
  select_sheet = file_d.sheets()[0]
  row_list0 = []
  row_list2 = []
  row_list5 = []
  # 获取总共的行数
  rows_num = select_sheet.nrows
  # 得到行数
  # print (rows_num)
  for row in range(1,rows_num):
    first_row = select_sheet.cell(row, 0).value
    row_list0.append(first_row)

  for row in range(1,rows_num):
    first_row = select_sheet.cell(row, 2).value
    row_list2.append(first_row)
  # print (row_list)
  for row in range(1,rows_num):
    first_row = select_sheet.cell(row, 5).value
    row_list5.append(first_row)
   
  return (row_list0),(row_list2),(row_list5)

getpra = GetDataFromTable("excel/20180705.xlsx")
# jstr = 
name = getpra[0]
do = getpra[1]
data = getpra[2]
for name_1,do_1,data_1 in zip(name,do,data):
	# print (do_1,data_1)
	match = re.findall(r"(.+?).do", do_1)
	# match_1 = re.findall(r"(.*)", match)
	match = match[0].replace("/", "_")
	print (match)
	jStr = ('[{"request":{"uri":"%s"},"response":{ "headers":{"Access-Control-Allow-Origin":"http://localhost:3000",'
			'"Access-Control-Allow-Credentials":"true"},"json":%s}}]')%(do_1,data_1)
	jStr = jStr.encode('utf-8')
	# json_str = json.dumps(jStr)
	# new_dict = json.loads(json_str) 
	# jStr = json.loads(jStr)
	file_z = open("api/%s.json" %match,"wb")
	file_z.write(jStr) 
	# json.dump(new_dict,file_z)
	file_z.close()
	file = open( "global.json", "r" )  
	content = file.read()  
	content_add = (',{ "file_root":"api/", "include":"%s.json" }' %match)   
	pos = content.find( "]")
	if pos != -1:  
		content = content[:pos] + content_add + content[pos:]  
		file = open( "global.json", "w" )  
		file.write( content ) 
		file.close() 



# with open("api/%s.json","wb") as f:%name
# 	f.write(jStr)
# file = open( "global.json", "r" )  
# content = file.read()  
# content_add = (',{ "file_root":"api/person", "include":"person.json" }')  
# pos = content.find( "]")
# if pos != -1:  
#         content = content[:pos] + content_add + content[pos:]  
#         file = open( "global.json", "w" )  
# #         file.write( content )   
# #         file.close()  


 
