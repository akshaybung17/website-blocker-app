import time
from datetime import datetime as dt

hosts_temp= "hosts"                                                      # test path
hosts_path="/etc/hosts"                                                  # main path
redirect="127.0.0.1"                                                     # ipv4
redirect_v6="::1"                                                        # ipv6
website_list=["www.facebook.com","facebook.com","www.goal.com", "goal.com"]    # list of websites to be blocked

while True:
    # conditions for blocking the websites when in working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Working hours...")
        # check if host file already has these websites listed which are to be blocked or not
        with open(hosts_path,'r+') as file:                              # open host file for reading and writing
            content=file.read()                                          # read file and store it to content variable
            for website in website_list:
                if website in content:                                   # if website name lready in file, then do not add website name to the hosts file
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")               # add website name to the file
                    file.write("\n"+redirect_v6+" "+website+"\n")
    # conditions for un-blocking the websites when in non-working hours
    else:
        with open(hosts_path,'r+') as file:
            # make a list of all items in the file
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()                                              # truncate the file contents below
        print("Fun hours...")
    time.sleep(5)                                                        # sleep for 5 secs
