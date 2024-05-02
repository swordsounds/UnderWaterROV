import socket
import time 
from time import sleep
import explorerhat as hat
bufferSize=16000
ServerPort=2222
ServerIP='192.168.1.142'
RPIServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIServer.bind=ì((ServerIP,ServerPort))
print('Server up and listening')
cnt2=0
while True:
    with open('YourFileHere.txt', 'w') as f:
        f.write('')
    cmd,address=RPIServer.recvfrom(bufferSize)
    cmd=cmd.decode('utf-8')
    slider_value_list = []
    while cnt !=5:
        cnt=0
        slider_value_list=[]
        with open('YourFileHere2.txt', 'w') as file:
            file.write('')
        while cnt !=20:
            #start to collect data
            slider=hat.analog.one.read()
            slider_value=(slider*100)/4
            slider_value_list.append(slider_value)
            with open('YourFileHere2.txt','a+') as file:
                file.writelines(str(slider_value)+ '\n')
            sleep(0.1)
            cnt+=1

        file=open('YourFileHere2.txt','r')
        list_value = file.read()
        with open ('YourFileHere.txt','a+') as f:
            f.writelines(str(list_value)+ '\n')
#We do the avarege of the list so we can confront the overall
# with the last slider value
        def Avarege (slider_value_list):
            return sum(slider_value_list) / len(slider_value_list)
        avarege = Avarege(slider_value_list)
        overall_value= round(avarege, 0)
        last_slider_value = round (avarege, 0)
        different = overall_value-last_slider_value
#if the difference is not high the float come back!!
        if different<5 and different>-5:
            print('come back')
        f.close()
        cnt2 += 1
        sleep(0.5)
    f= open('YourFileHere.txt', 'r')
    data = str (f.read())
    data=data.encode('utf_8')
    RPIServer.sendto(data, address)
    print('Client Address', address[0])
    f.close()
    sleep(1)

