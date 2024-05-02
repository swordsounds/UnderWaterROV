import socket
import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S") 

data = {
  "time": [],
  "depth": []
  }

df = pd.DataFrame(data)

serverAddress = ('192.168.1.142', 2222)
bufferSize = 1600000 
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with open('receiveFile.txt','w') as f:
    f.write('')
while True:
    cmd=input('data start or fat or final data?'+'\n')
    cmd=cmd.encode('utf-8')
    UDPClient.sendto(cmd, serverAddress)
    margin_output=input("Enter a margin of error: ")
    margin_output=margin_output.encode('utf-8') 
    UDPClient.sendto(margin_output, serverAddress)
    data,address=UDPClient.recvfrom(bufferSize)
    data=data.decode('utf-8')
    with open('receiveFile.txt','w') as f:
        f.write(data)
        f.writelines('file')
    f=open('receiveFile.txt','r')
    content = f.read()
    data['depth'].append(content)
    data['time'].append(current_time)
    df.to_csv('receiveFile.csv', encoding='utf-8', index=False)
    f.close()
