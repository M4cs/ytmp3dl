#!/usr/bin/python2
from __future__ import unicode_literals
import youtube_dl
import requests, os, sys, json, re, time
from sys import platform
from prettytable import PrettyTable


if platform == "linux" or platform == "linux2":
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        END = '\033[0m'
elif platform == "win32":
    class color:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        END = ''
elif platform == "darwin":
    class color:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        END = ''

class banner:
    header = """
YT Audio Downloader by Macs

[!] WARNING: Use of this tool may be illegal but it is not meant for that use,
If you use it for Illegal purposes I am not responsible for any concequences that come your way.[!]

No Need To Find A Link Do It All From The Command Line!

Simply search what ever video you want to download. Find it on the results. Pick the number and BOOM
Ez Pz Downloads in whatever audio format you'd like :)

Credits:

S0n1c for the great minitube API
Yak for helping out when I was confused
Cipher for the color compatibility on other systems than Linux
Google for making Youtube
shubhamaggarwal on GitHub for inspiration
""" + '\033[91m' + """[*] FILES WILL BE SAVED TO THE SAME DIRECTORY AS THE SCRIPT [*]"""

def scrape():
    print banner.header
    try:
        api = "https://server.s0n1c.org/minitube/"
        tagSearch = raw_input(color.BLUE + "\nWhat would you like to search?: ").replace(" ", "+")
        useragent = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        header = useragent
        query_url = api + "/search/" + tagSearch
        try:
            response = requests.get(query_url).json()
        except TypeError:
            pass
    except TypeError:
        pass
    try:
        title = []
        ref = []
        for x in response:
            title.append(x['title'])
            ref.append(x['id'])
        sequence = ["No.", "Title"]
        table = PrettyTable(sequence)
        size = len(title)
        print "Showing First 50 Results: "
        sys.setrecursionlimit(100000)
        for i in range(size):
            table.add_row([i + 1, title[i]])
        if len(title) != 0:
            print "\nResults: "
            print table
            choice = raw_input(color.YELLOW + "\nEnter the number you would like to download: " + color.END)
            if 1 <= int(choice) <= len(title):
                filename = title[int(choice) - 1]
                video_url = "https://www.youtube.com/watch?v=" + str(ref[int(choice) - 1])
                print "\nTitle: " + filename
                print "\nDirect Link: " + video_url
                return filename, video_url
            else:
                print "Invalid Entry.. Exiting"
                sys.exit()
        else:
            print "No Results Found Sorry"
    except TypeError:
        pass

def download():
    filename, video_url = scrape()
    format = raw_input(color.GREEN + "Please Choose A Format (mp3, aac, flac, m4a, opus, vorbis, or wav): " + color.END)
    print color.BLUE + "\nDownloading Your File Now!" + color.END
    os.system("youtube-dl " + video_url + " -x --audio-format " + format)
    print "Completed! Your file has been saved!"
    sys.exit()
download()
