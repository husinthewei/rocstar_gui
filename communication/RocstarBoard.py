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
        self.uzed_uptime = Register(0x0008, smtp_board, 1, format_method=Register.format_time)
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

        self.add_register("BasicStats", self.num_reg)
        self.add_register("BasicStats", self.beef_reg)
        self.add_register("BasicStats", self.dead_reg)
        self.add_register("BasicStats", self.a7_clk_reg)
        self.add_register("BasicStats", self.a7_cfg_program)
        self.add_register("BasicStats", self.a7_cfg)
        self.add_register("BasicStats", self.num_reg_2)
        self.add_register("BasicStats", self.uzed_uptime)
        self.add_register("BasicStats", self.count_reg)
        self.add_register("BasicStats", self.fw_yyyy)
        self.add_register("BasicStats", self.fw_mmdd)
        self.add_register("BasicStats", self.fw_hhmm)
        self.add_register("BasicStats", self.uztoa7)
        self.add_register("BasicStats", self.mcuclk_mhz)
        self.add_register("BasicStats", self.a7_lastword)
        self.add_register("BasicStats", self.a7_lastread)
        self.add_register("BasicStats", self.a7_bytesseen)
        self.add_register("BasicStats", self.a7_bytessent)
        self.add_register("BasicStats", self.a7_bus_data_conf)


        # config registers
        self.s6_zero_reg = Register(0x0000, smtp_board, 30, s6 = True)
        self.s6_beef_reg = Register(0x0001, smtp_board, 30, s6 = True)
        self.s6_uptime_reg = Register(0x0002, smtp_board, 1, s6 = True)
        self.gen_rw_reg = Register(0x0003, smtp_board, 1, s6 = True)
        self.s6_status_word = Register(0x0004, smtp_board, 5, s6 = True)
        self.s6_eb_error_count_ff = Register(0x0005, smtp_board, 5, s6 = True)
        self.s6_global_config_reg = Register(0x0006, smtp_board, 5, s6 = True)
        self.ad9633_pdwn_reg = Register(0x0007, smtp_board, 5, s6 = True)
        self.ad9222_pdwn_reg = Register(0x000A, smtp_board, 5, s6 = True)
        self.trig_pdwn_reg = Register(0x000B, smtp_board, 5, s6 = True)
        self.drs4_pdwn_reg = Register(0x000C, smtp_board, 5, s6 = True)
        self.drs4_denable_reg = Register(0x000D, smtp_board, 5, s6 = True)
        self.misc_config_reg = Register(0x000F, smtp_board, 5, s6 = True)
        
        self.add_register("Config", self.s6_zero_reg)
        self.add_register("Config", self.s6_beef_reg)
        self.add_register("Config", self.s6_uptime_reg)
        self.add_register("Config", self.gen_rw_reg)
        self.add_register("Config", self.s6_status_word)
        self.add_register("Config", self.s6_eb_error_count_ff)
        self.add_register("Config", self.s6_global_config_reg)
        self.add_register("Config", self.ad9633_pdwn_reg)
        self.add_register("Config", self.ad9222_pdwn_reg)
        self.add_register("Config", self.trig_pdwn_reg)
        self.add_register("Config", self.drs4_pdwn_reg)
        self.add_register("Config", self.drs4_denable_reg)
        self.add_register("Config", self.misc_config_reg)