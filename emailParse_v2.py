import re  #regex needed to find IPs
#http://searchsignals.com/tutorials/reverse-dns-lookup/
import socket #socket needed to evaluate reverse IP lookup

mylist=['Delivered','Return-Path','Received-SPF','Authentication-Results','From','To','Date','Subject','Thread-Topic','Message-ID','Accept-Language','Content-Language','acceptlanguage','Content-Type','MIME-Version','  client-ip','X-Originating-IP']

nhand=input('File name please: ')
try:
    fhand=open(nhand)
except:
    print("File" ,nhand, "cannot be opened")
    quit()

print()
for i in fhand:
    i=i.rstrip()
#    print(i)
    # content=i.split()
    for item in mylist:
        # Skip 'uninteresting lines'
        if not i.startswith(item):
            continue
        # Print interesting line
        print(i)
print()

#this section reopens the file and searches for all the IPs in the document
mylist=list()
fhand=open(nhand)
print('I have found the following IPs')
for x in fhand:
    x=x.rstrip()
    pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    finalIP = re.findall(pattern, x)
    if len(finalIP) < 1: continue
    print(finalIP[0]) #since this is a list, printing [0] will remove '' for prettiness
    mylist.append(finalIP[0]) #calling sub 0 makes sure we arnt nesting lists

print()
for x in mylist:
    # print(x)
    try:
        reversed_dns = socket.gethostbyaddr(x)
    except:
        print('Could not retreive reverse IP lookup',x)
        continue
    else:
        print(x, ':', reversed_dns[0])
print()
