import wx
from module.Module import Module

import GameData
import Utility

class InspirationPopper(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'Inspiration Popper Binds')

    def InitKeys(self):

        self.Data = {
            'InspEnabled'     : True,
            'RevInspEnabled'  : True,

            'AccuracyKey'     : "LSHIFT+A",
            'HealthKey'       : "LSHIFT+S",
            'DamageKey'       : "LSHIFT+D",
            'EnduranceKey'    : "LSHIFT+Q",
            'DefenseKey'      : "LSHIFT+W",
            'BreakFreeKey'    : "LSHIFT+E",
            'ResistDamageKey' : "LSHIFT+SPACE",

            'Feedback'        : True,
        }

        for Insp in sorted(GameData.Inspirations.keys()):
            self.Data[f"Rev{Insp}Key"]    = self.Data.get(f"Rev{Insp}Key"   , 'UNBOUND')
            self.Data[f"{Insp}Colors"]    = self.Data.get(f"{Insp}Colors"   , Utility.ColorDefault())
            self.Data[f"Rev{Insp}Colors"] = self.Data.get(f"Rev{Insp}Colors", Utility.ColorDefault())

    def MakeTopSizer(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        InspRows =    wx.FlexGridSizer(0,10,2,2)
        RevInspRows = wx.FlexGridSizer(0,10,2,2)

        for Insp in sorted(GameData.Inspirations.keys()):

            for order in ('', 'Rev'):

                RowSet = RevInspRows if order else InspRows

                RowSet.Add ( wx.StaticText(self, -1, f"{order} {Insp} Key"), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

                KeyPicker =  wx.Button(self, -1, self.Data[f"{order}{Insp}Key"])
                KeyPicker.SetToolTip( wx.ToolTip(f"Choose the key combo to activate a {Insp} inspiration") )
                RowSet.Add ( KeyPicker, 0, wx.EXPAND)

                RowSet.AddStretchSpacer(wx.EXPAND)

                ColorsCB = wx.CheckBox(self, -1, '')
                ColorsCB.SetToolTip( wx.ToolTip("Colorize Inspiration-Popper chat feedback") )
                RowSet.Add ( ColorsCB, 0, wx.ALIGN_CENTER_VERTICAL)

                RowSet.Add( wx.StaticText(self, -1, "Border"), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                bc = self.Data[f"{order}{Insp}Colors"]['border']
                RowSet.Add( wx.ColourPickerCtrl( self, -1, wx.Colour(bc['r'], bc['g'], bc['b']),))

                RowSet.Add( wx.StaticText(self, -1, "Background"), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                bc = self.Data[f"{order}{Insp}Colors"]['background']
                RowSet.Add( wx.ColourPickerCtrl( self, -1, wx.Colour(bc['r'], bc['g'], bc['b']),))

                RowSet.Add( wx.StaticText(self, -1, "Text"), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                bc = self.Data[f"{order}{Insp}Colors"]['foreground']
                RowSet.Add( wx.ColourPickerCtrl( self, -1, wx.Colour(bc['r'], bc['g'], bc['b']),))

        useCB = wx.CheckBox( self, -1, 'Enable Inspiration Popper Binds (Largest First)')
        useCB.SetValue( self.Data['InspEnabled'] )
        useCB.SetToolTip(wx.ToolTip('Check this to enable the Inspiration Popper Binds (largest used first)'))
        sizer.Add(useCB, 0, wx.ALL, 5)

        sizer.Add(InspRows, 0, wx.ALL, 10)

        useRevCB = wx.CheckBox( self, -1, 'Enable Reverse Inspiration Popper Binds (Smallest First)')
        useRevCB.SetValue( self.Data['RevInspEnabled'] )
        useRevCB.SetToolTip(wx.ToolTip('Check this to enable the Reverse Inspiration Popper Binds (smallest used first)'))
        sizer.Add(useRevCB, 0, wx.ALL, 5)

        sizer.Add(RevInspRows, 0, wx.ALL, 10)

        self.topSizer = sizer

    def PopulateBindFiles(self):
        profile = self.Profile

        ResetFile = profile.Data['ResetFile']

        for Insp in sorted(GameData.Inspirations.keys()):

            forwardOrder = '$$'.join(f"inspexecname {i}" for i in GameData.Inspirations[Insp])
            reverseOrder = '$$'.join(f"inspexecname {i}" for i in reversed(GameData.Inspirations[Insp]))

            if self.Data['Feedback']:
                forwardOrder = Utility.ChatColorOutput(self.Data[f"{Insp}Colors"])    + f"{Insp}$${forwardOrder}"
                reverseOrder = Utility.ChatColorOutput(self.Data[f"Rev{Insp}Colors"]) + f"{Insp}$${reverseOrder}"

            if self.Data['InspEnabled']:    self.Profile.Data['ResetFile'].SetBind(self.Data[f"{Insp}Key"],    forwardOrder)
            if self.Data['RevInspEnabled']: self.Profile.Data['ResetFile'].SetBind(self.Data[f"Rev{Insp}Key"], reverseOrder)

    def findconflicts(profile):

        if self.Data['enable']:
            cbCheckConflict(self.Data,'acckey',"Accuracy Key")
            cbCheckConflict(self.Data,'hpkey',"Healing Key")
            cbCheckConflict(self.Data,'damkey',"Damage Key")
            cbCheckConflict(self.Data,'endkey',"Endurance Key")
            cbCheckConflict(self.Data,'defkey',"Defense Key")
            cbCheckConflict(self.Data,'bfkey',"Breakfree Key")
            cbCheckConflict(self.Data,'reskey',"Resistance Key")

        if self.Data['reverse']:
            cbCheckConflict(self.Data,'racckey',"Reverse Accuracy Key")
            cbCheckConflict(self.Data,'rhpkey',"Reverse Healing Key")
            cbCheckConflict(self.Data,'rdamkey',"Reverse Damage Key")
            cbCheckConflict(self.Data,'rendkey',"Reverse Endurance Key")
            cbCheckConflict(self.Data,'rdefkey',"Reverse Defense Key")
            cbCheckConflict(self.Data,'rbfkey',"Reverse Breakfree Key")
            cbCheckConflict(self.Data,'rreskey',"Reverse Resistance Key")

    def bindisused(profile):
        return True if (self.Data['enable'] or self.Data['reverse']) else False

