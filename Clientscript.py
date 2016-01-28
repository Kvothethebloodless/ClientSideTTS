import numpy as np
import alsaaudio as aa
import wave as wv
import websocket as wb
import threading 
import requests
import json
import time
import os
import subprocess
import requests.exceptions as re
class sock():
    def __init__(self):
        
        self.username = "a18d40a6-098a-4bb7-b11e-37b523b5632e" 
        self.passwd = "EZ2LqHPVCF36"
        self.auth = (self.username,self.passwd)
        
        
        self.apilink = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
        self.initheaders = {"content-type": "application/json"} 
        self.data = {"text":"Hello World"}#, "accept":"audio/wav"}
        self.precmd = 'curl -u "'+self.username+'":"'+self.passwd+'" '+ "\ " + '"'
        self.full_cmd = """curl -u "a18d40a6-098a-4bb7-b11e-37b523b5632e":"EZ2LqHPVCF36" \ "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?text="""

        
    def getspeech(self,message):
        
        self.data['text'] = message
        #resp = requests.post(self.apilink, headers=self.initheaders, auth= self.auth,params=json.dumps(self.data))
        resp = requests.get(self.apilink, headers=self.initheaders, auth=self.auth, params=self.data)
       # self.fullcmd = self.precmd+resp.url+'" > transcript.wav'
       # self.fullcmd = self.full_cmd + 
       # os.system(self.full_cmd)
       # resp = 'tst'
        r = resp 
        path = 'playback.wav'
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        playcmd = 'xdg-open '+path
        os.system(playcmd)
        return
    def connectionerror(self):
        playcmd = 'xdg-open '+'ConnectionError.wav'
        os.system(playcmd)
    
    def pollserverformessages(self):
        messageserver = "http://manish.nvision.org.in/message"
        while(1):
            try:
                message_request = requests.get(messageserver)
                message = message_request.text
                if 'NoNoNoNo' in message:
                    print('No new message from the server')
                else:
                    print(message)
                    time.sleep(5)
                    self.getspeech(message)
            except re.ConnectionError,re.RequestException:
                self.connectionerror()
            time.sleep(3) 

"""     Are you gonna stay the night
     Are you gonna stay the night
     Oh oh oh oh, are you gonna stay the night

     Are you gonna stay the night
     Doesn't mean we're bound for life
     So oh oh oh, are you gonna stay the night

     Are you gonna stay the night
     Doesn't mean we're bound for life
     So oh oh oh, are you gonna stay the night

     I am fire gasoline,
     Come pour yourself all over me
     We'll let this place go down in flames only one more time

     You kill the lights, I'll draw the blinds
     Don't dull the sparkle in your eyes
     I know that we were made to break
     So what? I don't mind

     Are you gonna stay the night
     Are you gonna stay the night
     Oh oh oh oh, are you gonna stay the night

     Are you gonna stay the night
     Doesn't mean we're bound for life
     So oh oh oh, are you gonna stay the night (Night)

     Are you gonna stay the night

     Are you gonna stay the night
     Doesn't mean we're bound for life
     So oh oh oh, are you gonna stay the night"""




   

a = sock()
a.pollserverformessages()
