import socket
import time


def client():
    TCP_IP = "127.0.0.1"
    TCP_PORT = 6776
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    # for i in range(10):
    #     s.send(b"gripper#right#close")
    #     print(s.recv(BUFFER_SIZE))
    #     s.send(b"gripper#left#close")
    #     print(s.recv(BUFFER_SIZE))
    #     time.sleep(3)
    #     s.send(b"gripper#right#open")
    #     print(s.recv(BUFFER_SIZE))
    #     s.send(b"gripper#left#open")
    #     print(s.recv(BUFFER_SIZE))
    #     s.send(b"arm#right#0.8#-0.2#0.2#-0.373#0.928#0.0135#0.015")
    #     print(s.recv(BUFFER_SIZE))
    #     time.sleep(3)

    x, y, z = 0.8, -0.2, 0.2
    left, right = True, True 
    s.send(b"arm#right#{}#{}#{}#-0.373#0.928#0.0135#0.015".format(x, y, z))
    while True:
        mode=int(raw_input('Cmd:'))
        if mode == 0:
            break 
        elif mode == 1:
            x += 0.05    
        elif mode == 2:
            x -= 0.05    
        elif mode == 3:
            y += 0.05     
        elif mode == 4:
            y -= 0.05     
        elif mode == 5:
            z += 0.05     
        elif mode == 6:
            z -= 0.05     
        elif mode == 7:
            if right:
                s.send(b"gripper#right#{}".format('close'))
                right = False 
            else:
                s.send(b"gripper#right#{}".format('open'))
                right = True
            continue
        elif mode == 8:
            if left:
                s.send(b"gripper#left#{}".format('close'))
                left = False 
            else:
                s.send(b"gripper#left#{}".format('open'))
                left = True
            continue
        s.send(b"arm#right#{}#{}#{}#-0.373#0.928#0.0135#0.015".format(x, y, z))

    s.close()
    print("Fin")


if __name__ == "__main__":
    client()
