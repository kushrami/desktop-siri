#Author : kushrami


import os,pyttsx,urllib,feedparser
import speech_recognition as sr

def text_speech(text):
   engine = pyttsx.init()
   engine.setProperty('rate', 150)
   voice=pyttsx.voice.Voice
   voice.id= 0x0000000002CC9000
   engine.setProperty('male', voice.id)
   s=text
   engine.say(s)
   engine.runAndWait()
def speech_text():
   with sr.Microphone() as source:
      r = sr.Recognizer()
      audio = r.listen(source)
      print("You said " + r.recognize(audio))
      return r.recognize(audio)
      
def open_movie(string):
   a=""
   movie_list=["hulk","avengers","superman"]
   for word in string:
      if word in movie_list:
         a="E:/kush lepi/iron man 1,2,3/"+word+".mkv"
         s="sir, opening"+word+"movie, it's a awesome movie , enjoy it"
         text_speech(s)
         os.startfile(a)
         continuos_loop()
         
def open_software(string):
     software_list=["chrome","excel","word","notepad","wordpad","powerpoint","processing","putty","mspaint"]
     for software_name in string:
          if software_name in software_list:
              s="sir, i am opening "+software_name+" for you"
              text_speech(s)
              arg="start "+software_name+".exe"
              os.system(arg)
              continuos_loop()

def readmail():
    opener = urllib.FancyURLopener()
    _URL = "https://mail.google.com/gmail/feed/atom"
    f = opener.open(_URL)
    feed = f.read() 
    atom = feedparser.parse(feed)
    text_speech(atom.entries[1].title)
    continuos_loop()

def readnews(key):
    found=[]
    collect=[]
    url=["http://news.google.com/?output=rss","http://news.yahoo.com/rss/","http://rss.cnn.com/rss/edition.rss/rss/edition_us.rss"]
    for url in url:
       feed = feedparser.parse(url)
       entries = feed.entries
       for entry in entries:      
           if key in entry.title:
              text_speech(entry.title)
              collect.append(entry.title)
       if collect!=[]:
           found.append(collect)
    if found==[]:
        d="sorry sir there is no latest news on "+key
        text_speech(d)
    continuos_loop()      

def continuos_loop():
      print "inside continuos loop..."
      try:
        result=speech_text()
        print "looping..",result
        if result=="jarvis":
           main()
        else:
           continuos_loop()
           
      except LookupError:                            
        continuos_loop()  

def main():
   arg=""
   s=""
   try:
      text_speech("sir")
      result=speech_text()
      temp=result.split(" ")
      open_software(temp)
      if "movie" in temp:
          open_movie(temp)
      if "mail" in temp:    
          readmail()
      if "news" in temp:
          key=temp[-1]
          readnews(key);
      
        
   except LookupError:                            
      print("Could not understand audio")
      text_speech("sorry sir will you please repeat again")
      continuos_loop()


      

if __name__=="__main__":
   text="Hello sir .."
   text_speech(text)
   main()
