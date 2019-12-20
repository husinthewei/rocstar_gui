import wx
import wx.lib.scrolledpanel as scrolled
import wx.grid
import sys
import time

import numpy
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

sys.path.insert(0, 'communication')
from RocstarBoard import RocstarBoard

class StatsPanel(wx.Panel):
    def __init__(self, parent, rocstar_board, register_group):
        self.parent = parent
        self.register_group = register_group
        self.rocstar_board = rocstar_board
        wx.Panel.__init__(self, parent)
        self.sizer = None
    
    # Add static text
    def AST(self, text, szr = None):
        statictext = wx.StaticText(self, label=text)
        if szr is None: szr = self.sizer
        szr.Add(statictext)
        return statictext
    
    # Add register Label
    def ARL(self, register, szr = None):
        statictext = wx.StaticText(self, label=register.rfmt())
        if szr is None: szr = self.sizer
        szr.Add(statictext)
        self.rocstar_board.set_register_label(
            self.register_group,
            register,
            statictext)
        self.Layout()
        return statictext

class LogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        log = wx.TextCtrl(
            self, -1,
            style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        self.log = log
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 10)
        self.SetSizer(sizer)

class RedirectText:
    # recipe for redirecting stderr from
    #   http://bytes.com/topic/python/answers/
    #     665106-wxpython-redirect-stdout-textctrl
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl
        self.t0 = time.time()
    def write(self, string):
        t = time.time()
        if t-self.t0>2.0:
            string = time.ctime()+"\n"+string
            self.t0 = t
        self.out.WriteText(string)

class BasicStatsPanel(StatsPanel):
    def __init__(self, parent, rocstar_board, register_group):
        StatsPanel.__init__(self, parent, rocstar_board, register_group)
        self.sizer = wx.FlexGridSizer(0, 2, 8, 8)
        ast = self.AST
        arl = self.ARL
        ast("Rocstar")
        ast("uzed")
        ast("Beef: ")
        arl(rocstar_board.beef_reg)
        ast("uzed Uptime:")
        arl(rocstar_board.uzed_uptime)
        self.SetSizer(self.sizer)

class ConfigStatsPanel(StatsPanel):
    def __init__(self, parent, rocstar_board, register_group):
        StatsPanel.__init__(self, parent, rocstar_board, register_group)
        self.sizer = wx.FlexGridSizer(0, 2, 8, 8)
        ast = self.AST
        arl = self.ARL
        ast("Rocstar")
        ast("uzed")
        self.SetSizer(self.sizer)

class GraphTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the third tab", (20,20))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)

class MainFrame(wx.Frame):
    def __init__(self, rocstar_board):
        wx.Frame.__init__(self, None, title="Rocstar", size=(700,700))
        self.rocstar_board = rocstar_board

        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)
        self.nb = nb

        # Register Groups
        self.register_groups = {}
        self.register_groups[0] = "BasicStats"
        self.register_groups[1] = "Config"

        register_groups = self.register_groups
        # Create the tab windows
        tab1 = BasicStatsPanel(nb, rocstar_board, register_groups[0])
        tab2 = ConfigStatsPanel(nb, rocstar_board, register_groups[1])
        tab3 = GraphTab(nb)
        tab4 = LogPanel(nb)
        tab5 = LogPanel(nb)

        self.logpanel1 = tab4
        self.logpanel2 = tab5

        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Basic stats")
        nb.AddPage(tab2, "Config")
        nb.AddPage(tab3, "Graph")
        nb.AddPage(tab4, "stdout")
        nb.AddPage(tab5, "stderr")

        rocstar_board.set_selected_reg_group("BasicStats")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(1000)

    def OnTimer(self, e):
        group = self.register_groups.get(self.nb.GetSelection(), "")
        self.rocstar_board.update(group)

if __name__ == "__main__":
    app = wx.App()
    rocstar_board = RocstarBoard("192.168.1.45", 2525)
    frame = MainFrame(rocstar_board)
    redir = RedirectText(frame.logpanel1.log)
    sys.stdout = redir
    redir = RedirectText(frame.logpanel2.log)
    sys.stderr = redir
    frame.Show()
    app.MainLoop()