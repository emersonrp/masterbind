import wx

class Module(wx.Dialog):
    def __init__(self, parent, name):
        wx.Dialog.__init__(self, parent, title=name)

        self.Name = name
        self.Profile = parent

        self.Data = {}
        self.ModuleEnabled = False

        self.ButtonTitle = name
        self.HelpWindow = None
        self.HelpText = '-* PLACEHOLDER HELP TEXT *-'

        self.InitKeys()
        self.MakeTopSizer()

        self.SetSizerAndFit(self.topSizer)
        self.CenterOnParent()

        self.MakeControls()
        parent.Modules.append(self)

    def help(self, evt):
        if self.HelpWindow == None:
            HelpWindow = wx.MiniFrame ( None, -1, self.Name + " Help",)
            BoxSizer   = wx.BoxSizer  ( wx.VERTICAL )
            Panel      = wx.Panel     ( HelpWindow )
            HelpText   = wx.StaticText( Panel, label = self.HelpText, size = [10,10] )

            BoxSizer.Add( Panel, 1, wx.EXPAND )

            HelpWindow.SetSizer(BoxSizer)

            self.HelpWindow = HelpWindow

        self.HelpWindow.Toggle()

    def MakeTopSizer(self):
        raise NotImplementedError(f"MakeTopSizer not implemented in {self.Name}")

    def InitKeys(self):
        raise NotImplementedError(f"InitKeys not implemented in {self.Name}")

    def PopulateBindFiles(self):
        raise NotImplementedError(f"PopulateBindFiles not implemented in {self.Name}")

    def HelpText(self):
        'Help not currently implemented here'

    ###  CONTROLS FOR MAIN WINDOW
    def MakeControls(self):
        self.enableCB = wx.CheckBox(self.Profile)
        self.confbtn  = wx.Button(self.Profile, label = self.ButtonTitle)

        self.enableCB.SetValue( self.ModuleEnabled )
        self.enableModule()

        self.enableCB.Bind(wx.EVT_CHECKBOX, self.enableModule)
        self.confbtn .Bind(wx.EVT_BUTTON,   self.doShow)

        self.Profile.moduleSizer.Add(self.enableCB, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL)
        self.Profile.moduleSizer.Add(self.confbtn,  1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)

    def enableModule(self, evt=None):
        enabled = self.enableCB.IsChecked()
        self.ModuleEnabled = enabled
        self.confbtn.Enable(enabled)

    def doShow(self, evt):
        self.Show(not self.IsShown())
