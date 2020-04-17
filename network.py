import socket

P1PORT = 5001
P2PORT = 5002
P3PORT = 5003
NETWORK_PORT = 5006

# protocol(for easily parsing):
    # ClockreceiveSenderReceiverMsg
    # e.g.: 3receiveP1P2LetsDance
def process_str(msg):
    sender_index = msg.find("P")
    sender = msg[sender_index:sender_index+2]
    receiver = msg[sender_index+2:sender_index+4]
    receive_index = msg.find("receive")
    clock = int(msg[0:receive_index])
    message = msg[sender_index+4:]
    return clock, sender, receiver, message


# need to figure out the appropriate usage of Port
if __name__ == '__main__':
    print(process_str("3receiveP1P2LetsDance"))

    in_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    in_sock.bind(("localhost", NETWORK_PORT))
    in_sock.listen(1)

    while(True):
        stream, addr = in_sock.accept()
        data = stream.recv(1000)
        print(data)
        print(process_str(data.decode('utf-8')))

        # out_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # out_sock.connect((HOST, P1PORT))
        # out_sock.send_all


    # init three threads(sockets) connecting to three clients,
    # each does the same thing: receive -> parse -> send
