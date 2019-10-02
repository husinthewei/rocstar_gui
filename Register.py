from SmtpBoard import SmtpBoard

class Register:
    def __init__(self,
                 addr,
                 smtp_board,
                 name = "unnamed",
                 v5 = False,
                 format_method = None,
                 refresh_rate = 1):
        self.name = name
        self.addr = addr
        self.board = smtp_board
        if v5:
            self.read_method = Register.read_s6
            self.write_method = Register.write_s6
        else:
            self.read_method = Register.read_uzed
            self.write_method = Register.write_uzed
        self.fmt = format_method if format_method else Register.format_04x
        self.data = -1

    def write_s6(self, data):
        addr = self.addr | 0x10000
        return self.board.wr(addr, data)

    def write_uzed(self, data):
        return self.board.wr(self.addr, data)

    def read_s6(self):
        addr = self.addr | 0x10000
        self.data = self.board.rd(addr)
        return self.data

    def read_uzed(self):
        self.data = self.board.rd(self.addr)
        return self.data

    def rd(self):
        return self.read_method(self)

    def wr(self, data):
        return self.write_method(self, data)

    def rfmt(self):
        return self.fmt(self)

    def format_d(self):
        #format data as decimal int (%d)
        return "%d"%(self.data)

    def format_04x(self):
        #format data as 4-digit hexadecimal int (%04x)
        return "%04x"%(self.data)

    def format_time(self):
        # format data as time hh:mm:ss
        if self.data<0:
            return "??:??:??"
        d = self.data
        return "%02d:%02d:%02d"%(d/3600, (d%3600)/60, d%60)

test_board = SmtpBoard()
reg1 = Register(0x1000, test_board, v5 = True)
reg2 = Register(0x1000, test_board, v5 = False, format_method = Register.format_time)

print(reg1.wr(0x1))
print(reg2.wr(0xbeef))

print("reg1 %x"%(reg1.rd()))
print("reg2 %x"%(reg2.rd()))

print(reg1.rfmt())
print(reg2.rfmt())