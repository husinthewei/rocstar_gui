import wx
import wx.lib.scrolledpanel as scrolled
import wx.grid

import numpy
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

text = ""

# Define the tab content as classes:

# flex grid sizer?
class GridTab(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        grid = wx.grid.Grid(self)

        grid.CreateGrid(10, 5)
        grid.SetRowSize(0, 100)
        grid.SetColSize(0, 100)

        # set grid cell contents
        grid.SetCellValue(0, 0, 'some text here')

        self.Show()

class ScrollTab(scrolled.ScrolledPanel):
    def __init__(self, parent):

        scrolled.ScrolledPanel.__init__(self, parent, style=wx.VSCROLL)

        vbox = wx.BoxSizer(wx.HORIZONTAL)

        desc = wx.StaticText(self, -1, text)

        vbox.Add(desc, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(wx.StaticLine(self, -1, size=(1024, -1)), 0, wx.ALL, 5)
        vbox.Add((20, 20))

        self.SetSizer(vbox)
        self.SetupScrolling()

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
    def __init__(self):
        wx.Frame.__init__(self, None, title="testGUI", size=(700,700))

        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # Create the tab windows
        tab1 = GridTab(nb)
        tab2 = ScrollTab(nb)
        tab3 = GraphTab(nb)

        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Text")
        nb.AddPage(tab2, "Scroll")
        nb.AddPage(tab3, "Graph")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()