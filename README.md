# FeatherPicker
Non Twitter API based Twitter page scraper for the RIT CSEC Openhouse.


### About.
This application was developed for the Rochester Insitute of Technology's
open house event in the Fall of 2015.


### How it works.

This Python script scrapes a designated page for the format of
***CSEC.word1.word2***

The designated value tweeted to an individual is then parsed
where word1 is the machine and word2 is an action
to perform against said machine.

### Capabilities
* Killing firefox
* Logging off a user
* Killing Explorer
* Launching a thousand calc.exe (death by calc).

### Known issues
If there are a large ammount of requests occuring at once, then a race condition exists
and which ever tweet is first will be the once scraped by FeatherPicker.
