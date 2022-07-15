from flask import Flask, render_template, request
from flaskwebgui import FlaskUI 
import os
from datetime import datetime
import csv
from time import sleep

app = Flask(__name__)
ui = FlaskUI(app)

filelist = open(os.path.join("db", "db.txt"),"r").readlines()
companies=[]
for i in filelist:
	companies.append(i.strip())

def register(cid, desc, comp):
	if not os.path.exists("history"):
		os.makedirs("history")
	try:
		f = open(os.path.join("history", str(datetime.now().strftime("%d-%m-%Y")) + ".csv"), "r")
		f.close()
	except IOError:
		f = open(os.path.join("history", str(datetime.now().strftime("%d-%m-%Y")) + ".csv"), "w")
		f.close()
	finally:
			ff = open(os.path.join("history", str(datetime.now().strftime("%d-%m-%Y")) + ".csv"), "r")
			f = ff.readlines()
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
		desc = "-"
		comp = "-"
	fields=[datetime.now().strftime("%H:%M:%S"),cid,desc,comp, status]
	with open(os.path.join("history", str(datetime.now().strftime("%d-%m-%Y")) + ".csv"), 'a', newline='') as file:
		csv.writer(file).writerow(fields)
	file.close()
	print("Data recorded successfully!")
	ff.close()

#do your logic as usual in Flask
@app.route("/")
def index():  
    return render_template('home.html', companies=companies)

@app.route('/', methods=['POST'])
def form_post():
	cid = request.form['name']
	desc = request.form['purpose']
	comp = request.form['company']
	if cid.strip() == "" or cid == None:
		return render_template('errI.html')
	elif comp.strip() == "-1":
		return render_template('errD.html')
	else:
		register(cid, desc,comp)
	return render_template('done.html')

if __name__ == "__main__":
	ui.run()
 
