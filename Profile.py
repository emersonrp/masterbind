import wx
import winreg
from pathlib import Path

from BindFile import BindFile
from UI.ControlGroup import ControlGroup
import UI.Labels
import GameData



from module.BufferBinds import BufferBinds
from module.ComplexBinds import ComplexBinds
#from module.CustomBinds import CustomBinds  # no module file for this yet TODO make "importable / new" superclass
from module.FPSDisplay import FPSDisplay
from module.InspirationPopper import InspirationPopper
#from module.Mastermind import Mastermind
#from module.SimpleBinds import SimpleBinds
from module.SoD import SoD
from module.TeamPetSelect import TeamPetSelect
from module.ChatBinds import ChatBinds

class Profile(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # TODO -- here's where we'd load a profile from a file or something.

        self.Modules   = []
        self.BindFiles = {}
        self.BindKeys  = {}

        self.Data = {
            'Name'          : '',
            'Archetype'     : 'Scrapper',
            'Origin'        : "Magic",
            'Primary'       : 'Martial Arts',
            'Secondary'     : 'Super Reflexes',
            'Epic'          : 'Weapon Mastery',
            'BindsDir'      : "c:\\CoHTest\\",
            'ResetFile'     : self.GetBindFile('reset.txt'),
            'ResetKey'      : 'CTRL-R',
            'ResetFeedback' : 1,
            'Pool1'         : '',
            'Pool2'         : '',
            'Pool3'         : '',
            'Pool4'         : '',
        }
        # TODO - if (loaded profile doesn't have a BindsDir):
        try:
            tequila_reg =  winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                    'Software\Tequila\Settings', 0, winreg.KEY_QUERY_VALUE)
            cohdir, _ = winreg.QueryValueEx(tequila_reg,'CoHPath')
            self.Data['BindsDir'] = f"{cohdir}\\binds"
        except OSError as e:
            print("Couldn't open Tequila registry key, BindsDir not autopopulated.")
            print(e)
        finally:
            tequila_reg.Close()

        ArchData = GameData.Archetypes[self.Data['Archetype']]

        powersBox = ControlGroup(self, 'Powers and Info')

        powersBox.AddLabeledControl({
            'value' : 'Name',
            'type' : 'text',
            'parent' : self,
        })
        self.ArchPicker = powersBox.AddLabeledControl({
            'value' : 'Archetype',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(GameData.Archetypes.keys()),
            'tooltip' : '',
            'callback' : self.pickArchetype,
        })
        self.OriginPicker = powersBox.AddLabeledControl({
            'value' : 'Origin',
            'type' : 'combo',
            'parent' : self,
            'contents' : GameData.Origins,
            'tooltip' : '',
            'callback' : self.pickOrigin,
        })
        self.PrimaryPicker = powersBox.AddLabeledControl({
            'value' : 'Primary',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(ArchData['Primary'].keys()),
            'tooltip' : '',
            'callback' : self.pickPrimaryPowerSet,
        })
        self.SecondaryPicker = powersBox.AddLabeledControl({
            'value' : 'Secondary',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(ArchData['Secondary'].keys()),
            'tooltip' : '',
            'callback' : self.pickSecondaryPowerSet,
        })
        self.EpicPicker = powersBox.AddLabeledControl({
            'value' : 'Epic',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(ArchData['Epic'].keys()),
            'tooltip' : '',
            'callback' : self.pickEpicPowerSet,
        })
        self.Pool1Picker = powersBox.AddLabeledControl({
            'value' : 'Pool1',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(GameData.MiscPowers['Pool'].keys()),
            'tooltip' : '',
            'callback' : self.pickPoolPower,
        })
        self.Pool2Picker = powersBox.AddLabeledControl({
            'value' : 'Pool2',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(GameData.MiscPowers['Pool'].keys()),
            'tooltip' : '',
            'callback' : self.pickPoolPower,
        })
        self.Pool3Picker = powersBox.AddLabeledControl({
            'value' : 'Pool3',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(GameData.MiscPowers['Pool'].keys()),
            'tooltip' : '',
            'callback' : self.pickPoolPower,
        })
        self.Pool4Picker = powersBox.AddLabeledControl({
            'value' : 'Pool4',
            'type' : 'combo',
            'parent' : self,
            'contents' : sorted(GameData.MiscPowers['Pool'].keys()),
            'tooltip' : '',
            'callback' : self.pickPoolPower,
        })
        self.DirPicker = powersBox.AddLabeledControl({
            'value' : 'BindsDir',
            'type' : 'dirpicker',
            'parent' : self,
        })
        self.ResetKeyPicker = powersBox.AddLabeledControl({
            'value' : 'ResetKey',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'This key is used by certain modules to reset binds to a sane state.',
        })
        self.ResetFBCheckbox = powersBox.AddLabeledControl({
            'value' : 'ResetFeedback',
            'type' : 'checkbox',
            'parent' : self,
        })

        self.powersBox = powersBox

        self.moduleSizer = wx.FlexGridSizer(2, wx.Size(5,5))
        self.moduleSizer.AddGrowableCol(1)
        self.moduleSizer.Add( wx.StaticText(self, label = 'Enable'),    0, wx.ALIGN_CENTER )
        self.moduleSizer.Add( wx.StaticText(self, label = 'Configure'), 1, wx.ALIGN_CENTER )

        self.topSizer = wx.BoxSizer(wx.VERTICAL)
        self.topSizer.Add(self.powersBox, wx.EXPAND|wx.ALL, 5)
        self.topSizer.AddSpacer(10)
        self.topSizer.Add(self.moduleSizer, 0, wx.EXPAND)

        # Add the individual submodules, in order.
        self.SoD               = SoD(self)
        self.FPSDisplay        = FPSDisplay(self)
        self.TeamPetSelect     = TeamPetSelect(self)
        self.InspirationPopper = InspirationPopper(self)
        # self.MasterMind        = Mastermind(self)
        self.ChatBinds        = ChatBinds(self)
        # self.SimpleBinds       = SimpleBinds(self)
        self.BufferBinds       = BufferBinds(self)
        self.ComplexBinds      = ComplexBinds(self)
        # self.CustomBinds       = CustomBinds(self)

        self.SetSizerAndFit(self.topSizer)

    def pickArchetype(self, evt):
        self.Data['Archetype'] = evt.GetEventObject().GetValue()
        self.fillPickers()

    def pickOrigin(self, evt): self.fillPickers()

    def pickPoolPower(self, evt):
        print("PickPoolPower not implemented")

    def pickPrimaryPowerSet(self, evt):
        self.Data['Primary'] = evt.GetEventObject().GetValue()
        self.fillPickers()

    def pickSecondaryPowerSet(self, evt):
        self.Data['Secondary'] = evt.GetEventObject().GetValue()
        self.fillPickers()

    def pickEpicPowerSet(self, evt):
        self.Data['Epic'] = evt.GetEventObject().GetValue()
        self.fillPickers()

    def fillPickers(self):

        g = self.Data

        ArchData = GameData.Archetypes[g['Archetype']]
        self.ArchetypePicker.SetStringSelection(g['Archetype'])

        self.OriginPicker.SetStringSelection(g['Origin'])

        self.PrimaryPicker.Clear()
        self.PrimaryPicker.Append(sorted(ArchData['Primary'].keys()))
        self.PrimaryPicker.SetStringSelection(g['Primary']) or self.PrimaryPicker.SetSelection(1)

        self.SecondaryPicker.Clear()
        self.SecondaryPicker.Append(sorted(ArchData['Secondary'].keys()))
        self.SecondaryPicker.SetStringSelection(g['Secondary']) or self.SecondaryPicker.SetSelection(1)

        self.EpicPicker.Clear()
        self.EpicPicker.Append(sorted(ArchData['Epic'].keys()))
        self.EpicPicker.SetStringSelection(g['Epic']) or self.EpicPicker.SetSelection(1)

        self.Pool1Picker.Clear()
        self.Pool1Picker.Append(sorted(GameData.MiscPowers['Pool']))
        self.Pool1Picker.SetStringSelection(g['Pool1']) or self.Pool1Picker.SetSelection(1)

        self.Pool2Picker.Clear()
        self.Pool2Picker.Append(sorted(GameData.MiscPowers['Pool']))
        self.Pool2Picker.SetStringSelection(g['Pool2']) or self.Pool2Picker.SetSelection(1)

        self.Pool3Picker.Clear()
        self.Pool3Picker.Append(sorted(GameData.MiscPowers['Pool']))
        self.Pool3Picker.SetStringSelection(g['Pool3']) or self.Pool3Picker.SetSelection(1)

        self.Pool4Picker.Clear()
        self.Pool4Picker.Append(sorted(GameData.MiscPowers['Pool']))
        self.Pool4Picker.SetStringSelection(g['Pool4']) or self.Pool4Picker.SetSelection(1)


    UI.Labels.Add({
        'Name' : 'Name',
        'Archetype' : 'Archetype',
        'Origin' : 'Origin',
        'Primary' : 'Primary Powers',
        'Secondary' : 'Secondary Powers',
        'Epic' : 'Epic/Patron Powers',
        'Pool1' : 'Power Pool 1',
        'Pool2' : 'Power Pool 2',
        'Pool3' : 'Power Pool 3',
        'Pool4' : 'Power Pool 4',
        'BindsDir' : 'Binds Directory',
        'ResetKey' : 'Reset Key',
        'ResetFeedback' : 'Give Feedback on Reset',
    })

    # TODO - hacking together the catfile() by hand here seems ugly.
    def GetBindFile(self, *args):
        filename = str(Path(*args))

        # TODO - check / etc actual filename
        #my $filename = File::Spec->catfile(@filename)
        if not self.BindFiles.get(filename, ''):
            print(f"No bindfile for name {filename}, creating...")

            import re
            if re.match(r'$$', filename):
                print("WTF IS THIS {filename}")
                raise Error
            self.BindFiles[filename] = BindFile(self, filename)

        return self.BindFiles[filename]

    def WriteBindFiles(self, evt):
        for module in self.Modules:
            module.PopulateBindFiles()

        for bindfile in self.BindFiles:
            self.BindFiles[bindfile].Write()

