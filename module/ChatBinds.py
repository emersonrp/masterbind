import wx

from module.Module import Module

from UI.ControlGroup import ControlGroup
import UI.Labels

class ChatBinds(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'ChatBinds')


    def InitKeys(self):
        self.Typingnotifierlimit = { 'cmdlist' : ["Away From Keyboard","Emote"] }

        self.TabTitle = 'Chat Binds'

        self.Data = {
            'Enable'               : 1,
            'Message'              : "afk Typing Message",
            'StartChat'            : 'ENTER',
            'SlashChat'            : '/',
            'StartEmote'           : ';',
            'AutoReply'            : 'BACKSPACE',
            'TellTarget'           : 'COMMA',
            'QuickChat'            : "'",
            'TypingNotifierEnable' : 1,
            'TypingNotifier'       : '',
        }

    def FillTab(self):

        topSizer = wx.BoxSizer(wx.VERTICAL)

        enablecb = wx.CheckBox( self, -1, "Enable Chat Binds" )
        enablecb.SetToolTip('Check this to enable Custom Chat Binds')

        topSizer.Add( enablecb, 0, wx.ALL, 10 )

        sizer = ControlGroup(self, 'Chat Binds')

        for b in (
            ['StartChat',  'Choose the key combo that activates the Chat bar'],
            ['SlashChat',  'Choose the key combo that activates the Chat bar with a slash already typed'],
            ['StartEmote', 'Choose the key combo that activates the Chat bar with "/em" already typed'],
            ['AutoReply',  'Choose the key combo that AutoReplies to incoming tells'],
            ['TellTarget', 'Choose the key combo that starts a /tell to your current target'],
            ['QuickChat',  'Choose the key combo that activates QuickChat'],
        ):
            sizer.AddLabeledControl({
                'value'   : b[0],
                'type'    : 'keybutton',
                'parent'  : self,
                'tooltip' : b[1],
            })
        sizer.AddLabeledControl({
            'value'   : 'TypingNotifierEnable',
            'type'    : 'checkbox',
            'parent'  : self,
            'tooltip' : "Check this to enable the Typing Notifier",
        })
        sizer.AddLabeledControl({
            'value'   : 'TypingNotifier',
            'type'    : 'text',
            'parent'  : self,
            'tooltip' : "Choose the message to display when you are typing chat messages or commands",
        })

        topSizer.Add(sizer)
        self.SetSizer(topSizer)

    def PopulateBindfiles(self):
        ResetFile = self.Profile.General['ResetFile']

        Notifier = self.Data['TypingNotifier']
        if Notifier: Notifier = f"$${Notifier}"

        ResetFile.SetBind(self.Data['StartChat']  , f'show chat$$startchat{Notifier}')
        ResetFile.SetBind(self.Data['SlashChat']  , f'show chat$$slashchat{Notifier}')
        ResetFile.SetBind(self.Data['StartEmote'] , f'show chat$$em {Notifier}')
        ResetFile.SetBind(self.Data['AutoReply']  , f'autoreply{Notifier}')
        ResetFile.SetBind(self.Data['TellTarget'] , f'show chat$$beginchat /tell $target , {Notifier}')
        ResetFile.SetBind(self.Data['QuickChat']  , f'quickchat{Notifier}')

    def findconflicts(self):
        cbCheckConflict(self.Data, "StartChat", "Start Chat Key")
        cbCheckConflict(self.Data, "SlashChat", "Slashchat Key")
        cbCheckConflict(self.Data, "StartEmote","Emote Key")
        cbCheckConflict(self.Data, "AutoReply", "Autoreply Key")
        cbCheckConflict(self.Data, "TellTarget","Tell Target Key")
        cbCheckConflict(self.Data, "QuickChat", "Quickchat Key")

    def bindisused(self):
        return True if self.Data['enable'] else False

    UI.Labels.Add({
        'Enable'               : 'Enable Chat Binds',
        'Message'              : '"afk typing" message',
        'StartChat'            : 'Start Chat (no "/")',
        'SlashChat'            : 'Start Chat (with "/")',
        'StartEmote'           : 'Begin emote (types "/em")',
        'AutoReply'            : 'AutoReply to incoming /tell',
        'TellTarget'           : 'Send /tell to current target',
        'QuickChat'            : 'QuickChat',
        'TypingNotifierEnable' : 'Enable Typing Notifier',
        'TypingNotifier'       : 'Typing Notifier',
    })
