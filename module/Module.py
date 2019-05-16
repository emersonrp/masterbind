import wx

class Module(wx.Panel):
    def __init__(self, parent, name):
        wx.Panel.__init__(self, parent)

        self.Name = name
        self.Profile = parent

        self.Data = {}

        self.TabTitle = name
        self.HelpWindow = None
        self.HelpText = '-* PLACEHOLDER HELP TEXT *-'

        self.InitKeys()
        self.FillTab()

        parent.AddPage(self, self.TabTitle)

    def help(self, evt):

        if self.HelpWindow == None:
            HelpWindow = wx.MiniFrame ( None, -1, self.TabTitle + " Help",)
            BoxSizer   = wx.BoxSizer  ( wx.VERTICAL )
            Panel      = wx.Panel     ( HelpWindow, -1 )
            HelpText   = wx.StaticText( Panel, -1, self.HelpText, [10,10] )

            BoxSizer.Add( Panel, 1, wx.EXPAND )

            HelpWindow.SetSizer(BoxSizer)

            self.HelpWindow = HelpWindow

        self.HelpWindow.Toggle()


    def InitKeys(self):
        print("stub InitKeys called in " + self.Name)

    def PopulateBindFiles(self):
        print("stub PopBindFiles called in " + self.Name)

    def FillTab(self):
        self.TabTitle = self.Name

    def HelpText(self):
        'Help not currently implemented here'

