#### YOUTUBE VIDEO PART STARTS ##########

#Made by : Anshuman,Divam
from pytube import YouTube
import requests

def getTopVideo(q):
	url="https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&q="+q+"&key=AIzaSyBm6VqOgvsxgWHUbngQZCN3bf1rPjRkv9Y"
	r=requests.get(url)
	potato="https://www.youtube.com/watch?v="
	potato+=r.json()['items'][0]['id']['videoId']
	return potato

def getYURL(s):
	yt=YouTube(getTopVideo(s))
	video = yt.get('mp4', '360p')
	return video.url

#########################################

##### FACEBOOK PART : RUN ONLY ONCE #####

#Made by : Anshuman
import json
import time
# import facebook #sudo pip install facebook
# import fb  #sudo pip install fb 
from facepy import GraphAPI #sudo pip install facepy
import datetime

# def compare(a,b):
#   return a[3] < b[3]

# token=str(raw_input("Enter access token"))
token="CAACEdEose0cBAKPr36PR2RmzB4dcNdGwpqDgB6FN1M0Qz0x56WO9xEbxlvVoX0PHEjQwg2s093reIOWey1F27jWfiZBlmiWGBrbvVe4PXj9iJ4AZAVW4ZBHXUZBftGj5rf9AmIQY3ZCN8ZCYhpX0qefJd36oFvTorqrdb45Xd1wOAZBm9BiPsgHGDqeD4XZCjr71LyOSHtKrqgZDZD"
graph = GraphAPI(token)

#Hard-coded list of objects:
hard=["thinkdigit","comicbookdotcom","ScienceAlert"]
friends=["divamgupta","sarthak.madan","RounaqJJW"]
final=[]
#Poster,Image,Data,Timestamp
for i in hard:
  process=i+"/posts?date_format=U"
  feed=graph.get(process)
  for j in feed['data']:
    tomato=["NULL","NULL","NULL","NULL"]
    tomato[0]=i
    # tomato[3]=datetime.datetime.strptime(j['updated_time'])
    tomato[3]=j['updated_time']
    if 'picture' in j :
      tomato[1]=j['picture']
    if 'message' in j :
      tomato[2]=j['message']
    final.append(tomato)
  # print "HOOLA DANCE\n\n"
print "Fetched"

final.sort(key=lambda x: x[3])
# final=final[:2]
# for i in final:
#   print i[3]
j=1
for potato in final:
  code=[]
  # print potato
  f=open('template.html','r')
  for line in f:
    temp=line
    if(temp.find("parent42")!=-1):
      temp=temp.replace('parent42',potato[0])
    if(temp.find("image42")!=-1):
      temp=temp.replace('image42',potato[1])
    if(temp.find("content42")!=-1):
      temp=temp.replace('content42',potato[2])

    if(temp.find("NULL")==-1):
      code.append(temp)
  f.close()
  g=open('html_files/'+str(j)+'.html','w')
  for i in code:
    avocado=i.encode('ascii', 'ignore')
    g.write(avocado)
  g.close()
  j+=1


#########################################

############# DIFFBOT ###################

#Made by : Anshuman, Divam
import requests

def diffbot(url):
	token="b1df14f444825a46198148f81cf2af60"
	# url="http://www.digit.in/mobile-phones/lumia-950-and-950xl-how-does-liquid-cooling-in-phones-really-work-27483.html"
	param="http://api.diffbot.com/v3/analyze?token="+token+"&url="+url
	r=requests.get(param)
	g = r.json()['objects'][0]['html']
	f=open('current.html','w')
	f.write(g)
	f.close()

#########################################

########## AI QUERY #################

#Made by : Rounaq 
import tungsten,sys
import xml.etree.ElementTree as ET
def AIquery(x):
	client = tungsten.Tungsten('Q87PQR-6Y8VUGJXAX')
	result = client.query(x)
	k = 0
	for pod in result.pods:
	    if pod.xml_tree.find("subpod/plaintext").text:
		if(k==1):
			return str(pod.xml_tree.find("subpod/plaintext").text)
		k+=1
		if k == 6:
			break

#########################################

########## FLASK SERVER #################

#Made by : Anshuman, Divam
import os
import subprocess
from datetime import datetime
from flask import Flask
from flask import request
from random import randint
import tts_manage

app = Flask(__name__, static_folder='image_files', static_url_path='')

i=1
p=0
start=datetime.now().time()
ans=""
mp4url=""
duration=0


@app.route("/")
def welcome():
	return str(randint(1,10))

@app.route('/image_files/<path:path>/')
def root(path):
    return app.send_static_file(path)

@app.route("/gesture")
def gesture():
	global i,p
	# path, dirs, files = os.walk("/image_files").next()
	# file_count = len(files)
	file_count=50
	if(i<=file_count):
		i+=1
	else:
		i=1
	if(p==2):
		p=0
	else:
		p=1
	return "Noted"

@app.route("/poll")
def poll():
	global start
	global ans
	global p
	if(p==0):
		return ""
	elif(p==1):
		p=0
		return "PIC "+"http://192.168.49.237:5000/"+str(i)+".png"
	elif(p==2):
		p=0
		return "VID "+ mp4url
	elif(p==3):
		p=0
		subprocess.Popen(["python","tts.py",ans])
		# tts_manage.func(ans) #Answer bolo :)	
		return ans
	return ""

@app.route("/speech")
def speech():
	global mp4url
	global start
	global duration
	global p
	global ans
	st=request.args.get('string')
	st=st.lower()
	st=st.replace('jarvis','')
	st=st.strip()
	ST=st.split(' ')
	if(ST[0] == "play"):
		x=' '.join(ST[1:])
		# print ST[1:]
		mp4url=getYURL(x)
		# print mp4url
		p=2
		start=datetime.now().time()
		# duration=float(mp4url.split('dur=')[-1].split('&')[0])
		return mp4url
	if("facebook" in ST):
		p=1
	else:
		ans=AIquery(st)
		return str(ans)
	return st

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

#########################################