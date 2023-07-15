#!/usr/bin/env python
import os
from pytube import YouTube, Playlist

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

## Prerequisites: pytube, python3

def download_song(link, dir_name):
	try:
		stream = YouTube(link).streams.get_audio_only()
		file_name = stream.title+".mp3"
		print("Downloading file {title}".format(title=file_name))
		stream.download(output_path=dir_name, filename=file_name.replace("/", "|"))
	except:
		print("\nDownload failed for link "+link)

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
	
	directory_name = input("Enter the name for the resulting directory\n(or leave blank to use file name above)\n> ")
	if (directory_name == ''):
		directory_name = list_file_name.rsplit('.', 1)[0]
	##if ("playlist?list=" in list_file_name):
		## Download Playlist
		## https://www.youtube.com/playlist?list=PLbGPxEqspS_zYsXsKat52H95CNjdPpgPV
	##else:
	files_list = []
	with open(list_file_name, "r") as f:
		files_list = f.readlines()
	download_songs(files_list, directory_name)

	

