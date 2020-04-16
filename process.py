import re
import argparse
from client import Client
import threading
import queue
import socket
import time

P1PORT = 5001
P2PORT = 5002
P3PORT = 5003

shared_queue = queue.Queue()

""" input format:
    local event_name
    send P_i event_name """
# def process_str(input):
#     rule = re.compile(r"[^a-zA-Z0-9]")
#     message = ''
#     if input[:5] == "local":
#         input_list = input.strip().split()
#         event = input[6:]
#         for i in range(len(input_list)):
#             input_list[i] = rule.sub('',input_list[i])
#         return ("local", event, message)
#     else:
#         receiver = input[5:7]
#         message = input[8:]
#         return ("send", receiver, message)

#need to think about this more
def start_process(this_client):
    #where = ""
    while True:
        while shared_queue.empty():
            pass
        one_event = shared_queue.get()
        #print(one_event)
        if one_event[:5] == "local":  # e.g. local Wakeup
            where = "local"
            event = one_event[6:]
            this_client.update_clock(0)
            this_client.update_events("local: " + event)
        elif one_event[:5] == "send":
            where = "remote"
            receiver = one_event[5:7]
            message = one_event[8:]
            this_client.update_clock(0)
            this_client.update_events("send: " + receiver + message)

def send_msg(host,port,local_clock,msg):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    time.sleep(5)
    # communication process needs these
    # if receiver == "P1" or receiver == "p1":
    #     port = P1PORT
    # elif receiver == "P2" or receiver == "p2":
    #     port = P2PORT
    # elif receiver == "P3" or receiver == "p3":
    #     port = P3PORT
    # else:
    #     print("error receiver id")
    #     return
    s.connect((host,port))

    s.send()






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('port',type=int)
    parser.add_argument('pid', type=int)
    arg = parser.parse_args()
    #port = arg.port
    this_pid = arg.pid

    this_client = Client(this_pid)
    process_thread = threading.Thread(target=start_process, args=(this_client,))
    process_thread.start()

    while True:
        one_event = input()
        if one_event[:5] == "print":
            this_client.print_clock()
        elif one_event[:4] == "quit":
            break
        else:
            shared_queue.put(one_event)
    process_thread.join()
    exit()







