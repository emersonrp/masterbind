import wx
from UI.Labels import Label

class KeyBindDialog(wx.Dialog):
    def __init__(self, parent, button):
        wx.Dialog.__init__(self, None, title = "Select Key For Bind")

        self.parent = parent

        # Create sizer that will host all controls
        sizer = wx.BoxSizer(wx.VERTICAL)

        btnlabel = button.MasterBindLabel

        self.kbdesc = wx.StaticText(self, label = f"Press the Key Combo you'd like to use for {Label(btnlabel)}")
        self.cancel = wx.StaticText(self, label = "(Escape to cancel)" )
        self.kbfeed = wx.StaticText(self, label = button.GetLabel(), style = wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)

        sizer.Add( self.kbdesc, 0, wx.ALIGN_CENTER )
        sizer.Add( self.cancel, 0, wx.ALIGN_CENTER )
        sizer.Add( self.kbfeed, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)

        # Wrap everything in a vbox to add some padding
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(sizer, 0, wx.ALL, 10)

        self.Bind(wx.EVT_KEY_DOWN , self.handleBind , self)
        self.Bind(wx.EVT_CHAR     , self.handleBind , self)

        self.Bind(wx.EVT_LEFT_DOWN       , self.handleBind , self)
        self.Bind(wx.EVT_MIDDLE_DOWN     , self.handleBind , self)
        self.Bind(wx.EVT_RIGHT_DOWN      , self.handleBind , self)
        self.Bind(wx.EVT_MOUSE_AUX1_DOWN , self.handleBind , self)
        self.Bind(wx.EVT_MOUSE_AUX2_DOWN , self.handleBind , self)

        self.SetSizerAndFit(vbox)
        self.SetKeymap()

    # Private method to handle on character pressed event
    def handleBind(self, evt):
        evtType = evt.GetEventType()
        print("Got event at all")
        if (evtType == wx.EVT_KEY_DOWN):
            code = evt.GetKeyCode()
            # press escape to cancel
            print(f"Got a key code {code}")
            if (code == WXK_ESCAPE):
                self.EndModal(wx.CANCEL)

            KeyToBind = self.keymap[code]
        else:
            KeyToBind = [
                '', # 'button zero'
                'LBUTTON',
                'MBUTTON',
                'RBUTTON',
                'BUTTON4',
                'BUTTON5',
            ][evt.GetButton()]

        # check for each modifier key
        binding = ''
        if (evt.ControlDown()): binding = binding + 'CTRL-'
        if (evt.AltDown())    : binding = binding + 'ALT-'
        if (evt.ShiftDown())  : binding = binding + 'SHIFT-'

        binding = binding + KeyToBind
        self.kbfeed.SetLabel(binding)
        self.Layout()

        if (KeyToBind):
            # self->{'Handling'}++; # Don't take further input kthx
            # TODO - blink the selection like a menu selection, then return it.
            self.binding = binding
            self.EndModal(wx.OK)

        evt.Skip()

    # This keymap code was adapted from PADRE < http://padre.perlide.org/ >.
    def SetKeymap(self):
        # key choice list
        keymap = {
            wx.WXK_BACK            : 'BACKSPACE',
            wx.WXK_TAB             : 'TAB',
            wx.WXK_SPACE           : 'SPACE',
            wx.WXK_UP              : 'UP',
            wx.WXK_DOWN            : 'DOWN',
            wx.WXK_LEFT            : 'LEFT',
            wx.WXK_RIGHT           : 'RIGHT',
            wx.WXK_INSERT          : 'INSERT',
            wx.WXK_DELETE          : 'DELETE',
            wx.WXK_HOME            : 'HOME',
            wx.WXK_END             : 'END',
            wx.WXK_CAPITAL         : 'CAPITAL',
            wx.WXK_PAGEUP          : 'PAGEUP',
            wx.WXK_PAGEDOWN        : 'PAGEDOWN',
            wx.WXK_PRINT           : 'SYSRQ',
            wx.WXK_SCROLL          : 'SCROLL',
            wx.WXK_MENU            : 'APPS',
            wx.WXK_PAUSE           : 'PAUSE',
            wx.WXK_NUMPAD0         : 'NUMPAD0',
            wx.WXK_NUMPAD1         : 'NUMPAD1',
            wx.WXK_NUMPAD2         : 'NUMPAD2',
            wx.WXK_NUMPAD3         : 'NUMPAD3',
            wx.WXK_NUMPAD4         : 'NUMPAD4',
            wx.WXK_NUMPAD5         : 'NUMPAD5',
            wx.WXK_NUMPAD6         : 'NUMPAD6',
            wx.WXK_NUMPAD7         : 'NUMPAD7',
            wx.WXK_NUMPAD8         : 'NUMPAD8',
            wx.WXK_NUMPAD9         : 'NUMPAD9',
            wx.WXK_NUMPAD_MULTIPLY : 'MULTIPLY',
            wx.WXK_NUMPAD_ADD      : 'ADD',
            wx.WXK_NUMPAD_SUBTRACT : 'SUBTRACT',
            wx.WXK_NUMPAD_DECIMAL  : 'DECIMAL',
            wx.WXK_NUMPAD_DIVIDE   : 'DIVIDE',
            wx.WXK_NUMPAD_ENTER    : 'NUMPADENTER',
            wx.WXK_F1              : 'F1',
            wx.WXK_F2              : 'F2',
            wx.WXK_F3              : 'F3',
            wx.WXK_F4              : 'F4',
            wx.WXK_F5              : 'F5',
            wx.WXK_F6              : 'F6',
            wx.WXK_F7              : 'F7',
            wx.WXK_F8              : 'F8',
            wx.WXK_F9              : 'F9',
            wx.WXK_F10             : 'F10',
            wx.WXK_F11             : 'F11',
            wx.WXK_F12             : 'F12',
            wx.WXK_F13             : 'F13',
            wx.WXK_F14             : 'F14',
            wx.WXK_F15             : 'F15',
            wx.WXK_F16             : 'F16',
            wx.WXK_F17             : 'F17',
            wx.WXK_F18             : 'F18',
            wx.WXK_F19             : 'F19',
            wx.WXK_F20             : 'F20',
            wx.WXK_F21             : 'F21',
            wx.WXK_F22             : 'F22',
            wx.WXK_F23             : 'F23',
            wx.WXK_F24             : 'F24',
            ord('~')               : 'TILDE',
            ord('-')               : '-',
            ord('=')               : 'EQUALS',
            ord('[')               : '[',
            ord(']')               : ']',
            ord("\\")              : "\\",
            ord(';')               : ';',
            ord("'")               : "'",
            ord(',')               : 'COMMA',
            ord('.')               : '.',
            ord('/')               : '/',
        }

        # Add alphanumerics
        for alphanum in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
            keymap[ord(alphanum)] = alphanum

        self.keymap = keymap

