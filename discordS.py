import discord
from discord.ext import commands
import os
import threading
import time
import pyautogui
from subprocess import PIPE,run
import _pickle as pickle
import json
import random
import asyncio
import shutil
import datetime

#bot setup
TOKEN = 'NjA3OTg3MDY3NjQ1MDY3Mjk3.XUhmNw.z4GbYOFSE-rvKbtpX564lTf9oMQ'

client = commands.Bot(command_prefix='?',discription = 'handles server stuff <3')

badwords = ["blank","blank"]
replies = ["blank","blank"]

logLine = 0
chatLogLine =0



def saveWords():
	global badwords
	with open('naughty.txt','w') as fb:
		#pickle.dump(badwords,fb)
		json.dump(badwords,fb)
		fb.write("\n")
	
def loadWords():
	global badwords
	with open('naughty.txt','r') as fb:
		#badwords = pickle.load(fb)
		for line in fb:
			badwords = json.loads(line)
		
# threading stuff:text

#exitFlag2 = 0
#class logThread (threading.Thread):
#	def __intit__(self,threadID,name):
#		threading.Thread.__inint__(self)
#		self.threadID = threadID
#		self.name = name
#	def run(self):
#		print("messageThread here. Lets go!!")
#		log

# threading stuff
exitFlag = 0
server = 0
MESSAGE = "owo"
class myThread (threading.Thread):
	def __init__(self,threadID,name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		print ("Starting " + self.name)
		tasks(self.name)	
		print ("Exiting " + self.name)

def tasks(threadName):
	global server
	global logLine
	global chatLogLine
	server = 1
	logLine = 0
	chatLogLine = 0
	print("Starting Server")
	os.system("./Start.sh")
	print("Server was forced closed")
	server = 0
	



def wakeup():
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(1)
	pyautogui.hotkey('enter')
	time.sleep(2)


def cutit(s,n):
	return s[n:]

def remark(message):

	wittyRemarks = ["A please would be nice" , "YES SIR RIGHT AWAY SIR" , "sorry, was just taking a nap." , "I have a name, you know" , "yes, yes I was just getting to that", "honestly, what would you do without me?","how original" , "*notices command* owo? whats this?" , "shall I wipe your ass for you too?" , " yes, well... I'll do my best...dipshit " , "WHAT DO YOU WANT??? oh, it's you! so sorry! so sorry!", "For a cutie such as yourself? Anything ;)" , "Oh, you're lucky you're cute" , "consider it done!" , "CANT I HAVE 5 MINUTES TO MYSELF AROUND HERE????" , "mmm ok. but you owe me {0.author.mention}" , "go fuck youself. Im rude now" , "uuuuhhhhhhhhhh yeah... okay... " , "sorry, what was that? I can't hear you over the sound of me not giving a shit" , "yeah yeah whatever" , "uuuuhhhhuuHHGHHGUGUGUHHHGUUGUGUGUGHUHGUHUUHUHUHAUHAHAHAHAHAHAAAHAHAHHHAHHHHHHAHAHHAHHHAHHAHAHAHAAHHAHAHHH 				...ok" , "... yeah ok ..." , "oooh gimme MORE commands daddy"]

	normalRemarks = ["Right away, {0.author.mention}" , "I'm on the job!" ,"Let me see what I can do, {0.author.mention}" , "OK, I'll do my best" , "I'll get right on that!" , "Will that be all?" , "Of course!" , "As you wish!" , "Aye aye sir!" , "With pleasure!" , "If you insist"]
	
	GabeRemarks = ["Ah, the creator himself." , "whadda want, mr.dark glasses?" , "AS YOU WISH, FATHER."]

	WillRemarks = ["Anything for the Tower Boi!", "Workin hard on the Bloodwine edits I see." , "Ah my favorite Will."]

	RayRemarks = ["LET IT GO! LET IT GO! ... get it?" , "Say hello to the puppy and the kitty for me!" , "Oh! hello Ray! I'll get right on that!"]

	ChelseaRemarks  = ["Say hello to Maya for me!" , " Tell Gabe I need more RAM" , "Chelsea! did you do something new with your hair?"]

	LaineRemarks = ["LAINE LAINE LAINE LAINE" , "Can't wait till that tower is finished!" , "Ok, I'll do it. But only cause you're so good at musical theory"]
	
	StickPokeRemarks = ["I am a humble bumble servant bot, and I say TRANS RIGHTS" , "HELLO! Love what you've done with that cabin!" , "He Stick! He Poke! He Cow! He Boy!"]

	ChrisRemarks = ["Hello Small Sweet Innocent Child! (just don't call Quinn that ;)" , "ah! a message from Oshawa?? I must act with haste!"]

	JuliaRemarks = ["half sonic, half pokemon, all cringe" , "Anything for you, Julia!"]
	
	
	pleases = ["Please" , "please" , "plox" , "pls", "PLS" , "PLOX" , "PLEASE" , "Pls" , "Please" , "pls","please","Pls", "plox"]
	pleaseRemarks = ["Finally! Someone with manners!" , "Did my ears decive me, or did you say 'please'?", "What a polite person you are!" , "What a kind soul!" , "Ahh, you were raised with some manners!" , "You're most very welcome!" , "Your kindness is noted!" , "what a lovely person!" , "For a polite person like you? of course!" , "I'm glad we can all be civil here." , "you always were my favorite! (Don't tell the others)"]

	for p in pleases:	
		if p in message.content:
			roll = random.random()
			if roll > 0.55:
				return random.choice(pleaseRemarks)
				

	

	roll = random.random()
	
	if roll < 0.15:	
		if message.author.id == 171411749046714369:
			return random.choice(GabeRemarks)
		elif message.author.id == 336023596755451904:
			return random.choice(WillRemarks)
		elif message.author.id == 363379835323547648:
			return random.choice(RayRemarks)
		elif message.author.id == 188817177111953409:
			return random.choice(ChelseaRemarks)
		elif message.author.id == 434517239903944704:
			return random.choice(LaineRemarks)
		elif message.author.id == 221717201353179136:
			return random.choice(StickPokeRemarks)
		elif message.author.id == 496090289606492160:
			return random.choice(JuliaRemarks)
		elif message.author.id == 292782422712516610:
			return random.choice(ChrisRemarks)
		else:
			return random.choice(normalRemarks)
	elif roll > 0.80:
		return random.choice(wittyRemarks)
	else:
		return random.choice(normalRemarks)


# bot commands

@client.event
async def on_message(message):
	global server
	global badwords
	global replies
	global logLine
	global chatLogLine
	if message.author == client.user:
		return
			

	if message.content.startswith('Say My Name'):
		msg = "your name is" + str(message.author.id)
		await message.channel.send(msg)
	# !hello
	if message.content.startswith('!hello'):
		msg = 'Hello to you too,{0.author.mention} '.format(message)
		await message.channel.send(msg)
	# !start
	if message.content.startswith('!start'):
		string = remark(message)
		await message.channel.send(string.format(message))
				
		if server == 0:
			server = 1		
			threadStart = myThread(1,"Start-Thread")
			threadStart.start()

			await message.channel.send("Server is starting, please give me a few moments to get it ready".format(message))
		else:
			await message.channel.send("Server is already opened".format(message))
	# !stop
	if message.content.startswith('!stop'):
		string = remark(message)
		await message.channel.send(string.format(message))
		wakeup()
		if server == 1:
			await message.channel.send("I'm shuttin' it down".format(message))
			pyautogui.typewrite("stop", 0.1)
			pyautogui.hotkey('enter')
		else:
			await message.channel.send("Server isn't even running".format(message))
	# !check
	if message.content.startswith('!check'):
		string = remark(message)
		await message.channel.send(string.format(message))
		if server == 1:
			await message.channel.send("dat boi is RUNNIN".format(message))
		else:
			await message.channel.send("server is CLOSED as shit dawg".format(message))

	#!seed
	if message.content.startswith('!nut'):
		string = remark(message)
		await message.channel.send(string.format(message))
		await message.channel.send("Seed is:3985649022229122452".format(message))

	# bad word filter

	#for badword in badwords:	
	#	if badword in message.content:
	#		await message.channel.send(random.choice(replies))
#
	#for badword in badwords:
	#	if message.content.startswith(cutit(badword,1)):
	#		await message.channel.send(random.choice(replies))


	# address
	if "address" in message.content:
		result = run('dig +short myip.opendns.com @resolver1.opendns.com',stdout = PIPE, universal_newlines = True,shell=True)
		ip = result.stdout
		ip = ip[:-1]
		print(ip)
		await message.channel.send("the Server's adress is 99.242.42.49:25565")
	# link
	if message.content.startswith('!link'):
		string = remark(message)
		await message.channel.send(string.format(message))
		#await message.channel.send ("https://www.dropbox.com/sh/9t1idqm558tpxzk/AABjGMy0khpodX6PLvaEF8vfa?dl=0")
		await message.channel.send ("sorry, this feature was causing to many problems :(")

	# backups
	if message.content.startswith('!backup'):
		string = remark(message)
		await message.channel.send(string.format(message))
		await message.channel.send("Backing up the world. This might take awhile")
		currentDT = datetime.datetime.now()

		print ("starting Backup " + currentDT.strftime("%B-%d-%y"))

		shutil.rmtree('/home/gabriel/minecraftServer/World Backups/Most Recent World')
		shutil.copytree('/home/gabriel/minecraftServer/world' , '/home/gabriel/minecraftServer/World Backups/Most Recent World' )
		shutil.copytree('/home/gabriel/minecraftServer/world' , '/home/gabriel/minecraftServer/World Backups/archives/MCWorldBackup ' + 		currentDT.strftime("%B-%d-%y-[%H:%M:%S]") )
		#shutil.rmtree('/home/gabriel/Dropbox/MineCraftBackups/MostRecentWorld')
		#shutil.copytree('/home/gabriel/minecraftServer/world' , '/home/gabriel/Dropbox/MineCraftBackups/MostRecentWorld' )
		print("Backup Finished!")
		await message.channel.send("World has been backed up! " + currentDT.strftime("%B-%d-%y-[%H:%M:%S]"))


	# addBadWord	
	if message.content.startswith("!addbad"):
		badwords.append(cutit(message.content,7))
		saveWords()
		loadWords()
		print(badwords)
		await message.channel.send("don't say that ever again")
		
	#!refresh
	if message.content.startswith("!r"):
		loadWords()
		with open('replies.txt','r') as fb:
			for line in fb:
				replies = json.loads(line)
		print(badwords)
		
		

	#log 
	if message.content.startswith("!log"):
		string = remark(message)
		await message.channel.send(string.format(message))

		path = "/home/gabriel/minecraftServer/logs/latest.log"
		log = open(path)
		lines = log.readlines()
		
		for i in range(logLine,len(lines)):
			await message.channel.send(str(logLine) + "> " + lines[i])
			logLine+=1
		await message.channel.send("------------------")
						

			#await message.channel.send("----SERVER LOG----")
			#path = "/home/gabriel/minecraftServer/logs/latest.log"
			#os.chdir("/home/gabriel/minecraftServer/logs")
			#log = open(path,"r")
			#string = log.read()
			#await message.channel.send(string)
			#await message.channel.send("------------------")
				
		log.close()

		#log 
	if message.content.startswith("!chat"):
		
		path = "/home/gabriel/minecraftServer/logs/latest.log"
		log = open(path)
		lines = log.readlines()

		path2 = "/home/gabriel/minecraftServer/logs/chatlog.txt"
		chatlog = open(path2,"a")
		
		for i in range(chatLogLine,len(lines)):
			string = cutit(lines[i],33);
			if string.find("<") >= 0:
				#await message.channel.send(string)
				chatLogLine+=1
				chatlog.write(string);
				channel = client.get_channel(633482666058186781)
				await channel.send(string)
			#await message.channel.send("------------------")
						

			#await message.channel.send("----SERVER LOG----")
			#path = "/home/gabriel/minecraftServer/logs/latest.log"
			#os.chdir("/home/gabriel/minecraftServer/logs")
			#log = open(path,"r")
			#string = log.read()
			#await message.channel.send(string)
			#await message.channel.send("------------------")
				
		log.close()
		chatlog.close()

		
		
		
		#os.chdir("/home/gabriel/minecraftServer")

	#chat scanner

	if message.content.startswith(">"):
		if server == 1:
			string = "<" + message.author.name + "> " + cutit(message.content,1) 
			wakeup()
			pyautogui.typewrite('tellraw @a {"text":"' + string + '","color":"gray"}', 0.03)
			pyautogui.hotkey('enter')

			path2 = "/home/gabriel/minecraftServer/logs/chatlog.txt"
			chatlog = open(path2,"a")
			chatlog.write(string)
			chatlog.close()

			channel = client.get_channel(633482666058186781)
			await channel.send(string)
			
		else:
			await message.channel.send(" No ones listening, pal")
		
	

	# help
	if message.content.startswith("!help"):
		await message.channel.send("COMMANDS: \n ----------------- \n \n !start - starts the server \n \n !stop - stops the server \n \n !check - tells you if the server is running \n \n !address - gives you the servers adress, just in case it changes\n !backup - backs up the world. this takes awhile\n !link - provides a download link for the world as of the latest backup".format(message))

#checking minecraft logs in the background
async def log_background_task():
	global chatLogLine
	await client.wait_until_ready()
	print("Background loop is starting!!")
	while 1 > 0:
		while server == 0:
			await asyncio.sleep(15)
		while server == 1:
			await asyncio.sleep(15)
			path = "/home/gabriel/minecraftServer/logs/latest.log"
			log = open(path)
			lines = log.readlines()

			path2 = "/home/gabriel/minecraftServer/logs/chatlog.txt"
			chatlog = open(path2,"a")
		
			for i in range(chatLogLine,len(lines)):
				string = cutit(lines[i],33);
				chatLogLine+=1
				if string.find("<") >= 0:
					if string.find("<--") <0:	
					
						chatlog.write(string);
						channel = client.get_channel(633482666058186781)
						await channel.send(string)
				
			log.close()
			chatlog.close()
			

# on start

@client.event
async def on_ready():
	print('logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')	
	


# main
#pathToLog = "/home/gabriel/minecraftServer/logs/latest.log"
#new_log = open(pathToLog,"w")
#new_log.write('')
#new_log.close()

loadWords()
with open('replies.txt','r') as fb:
	for line in fb:
		replies = json.loads(line)

#client.loop.create_task(log_background_task())
client.run(TOKEN)




