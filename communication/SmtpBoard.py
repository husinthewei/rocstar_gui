import socket

class SmtpBoard:
    def __init__(self, addr = "127.0.0.1", port = 31415):
        self.addr = addr
        self.port = port

        # use TCP for board I/O
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.addr, self.port))
        # 10 millisecond I/O timeout for reponses from board
        self.socket.settimeout(self.TIMEOUT_SECONDS)
    
    RECVBUFFERLEN = 2048
    TIMEOUT_SECONDS = 0.010

    def rd(self, addr):
        message = "R %x\n"%(addr)
        self.socket.send(message.encode())
        data = None

        while (data == None):
            try:
                data = self.socket.recv(self.RECVBUFFERLEN)
            except socket.timeout:
                pass

        data = str(data.decode())
        data_pieces = data.split(" ")
        if data_pieces[0] == "250" and int(data_pieces[2], 16) == addr:
            return int(data_pieces[3].split("\n")[0], 16)
        else:
            return -1

    # Returns data written on success, otherwise -1
    def wr(self, addr, data):
        message = "W %x %x\n"%(addr, data)
        self.socket.send(message.encode())
        response = self.socket.recv(self.RECVBUFFERLEN)
        response_pieces = str(response)[2:][:-3].split(" ")
        if response_pieces[0] == "250":
            return int(response_pieces[3], 16)
        else:
            return -1
