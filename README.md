# BMS-Crawler
A program will send text message to your phone when selected event will be available on BookMyShow. Program can be set on cron scheduling to run periodically.
# Requirments
- twilio messaging api
# Instruction
Set your token and SID. 
Input the event keyword for which you want to get notified.

Enter the details about phone numbers(Sender's number will be provided by twilio).

Following command will set crontab to execute code by every 10 minutes.

*/10 * * * * /usr/bin/env python2 /path/to/crawl.py
