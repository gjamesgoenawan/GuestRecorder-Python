import os
from datetime import datetime
import csv
from time import sleep

def clear():
	os.system("cls")
	print("")
	print("--------------------------------------------------------".center(100))
	print("TULIPA OFFICE AND COWORKING SPACE VISITOR RECORDER".center(100))
	print("--------------------------------------------------------".center(100))
	print("\n\n")

print("Loading Database...")
os.system("mode con:cols=100 lines=23")
os.system("Title TULIPA OFFICE AND COWORKING SPACE VISITOR RECORDER")
if not os.path.exists("..\\History"):
    os.makedirs("..\\History")
try:
	f = open("..\\History\\"+str(datetime.now().strftime("%d-%m-%Y")) + ".csv", "r")
	f.close()
except IOError:
	f = open("..\\History\\"+str(datetime.now().strftime("%d-%m-%Y")) + ".csv", "w")
	f.close()
clear()
while True:
	ff = open("..\\History\\"+str(datetime.now().strftime("%d-%m-%Y")) + ".csv", "r")
	f = ff.readlines()
	cid = input("Input Identification Number> ")
	clear()
	if cid == "exitexitexit":
		clear()
		break
	else:
		cnt = 0
		for i in f:
			if i == "\n":
				continue
			else:
				tid = i.split(",")[1]
				if tid.find(str(cid))!=-1:
					cnt+=1
				else:
					continue
		if cnt%2 == 0:
			status = "In"
		else:
			status = "Out"
		if status == "In":
			desc = input("Purpose of Visit> ")
		else: 
			desc = "-"
		clear()
		print("Identification Number: "+str(cid)+"\nPurpose of visit: "+desc+"\nStatus: Checking "+status+"\n")

		cnfrm = input("Confirm? (Y/N)")
		clear()

		if cnfrm == "y" or cnfrm == "Y":
			fields=[datetime.now().strftime("%H:%M:%S"),cid,desc,status]
			with open("..\\History\\" + str(datetime.now().strftime("%d-%m-%Y")) + ".csv", 'a', newline='') as file:
				csv.writer(file).writerow(fields)
			file.close()
			print("Data recorded successfully!")
		sleep(2)
		clear()
		ff.close()
print("Exiting Program...")
ff.close()


