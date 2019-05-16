import wx
from module.Module import Module

class FPSDisplay(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'FPSDisplay')

    def InitKeys(self):
        if self.Data == None:
            self.Data = {
                Enable : 1,
                Bindkey: "P",
            }

    def FillTab(self):

        self.TabTitle = "FPS / Netgraph"

        sizer = wx.BoxSizer(wx.VERTICAL)

        useCB = wx.CheckBox( self, -1, 'Enable FPS Binds')

        useCB.SetToolTip(wx.ToolTip('Check this to enable the FPS and Netgraph Toggle Binds'))

        sizer.Add(useCB, 0, wx.ALL, 10)

        minisizer = wx.FlexGridSizer(0,2,5,5)
        minisizer.Add( wx.StaticText(self, -1, 'Toggle FPS/Netgraph'), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        minisizer.Add( wx.Button    (self, -1, self.Data['Bindkey']))

        sizer.Add(minisizer)

        self.SetSizerAndFit(sizer)


    def PopulateBindFiles(self):
        ResetFile = self.Profile.General.Data['ResetFile']
        ResetFile.SetBind(self.Data['Bindkey'],'++showfps$$++netgraph')

    def findconflicts(self):
        cbCheckConflict(self.Data,"Bindkey","FPS Display Toggle")

    def bindisused(self):
        return True if self.Data['Enable'] else False
