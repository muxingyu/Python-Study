#! /usr/bin/env python
# -*- coding:utf8 -*-
#Addgithub

import os
from datetime import date
import re
import winreg
import shutil

#获得最后一个盘符
def get_drive():
	for i in range(65,91):
		vol = chr(i) + ':'
		if os.path.isdir(vol):
			drive = vol
	return drive

#获得桌面路径
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  
    return winreg.QueryValueEx(key, "Desktop")[0]

#建立备份路径
def mk_dir(drive):
#	date = date.today()
	today = re.sub('-','',str(date.today()))
	backup_dir = drive + '\desktop_' + today
	print (backup_dir)
	if os.path.exists(backup_dir):
		print('file exists')
#		quit()
	else:
		os.mkdir(backup_dir)
	return backup_dir

#备份桌面文件
def move_desktopfile(desktop_dir,backup_dir):
#	user = getpass.getuser()
	for i in os.listdir(desktop_dir):
		src = desktop_dir+ '\\' + i
		print (src)
		if i.split('.')=='lnk':
			continue
		else:
			shutil.move(src,backup_dir)

if __name__ == '__main__':
	drive = get_drive()
	backup_dir = str(mk_dir(drive))
	desktop_dir = str(get_desktop())
	move_desktopfile(desktop_dir,backup_dir)

