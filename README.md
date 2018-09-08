# ytmp3dl
ytmp3dl is a program made to download any audio from youtube. It is done completely on the command line using Python2. It is compatible on any system that can run and install modules with Python. Read this documentation in order to understand how it works and to get started!

# Getting Started
To start using ytmp3dl first you must install a few Python Modules. Lucky for you I have included a requirements.txt so it will be much easier for you. To start clone this repo and cd into the directory you saved it in with terminal. Once you do that run this command: 
```
pip install -r requirements.txt
```

This will install all necessary modules for this program without you having to do them individually.

From there all you need to do is type:
```
python ytmp3dl.py
```

and you will be able to enter your search and use the program. Once you run the program you will be asked what you would like to search for. Treat this as you would the search box on Youtube itself. After entering your query you will see a table displayed with the top 50 results. I don't think you will need much more as what you want will most likely be up at the top. **Be careful however as there are some results that may be a Channel or Topic rather than a video.** After this you will enter a number to choose what song/video you'd like to download.

The program will then ask you what audio format you would like to use. Most of the time mp3 will be the best bet but you have an option of some other formats such as aac, flac, m4a, opus, vorbis, or wav. If you want the best possible quality you can always use the option best. 

If you have any issues feel free to report them to my Issues page!

# How Does It Work?
The program starts by taking in a user input as the search query. From there it requests a query to S0n1c's minitube API which returns a json reponse that includes titles, ids, page types, and more. We use this to pull the ID and Title of each result. PrettyTable then displays it with the number choice on the left and the title of the song/video on the right. We then take a user input as to which video number we would like to download. From there it uses the youtube-dl module to grab the webpage, download it, and rip the audio from the .webm file of the video. Basic stuff.

# Credits

[youtube-dl](https://rg3.github.io/youtube-dl/index.html) Python Module is used for downloading purposed.

[@S0n1c_Dev](https://twitter.com/S0n1c_Dev) for his awesome MiniTube API.

[shubhamaggarwal](https://github.com/shubhamaggarwal) for inspiration from youtube-mp3-downloader

# Links

Follow me on [Twitter Here](https://twitter.com/maxbridgland)

Join my Dev Discord Server [Here](https://discord.gg/kuCqSMt)
