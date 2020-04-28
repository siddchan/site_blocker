#this app can be used to block the sites you mention below
#this can be used to increase productivity
#do disable any query in antivirus


import time
from datetime import datetime as dt

hosts_temp="hosts"
#this is a temp file
# remove below hash tag to enable system wide blocker
# hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
#enter name of site want to block
websites_list=["www.facebook.com","epcigames.com","facebook.com"]

start_time= 8
#enter the start time here
end_time=17
#enter the ending time here
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):
        print("CONCENTRATE ON YOUR WORK")
        with open(hosts_temp,'r+') as file:
            content= file.read()
            for website in websites_list:
                 if website in content:
                    pass
                 else:
                    file.write(redirect +" "+ website +"\n")

    else:
        with open("hosts",'r+') as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("ITS TIME FOR PLAY")

    time.sleep(5)

