from SmtpBoard import SmtpBoard
from Register import Register
from RegisterBoard import RegisterBoard

class RocstarBoard(RegisterBoard):
	def __init__(self, addr = "127.0.0.1", port = 31415):
		smtp_board = SmtpBoard(addr, port)
		self.smtp_board = smtp_board
		RegisterBoard.__init__(self, smtp_board, "Rocstar")

		# Debug registers
		zero_reg = Register(0x0000, smtp_board, 10)
		beef_reg = Register(0x0001, smtp_board, 10)
		uptime_reg = Register(0x0002, smtp_board, 1)
		self.add_register("debug", zero_reg)
		self.add_register("debug", beef_reg)
		self.add_register("debug", uptime_reg)