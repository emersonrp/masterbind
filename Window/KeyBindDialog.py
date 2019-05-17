import wx
import re
from UI.Labels import Label

class KeyBindDialog(wx.Dialog):
    def __init__(self, parent, button):
        wx.Dialog.__init__(self, None, title = "Select Key For Bind")

        self.parent  = parent
        self.keymap  = self.GetKeymap()
        self.buttons = [
                '', # 'button zero'
                'LBUTTON',
                'MBUTTON',
                'RBUTTON',
                'BUTTON4',
                'BUTTON5',
            ]

        # Create sizer that will host all controls
        sizer = wx.BoxSizer(wx.VERTICAL)

        btnlabel = button.MasterBindLabel

        self.kbdesc = wx.StaticText(self, label = f"Press the Key/Mouse Combo you'd like to use for '{Label(btnlabel)}'")
        self.kbkeys = wx.StaticText(self, label = button.GetLabel(),
                style = wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE|wx.BORDER_SIMPLE)

        buttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        cancel_btn = wx.Button(self, wx.CANCEL, label = "Cancel")
        clear_btn  = wx.Button(self, wx.NO,     label = "Clear Bind")
        accept_btn = wx.Button(self, wx.OK,     label = "Accept")

        buttonsizer.Add( cancel_btn, wx.EXPAND )
        buttonsizer.Add( clear_btn,  wx.EXPAND )
        buttonsizer.Add( accept_btn, wx.EXPAND )
        buttonsizer.Layout()

        sizer.Add( self.kbdesc, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 5 )
        sizer.Add( self.kbkeys, 1, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 5 )
        #sizer.AddSeparator()
        sizer.Add( buttonsizer, 1, wx.EXPAND|wx.ALL, 5 )

        # Wrap everything in a vbox to add some padding
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(sizer, 0, wx.ALL, 10)

        self.SetSizerAndFit(vbox)

        # Add some events etc.
        accept_btn.SetFocus()

        accept_btn.Bind(wx.EVT_BUTTON, self.doAccept)
        cancel_btn.Bind(wx.EVT_BUTTON, self.doCancel)
        clear_btn.Bind (wx.EVT_BUTTON, self.doClear)

        self.Bind(wx.EVT_CHAR_HOOK, self.handleBind)

        for e in (wx.EVT_LEFT_DOWN, wx.EVT_MIDDLE_DOWN, wx.EVT_RIGHT_DOWN, wx.EVT_MOUSE_AUX1_DOWN, wx.EVT_MOUSE_AUX2_DOWN):
            self.Bind       (e, self.handleBind)
            self.kbkeys.Bind(e, self.handleBind)
            self.kbdesc.Bind(e, self.handleBind)


    def doAccept(self, evt = None): self.EndModal(wx.OK)

    def doCancel(self, evt = None): self.EndModal(wx.CANCEL)

    def doClear(self, evt = None):
        self.kbkeys.Disable()
        self.kbkeys.SetLabel("DISABLED")

    def handleBind(self, evt):
        KeyToBind = ''
        binding = ''

        if (isinstance(evt, wx.KeyEvent)):
            code = evt.GetKeyCode()
            # press escape to cancel
            if (code == wx.WXK_ESCAPE):
                self.doCancel()
                return

            if code not in (wx.WXK_SHIFT, wx.WXK_CONTROL, wx.WXK_ALT, wx.WXK_WINDOWS_LEFT, wx.WXK_WINDOWS_RIGHT):
                KeyToBind = self.keymap.get(code, '')
                if not KeyToBind:
                    print(f"got unknown key code {code} which is {chr(code)}!!!")
            elif code == wx.WXK_CONTROL:
                if re.match(r'CTRL-', self.kbkeys.GetLabel())  : return
            elif code == wx.WXK_SHIFT:
                if re.match(r'SHIFT-', self.kbkeys.GetLabel()) : return
            elif code == wx.WXK_ALT:
                if re.match(r'ALT-', self.kbkeys.GetLabel())   : return
        else:
            KeyToBind = self.buttons[evt.GetButton()]
            evt.Skip()

        self.kbkeys.Enable()
        # check for each modifier key
        if (evt.ControlDown()): binding = binding + 'CTRL-'
        if (evt.AltDown())    : binding = binding + 'ALT-'
        if (evt.ShiftDown())  : binding = binding + 'SHIFT-'

        binding = binding + KeyToBind

        if binding:
            self.kbkeys.SetLabel(binding)
            self.kbkeys.Enable()

    # This keymap code was adapted from PADRE < http://padre.perlide.org/ >.
    def GetKeymap(self):
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
            ord('`')               : 'TILDE',
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

        return keymap

