import os
import sys
import re

filename_pattern = r"^([^\.0-9]*)(\d+)([^0-9].*)$"

def main():
	if not(len(sys.argv)==1 or len(sys.argv)==4):
		print("Command must be: python prefixzeroes.py <directory> <recurse(y/n)> <digits(2/3/..)>\n(Arguments are optional in command line)")
	else:
		if len(sys.argv)==1:
			dir_path,recurse,digits = takeInput('console')
		elif len(sys.argv)==4:
			dir_path,recurse,digits = takeInput('arguments')
		if not os.path.exists(dir_path):
			print('Requested directory does not exist')
		else:
			traverse(dir_path,recurse,digits,0)
			print("Rename the above shown changes? (y/n) : ",end="")
			c = input()
			if c=='y' or c=='Y':
				traverse(dir_path,recurse,digits,1)
				print("Renaming Done !")


def takeInput(mode):
	if mode=='arguments':
		dir_path = sys.argv[1]
		recurse = sys.argv[2]
		digits = int(sys.argv[3])
	elif mode=='console':
		print("Enter directory path (surround with double quotes):")
		dir_path = input()
		print("Recurse in sub-directories? (y/n) : ")
		recurse = input()
		print("Enter digits (2/3/..):")
		digits = int(input())
	return dir_path,recurse,digits


def traverse(dir_path,recurse,digits,renameConfirm=0):
	if not(dir_path.endswith("/")):
		dir_path = dir_path+"/"
	for file_name in os.listdir(dir_path):
		if os.path.isfile(dir_path+file_name) and re.match(filename_pattern,file_name):
			renumber(dir_path,file_name,digits,renameConfirm)
		elif recurse=='y' and os.path.isdir(dir_path+file_name):
			traverse(dir_path+file_name,recurse,digits,renameConfirm)


def renumber(dir_path,file_name,digits=2,renameConfirm=0):
	res = re.match(filename_pattern,file_name)
	prefix,num,suffix = res.group(1),res.group(2),res.group(3)
	num = num.zfill(digits)
	new_file_name = prefix + num + suffix
	if renameConfirm==0:
		print("Old name :",file_name)
		print("New name :",new_file_name)
		print("")
	else:
		os.rename(dir_path+file_name,dir_path+new_file_name)


main()