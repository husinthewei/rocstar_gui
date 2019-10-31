from SmtpBoard import SmtpBoard
from Register import Register

import threading

class RegisterBoard:
    def __init__(self,
                 smtp_board,
                 name = "unnamed"):
        # Identifiers
        self.name = name
        self.smtp_board = smtp_board

        # Group registers for updating
        self.selected_group = ""
        self.register_groups = {}

        # Timing logic
        self.uptime = 0
        self.timer = threading.Timer(1.0, self.OnTimer)
        self.timer.start()

    def set_selected_reg_group(self, group):
        self.selected_group = group

    def add_register(self, group_name, reg):
        group = self.register_groups.get(group_name, [])
        group.append(reg)
        self.register_groups[group_name] = group

    def update_values(self):
        group_name = self.selected_group
        group = self.register_groups.get(group_name, [])
        for register in group:
            register.update(self.uptime)

    def OnTimer(self):
        self.uptime += 1
        self.update_values()
        self.timer = threading.Timer(1.0, self.OnTimer)
        self.timer.start()