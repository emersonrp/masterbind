import wx

from Window.KeyBindDialog import KeyBindDialog

class KeyPickerButton(wx.Button):
    def __init__(self, parent, label = ''):
        wx.Button.__init__(self, parent)

        self.Bind(wx.EVT_BUTTON, self.KeyPickerDialog)

        # explicitly set the label here so we go through the colour-picking logic
        self.SetLabel(label)


    def KeyPickerDialog(self, evt):
        button = evt.GetEventObject()

        with KeyBindDialog(self, button) as pickerdlg:

            if pickerdlg.ShowModal() == wx.OK:
                newKey = pickerdlg.kbkeys.GetLabel()
                value  = button.MasterBindValName

                # TODO -- check for conflicts
                # TODO -- actually do this inside keypicker dialog
                # my $otherThingWithThatBind = checkConflicts($newKey)

                # TODO TODO TODO update the associated profile var
                # self.parent.Data[value] = newKey

                # re-label the button
                self.SetLabel(newKey)


    def SetLabel(self, label):
        super(wx.Button, self).SetLabel(label)

        if label == 'UNBOUND':
            self.SetForegroundColour(wx.TheColourDatabase.Find('GREY'))
        else:
            self.SetForegroundColour(None)
