# UDP communication between python and Unity
#%%
import socket
import time
import numpy as np



# use ip for localhost: '127.0.0.1' with port: '1234' to communicate with the unity c# script provided
UDP_IP="127.0.0.1"
UDP_PORT=1234
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def positional_data(x_position,z_position,y_position,roll,pitch,yaw):
    
    # Positional coordinates
    ## xz makes up the ground plane


    # Cocatinated string, converted into utf-8
    pos = str(x_position)+','+str(y_position)+','+str(z_position)+','+str(roll)+','+str(yaw)+','+str(pitch)
    pos = bytes(pos,'utf-8')
    return pos

def send_UDP(msg,ip_addr,port):
    # This method exists because i dont like to deal with the sock methods
    sock.sendto(msg,(ip_addr,port))




def test_connection():
    x_pos=0
    while True:
        
        speed = 1
        x_pos+=speed
        pos = positional_data(x_pos,1,1,0,0,0)
        send_UDP(pos,'127.0.0.1',1234)
        time.sleep(.5)





if __name__ =='__main__':
    test_connection()


