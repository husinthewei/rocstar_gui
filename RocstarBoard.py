from SmtpBoard import SmtpBoard
from Register import Register
from RegisterBoard import RegisterBoard

class RocstarBoard(RegisterBoard):
	def __init__(self, addr = "127.0.0.1", port = 31415):
		smtp_board = SmtpBoard(addr, port)
		self.smtp_board = smtp_board
		RegisterBoard.__init__(self, smtp_board, "Rocstar")

		# uzed registers
		num_reg = Register(0x0000, smtp_board, 10)
		beef_reg = Register(0x0001, smtp_board, 10)
		dead_reg = Register(0x0002, smtp_board, 10)
		a7_clk_reg = Register(0x0003, smtp_board, 5)
		a7_cfg_program = Register(0x0004, smtp_board, 5)
		a7_cfg = Register(0x0005, smtp_board, 5)
		num_reg_2 = Register(0x0007, smtp_board, 10)
		uzed_uptime = Register(0x0008, smtp_board, 1)
		count_reg = Register(0x0009, smtp_board, 1);
		fw_yyyy = Register(0x0010, smtp_board, 60)
		fw_mmdd = Register(0x0011, smtp_board, 60)
		fw_hhmm = Register(0x0012, smtp_board, 1)
		uztoa7 = Register(0x0019, smtp_board, 1)
		mcuclk_mhz = Register(0x001a, smtp_board, 1)
		a7_lastword = Register(0x0080, smtp_board, 1)
		a7_lastread = Register(0x0081, smtp_board, 1)
		a7_bytesseen = Register(0x0083, smtp_board, 1)
		a7_bytessent = Register(0x0084, smtp_board, 1)

		a7_bus_data_conf = Register(0x000d, smtp_board, 1)


		self.add_register("uzed", num_reg)
		self.add_register("uzed", beef_reg)
		self.add_register("uzed", dead_reg)
		self.add_register("uzed", a7_clk_reg)
		self.add_register("uzed", a7_cfg_program)
		self.add_register("uzed", a7_cfg)
		self.add_register("uzed", num_reg_2)
		self.add_register("uzed", uzed_uptime)
		self.add_register("uzed", count_reg)
		self.add_register("uzed", fw_yyyy)
		self.add_register("uzed", fw_mmdd)
		self.add_register("uzed", fw_hhmm)
		self.add_register("uzed", uztoa7)
		self.add_register("uzed", mcuclk_mhz)
		self.add_register("uzed", a7_lastword)
		self.add_register("uzed", a7_lastread)
		self.add_register("uzed", a7_bytesseen)
		self.add_register("uzed", a7_bytessent)
		self.add_register("uzed", a7_bus_data_conf)