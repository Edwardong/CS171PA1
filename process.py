import re
import argparse
import client
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
def start_process():
    #where = ""
    while True:
        while shared_queue.empty():
            pass
        one_event = shared_queue.get()
        if one_event[:5] == "local":  # e.g. local Wakeup
            where = "local"
            event = input[6:]
            this_client.update_clock(1)
            this_client.update_event("local: " + event)
        elif one_event[:5] == "send":
            where = "remote"
            receiver = input[5:7]
            message = input[8:]
            this_client.update_clock(1)
            this_client.update("send: " + receiver + message)
    return

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

    this_client = client(this_pid)
    process_thread = threading.Thread(target=start_process, args=this_client)

    while True:
        one_event = input()
        if one_event[:5] == "print":
            this_client.print_clock()
        else:
            shared_queue.put(one_event)








