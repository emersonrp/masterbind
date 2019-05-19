import wx
from module.Module import Module

class FPSDisplay(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'FPS Display Binds')

    def InitKeys(self):
        self.Data = {
            'Enabled' : True,

            'Bindkey': "P",
        }

    def MakeTopSizer(self):

        sizer = wx.BoxSizer(wx.VERTICAL)

        minisizer = wx.FlexGridSizer(0,2,5,5)
        minisizer.Add( wx.StaticText(self, -1, 'Toggle FPS/Netgraph'), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        minisizer.Add( wx.Button    (self, -1, self.Data['Bindkey']))

        sizer.Add(minisizer, 1, wx.ALL, 10)

        self.topSizer = sizer


    def PopulateBindFiles(self):
        ResetFile = self.Profile.Data['ResetFile']
        ResetFile.SetBind(self.Data['Bindkey'],'++showfps$$++netgraph')

    def findconflicts(self):
        cbCheckConflict(self.Data,"Bindkey","FPS Display Toggle")

    def bindisused(self):
        return True if self.Data['Enable'] else False
