import wx
from module.BufferBinds import BufferBinds
#from module.ComplexBinds import ComplexBinds
#from module.CustomBinds import CustomBinds
#from module.FPSDisplay import FPSDisplay
from module.General import General
#from module.InspirationPopper import InspirationPopper
#from module.Mastermind import Mastermind
#from module.SimpleBinds import SimpleBinds
from module.SoD import SoD
from module.TeamPetSelect import TeamPetSelect
from module.ChatBinds import ChatBinds

class Profile(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)

        # TODO -- here's where we'd load a profile from a file or something.



        self.Modules   = []
        self.BindFiles = []

        # Add the individual tabs, in order.
        self.General           = General(self)
        self.SoD               = SoD(self)
        #self.FPSDisplay        = FPSDisplay(self)
        self.TeamPetSelect     = TeamPetSelect(self)
        # self.InspirationPopper = InspirationPopper(self)
        # self.MasterMind        = Mastermind(self)
        self.ChatBinds        = ChatBinds(self)
        # self.SimpleBinds       = SimpleBinds(self)
        self.BufferBinds       = BufferBinds(self)
        # self.ComplexBinds      = ComplexBinds(self)
        # self.CustomBinds       = CustomBinds(self)

    # TODO - hacking together the catfile() by hand here seems ugly.
    def GetBindFile(self, filename):
        pass
        #my $filename = File::Spec->catfile(@filename)
        #$self->{'BindFiles'}->{$filename} ||= BindFile(@filename)

    def WriteBindFiles(self, evt):
        for module in self.Modules:
            module.PopulateBindFiles()

        for bindfile in self.Bindfiles:
            bindfile.Write()

