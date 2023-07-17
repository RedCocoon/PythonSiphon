#!/usr/bin/env python
import os
from pytube import YouTube, Playlist
from pydub import AudioSegment

conv_format = ""

## This is a tool to download youtube videos and playlists automatically.
## To use, put this .py file in the same directory as a file with a list
## of the videos/playlists you wanted to download, separated by new lines for each
## entry.

## Example to use (remove the ###)
###https://www.youtube.com/watch?v=dQw4w9WgXcQ
###https://www.youtube.com/watch?v=xvFZjo5PgG0
###https://www.youtube.com/watch?v=BBJa32lCaaY
###https://www.youtube.com/playlist?list=PLXa7L1ovsDcMwMxwBF4vyh-RLYkFABlb2

## Code by Red Cocoon, all rights reserved.

## Prerequisites: 
## - PIP > pytube, ffprobe, pydub
## - System > ffmpeg, python3

def download_song(link, dir_name):
	#try:
		
				    	
	stream = YouTube(link).streams.get_audio_only()
	file_name = stream.title
	
	m4a_file = file_name.replace("/", "|")+".m4a"
	conv_file = file_name.replace("/", "|")+"."+conv_format
	print("Downloading file {title}".format(title=m4a_file))
	stream.download(output_path=dir_name, filename=m4a_file)
	
	print("File {0} sucessfully downloaded ".format(m4a_file), end='')
	
	if (conv_format != "m4a"):
		try:
			sound = AudioSegment.from_file(dir_name+"/"+m4a_file, format='m4a')
			file_handle = sound.export(dir_name+"/"+conv_file, format=conv_format)
		except:
			print("but failed to convert.")
			return
		
		os.remove(dir_name+"/"+m4a_file)
		print("and converted", end='')
	print(".")
		
	#except:
	#	print("\nDownload failed for link "+link)

def download_songs(files_list, dir_name):
	index = 1
	total = len(files_list)
	for i in files_list:
		print("[{current}/{total}]".format(current=index, total=total), end=' ')
		if (i.find("playlist") != -1):
			 ## Download Playlist
			 p = Playlist(i)
			 playlist_title = p.title
			 print("Downloading playlist {title}".format(title=playlist_title))
			 for url in p.video_urls:
			 	download_song(url, dir_name+"/"+playlist_title)
		else:
			download_song(i, dir_name)
		index += 1

while (True):
	list_file_name = input("Enter the file name containing the list\n(or 'done' to stop)\n> ")
	if (list_file_name == "done"):
		exit()
	files_list = []
	try:
		with open(list_file_name, "r") as f:
			files_list = f.readlines()
	except:
		print("[Error] with opening list file. Is the file name correct with extension?\n")
		continue
	
	directory_name = input("Enter the name for the resulting directory\n(or leave blank to use file name above)\n> ")
	

	conv_format = input("Enter the target audio format, or leave blank for .m4a\n(accepts all FFMPEG supported formats)\n> ")
	
	if (conv_format == ''):
		conv_format = "m4a"
	
	if (directory_name == ''):
		directory_name = list_file_name.rsplit('.', 1)[0]
	##if ("playlist?list=" in list_file_name):
		## Download Playlist
		## https://www.youtube.com/playlist?list=PLbGPxEqspS_zYsXsKat52H95CNjdPpgPV
	##else:
	download_songs(files_list, directory_name)

	

