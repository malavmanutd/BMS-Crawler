from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
url = "https://in.bookmyshow.com/ahmedabad/events"
account_sid = #your account sid
auth_token = #your token
client = Client(account_sid, auth_token)



source_code = requests.get(url)
#print(source_code)
plain_text = source_code.text
#print(plain_text)
soup = BeautifulSoup(plain_text,"html.parser")
flag=0
for link in soup.find_all('div',{'class':'card-title'}):
    #print(link.text)
   # print( link.text[0:4])
    if link.text[1:4] == "AFC": #AFC can be reaplaced with your event key words. I was checking for event named AFC
        print("event found")

        message = client.messages \
            .create(
            body="your event "+ link.text + "is available on BookMyShow",
            from_=#sender mobile no,
            to=#mobile no
        )
        print(message.sid)
