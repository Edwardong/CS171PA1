import socket
from public import P1PORT, P2PORT, P3PORT, NETWORK_PORT, process_str

# protocol(for easily parsing):
    # ClockreceiveSenderReceiverMsg
    # e.g.: 3receiveP1P2LetsDance

# need to figure out the appropriate usage of Port
if __name__ == '__main__':

    in_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    in_sock.bind(("localhost", NETWORK_PORT))
    in_sock.listen(1)

    while(True):
        stream, addr = in_sock.accept()
        data = stream.recv(1000)
        print(data)
        clock, sender, receiver, message = process_str(data.decode('utf-8'))

        out_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        out_sock.connect(("localhost", P1PORT))
        out_sock.sendall(data)


    # init three threads(sockets) connecting to three clients,
    # each does the same thing: receive -> parse -> send
