import wx
from UI.Labels import Label, Labels
from Window.KeyBindDialog import KeyBindDialog

PADDING = 5

class ControlGroup(wx.StaticBoxSizer):

    def __init__(self, parent, name):
        wx.StaticBoxSizer.__init__(self, wx.VERTICAL, parent, name)

        self.InnerSizer = wx.FlexGridSizer(0,2,PADDING,PADDING)
        self.Add(self.InnerSizer, 0, wx.ALIGN_RIGHT, PADDING)

        self.parent = parent
        self.Name = name
        self.controls = {}


    def AddLabeledControl(self, p):

        sizer = self.InnerSizer

        type     = p.get('type', '')
        parent   = p.get('parent', '')
        module   = parent.Data
        value    = p.get('value', '')
        contents = p.get('contents', '')
        tooltip  = p.get('tooltip', '')
        callback = p.get('callback', '')

        text = wx.StaticText(parent, -1, Label(value) + ':')

        control = None
        if type == 'keybutton':
            control = wx.Button(parent, label = str(module[value]))
            control.Bind(wx.EVT_BUTTON, self.KeyPickerDialog, control)
        elif type == 'combo':
            control = wx.ComboBox(parent = parent, value = module[value], choices = contents, style = wx.CB_READONLY)
            if callback:
                control.Bind(wx.EVT_COMBOBOX, callback, control)
        elif type == 'text':
            control = wx.TextCtrl(parent, -1, module[value])
        elif type == 'checkbox':
            control = wx.CheckBox(parent, -1, Labels[value] or value)
            text.SetLabel('')
            control.SetValue(module[value])
        elif type == 'spinbox':
            control = wx.SpinCtrl(parent)
            control.SetValue(module[value])
            minval, maxval = contents
            control.SetRange(minval, maxval)
        elif type == 'dirpicker':
            control = wx.DirPickerCtrl(
                parent = parent, path = module[value], name = value,
                style = wx.DIRP_USE_TEXTCTRL|wx.ALL)
        else:
            print(f"wtf?!  I don't know how to make a {type} in ControlGroup.py")
            return

        if tooltip:
            control.SetToolTip(wx.ToolTip(tooltip))

        control.MasterBindLabel   = text.GetLabel()
        control.MasterBindValName = value

        sizer.Add( text,    0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add( control, 0, wx.ALL|wx.EXPAND)

        self.Layout()

        self.controls[value] = control

        return self

    def KeyPickerDialog(self, evt):
        button = evt.GetEventObject()

        with KeyBindDialog(self, button) as pickerdlg:

            if pickerdlg.ShowModal() == wx.OK:
                newKey = pickerdlg.kbfeed.GetLabel()
                value  = button.MasterBindValName

                # TODO -- check for conflicts
                # my $otherThingWithThatBind = checkConflicts($newKey)

                # update the associated profile var
                self.parent.Data[value] = newKey

                # re-label the button
                self.controls[value].SetLabel(newKey)
