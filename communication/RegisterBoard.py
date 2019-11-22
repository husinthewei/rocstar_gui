from SmtpBoard import SmtpBoard
from Register import Register

import threading

class RegisterGroup:
    def __init__(self):
        # Map from register to WXGUI static text
        self.registers = {}

    def add_register(self, reg):
        self.registers[reg] = None

    def set_register_label(self, reg, label):
        self.registers[reg] = label

    def get_registers(self):
        return self.registers.keys()

    def update_gui(self):
        for reg, label in self.registers.items():
            if label:
                text = reg.rfmt() if reg.data else "??"  
                label.SetLabel(text)

class RegisterBoard:
    def __init__(self,
                 smtp_board,
                 name = "unnamed"):
        # Identifiers
        self.name = name
        self.smtp_board = smtp_board

        # Group registers for updating
        self.selected_group = ""

        # map from group name to register group object
        self.register_groups = {}

        # Timing logic
        self.uptime = 0

    def set_selected_reg_group(self, group):
        self.selected_group = group

    def add_register(self, group_name, reg):
        group = self.register_groups.get(group_name, RegisterGroup())
        group.add_register(reg)
        self.register_groups[group_name] = group

    def set_register_label(self, group_name, reg, static_text_label):
        group = self.register_groups.get(group_name, None)
        if group == None:
            return 
        group.set_register_label(reg, static_text_label)

    def update_values(self):
        group_name = self.selected_group
        group = self.register_groups.get(group_name, None)
        if group == None:
            return 
        for register in group.get_registers():
            register.update(self.uptime)

    def update_gui(self):
        group_name = self.selected_group
        group = self.register_groups.get(group_name, None)
        if group == None:
            return
        group.update_gui()

    def update(self, register_group):
        self.uptime += 1
        self.selected_group = register_group
        self.update_values()
        self.update_gui()