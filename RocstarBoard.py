from SmtpBoard import SmtpBoard
from Register import Register
from RegisterBoard import RegisterBoard

class RocstarBoard(RegisterBoard):
	def __init__(self, addr = "127.0.0.1", port = 31415):
		smtp_board = SmtpBoard(addr, port)
		self.smtp_board = smtp_board
		RegisterBoard.__init__(self, smtp_board, "Rocstar")

		# uzed registers
		self.num_reg = Register(0x0000, smtp_board, 10)
		self.beef_reg = Register(0x0001, smtp_board, 10)
		self.dead_reg = Register(0x0002, smtp_board, 10)
		self.a7_clk_reg = Register(0x0003, smtp_board, 5)
		self.a7_cfg_program = Register(0x0004, smtp_board, 5)
		self.a7_cfg = Register(0x0005, smtp_board, 5)
		self.num_reg_2 = Register(0x0007, smtp_board, 10)
		self.uzed_uptime = Register(0x0008, smtp_board, 1)
		self.count_reg = Register(0x0009, smtp_board, 1);
		self.fw_yyyy = Register(0x0010, smtp_board, 60)
		self.fw_mmdd = Register(0x0011, smtp_board, 60)
		self.fw_hhmm = Register(0x0012, smtp_board, 1)
		self.uztoa7 = Register(0x0019, smtp_board, 1)
		self.mcuclk_mhz = Register(0x001a, smtp_board, 1)
		self.a7_lastword = Register(0x0080, smtp_board, 1)
		self.a7_lastread = Register(0x0081, smtp_board, 1)
		self.a7_bytesseen = Register(0x0083, smtp_board, 1)
		self.a7_bytessent = Register(0x0084, smtp_board, 1)
		self.a7_bus_data_conf = Register(0x000d, smtp_board, 1)

		self.add_register("uzed", self.num_reg)
		self.add_register("uzed", self.beef_reg)
		self.add_register("uzed", self.dead_reg)
		self.add_register("uzed", self.a7_clk_reg)
		self.add_register("uzed", self.a7_cfg_program)
		self.add_register("uzed", self.a7_cfg)
		self.add_register("uzed", self.num_reg_2)
		self.add_register("uzed", self.uzed_uptime)
		self.add_register("uzed", self.count_reg)
		self.add_register("uzed", self.fw_yyyy)
		self.add_register("uzed", self.fw_mmdd)
		self.add_register("uzed", self.fw_hhmm)
		self.add_register("uzed", self.uztoa7)
		self.add_register("uzed", self.mcuclk_mhz)
		self.add_register("uzed", self.a7_lastword)
		self.add_register("uzed", self.a7_lastread)
		self.add_register("uzed", self.a7_bytesseen)
		self.add_register("uzed", self.a7_bytessent)
		self.add_register("uzed", self.a7_bus_data_conf)