import os
import sys
import re

filename_pattern = r"[^\d](\d{1,2})[^\d]+(\d{1,2})"

def main():
	if not(len(sys.argv)==1 or len(sys.argv)==4):
		print("Use one of the following forms :")
		print("1) python tv_series_renamer.py")
		print("2) python tv_series_renamer.py <directory> <recurse(y/n)> <Name of show>")
	else:
		if len(sys.argv)==1:
			dir_path,recurse,series_name = takeInput('console')
		elif len(sys.argv)==4:
			dir_path,recurse,series_name = takeInput('arguments')
		if not os.path.exists(dir_path):
			print('Requested directory does not exist')
		else:
			traverse(dir_path,recurse,series_name,0)
			print("Rename the above shown changes? (y/n) : ",end="")
			c = input()
			if c=='y' or c=='Y':
				traverse(dir_path,recurse,series_name,1)
				print("Renaming Done !")


def takeInput(mode):
	if mode=='arguments':
		dir_path = sys.argv[1]
		recurse = sys.argv[2]
		series_name = sys.argv[3]
	elif mode=='console':
		print("Directory path (enclose in double quotes) : ")
		dir_path = input()
		print("Recurse in sub-directories? (y/n) : ")
		recurse = input()
		print("Series name (enclose in double quotes) : ")
		series_name = input()
	return dir_path,recurse,series_name


def traverse(dir_path,recurse,series_name,rename_mode):
	if not(dir_path.endswith("/")):
		dir_path = dir_path+"/"
	for file_name in os.listdir(dir_path):
		if os.path.isfile(dir_path+file_name):
			modify_name(dir_path,file_name,series_name,rename_mode)
		elif recurse=='y' and os.path.isdir(dir_path+file_name):
			traverse(dir_path+file_name,recurse,series_name,rename_mode)


def modify_name(dir_path,file_name,series_name,rename_mode):
	res = re.findall(filename_pattern,file_name)
	if len(res)==1:
		season,episode = res[0][0],res[0][1]
		season = season.zfill(2)
		episode = episode.zfill(2)
		new_file_name = series_name+" - S"+season+"E"+episode
		ext = (file_name.split("."))[-1]
		new_file_name = new_file_name + "." + ext
		if rename_mode==1:
			os.rename(dir_path+file_name,dir_path+new_file_name)
		else:
			print("Old name :",file_name)
			print("New name :",new_file_name)
			print("")


main()
