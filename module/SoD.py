import wx
import re
from module.Module import Module

# TODO - would be nice to scoot this out into BindFile
from pathlib import Path

import GameData
import UI.Labels
from UI.ControlGroup import ControlGroup
from BindFile import BindFile

class SoD(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'Speed On Demand Binds')

    def InitKeys(self):
        self.Data = {
            'Up'            : "SPACE",
            'Down'          : "X",
            'Forward'       : "W",
            'Back'          : "S",
            'Left'          : "A",
            'Right'         : "D",
            'TurnLeft'      : "Q",
            'TurnRight'     : "E",
            'AutoRun'       : "R",
            'Follow'        : "TILDE",
            'DefaultMode'   : '',
            'MousechordSoD' : 1,
            'AutoMouseLook' : 0,

            'SprintPower' : 'Sprint',

            'ChangeCamdist' : 1,
            'CamdistBase' : 15,
            'CamdistTravelling' : 60,

            'ChangeDetail' : 1,
            'DetailBase' : 100,
            'DetailTravelling' : 50,

            'NonSoD' : 1,
            'NonSoDMode' : 1,
            'Sprint' : 1,
            'SprintMode' : 1,
            'ToggleSoD' : 'CTRL-M',

            'JumpMode' : "T",
            'SimpleSJCJ' : 1,
            'JumpCJ' : 1,
            'JumpSJ' : 1,

            'RunMode' : "C",
            'SSOnlyWhenMoving' : 0,
            'SSSJModeEnable' : 1,

            'FlyMode' : "F",
            'GFlyMode' : "G",

            'SelfTellOnChange' : 1,

            'TPEnable' : 1,
            'TPMode' : 'SHIFT-LBUTTON',
            'TPCombo' : 'SHIFT',
            'TPReset' : 'CTRL-T',

            'TTPEnable' : 1,
            'TTPMode' : 'SHIFT-CTRL-LBUTTON',
            'TTPCombo' : 'SHIFT-CTRL',
            'TTPReset' : 'SHIFT-CTRL-T',

            'AutoHoverTP' : 1,
            'HideWinsDuringTP' : 1,
            'AutoGFlyTTP' : 1,

            'RunPrimary' : "Super Speed",
            'RunPrimaryNumber' : 1,
            'RunSecondary' : "Sprint",
            'RunSecondaryNumber' : 1,
            'FlyHover' : 1,
            'FlyFly' : '',
            'FlyGFly' : '',
            'Unqueue' : 1,
            'ToggleSoD' : "CTRL+M",
            'Enable' : None,

            'NovaMode' : 'T',
            'NovaTray' : 4,

            'DwarfMode' : 'G',
            'DwarfTray' : 5,

            'Temp'           : 1,
            'TempTray'       : '6',
            'TempTrayToggle' : "UNBOUND",
            'TempMode'       : "UNBOUND",
        }

        self.ModuleEnabled = True

        if self.Profile.Data['Archetype'] == "Peacebringer":
            self.Data['NovaNova'] = "Bright Nova"
            self.Data['DwarfDwarf'] = "White Dwarf"
            self.Data['HumanFormShield'] = self.Data.get('HumanFormShield', "Shining Shield")

        elif self.Profile.Data['Archetype'] == "Warshade":
            self.Data['NovaNova'] = "Dark Nova"
            self.Data['DwarfDwarf'] = "Black Dwarf"
            self.Data['HumanFormShield'] = self.Data.get('HumanFormShield', "Gravity Shield")

        self.Data['HumanMode']       = self.Data.get('HumanMode'       , "UNBOUND")
        self.Data['HumanTray']       = self.Data.get('HumanTray'       , "1")
        self.Data['HumanHumanPBind'] = self.Data.get('HumanHumanPBind' , "nop")
        self.Data['HumanNovaPBind']  = self.Data.get('HumanNovaPBind'  , "nop")
        self.Data['HumanDwarfPBind'] = self.Data.get('HumanDwarfPBind' , "nop")

    def MakeTopSizer(self):

        topSizer = wx.FlexGridSizer(0,2,10,10)

        leftColumn = wx.BoxSizer(wx.VERTICAL)
        rightColumn = wx.BoxSizer(wx.VERTICAL)

        ##### MOVEMENT KEYS
        movementSizer = ControlGroup(self, 'Movement Keys')

        for cmd in ("Up","Down","Forward","Back","Left","Right","TurnLeft","TurnRight"):
            movementSizer.AddLabeledControl({
                'value' : cmd,
                'type' : 'keybutton',
                'parent' : self,
            })

        # TODO!  fill this picker with only the appropriate bits.
        movementSizer.AddLabeledControl({
            'value' : 'DefaultMode',
            'type' : 'combo',
            'contents' : ['No SoD', 'Sprint', 'Super Speed', 'Jump', 'Fly'],
            'parent' : self,
        })
        movementSizer.AddLabeledControl({
            'value' : 'MousechordSoD',
            'type' : 'checkbox',
            'parent' : self,
        })
        leftColumn.Add(movementSizer, 0, wx.EXPAND)


        ##### GENERAL SETTINGS
        generalSizer = ControlGroup(self, 'General Settings')

        generalSizer.AddLabeledControl({
            'value' : 'AutoMouseLook',
            'type' : 'checkbox',
            'tooltip' : 'Automatically Mouselook when moving',
            'parent' : self,
        })
        # TODO add SprintPowers to GameData
        #generalSizer.AddLabeledControl({
        #    'value' : 'SprintPower',
        #    'type' : 'combo',
        #    'contents' : GameData.SprintPowers,
        #    'parent' : self,
        #})

        # TODO -- decide what to do with this.
        # generalSizer.Add( wx.CheckBox(self, SPRINT_UNQUEUE, "Exec powexecunqueue"))

        generalSizer.AddLabeledControl({
            'value' : 'AutoRun',
            'type' : 'keybutton',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'Follow',
            'type' : 'keybutton',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'NonSoD',
            'type'  : 'checkbox',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'NonSoDMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'ToggleSoD',
            'type' : 'keybutton',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'Sprint',
            'type' : 'checkbox',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'ChangeCamdist',
            'type' : 'checkbox',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'CamdistBase',
            'type' : 'spinbox',
            'contents' : [1, 100],
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'CamdistTravelling',
            'type' : 'spinbox',
            'contents' : [1, 100],
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'ChangeDetail',
            'type' : 'checkbox',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'DetailBase',
            'type' : 'spinbox',
            'contents' : [1, 100],
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'DetailTravelling',
            'type' : 'spinbox',
            'contents' : [1, 100],
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'HideWinsDuringTP',
            'type' : 'checkbox',
            'parent' : self,
        })
        generalSizer.AddLabeledControl({
            'value' : 'SelfTellOnChange',
            'type' : 'checkbox',
            'parent' : self,
        })
        leftColumn.Add(generalSizer, 0, wx.EXPAND)


        ##### SUPER SPEED
        superSpeedSizer = ControlGroup(self, 'Super Speed')
        superSpeedSizer.AddLabeledControl({
            'value' : 'RunMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        superSpeedSizer.AddLabeledControl({
            'value' : 'SSOnlyWhenMoving',
            'type' : 'checkbox',
            'parent' : self,
        })
        superSpeedSizer.AddLabeledControl({
            'value' : 'SSSJModeEnable',
            'type' : 'checkbox',
            'parent' : self,
        })
        rightColumn.Add(superSpeedSizer, 0, wx.EXPAND)

        ##### SUPER JUMP
        superJumpSizer = ControlGroup(self, 'Super Jump')
        superJumpSizer.AddLabeledControl({
            'value' : 'JumpCJ',
            'type' : 'checkbox',
            'parent' : self,
        })
        superJumpSizer.AddLabeledControl({
            'value' : 'JumpSJ',
            'type' : 'checkbox',
            'parent' : self,
        })
        superJumpSizer.AddLabeledControl({
            'value' : 'JumpMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        superJumpSizer.AddLabeledControl({
            'value' : 'SimpleSJCJ',
            'type' : 'checkbox',
            'parent' : self,
        })
        rightColumn.Add(superJumpSizer, 0, wx.EXPAND)


        ##### FLY
        flySizer = ControlGroup(self, 'Flight')

        flySizer.AddLabeledControl({
            'value' : 'FlyMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        flySizer.AddLabeledControl({
            'value' : 'GFlyMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        rightColumn.Add(flySizer, 0, wx.EXPAND)

        ##### TELEPORT
        teleportSizer = ControlGroup(self, 'Teleport')

        # if (at == peacebringer) "Dwarf Step"
        # if (at == warshade) "Shadow Step / Dwarf Step"

        teleportSizer.AddLabeledControl({
            'value' : "TPMode",
            'type' : 'keybutton',
            'parent' : self,
        })
        teleportSizer.AddLabeledControl({
            'value' : "TPCombo",
            'type' : 'keybutton',
            'parent' : self,
        })
        teleportSizer.AddLabeledControl({
            'value' : "TPReset",
            'type' : 'keybutton',
            'parent' : self,
        })

        # if (player has hover):
        teleportSizer.AddLabeledControl({
            'value' : 'AutoHoverTP',
            'type' : 'checkbox',
            'parent' : self,
        })
        #

        ##### TEAM TELEPORT
        # if (player has team-tp):

        teamteleportSizer = ControlGroup(self, 'Team Teleport')

        teamteleportSizer.AddLabeledControl({
            'value' : "TTPMode",
            'type' : 'keybutton',
            'parent' : self,
        })
        teamteleportSizer.AddLabeledControl({
            'value' : "TTPCombo",
            'type' : 'keybutton',
            'parent' : self,
        })
        teamteleportSizer.AddLabeledControl({
            'value' : "TTPReset",
            'type' : 'keybutton',
            'parent' : self,
        })

            # if (player has group fly):
        teamteleportSizer.AddLabeledControl({
            'value' : 'AutoGFlyTTP',
            'type' : 'checkbox',
            'parent' : self,
        })
            #
        #
        rightColumn.Add(teleportSizer,     0, wx.EXPAND)
        rightColumn.Add(teamteleportSizer, 0, wx.EXPAND)

        ##### TEMP TRAVEL POWERS
        tempSizer = ControlGroup(self, 'Temp Travel Powers')
        # if (temp travel powers exist)?  Should this be "custom"?
        tempSizer.AddLabeledControl({
            'value' : 'Temp',
            'type' : 'checkbox',
            'parent' : self,
        })
        tempSizer.AddLabeledControl({
            'value' : 'TempMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        tempSizer.AddLabeledControl({
            'value' : 'TempTray',
            'type' : 'spinbox',
            'contents' : [1, 8],
            'parent' : self,
        })
        tempSizer.AddLabeledControl({
            'value' : 'TempTrayToggle',
            'type' : 'keybutton',
            'parent' : self,
        })
        rightColumn.Add(tempSizer, 0, wx.EXPAND)

        ##### KHELDIAN TRAVEL POWERS
        kheldianSizer = ControlGroup(self, 'Nova / Dwarf Travel Powers')

        kheldianSizer.AddLabeledControl({
            'value' : 'NovaMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        kheldianSizer.AddLabeledControl({
            'value' : 'NovaTray',
            'type' : 'spinbox',
            'contents' : [1, 8],
            'parent' : self,
        })
        kheldianSizer.AddLabeledControl({
            'value' : 'DwarfMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        kheldianSizer.AddLabeledControl({
            'value' : 'DwarfTray',
            'type' : 'spinbox',
            'contents' : [1, 8],
            'parent' : self,
        })

        # do we want a key to change directly to human form, instead of toggles?
        kheldianSizer.AddLabeledControl({
            'value' : 'HumanMode',
            'type' : 'keybutton',
            'parent' : self,
        })
        kheldianSizer.AddLabeledControl({
            'value' : 'HumanTray',
            'type' : 'spinbox',
            'contents' : [1, 8],
            'parent' : self,
        })

        rightColumn.Add(kheldianSizer, 0, wx.EXPAND)

        topSizer.Add(leftColumn)
        topSizer.Add(rightColumn)

        self.topSizer = topSizer

    def makeSoDFile(self, p):
        t = p['t']

        bl   = t.bl(p['bl'])   if p.get('bl', '')   else ''
        bla  = t.bl(p['bla'])  if p.get('bla', '')  else ''
        blf  = t.bl(p['blf'])  if p.get('blf', '')  else ''
        blbo = t.bl(p['blbo']) if p.get('blbo', '') else ''
        blsd = t.bl(p['blsd']) if p.get('blsd', '') else ''

        path   = t.path(p['path'])   if p.get('path', '')   else ''
        pathr  = t.path(p['pathr'])  if p.get('pathr', '')  else ''
        pathf  = t.path(p['pathf'])  if p.get('pathf', '')  else ''
        pathbo = t.path(p['pathbo']) if p.get('pathbo', '') else ''
        pathsd = t.path(p['pathsd']) if p.get('pathsd', '') else ''

        mobile     = p.get('mobile', '')
        stationary = p.get('stationary', '')
        modestr    = p.get('modestr', '')
        flight     = p.get('flight', '')
        fix        = p.get('fix', '')
        turnoff    = p.get('turnoff', '')
        sssj       = p.get('sssj', '')

        # this wants to be $turnoff ||= mobile, stationary once we know what those are.  arrays?  hashes?
        turnoff = turnoff or [mobile, stationary]

        if self.Data['DefaultMode'] == modestr and t['totalkeys'] == 0:

            curfile = self.Profile.Data['ResetFile']
            self.sodDefaultResetKey(mobile, stationary)

            self.sodUpKey     (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
            self.sodDownKey   (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
            self.sodForwardKey(t, bl, curfile, mobile, stationary, flight,'','','', sssj)
            self.sodBackKey   (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
            self.sodLeftKey   (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
            self.sodRightKey  (t, bl, curfile, mobile, stationary, flight,'','','', sssj)

            if (modestr == "NonSoD"): self.makeNonSoDModeKey(t,"r",  curfile, [mobile, stationary])
            if (modestr == "Sprint")  : self.makeSprintModeKey  (t,"r",  curfile, turnoff, fix)
            if (modestr == "Fly")   : self.makeFlyModeKey   (t,"bo", curfile, turnoff, fix)
            if (modestr == "GFly")  : self.makeGFlyModeKey  (t,"gf", curfile, turnoff, fix)
            if (modestr == "Run")   : self.makeSpeedModeKey (t,"s",  curfile, turnoff, fix)
            if (modestr == "Jump")  : self.makeJumpModeKey  (t,"j",  curfile, turnoff, path)
            if (modestr == "Temp")  : self.makeTempModeKey  (t,"r",  curfile, turnoff, path)
            #if (modestr == "QFly")  : self.makeQFlyModeKey  (t,"r",  curfile, turnoff, modestr)

            self.sodAutoRunKey(t, bla, curfile, mobile, sssj)

            self.sodFollowKey(t, blf, curfile, mobile)


        if (flight == "Fly") and pathbo:
            #  blast off
            curfile = self.Profile.GetBindFile(pathbo)
            self.sodResetKey(curfile, path, self.actPower_toggle(None, stationary, mobile), '')

            self.sodUpKey     (t, blbo, curfile, mobile, stationary, flight, '', '', "bo", sssj)
            self.sodDownKey   (t, blbo, curfile, mobile, stationary, flight, '', '', "bo", sssj)
            self.sodForwardKey(t, blbo, curfile, mobile, stationary, flight, '', '', "bo", sssj)
            self.sodBackKey   (t, blbo, curfile, mobile, stationary, flight, '', '', "bo", sssj)
            self.sodLeftKey   (t, blbo, curfile, mobile, stationary, flight, '', '', "bo", sssj)
            self.sodRightKey  (t, blbo, curfile, mobile, stationary, flight, '', '', "bo", sssj)

            # if (modestr == "Sprint"): self.makeSprintModeKey(t, "r", curfile, turnoff, fix)
            t['ini'] = '-down$$'

            if self.Data['DefaultMode'] == "Fly":
                if self.Data['NonSoD'] : t['FlyMode'] = t['NonSoDMode']
                if self.Data['Sprint'] : t['FlyMode'] = t['SprintMode']
                if t['canss']          : t['FlyMode'] = t['RunMode']
                if t['canjmp']         : t['FlyMode'] = t['JumpMode']
                if self.Data['Temp']   : t['FlyMode'] = t['TempMode']
            self.makeFlyModeKey(t, "a", curfile, turnoff, fix)

            t['ini'] = ''
            # if modestr == "GFly" : self.makeGFlyModeKey  (t, "gbo", curfile, turnoff, fix)
            # if modestr == "Run"  : self.makeSpeedModeKey (t, "s",   curfile, turnoff, fix)
            # if modestr == "Jump" : self.makeJumpModeKey  (t, "j",   curfile, turnoff, path)

            self.sodAutoRunKey(t, bla, curfile, mobile, sssj)

            self.sodFollowKey(t, blf, curfile, mobile)

            # curfile = self.Profile.GetBindFile(pathsd)

            self.sodResetKey(curfile, path,self.actPower_toggle(None, stationary, mobile),'')

            self.sodUpKey     (t, blsd, curfile, mobile, stationary, flight,'','',"sd", sssj)
            self.sodDownKey   (t, blsd, curfile, mobile, stationary, flight,'','',"sd", sssj)
            self.sodForwardKey(t, blsd, curfile, mobile, stationary, flight,'','',"sd", sssj)
            self.sodBackKey   (t, blsd, curfile, mobile, stationary, flight,'','',"sd", sssj)
            self.sodLeftKey   (t, blsd, curfile, mobile, stationary, flight,'','',"sd", sssj)
            self.sodRightKey  (t, blsd, curfile, mobile, stationary, flight,'','',"sd", sssj)

            t['ini'] = '-down$$'
            # if (modestr == "Sprint") : self.makeSprintModeKey(t, "r",   curfile, turnoff, fix)
            # if (modestr == "Fly")  : self.makeFlyModeKey (t, "a",   curfile, turnoff, fix)
            # if (modestr == "GFly") : self.makeGFlyModeKey(t, "gbo", curfile, turnoff, fix)
            t['ini'] = ''
            # if (modestr == "Jump") : self.makeJumpModeKey(t,"j", curfile, turnoff, path)

            self.sodAutoRunKey(t, bla, curfile, mobile, sssj)
            self.sodFollowKey(t, blf, curfile, mobile)

        curfile = self.Profile.GetBindFile(path)

        self.sodResetKey(curfile, path,self.actPower_toggle(None, stationary, mobile),'')

        self.sodUpKey     (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
        self.sodDownKey   (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
        self.sodForwardKey(t, bl, curfile, mobile, stationary, flight,'','','', sssj)
        self.sodBackKey   (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
        self.sodLeftKey   (t, bl, curfile, mobile, stationary, flight,'','','', sssj)
        self.sodRightKey  (t, bl, curfile, mobile, stationary, flight,'','','', sssj)

        if (flight == "Fly") and pathbo:
            #  Base to set down
            if (modestr == "NonSoD") : self.makeNonSoDModeKey(t,"r", curfile, [mobile, stationary], sodSetDownFix)
            if (modestr == "Sprint")   : self.makeSprintModeKey  (t,"r", curfile, turnoff, sodSetDownFix)
            # if (t['SprintMode']):
                # curfile.SetBind(t['SprintMode'],"+down$$down 1" + self.actPower_name(1, mobile) + t['detailhi'] + t['runcamdist'] + t['blsd'])
            #
            if (modestr == "Run")     : self.makeSpeedModeKey (t,"s",  curfile, turnoff, sodSetDownFix)
            if (modestr == "Fly")     : self.makeFlyModeKey   (t,"bo", curfile, turnoff, fix)
            if (modestr == "Jump")    : self.makeJumpModeKey  (t,"j",  curfile, turnoff, path)
            if (modestr == "Temp")    : self.makeTempModeKey  (t,"r",  curfile, turnoff, path)
            #if (modestr == "QFly")    : self.makeQFlyModeKey  (t,"r",  curfile, turnoff, modestr)
        else:
            if (modestr == "NonSoD")  : self.makeNonSoDModeKey(t,"r",  curfile, [mobile, stationary])
            if (modestr == "Sprint")    : self.makeSprintModeKey  (t,"r",  curfile, turnoff, fix)
            if (flight == "Jump"):
                if (modestr == "Fly") : self.makeFlyModeKey   (t,"a",  curfile, turnoff, fix,None,1)
            else:
                if (modestr == "Fly") : self.makeFlyModeKey   (t,"bo", curfile, turnoff, fix)
            if (modestr == "Run")     : self.makeSpeedModeKey (t,"s",  curfile, turnoff, fix)
            if (modestr == "Jump")    : self.makeJumpModeKey  (t,"j",  curfile, turnoff, path)
            if (modestr == "Temp")    : self.makeTempModeKey  (t,"r",  curfile, turnoff, path)
            #if (modestr == "QFly")    : self.makeQFlyModeKey  (t,"r",  curfile, turnoff, modestr)

        self.sodAutoRunKey(t, bla, curfile, mobile, sssj)

        self.sodFollowKey(t, blf, curfile, mobile)

        # AutoRun Binds
        curfile = self.Profile.GetBindFile(pathr)

        self.sodResetKey(curfile, path,self.actPower_toggle(None, stationary, mobile),'')

        self.sodUpKey     (t, bla, curfile, mobile, stationary, flight,1,'','', sssj)
        self.sodDownKey   (t, bla, curfile, mobile, stationary, flight,1,'','', sssj)
        self.sodForwardKey(t, bla, curfile, mobile, stationary, flight, bl, '','', sssj)
        self.sodBackKey   (t, bla, curfile, mobile, stationary, flight, bl, '','', sssj)
        self.sodLeftKey   (t, bla, curfile, mobile, stationary, flight,1,'','', sssj)
        self.sodRightKey  (t, bla, curfile, mobile, stationary, flight,1,'','', sssj)

        if (flight == "Fly") and pathbo:
            if modestr == "NonSoD" : self.makeNonSoDModeKey(t,"ar", curfile, [mobile, stationary], sodSetDownFix)
            if modestr == "Sprint"   : self.makeSprintModeKey  (t,"gr", curfile, turnoff, sodSetDownFix)
            if modestr == "Run"    : self.makeSpeedModeKey (t,"as", curfile, turnoff, sodSetDownFix)
        else:
            if modestr == "NonSoD" : self.makeNonSoDModeKey(t,"ar", curfile, [mobile, stationary])
            if modestr == "Sprint"   : self.makeSprintModeKey  (t,"gr", curfile, turnoff, fix)
            if modestr == "Run"    : self.makeSpeedModeKey (t,"as", curfile, turnoff, fix)

        if modestr == "Fly"        : self.makeFlyModeKey   (t,"af", curfile, turnoff, fix)
        if modestr == "Jump"       : self.makeJumpModeKey  (t,"aj", curfile, turnoff, pathr)
        if modestr == "Temp"       : self.makeTempModeKey  (t,"ar", curfile, turnoff, path)
        #if modestr == "QFly"       : self.makeQFlyModeKey  (t,"ar", curfile, turnoff, modestr)

        self.sodAutoRunOffKey(t, bl, curfile, mobile, stationary, flight)

        curfile.SetBind(self.Data['Follow'],'nop')

        # FollowRun Binds
        curfile = self.Profile.GetBindFile(pathf)

        self.sodResetKey(curfile, path, self.actPower_toggle(None, stationary, mobile),'')

        self.sodUpKey     (t, blf, curfile, mobile, stationary, flight,'', bl,'', sssj)
        self.sodDownKey   (t, blf, curfile, mobile, stationary, flight,'', bl,'', sssj)
        self.sodForwardKey(t, blf, curfile, mobile, stationary, flight,'', bl,'', sssj)
        self.sodBackKey   (t, blf, curfile, mobile, stationary, flight,'', bl,'', sssj)
        self.sodLeftKey   (t, blf, curfile, mobile, stationary, flight,'', bl,'', sssj)
        self.sodRightKey  (t, blf, curfile, mobile, stationary, flight,'', bl,'', sssj)

        if (flight == "Fly") and pathbo:
            if modestr == "NonSoD" : self.makeNonSoDModeKey   (t,"fr", curfile, [mobile, stationary], sodSetDownFix)
            if modestr == "Sprint"   : self.makeSprintModeKey     (t,"fr", curfile, turnoff, sodSetDownFix)
            if modestr == "Run"    : self.makeSpeedModeKey    (t,"fs", curfile, turnoff, sodSetDownFix)
        else:
            if modestr == "NonSoD" : self.makeNonSoDModeKey   (t,"fr", curfile, [mobile, stationary])
            if modestr == "Sprint"   : self.makeSprintModeKey     (t,"fr", curfile, turnoff, fix)
            if modestr == "Run"    : self.makeSpeedModeKey    (t,"fs", curfile, turnoff, fix)

        if modestr == "Fly"        : self.makeFlyModeKey   (t,"ff", curfile, turnoff, fix)
        if modestr == "Jump"       : self.makeJumpModeKey  (t,"fj", curfile, turnoff, pathf)
        if modestr == "Temp"       : self.makeTempModeKey  (t,"fr", curfile, turnoff, path)
        #if modestr == "QFly"       : self.makeQFlyModeKey  (t,"fr", curfile, turnoff, modestr)

        curfile.SetBind(self.Data['AutoRun'],'nop')

        self.sodFollowOffKey(t, bl, curfile, mobile, stationary, flight)

    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeNonSoDModeKey(self, t, bl, cur, toff, fix = None, fb = None):
        p = self.Profile
        key = t['NonSoDMode']
        if (not key) or key == 'UNBOUND' : return

        feedback = ''
        if self.Data['SelfTellOnChange']:
            feedback = fb or '$$t $name, Non-SoD Mode'

        if bl == "r":
            bindload = t.bl('n')
            if fix:
                fix(p, t, key, self.makeNonSoDModeKey,"n", bl, cur, toff,'', feedback)
            else:
                cur.SetBind(key, t['ini'] + self.actPower_toggle(None, None, toff) + t.dirs('UDFBLR') + t['detailhi'] + t['runcamdist'] + feedback + bindload)

        elif bl == "ar":
            bindload = t.bl('an')
            if fix:
                fix(p, t, key, self.makeNonSoDModeKey,"n", bl, cur, toff,"a", feedback)
            else:
                cur.SetBind(key, t['ini'] + self.actPower_toggle(None, None, toff) + t['detailhi'] + t['runcamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload)

        else:
            if fix:
                fix(p, t, key, self.makeNonSoDModeKey,"n", bl, cur, toff,"f", feedback)
            else:
                cur.SetBind(key, t['ini'] + self.actPower_toggle(None, None, toff) + t['detailhi'] + t['runcamdist'] + '$$up 0' + feedback + t.bl('fn'))
        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeTempModeKey(self, t, bl, cur, toff, path):
        # TODO path unused?
        p = self.Profile
        key = t['TempMode']
        if (not key) or key == "UNBOUND": return

        feedback = '$$t $name, Temp Mode' if self.Data['SelfTellOnChange'] else ''
        trayslot = "1 " + self.Data['TempTray']

        if bl == "r":
            bindload = t.bl('t')
            cur.SetBind(key, t['ini'] + actPower(None,1, trayslot, toff) + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)
        elif bl == "ar":
            bindload  = t.bl('at')
            bindload2 = t.bl('at','_t')
            tgl = p.GetBindFile(bindload2)
            cur.SetBind(key, t['in']  + actPower(None,1, trayslot, toff) + t['detaillo'] + t['flycamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload2)
            tgl.SetBind(key, t['in']  + actPower(None,1, trayslot, toff) + t['detaillo'] + t['flycamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload)
        else:
            cur.SetBind(key, t['ini'] + actPower(None,1, trayslot, toff) + t['detaillo'] + t['flycamdist'] + '$$up 0' + feedback + t.bl('ft'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeQFlyModeKey(self, t, bl, cur, toff, modestr):
        p = self.Profile
        key = t['QFlyMode']
        if (not key) or key == "UNBOUND": return

        if modestr == "NonSoD":
            cur.SetBind(key, "powexecname Quantum Flight")
            return

        feedback = '$$t $name, QFlight Mode' if self.Data['SelfTellOnChange'] else ''

        if bl == "r":
            bindload  = t.bl('n')
            bindload2 = t.bl('n','_q')
            tgl = p.GetBindFile(bindload2)

            tray = '$$gototray 1' if (modestr == 'Nova' or modestr == 'Dwarf') else ''

            cur.SetBind(key, t['ini'] + actPower(None,1,'Quantum Flight', toff) + tray + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload2)
            tgl.SetBind(key, t['ini'] + actPower(None,1,'Quantum Flight', toff) + tray + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

        elif bl == "ar":
            bindload  = t.bl('an')
            bindload2 = t.bl('an','_t')
            tgl = p.GetBindFile(bindload2)
            cur.SetBind(key, t['in'] + actPower(None,1,'Quantum Flight', toff) + t['detaillo'] + t['flycamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload2)
            tgl.SetBind(key, t['in'] + actPower(None,1,'Quantum Flight', toff) + t['detaillo'] + t['flycamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload)
        else:
            cur.SetBind(key, t['ini'] + actPower(None,1,'Quantum Flight', toff) + t['detaillo'] + t['flycamdist'] + '$$up 0' + feedback + t.bl('fn'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeSprintModeKey(self, t, bl, cur, toff, modestr):
        p = self.Profile
        key = t['SprintMode']
        if (not key) or key == "UNBOUND": return

        feedback = (fb or '$$t $name, Sprint-SoD Mode') if self.Data['SelfTellOnChange'] else ''

        if bl == "r":
            bindload  = t.bl()

            ton = self.actPower_toggle(1, (t['sprint'] if t['horizkeys'] else ''), toff)

            if fix:
                fix(p, t, key, self.makeSprintModeKey,"r", bl, cur, toff, '', feedback)
            else:
                cur.SetBind(key, t['ini'] + ton + t.dirs('UDFBLR') + t['detailhi'] + t['runcamdist'] + feedback + bindload) 

        elif bl == "ar":
            bindload  = t.bl('gr')

            if fix:
                fix(p, t, key, self.makeSprintModeKey,"r", bl, cur, toff,"a", feedback)
            else:
                cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['sprint'], toff) + t['detailhi'] +  t['runcamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload)

        else:
            if fix:
                fix(p, t, key, self.makeSprintModeKey,"r", bl, cur, toff,"f", feedback)
            else:
                cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['sprint'], toff) + t['detailhi'] + t['runcamdist'] + '$$up 0' + fb + t.bl('fr'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeSpeedModeKey(self, t, bl, cur, toff, fix = None, fb = None):
        p = self.Profile
        key = t['RunMode']
        feedback = (fb or '$$t $name, Superspeed Mode') if self.Data['SelfTellOnChange'] else ''

        if t['canss']:
            if bl == 's':
                bindload = t.bl('s')
                if fix:
                    fix(p, t, key, self.makeSpeedModeKey,"s", bl, cur, toff,'', feedback)
                else:
                    cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['speed'], toff) + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            elif bl == "as":
                bindload = t.bl('as')
                if fix:
                    fix(p, t, key, self.makeSpeedModeKey,"s", bl, cur, toff,"a", feedback)
                elif not feedback:
                    cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['speed'], toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)
                else:
                    bindload  = t.bl('as')
                    bindload2 = t.bl('as','_s')
                    tgl = p.GetBindFile(bindload2)
                    cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['speed'], toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload2)
                    tgl.SetBind(key, t['ini'] + self.actPower_toggle(1, t['speed'], toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            else:
                if fix:
                    fix(p, t, key, self.makeSpeedModeKey,"s", bl, cur, toff,"f", feedback)
                else:
                    cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['speed'], toff) + '$$up 0' +  t['detaillo'] + t['flycamdist'] + feedback + t.bl('fs'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeJumpModeKey(self, t, bl, cur, toff, fbl):
        p = self.Profile
        key = t['JumpMode']
        if (t['canjmp'] and not self.Data['SimpleSJCJ']):

            feedback = '$$t $name, Superjump Mode' if self.Data['SelfTellOnChange'] else ''
            tgl = p.GetBindFile(fbl)

            if bl == "j":
                if (t['horizkeys'] + t['space'] > 0):
                    a = actPower(None,1, t['jump'], toff) + '$$up 1'
                else:
                    a = actPower(None,1, t['cjmp'], toff)

                bindload = t.bl('j')
                tgl.SetBind(key, '-down' + a + t['detaillo'] + t['flycamdist'] + bindload)
                cur.SetBind(key, '+down' + feedback + p.GetBindFile(fbl).BLF())
            elif bl == "aj":
                bindload = t.bl('aj')
                tgl.SetBind(key, '-down' + actPower(None,1, t['jump'], toff) + '$$up 1' + t['detaillo'] + t['flycamdist'] + t.dirs('DLR') + bindload)
                cur.SetBind(key, '+down' + feedback + p.GetBindFile(fbl).BLF())
            else:
                tgl.SetBind(key, '-down' + actPower(None,1, t['jump'], toff) + '$$up 1' + t['detaillo'] + t['flycamdist'] + t.bl('fj'))
                cur.SetBind(key, '+down' + feedback + p.GetBindFile(fbl).BLF())

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeFlyModeKey(self, t, bl, cur, toff, fix, fb = None, fb_on_a = None):
        p = self.Profile
        key = t['FlyMode']
        if (not key) or key == "UNBOUND": return

        feedback = (fb or '$$t $name, Flight Mode') if self.Data['SelfTellOnChange'] else ''

        if t['canhov'] + t['canfly'] > 0:
            if bl == "bo":
                bindload = t.bl('bo')
                if fix:
                    fix(p, t, key, self.makeFlyModeKey,"f", bl, cur, toff,'', feedback)
                else:
                    cur.SetBind(key,'+down$$' + self.actPower_toggle(1, t['flyx'], toff) + '$$up 1$$down 0' + t.dirs('FBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            elif bl == "a":
                if (not fb_on_a): feedback = ''

                bindload = t.bl('a')
                ton = t['flyx'] if t['tkeys'] else t['hover']
                if fix:
                    fix(p, t, key, self.makeFlyModeKey,"f", bl, cur, toff,'', feedback)
                else:
                    cur.SetBind(t['FlyMode'], t['ini'] + self.actPower_toggle(1, ton , toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            elif bl == "af":
                bindload = t.bl('af')
                if fix:
                    fix(p, t, key, self.makeFlyModeKey,"f", bl, cur, toff,"a", feedback)
                else:
                    cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['flyx'], toff) + t['detaillo'] + t['flycamdist'] + t.dirs('DLR') + feedback + bindload)

            else:
                if fix:
                    fix(p, t, key, self.makeFlyModeKey,"f", bl, cur, toff,"f", feedback)
                else:
                    cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['flyx'], toff) + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + t.bl('ff'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeGFlyModeKey (self, t, bl, cur, toff, fix):
        p = self.Profile
        key = t['GFlyMode']

        if t['cangfly'] > 0:
            if bl == "gbo":
                bindload = t.bl('gbo')
                if fix:
                    fix(p, t, key, self.makeGFlyModeKey,"gf", bl, cur, toff,'','')
                else:
                    cur.SetBind(key, t['ini'] + '$$up 1$$down 0' + self.actPower_toggle(None, t['gfly'], toff) + t.dirs('FBLR') + t['detaillo'] + t['flycamdist'] .bindload)

            elif bl == "gaf":
                bindload = t.bl('gaf')
                if fix:
                    fix(p, t, key, self.makeGFlyModeKey,"gf", bl, cur, toff,"a")
                else:
                    cur.SetBind(key, t['ini'] + t['detaillo'] + t['flycamdist'] + t.dirs('UDLR') + bindload)

            else:
                if fix:
                    fix(p, t, key, self.makeGFlyModeKey,"gf", bl, cur, toff,"f")
                else:
                    if bl == "gf":
                        cur.SetBind(key, t['ini'] + self.actPower_toggle(1, t['gfly'], toff) + t['detaillo'] + t['flycamdist'] + t.bl('gff'))
                    else:
                        cur.SetBind(key, t['ini'] + t['detaillo'] + t['flycamdist'] + t.bl('gff'))
        t['ini'] = ''


    def iupMessage(self):
            print("ZOMG SOMEBODY IMPLEMENT A WARNING DIALOG!!!\n")

    def PopulateBindFiles(self):

        ResetFile = self.Profile.Data['ResetFile']

        # $ResetFile.SetBind(petselect['sel5'] + ' "petselect 5')
        if (self.Data['DefaultMode'] == "NonSoD"):
            if (not self.Data['NonSoD']): iupMessage("Notice","Enabling NonSoD mode, since it is set as your default mode.")
            self.Data['NonSoD'] = 1

        if (self.Data['DefaultMode'] == "Sprint" and not self.Data['Sprint']):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Sprint SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['DefaultMode'] = "NonSoD"

        if (self.Data['DefaultMode'] == "Fly" and not (self.Data['FlyHover'] or self.Data['FlyFly'])):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Flight SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['DefaultMode'] = "NonSoD"

        if (self.Data['DefaultMode'] == "Jump" and not (self.Data['JumpCJ'] or self.Data['JumpSJ'])):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Superjump SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['DefaultMode'] = "NonSoD"

        if (self.Data['DefaultMode'] == "Run" and self.Data['RunPrimaryNumber'] == 1):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Superspeed SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['DefaultMode'] = "NonSoD" 

        t = SoD_Table({
            'profile'    : self.Profile,
            'sprint'     : '',
            'speed'      : '',
            'hover'      : '',
            'fly'        : '',
            'flyx'       : '',
            'jump'       : '',
            'cjmp'       : '',
            'canhov'     : 0,
            'canfly'     : 0,
            'canqfly'    : 0,
            'cangfly'    : 0,
            'cancj'      : 0,
            'canjmp'     : 0,
            'canss'      : 0,
            'tphover'    : '',
            'ttpgrpfly'  : '',
            'on'         : '$$powexectoggleon ',
            # 'on'       : '$$powexecname ',
            'off'        : '$$powexectoggleoff ',
            'mlon'       : '',
            'mloff'      : '',
            'runcamdist' : '',
            'flycamdist' : '',
            'detailhi'   : '',
            'detaillo'   : '',

            'NonSoDMode' : 0,

            'ini' : '',
        })

        if (self.Data['JumpCJ'] and not self.Data['JumpSJ']):
            t['cancj'] = 1
            t['cjmp'] = "Combat Jumping"
            t['jump'] = "Combat Jumping"

        if (not self.Data['JumpCJ'] and self.Data['JumpSJ']):
            t['canjmp'] = 1
            t['jump'] = "Super Jump"
            t['jumpifnocj'] = "Super Jump"

        if (self.Data['JumpCJ'] and self.Data['JumpSJ']):
            t['cancj'] = 1
            t['canjmp'] = 1
            t['cjmp'] = "Combat Jumping"
            t['jump'] = "Super Jump" 

        if (self.Profile.Data['Archetype'] == "Peacebringer"):
            if (self.Data['FlyHover']):
                t['canhov'] = 1
                t['canfly'] = 1
                t['hover'] = "Combat Flight"
                t['fly'] = "Energy Flight"
                t['flyx'] = "Energy Flight"
            else:
                t['canfly'] = 1
                t['hover'] = "Energy Flight"
                t['flyx'] = "Energy Flight"

        elif (not (self.Profile.Data['Archetype'] == "Warshade")):
            if (self.Data['FlyHover'] and not self.Data['FlyFly']):
                t['canhov'] = 1
                t['hover'] = "Hover"
                t['flyx'] = "Hover"
                if (self.Data['AutoHoverTP']): t['tphover'] = '$$powexectoggleon Hover'

            if (not self.Data['FlyHover'] and self.Data['FlyFly']):
                t['canfly'] = 1
                t['hover'] = "Fly"
                t['flyx'] = "Fly"

            if (self.Data['FlyHover'] and self.Data['FlyFly']):
                t['canhov'] = 1
                t['canfly'] = 1
                t['hover'] = "Hover"
                t['fly'] = "Fly"
                t['flyx'] = "Fly"
                if (self.Data['AutoHoverTP']): t['tphover'] = '$$powexectoggleon Hover' 

        #if ((self.Profile.Data['Archetype'] == "Peacebringer") and self.Data['FlyQFly']):
            #t['canqfly'] = 1

        if (self.Data['FlyGFly']):
            t['cangfly'] = 1
            t['gfly'] = "Group Fly"
            if (self.Data['TTPTPGFly']): t['ttpgfly'] = '$$powexectoggleon Group Fly'

        t['sprint'] = self.Data['RunSecondary']
        if (self.Data['RunPrimaryNumber'] == 1):
            t['speed']  = self.Data['RunSecondary']
        else:
            t['speed']  = self.Data['RunPrimary']
            t['canss'] = 1

        t['unqueue'] = '$$powexecunqueue' if self.Data['Unqueue'] else ''
        if (self.Data['AutoMouseLook']):
            t['mlon']  = '$$mouselook 1'
            t['mloff'] = '$$mouselook 0'

        #if (self.Data['RunUseCamdist']):
        #    t['runcamdist'] = '$$camdist ' + self.Data['RunCamdist']

        #if (self.Data['FlyUseCamdist']):
        #    t['flycamdist'] = '$$camdist ' + self.Data['FlyCamdist']

        if self.Data['ChangeCamdist']:
            t['runcamdist'] = t['flycamdist'] = '$$camdist ' + str(self.Data['CamdistTravelling'])

        if self.Data['ChangeDetail']:
            t['detailhi'] = '$$visscale ' + str(self.Data['DetailBase'])       + '$$shadowvol 0$$ss 0'
            t['detaillo'] = '$$visscale ' + str(self.Data['DetailTravelling']) + '$$shadowvol 0$$ss 0'

        windowhide = windowshow = ''
        if self.Data['HideWinsDuringTP']:
            windowhide = '$$windowhide health$$windowhide chat$$windowhide target$$windowhide tray'
            windowshow = '$$show health$$show chat$$show target$$show tray'

        # turn = "+zoomin$$-zoomin"  # a non functioning bind used only to activate the keydown/keyup functions of +commands
        t['turn'] = "+down";  # a non functioning bind used only to activate the keydown/keyup functions of +commands

        #  temporarily set self.Data['DefaultMode'] to "NonSoD"
        # self.Data['DefaultMode'] = "Base"
        #  set up the keys to be used.
        t['NonSoDMode'] = self.Data['NonSoDMode'] if (self.Data['DefaultMode'] == "NonSoD") else None
        t['SprintMode'] = self.Data['SprintMode'] if (self.Data['DefaultMode'] == "Sprint") else None
        t['FlyMode']    = self.Data['FlyMode']    if (self.Data['DefaultMode'] == "Fly")    else None
        t['JumpMode']   = self.Data['JumpMode']   if (self.Data['DefaultMode'] == "Jump")   else None
        t['RunMode']    = self.Data['RunMode']    if (self.Data['DefaultMode'] == "Run")    else None
     #   t['GFlyMode']  = self.Data['GFlyMode']    if (self.Data['DefaultMode'] == "GFly")   else None
        t['TempMode']   = self.Data['TempMode']
        #t['QFlyMode']  = self.Data['QFlyMode']

        for space in (0,1):
            t['space'] = space
            t['up']    = f'$$up {space}'
            t['upx']   = f'$$up {(1-space)}'

            for X in (0,1):
                t['X']    = X
                t['dow']  = f'$$down {X}'
                t['dowx'] = f'$$down {(1-X)}'

                for W in (0,1):
                    t['W']    = W
                    t['forw'] = f'$$forward {W}'
                    t['forx'] = f'$$forward {(1-W)}'

                    for S in (0,1):
                        t['S']    = S
                        t['bac']  = f'$$backward {S}'
                        t['bacx'] = f'$$backward {(1-S)}'

                        for A in (0,1):
                            t['A']    = A
                            t['lef']  = f'$$left {A}'
                            t['lefx'] = f'$$left {(1-A)}'

                            for D in (0,1):
                                t['D']    = D
                                t['rig']  = f'$$right {D}'
                                t['rigx'] = f'$$right {(1-D)}'

                                t['totalkeys'] = space+X+W+S+A+D;  # total number of keys down
                                t['horizkeys'] = W+S+A+D;          # total # of horizontal move keys.  So Sprint isn't turned on when jumping
                                t['vertkeys'] = space+X
                                t['jkeys'] = t['horizkeys']+t['space']

                                if self.Data['NonSoD'] or t['canqfly']:
                                    t[self.Data['DefaultMode'] + "Mode"] = t['NonSoDMode']
                                    self.makeSoDFile({
                                        't'          : t,
                                        'bl'         : 'n',
                                        'bla'        : 'an',
                                        'blf'        : 'fn',
                                        'path'       : 'n',
                                        'pathr'      : 'an',
                                        'pathf'      : 'fn',
                                        'mobile'     : '',
                                        'stationary' : '',
                                        'modestr'    : "NonSoD",
                                    })
                                    t[self.Data['DefaultMode'] + "Mode"] = None

                                if self.Data['Sprint']:
                                    t[self.Data['DefaultMode'] + "Mode"] = t['SprintMode']
                                    self.makeSoDFile({
                                        't'          : t,
                                        'bl'         : 'r',
                                        'bla'        : 'gr',
                                        'blf'        : 'fr',
                                        'path'       : 'r',
                                        'pathr'      : 'ar',
                                        'pathf'      : 'fr',
                                        'mobile'     : t['sprint'],
                                        'stationary' : '',
                                        'modestr'    : "Sprint",
                                    })
                                    t[self.Data['DefaultMode'] + "Mode"] = None

                                if t['canss']:
                                    t[self.Data['DefaultMode'] + "Mode"] = t['RunMode']
                                    if self.Data['SSSJModeEnable']:
                                        sssj = t['jump']
                                    if self.Data['SSOnlyWhenMoving']:
                                        self.makeSoDFile({
                                            't'          : t,
                                            'bl'         : 's',
                                            'bla'        : 'as',
                                            'blf'        : 'fs',
                                            'path'       : 's',
                                            'pathr'      : 'as',
                                            'pathf'      : 'fs',
                                            'mobile'     : t['speed'],
                                            'stationary' : '',
                                            'modestr'    : "Run",
                                            'sssj'       : sssj,
                                        })
                                    else:
                                        self.makeSoDFile({
                                            't'          : t,
                                            'bl'         : 's',
                                            'bla'        : 'as',
                                            'blf'        : 'fs',
                                            'path'       : 's',
                                            'pathr'      : 'as',
                                            'pathf'      : 'fs',
                                            'mobile'     : t['speed'],
                                            'stationary' : t['speed'],
                                            'modestr'    : "Run",
                                            'sssj'       : sssj,
                                        })

                                    t[self.Data['DefaultMode'] + "Mode"] = None

                                if (t['canjmp'] > 0) and (not self.Data['SimpleSJCJ']):
                                    t[self.Data['DefaultMode'] + "Mode"] = t['JumpMode']
                                    if (t['jump'] == t['cjmp']):
                                        jturnoff = t['jumpifnocj']
                                    self.makeSoDFile({
                                        't'          : t,
                                        'bl'         : 'j',
                                        'bla'        : 'aj',
                                        'blf'        : 'fj',
                                        'path'       : 'j',
                                        'pathr'      : 'aj',
                                        'pathf'      : 'fj',
                                        'mobile'     : t['jump'],
                                        'stationary' : t['cjmp'],
                                        'modestr'    : "Jump",
                                        'flight'     : "Jump",
                                        'fix'        : sodJumpFix,
                                        'turnoff'    : jturnoff,
                                    })
                                    t[self.Data['DefaultMode'] + "Mode"] = None

                                if (t['canhov'] + t['canfly'] > 0):
                                    t[self.Data['DefaultMode'] + "Mode"] = t['FlyMode']
                                    self.makeSoDFile({
                                        't'          : t,
                                        'bl'         : 'r',
                                        'bla'        : 'af',
                                        'blf'        : 'ff',
                                        'path'       : 'r',
                                        'pathr'      : 'af',
                                        'pathf'      : 'ff',
                                        'mobile'     : t['flyx'],
                                        'stationary' : t['hover'],
                                        'modestr'    : "Fly",
                                        'flight'     : "Fly",
                                        'pathbo'     : 'bo',
                                        'pathsd'     : 'sd',
                                        'blbo'       : 'bo',
                                        'blsd'       : 'sd',
                                    })
                                    t[self.Data['DefaultMode'] + "Mode"] = None

                                #if t['canqfly'] > 0:
                                #    t[self.Data['DefaultMode'] + "Mode"] = t['QFlyMode']
                                #    self.makeSoDFile({
                                #        't'          : t,
                                #        'bl'         : 'q',
                                #        'bla'        : 'aq',
                                #        'blf'        : 'fq',
                                #        'path'       : 'q',
                                #        'pathr'      : 'aq',
                                #        'pathf'      : 'fq',
                                #        'mobile'     : "Quantum Flight",
                                #        'stationary' : "Quantum Flight",
                                #        'modestr'    : "QFly",
                                #        'flight'     : "Fly",
                                #    })
                                #    t[self.Data['DefaultMode'] + "Mode"] = None

                                if t['cangfly']:
                                    t[self.Data['DefaultMode'] + "Mode"] = t['GFlyMode']
                                    self.makeSoDFile({
                                        't'          : t,
                                        'bl'         : 'a',
                                        'bla'        : 'af',
                                        'blf'        : 'ff',
                                        'path'       : 'ga',
                                        'pathr'      : 'gaf',
                                        'pathf'      : 'gff',
                                        'mobile'     : t['gfly'],
                                        'stationary' : t['gfly'],
                                        'modestr'    : "GFly",
                                        'flight'     : "GFly",
                                        'pathbo'     : 'gbo',
                                        'pathsd'     : 'gsd',
                                        'blbo'       : 'gbo',
                                        'blsd'       : 'gsd',
                                    })
                                    t[self.Data['DefaultMode'] + "Mode"] = None

                                if (self.Data['Temp'] and self.Data['TempTrayToggle']):
                                    trayslot = "1 " + self.Data['TempTray']
                                    t[self.Data['DefaultMode'] + "Mode"] = t['TempMode']
                                    self.makeSoDFile({
                                        't'          : t,
                                        'bl'         : 't',
                                        'bla'        : 'at',
                                        'blf'        : 'ft',
                                        'path'       : 't',
                                        'pathr'      : 'at',
                                        'pathf'      : 'ft',
                                        'mobile'     : trayslot,
                                        'stationary' : trayslot,
                                        'modestr'    : "Temp",
                                        'flight'     : "Fly",
                                    })
                                    t[self.Data['DefaultMode'] + "Mode"] = None 

        t['space'] = t['X'] = t['W'] = t['S'] = t['A'] = t['D'] = 0

        t['up']   = f"$$up {t['space']}"
        t['upx']  = f"$$up {(1-t['space'])}"
        t['dow']  = f"$$down {t['X']}"
        t['dowx'] = f"$$down {(1-t['X'])}"
        t['forw'] = f"$$forward {t['W']}"
        t['forx'] = f"$$forward {(1-t['W'])}"
        t['bac']  = f"$$backward {t['S']}"
        t['bacx'] = f"$$backward {(1-t['S'])}"
        t['lef']  = f"$$left {t['A']}"
        t['lefx'] = f"$$left {(1-t['A'])}"
        t['rig']  = f"$$right {t['D']}"
        t['rigx'] = f"$$right {(1-t['D'])}"

        if (self.Data['TurnLeft']  != "UNBOUND"): ResetFile.SetBind(self.Data['TurnLeft'], "+turnleft")
        if (self.Data['TurnRight'] != "UNBOUND"): ResetFile.SetBind(self.Data['TurnRight'],"+turnright")

        if self.Data['Temp']:
            temptogglefile1 = self.Profile.GetBindFile("temptoggle1.txt")
            temptogglefile2 = self.Profile.GetBindFile("temptoggle2.txt")
            temptogglefile2.SetBind(self.Data['TempTrayToggle'],'-down$$gototray 1'                        + self.Profile.GetBindFile('temptoggle1.txt').BLF())
            temptogglefile1.SetBind(self.Data['TempTrayToggle'],'+down$$gototray ' + self.Data['TempTray'] + self.Profile.GetBindFile('temptoggle2.txt').BLF())
            ResetFile.      SetBind(self.Data['TempTrayToggle'],'+down$$gototray ' + self.Data['TempTray'] + self.Profile.GetBindFile('temptoggle2.txt').BLF()) 

        (dwarfTPPower, normalTPPower, teamTPPower) = ('','','')
        if (self.Profile.Data['Archetype'] == "Warshade"):
            dwarfTPPower  = "powexecname Black Dwarf Step"
            normalTPPower = "powexecname Shadow Step"
        elif (self.Profile.Data['Archetype'] == "Peacebringer"):
            dwarfTPPower = "powexecname White Dwarf Step"
        else: # TODO ...if we have teleport
            normalTPPower = "powexecname Teleport"
            teamTPPower   = "powexecname Team Teleport"

        (dwarfpbind, novapbind, humanpbind, humanBindKey) = ('','','','')

        if ((self.Profile.Data['Archetype'] == "Peacebringer") or (self.Profile.Data['Archetype'] == "Warshade")):
            humanBindKey = self.Data['HumanMode']
            humanpbind = cbPBindToString(self.Data['HumanHumanPBind'], self.Profile)
            novapbind  = cbPBindToString(self.Data['HumanNovaPBind'],  self.Profile)
            dwarfpbind = cbPBindToString(self.Data['HumanDwarfPBind'], self.Profile)
            if (humanBindKey):
                ResetFile.SetBind(humanBindKey, humanpbind) 

#        #  kheldian form support
#        #  create the Nova and Dwarf form support files if enabled.
#        Nova  = self.Data['Nova']
#        Dwarf = self.Data['Dwarf']
#
#        fullstop = '$$up 0$$down 0$$forward 0$$backward 0$$left 0$$right 0'
#
#        if Nova['Enable']:
#            ResetFile.SetBind(Nova['Mode'],f"t $name, Changing to {Nova['Nova']} Form{fullstop}{t['on']}{Nova['Nova']}$$gototray {Nova['Tray']}" + self.Profile.GetBindFile('nova.txt').BLF())
#
#            novafile = self.Profile.GetBindFile("nova.txt")
#
#            if Dwarf['Enable']:
#                novafile.SetBind(Dwarf['Mode'],f"t $name, Changing to {Dwarf['Dwarf']} Form{fullstop}{t['off']}{Nova['Nova']}{t['on']}{Dwarf['Dwarf']}$$gototray {Dwarf['Tray']}" + self.Profile.GetBindFile('dwarf.txt').BLF())
#
#            humanBindKey = humanBindKey or Nova['Mode']
#
#            humpower = '$$powexectoggleon ' if (self.Data['UseHumanFormPower'] + self.Data['HumanFormShield']) else ''
#
#            novafile.SetBind(humanBindKey,"t \$name, Changing to Human Form, SoD Mode{fullstop}$$powexectoggleoff {Nova['Nova']} {humpower}$$gototray 1" + self.Profile.GetBindFile('reset.txt').BLF())
#
#            if humanBindKey == Nova['Mode']: humanBindKey = None
#
#            if novapbind: novafile.SetBind(Nova['Mode'], novapbind)
#
#            #if t['canqfly']: self.makeQFlyModeKey(t,"r", novafile, Nova['Nova'],"Nova")
#
#            novafile.SetBind(self.Data['Forward'],"+forward")
#            novafile.SetBind(self.Data['Left'],"+left")
#            novafile.SetBind(self.Data['Right'],"+right")
#            novafile.SetBind(self.Data['Back'],"+backward")
#            novafile.SetBind(self.Data['Up'],"+up")
#            novafile.SetBind(self.Data['Down'],"+down")
#            novafile.SetBind(self.Data['AutoRun'],"++forward")
#            novafile.SetBind(self.Data['FlyMode'],'nop')
#            if (self.Data['FlyMode'] != self.Data['RunMode']):
#                novafile.SetBind(self.Data['RunMode'],'nop')
#            if (self.Data['MousechordSoD']):
#                novafile.SetBind('mousechord "' + "+down$$+forward")
#
#            if (self.Data['TPMode'] and self.Data['TPEnable']):
#                novafile.SetBind(self.Data['TPCombo'],'nop')
#                novafile.SetBind(self.Data['TPMode'],'nop')
#                novafile.SetBind(self.Data['TPReset'],'nop')
#
#            novafile.SetBind(self.Data['Follow'],"follow")
#            # novafile.SetBind(self.Data['ToggleKey'],'t $name, Changing to Human Form, Normal Mode$$up 0$$down 0$$forward 0$$backward 0$$left 0$$right 0$$powexectoggleoff ' + Nova['Nova'] + '$$gototray 1' + self.Profile.GetBindFile('reset.txt').BLF()) 
#
#        if Dwarf['Enable']:
#            ResetFile.SetBind(Dwarf['Mode'],f"t $name, Changing to {Dwarf['Dwarf']} Form{fullstop}$$powexectoggleon {Dwarf['Dwarf']}$$gototray {Dwarf['Tray']}" + self.Profile.GetBindFile('dwarf.txt').BLF())
#            dwrffile = self.Profile.GetBindFile("dwarf.txt")
#            if Nova['Enable']:
#                dwrffile.SetBind(Nova['Mode'],f"t \$name, Changing to {Nova['Nova']} Form{fullstop}$$powexectoggleoff {Dwarf['Dwarf']}$$powexectoggleon {Nova['Nova']}$$gototray {Nova['Tray']}" + self.Profile.GetBindFile('nova.txt').BLF()) 
#
#            humanBindKey = humanBindKey or Dwarf['Mode']
#            humpower = '$$powexectoggleon ' + self.Data['HumanFormShield'] if self.Data['UseHumanFormPower'] else ''
#
#            dwrffile.SetBind(humanBindKey,f"t \$name, Changing to Human Form, SoD Mode{fullstop}$$powexectoggleoff {Dwarf['Dwarf']}{humpower}$$gototray 1" + self.Profile.GetBindFile('reset.txt').BLF())
#
#            if dwarfpbind:   dwrffile.SetBind(Dwarf['Mode'], dwarfpbind)
#            #if t['canqfly']: self.makeQFlyModeKey(t,"r", dwrffile, Dwarf['Dwarf'],"Dwarf")
#
#            dwrffile.SetBind(self.Data['Forward'],"+forward")
#            dwrffile.SetBind(self.Data['Left'],"+left")
#            dwrffile.SetBind(self.Data['Right'],"+right")
#            dwrffile.SetBind(self.Data['Back'],"+backward")
#            dwrffile.SetBind(self.Data['Up'],"+up")
#            dwrffile.SetBind(self.Data['Down'],"+down")
#            dwrffile.SetBind(self.Data['AutoRun'],"++forward")
#            dwrffile.SetBind(self.Data['FlyMode'],'nop')
#            dwrffile.SetBind(self.Data['Follow'],"follow")
#            if (self.Data['FlyMode'] != self.Data['RunMode']):
#                dwrffile.SetBind(self.Data['RunMode'],'nop')
#            if (self.Data['MousechordSoD']):
#                dwrffile.SetBind('mousechord "' + "+down$$+forward")
#
#            if self.Data['TPMode'] and self.Data['TPEnable']:
#                dwrffile.SetBind(self.Data['TPCombo'],'+down$$' + dwarfTPPower + t['detaillo'] + t['flycamdist'] + windowhide + self.Profile.GetBindFile('dtp','tp_on1.txt').BLF())
#                dwrffile.SetBind(self.Data['TPMode'],'nop')
#                dwrffile.SetBind(self.Data['TPReset'],t['detailhi'][2:] + t['runcamdist'] + windowshow + self.Profile.GetBindFile('dtp','tp_off.txt').BLF())
#                #  Create tp_off file
#                tp_off = self.Profile.GetBindFile("dtp","tp_off.txt")
#                tp_off.SetBind(self.Data['TPCombo'],'+down$$' + dwarfTPPower + t['detaillo'] + t['flycamdist'] + windowhide + self.Profile('dtp','tp_on1.txt').BLF())
#                tp_off.SetBind(self.Data['TPMode'],'nop')
#
#                tp_on1 = self.Profile.GetBindFile("dtp","tp_on1.txt")
#                tp_on1.SetBind(self.Data['TPCombo'],'-down$$powexecunqueue' + t['detailhi'] + t['runcamdist'] + windowshow + self.Profile.GetBindFile('dtp','tp_off.txt').BLF())
#                tp_on1.SetBind(self.Data['TPMode'],'+down' + self.Profile.GetBindFile('dtp','tp_on2.txt').BLF())
#
#                tp_on2 = self.Profile.GetBindFile("dtp","tp_on2.txt")
#                tp_on2.SetBind(self.Data['TPMode'],'-down$$' + dwarfTPPower + self.Profile.GetBindFile('dtp','tp_on1.txt').BLF())
#
#            # dwrffile.SetBind(self.Data['ToggleKey'],f"t \$name, Changing to Human Form, Normal Mode{fullstop}$$powexectoggleoff {Dwarf['Dwarf']}$$gototray 1" + self.Profile.GetBindFile('reset.txt').BLF()) 

        if (self.Data['SimpleSJCJ']):
            if (self.Data['JumpCJ'] and self.Data['JumpSJ']):
                ResetFile.SetBind(self.Data['JumpMode'],'powexecname Super Jump$$powexecname Combat Jumping')
            elif (self.Data['JumpSJ']):
                ResetFile.SetBind(self.Data['JumpMode'],'powexecname Super Jump')
            elif (self.Data['JumpCJ']):
                ResetFile.SetBind(self.Data['JumpMode'],'powexecname Combat Jumping')

        if (self.Data['TPMode'] and self.Data['TPEnable'] and not normalTPPower):
            ResetFile.SetBind(self.Data['TPCombo'],'nop')
            ResetFile.SetBind(self.Data['TPMode'],'nop')
            ResetFile.SetBind(self.Data['TPReset'],'nop')

        if (self.Data['TPMode'] and self.Data['TPEnable'] and not (self.Profile.Data['Archetype'] == "Peacebringer") and normalTPPower):
            tphovermodeswitch = ''
            if not t['tphover']:
                # TODO hmm can't get this from .KeyState directly?
                tphovermodeswitch = t.bl('r') + "000000.txt"
                #($tphovermodeswitch = t.bl('r')) =~ s/\d\d\d\d\d\d/000000/

            ResetFile.SetBind(self.Data['TPCombo'],'+down$$' + normalTPPower + t['detaillo'] + t['flycamdist'] + windowhide + self.Profile.GetBindFile('tp','tp_on1.txt').BLF())
            ResetFile.SetBind(self.Data['TPMode'],'nop')
            ResetFile.SetBind(self.Data['TPReset'],t['detailhi'][2:] + t['runcamdist'] + windowshow + self.Profile.GetBindFile('tp','tp_off.txt').BLF() + tphovermodeswitch)
            #  Create tp_off file
            tp_off = self.Profile.GetBindFile("tp","tp_off.txt")
            tp_off.SetBind(self.Data['TPCombo'],'+down$$' + normalTPPower + t['detaillo'] + t['flycamdist'] + windowhide + self.Profile.GetBindFile('tp','tp_on1.txt').BLF())
            tp_off.SetBind(self.Data['TPMode'],'nop')

            tp_on1 = self.Profile.GetBindFile("tp","tp_on1.txt")
            zoomin = '' if t['tphover'] else (t['detailhi'] + t['runcamdist'])
            tp_on1.SetBind(self.Data['TPCombo'],'-down$$powexecunqueue' + zoomin + windowshow + self.Profile.GetBindFile('tp','tp_off.txt').BLF() + tphovermodeswitch)
            tp_on1.SetBind(self.Data['TPMode'],'+down' + t['tphover'] + self.Profile.GetBindFile('tp','tp_on2.txt').BLF())

            tp_on2 = self.Profile.GetBindFile("tp","tp_on2.txt")
            tp_on2.SetBind(self.Data['TPMode'],'-down$$' + normalTPPower + self.Profile.GetBindFile('tp','tp_on1.txt').BLF())

        if (self.Data['TTPMode'] and self.Data['TTPEnable'] and not (self.Profile.Data['Archetype'] == "Peacebringer") and teamTPPower):
            tphovermodeswitch = ''
            ResetFile.SetBind(self.Data['TTPCombo'],'+down$$' + teamTPPower + t['detaillo'] + t['flycamdist'] + windowhide + self.Profile.GetBindFile('ttp','ttp_on1.txt').BLF())
            ResetFile.SetBind(self.Data['TTPMode'],'nop')
            # TODO does this substr / [2:]  dtrt?
            ResetFile.SetBind(self.Data['TTPReset'],t['detailhi'][2:] + t['runcamdist'] + windowshow + self.Profile.GetBindFile('ttp','ttp_off').BLF() + tphovermodeswitch)
            #  Create tp_off file
            ttp_off = self.Profile.GetBindFile("ttp","ttp_off.txt")
            ttp_off.SetBind(self.Data['TTPCombo'],'+down$$' + teamTPPower + t['detaillo'] + t['flycamdist'] + windowhide + self.Profile.GetBindFile('ttp','ttp_on1.txt').BLF())
            ttp_off.SetBind(self.Data['TTPMode'],'nop')

            ttp_on1 = self.Profile.GetBindFile("ttp","ttp_on1.txt")
            ttp_on1.SetBind(self.Data['TTPCombo'],'-down$$powexecunqueue' + t['detailhi'] + t['runcamdist'] + windowshow + self.Profile.GetBindFile('ttp','ttp_off').BLF() + tphovermodeswitch)
            ttp_on1.SetBind(self.Data['TTPMode'],'+down' + self.Profile.GetBindFile('ttp','ttp_on2.txt').BLF())

            ttp_on2 = self.Profile.GetBindFile("ttp","ttp_on2.txt")
            ttp_on2.SetBind(self.Data['TTPMode'],'-down$$' + teamTPPower + self.Profile.GetBindFile('ttp','ttp_on1.txt').BLF())


    def sodResetKey(self, curfile, path, turnoff, moddir):
        re.sub(r'\d\d\d\d\d\d', '000000', str(path)) # ick ick ick
        bf = self.Profile.GetBindFile(path)

        (u, d) = (0, 0)
        if (moddir == 'up')  : u = '1'
        if (moddir == 'down'): d = '1'
        curfile.SetBind(self.Profile.Data['ResetKey'],
                f'up {u}$$down {d}$$forward 0$$backward 0$$left 0$$right 0' +
                turnoff + '$$t $name, SoD Binds Reset' + bf.BaseReset() + bf.BLF())


    def sodDefaultResetKey(self, mobile, stationary):
        pass
        # TODO -- decide where to keep 'resetstring' and make this def update it.
        #cbAddReset('up 0$$down 0$$forward 0$$backward 0$$left 0$$right 0'.self.actPower_name(1, stationary, mobile) + '$$t $name, SoD Binds Reset')



    # TODO TODO TODO -- the s/\d\d\d\d\d\d/$newbits/ scheme in the following six subs is a vile evil (live veil ilve vlie) hack.
    def sodUpKey(self, t, bl, curfile, mobile, stationary, flight, autorun, followbl, bo, sssj):
        bl = str(bl)
        followbl = str(followbl)

        (upx, dow, forw, bac, lef, rig) = (t['upx'], t.D(), t.F(), t.B(), t.L(), t.R())

        (ml, toggle, toggleon, toggleoff, toggleoff2) = ('','','','','')

        actkeys = t['totalkeys']

        if (not flight and not sssj): mobile = stationary = None

        if (bo == "bo"):
            upx = '$$up 1'
            dow = '$$down 0'
        if (bo == "sd"):
            upx = '$$up 0'
            dow = '$$down 1'

        if mobile     == "Group Fly": mobile = None
        if stationary == "Group Fly": stationary = None

        if flight == "Jump":
            dow = '$$down 0'
            actkeys = t['jkeys']
            if (t['totalkeys'] == 1 and t['space'] == 1):
                upx = '$$up 0'
            elif (t['X'] == 1):
                upx = '$$up 0'

        toggleon = mobile
        if (actkeys == 0):
            ml = t['mlon']
            toggleon = mobile
            if (not (mobile and (mobile == stationary))): toggleoff = stationary
        else:
            toggleon = None 

        if (t['totalkeys'] == 1 and t['space'] == 1):
            ml = t['mloff']
            if (not (stationary and (mobile == stationary))): toggleoff = mobile
            toggleon = stationary
        else:
            toggleoff = None 

        if sssj:
            if (t['space'] == 0): #  if we are hitting the space bar rather than releasing it..
                toggleon  = sssj
                toggleoff = mobile
                if (stationary and stationary == mobile):
                    toggleoff2 = stationary
                elif (t['space'] == 1): #  if we are releasing the space bar ..
                    toggleoff = sssj
                if (t['horizkeys'] > 0 or autorun): #  and we are moving laterally, or in autorun..
                    toggleon = mobile
                else:
                    toggleon = stationary

        if (toggleon or toggleoff):
            toggle = self.actPower_name(1, toggleon, toggleoff, toggleoff2)

        newbits = t.KeyState({'toggle' : 'space'})
        re.sub(r'\d\d\d\d\d\d', newbits, str(bl))

        ini = '-down' if (t['space'] == 1) else '+down'

        if followbl:
            move = ''
            if (t['space'] != 1):
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, str(bl))
                move = upx + dow + forw + bac + lef + rig

            curfile.SetBind(self.Data['Up'], ini + move + bl)
        elif (not autorun):
            curfile.SetBind(self.Data['Up'], ini + upx + dow + forw + bac + lef + rig + ml + toggle + bl)
        else:
            if (not sssj):
                toggle = '' #  returns the following line to the way it was before sssj
            curfile.SetBind(self.Data['Up'], ini + upx + dow + '$$backward 0' + lef + rig + toggle + t['mlon'] + bl)

    def sodDownKey(self, t, bl, curfile, mobile, stationary, flight, autorun, followbl, bo, sssj):
        bl = str(bl)
        followbl = str(followbl)

        (up, dowx, forw, bac, lef, rig) = (t.U(), t['dowx'], t.F(), t.B(), t.L(), t.R())

        (ml, toggle, toggleon, toggleoff) = ('','','','')
        actkeys = t['totalkeys']

        if (not flight): mobile = stationary = ''
        if (bo == 'bo'):
            up   = '$$up 1'
            dowx = '$$down 0'
        if (bo == 'sd'):
            up   = '$$up 0'
            dowx = '$$down 1'

        if (mobile     and mobile     == 'Group Fly'): mobile     = None
        if (stationary and stationary == 'Group Fly'): stationary = None

        if (flight == 'Jump'):
            dowx = '$$down 0'
            # if (t['cancj']  == 1): aj = t['cjmp']
            # if (t['canjmp'] == 1): aj = t['jump']
            actkeys = t['jkeys']
            if (t['X'] == 1 and t['totalkeys'] > 1): up = '$$up 1'

        if (actkeys == 0):
            ml = t['mlon']
            toggleon = mobile
            if (not (mobile and mobile == stationary)): toggleoff = stationary
        else:
            toggleon = None 

        if (t['totalkeys'] == 1 and t['X'] == 1):
            ml = t['mloff']
            if (not (stationary and mobile == stationary)): toggleoff = mobile
            toggleon = stationary
        else:
            toggleoff = None

        if (toggleon or toggleoff):
            toggle = self.actPower_name(1, toggleon, toggleoff)

        newbits = t.KeyState({'toggle' : 'X'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['X'] == 1) else '+down'

        if (followbl):
            move = ''
            if (t['X'] != 1):
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = up + dowx + forw + bac + lef + rig

            curfile.SetBind(self.Data['Down'], ini + move + bl)
        elif (not autorun):
            curfile.SetBind(self.Data['Down'], ini + up + dowx + forw + bac + lef + rig + ml + toggle + bl)
        else:
            curfile.SetBind(self.Data['Down'], ini + up + dowx + '$$backward 0' + lef + rig + t['mlon'] + bl)

    ###### HERE!

    def sodForwardKey(self, t, bl, curfile, mobile, stationary, flight, autorunbl, followbl, bo, sssj):
        bl = str(bl)
        followbl = str(followbl)

        (up, dow, forx, bac, lef, rig) = (t.U(), t.D(), t['forx'], t.B(), t.L(), t.R())
        (ml, toggle, toggleon, toggleoff) = ('','','','')
        actkeys = t['totalkeys']
        if (bo == "bo"):
            up = '$$up 1'
            dow = '$$down 0'
        if (bo == "sd"):
            up = '$$up 0'
            dow = '$$down 1'

        if (mobile     == 'Group Fly'): mobile     = None
        if (stationary == 'Group Fly'): stationary = None

        if (flight == "Jump"):
            dow = '$$down 0'
            actkeys = t['jkeys']
            if ( (t['totalkeys'] == 1 and t['W'] == 1) or (t['X'] == 1)) :
                 up = '$$up 0'

        toggleon = mobile
        if (t['totalkeys'] == 0):
            ml = t['mlon']
            if (not (mobile and mobile == stationary)):
                toggleoff = stationary 

        if (t['totalkeys'] == 1 and t['W'] == 1):
            ml = t['mloff'] 

        testKeys = t['totalkeys'] if flight else t['horizkeys']
        if (testKeys == 1 and t['W'] == 1):
            if (not (stationary and mobile == stationary)):
                toggleoff = mobile

            toggleon = stationary 

        if (sssj and t['space'] == 1): #  if (we are jumping with SS+SJ mode enabled
            toggleon = sssj
            toggleoff = mobile 

        if (toggleon or toggleoff):
            toggle = self.actPower_name(1, toggleon, toggleoff) 

        newbits = t.KeyState({'toggle' : 'W'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['W'] == 1) else '+down'

        if (followbl):
            if (t['W'] == 1):
                move = ini
            else:
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = ini + up + dow + forx + bac + lef + rig

            curfile.SetBind(self.Data['Forward'], move + bl)
            if (self.Data['MousechordSoD']):
                if (t['W'] == 1): move = ini + up + dow + forx + bac + rig + lef
                curfile.SetBind('mousechord', move + bl)

        elif (not autorunbl):
            curfile.SetBind(self.Data['Forward'], ini + up + dow + forx + bac + lef + rig + ml + toggle + bl)
            if (self.Data['MousechordSoD']):
                curfile.SetBind('mousechord', ini + up + dow + forx + bac + rig + lef + ml + toggle + bl)

        else:
            if (t['W'] == 1):
                bl = autorunbl
                re.sub('\d\d\d\d\d\d', newbits, bl)

            curfile.SetBind(self.Data['Forward'], ini + up + dow + '$$forward 1$$backward 0' + lef + rig + t['mlon'] + bl)
            if (self.Data['MousechordSoD']):
                curfile.SetBind('mousechord', ini + up + dow + '$$forward 1$$backward 0' + rig + lef + t['mlon'] + bl) 


    def sodBackKey(self, t, bl, curfile, mobile, stationary, flight, autorunbl, followbl, bo, sssj):
        bl = str(bl)
        followbl = str(followbl)
        (up, dow, forw, bacx, lef, rig) = (t.U(), t.D(), t.F(), t['bacx'], t.L(), t.R())

        (ml, toggle, toggleon, toggleoff) = ('','','','')

        actkeys = t['totalkeys']
        if (bo == "bo"):
            up = '$$up 1';
            dow = '$$down 0'
        if (bo == "sd"):
            up = '$$up 0';
            dow = '$$down 1'

        if (mobile     == 'Group Fly'): mobile = None
        if (stationary == 'Group Fly'): stationary = None

        if (flight == "Jump"):
            dow = '$$down 0'
            actkeys = t['jkeys']
            if (t['totalkeys'] == 1 and t['S'] == 1): up = '$$up 0'
            if (t['X'] == 1): up = '$$up 0' 

        toggleon = mobile
        if (t['totalkeys'] == 0):
            ml = t['mlon']
            toggleon = mobile
            if (not (mobile and mobile == stationary)):
                toggleoff = stationary 

        if (t['totalkeys'] == 1 and t['S'] == 1):
            ml = t['mloff'] 

        testKeys = t['totalkeys'] if flight else t['horizkeys']
        if (testKeys == 1 and t['S'] == 1):
            if (not (stationary and mobile == stationary)):
                toggleoff = mobile

            toggleon = stationary 

        if (sssj and t['space'] == 1): #  if (we are jumping with SS+SJ mode enabled
            toggleon = sssj
            toggleoff = mobile 

        if (toggleon or toggleoff):
            toggle = self.actPower_name(1, toggleon, toggleoff) 

        newbits = t.KeyState({'toggle' : 'S'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['S'] == 1) else "+down"

        if (followbl):
            if (t['S'] == 1):
                move = ini
            else:
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = ini + up + dow + forw + bacx + lef + rig

            curfile.SetBind(self.Data['Back'], move + bl)
        elif (not autorunbl):
            curfile.SetBind(self.Data['Back'], ini + up + dow + forw + bacx + lef + rig + ml + toggle + bl)
        else:
            if (t['S'] == 1):
                move = '$$forward 1$$backward 0'
            else:
                move = '$$forward 0$$backward 1'
                bl = autorunbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)

            curfile.SetBind(self.Data['Back'], ini + up + dow + move + lef + rig + t['mlon'] + bl) 


    def sodLeftKey (self, t, bl, curfile, mobile, stationary, flight, autorun, followbl, bo, sssj):
        bl = str(bl)
        followbl = str(followbl)

        (up, dow, forw, bac, lefx, rig) = (t.U(), t.D(), t.F(), t.B(), t['lefx'], t.R())

        (ml, toggle, toggleon, toggleoff) = ('','','','')

        actkeys = t['totalkeys']
        if (bo == "bo"):
            up = '$$up 1'
            dow = '$$down 0'
        if (bo == "sd"):
            up = '$$up 0'
            dow = '$$down 1'

        if (mobile     == 'Group Fly'): mobile = None
        if (stationary == 'Group Fly'): stationary = None

        if (flight == "Jump"):
            dow = '$$down 0'
            actkeys = t['jkeys']
            if (t['totalkeys'] == 1 and t['A'] == 1): up = '$$up 0'
            if (t['X'] == 1): up = '$$up 0'

        toggleon = mobile
        if (t['totalkeys'] == 0):
            ml = t['mlon']
            toggleon = mobile
            if (not (mobile and mobile == stationary)):
                toggleoff = stationary

        if (t['totalkeys'] == 1 and t['A'] == 1):
            ml = t['mloff']

        testKeys = t['totalkeys'] if flight else t['horizkeys']
        if (testKeys == 1 and t['A'] == 1):
            if (not (stationary and mobile == stationary)):
                toggleoff = mobile

            toggleon = stationary

        if (sssj and t['space'] == 1): #  if (we are jumping with SS+SJ mode enabled
            toggleon = sssj
            toggleoff = mobile 

        if (toggleon or toggleoff):
            toggle = self.actPower_name(1, toggleon, toggleoff) 

        newbits = t.KeyState({'toggle' : 'A'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['A'] == 1) else '+down'

        if (followbl):
            if (t['A'] == 1):
                move = ini
            else:
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = ini + up + dow + forw + bac + lefx + rig

            curfile.SetBind(self.Data['Left'], move + bl)
        elif (not autorun):
            curfile.SetBind(self.Data['Left'], ini + up + dow + forw + bac + lefx + rig + ml + toggle + bl)
        else:
            curfile.SetBind(self.Data['Left'], ini + up + dow + '$$backward 0' + lefx + rig + t['mlon'] + bl) 


    def sodRightKey(self, t, bl, curfile, mobile, stationary, flight, autorun, followbl, bo, sssj):
        bl = str(bl)
        followbl = str(followbl)
        (up, dow, forw, bac, lef, rigx) = (t.U(), t.D(), t.F(), t.B(), t.L(), t['rigx'])

        (ml, toggle, toggleon, toggleoff) = ('','','','')

        actkeys = t['totalkeys']
        if (bo == "bo"): up = '$$up 1'; dow = '$$down 0'
        if (bo == "sd"): up = '$$up 0'; dow = '$$down 1'

        if (mobile     == 'Group Fly'): mobile = None
        if (stationary == 'Group Fly'): stationary = None

        if (flight == "Jump"):
            dow = '$$down 0'
            actkeys = t['jkeys']
            if (t['totalkeys'] == 1 and t['D'] == 1): up = '$$up 0'
            if (t['X'] == 1): up = '$$up 0'

        toggleon = mobile
        if (t['totalkeys'] == 0):
            ml = t['mlon']
            toggleon = mobile
            if (not (mobile and mobile == stationary)):
                toggleoff = stationary

        if (t['totalkeys'] == 1 and t['D'] == 1):
            ml = t['mloff']

        testKeys = t['totalkeys'] if flight else t['horizkeys']
        if (testKeys == 1 and t['D'] == 1):
            if (not (stationary and mobile == stationary)):
                toggleoff = mobile

            toggleon = stationary

        if (sssj and t['space'] == 1): #  if (we are jumping with SS+SJ mode enabled
            toggleon = sssj
            toggleoff = mobile

        if (toggleon or toggleoff):
            toggle = self.actPower_name(1, toggleon, toggleoff)

        newbits = t.KeyState({'toggle' : 'D'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['D'] == 1) else '+down'

        if (followbl):
            if (t['D'] == 1):
                move = ini
            else:
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = ini + up + dow + forw + bac + lef + rigx

            curfile.SetBind(self.Data['Right'], move + bl)
        elif (not autorun):
            curfile.SetBind(self.Data['Right'], ini + up + dow + forw + bac + lef + rigx + ml + toggle + bl)
        else:
            curfile.SetBind(self.Data['Right'], ini + up + dow + '$$forward 1$$backward 0' + lef + rigx + t['mlon'] + bl) 


    def sodAutoRunKey(self, t, bl, curfile, mobile, sssj):
        bl = str(bl)

        if (sssj and t['space'] == 1):
            curfile.SetBind(self.Data['AutoRun'],'forward 1$$backward 0' + t.dirs('UDLR') + t['mlon'] + self.actPower_name(1, sssj, mobile) + bl)
        else:
            curfile.SetBind(self.Data['AutoRun'],'forward 1$$backward 0' + t.dirs('UDLR') + t['mlon'] + self.actPower_name(1, mobile) + bl)

    def sodAutoRunOffKey(self, t, bl, curfile, mobile, stationary, flight, sssj = None):
        bl = str(bl)

        if (not flight and not sssj):
            if (t['horizkeys'] > 0):
                toggleon = t['mlon'] + self.actPower_name(1, mobile)
            else:
                toggleon = t['mloff'] + self.actPower_name(1, stationary, mobile)

        elif (sssj):
            if (t['horizkeys'] > 0 or t['space'] == 1):
                toggleon = t['mlon'] + self.actPower_name(1, mobile, toggleoff)
            else:
                toggleon = t['mloff'] + self.actPower_name(1, stationary, mobile, toggleoff)

        else:
            if (t['totalkeys'] > 0):
                toggleon = t['mlon'] + self.actPower_name(1, mobile)
            else:
                toggleon = t['mloff'] + self.actPower_name(1, stationary, mobile) 

        bindload = bl + t.KeyState() + '.txt'
        curfile.SetBind(self.Data['AutoRun'], t.dirs('UDFBLR') + toggleon + bindload)


    def sodFollowKey(self, t, bl, curfile, mobile):
        curfile.SetBind(self.Data['Follow'],'follow' + self.actPower_name(1, mobile) + bl + t.KeyState() + '.txt')


    def sodFollowOffKey(self, t, bl, curfile, mobile, stationary, flight):
        bl = str(bl)

        toggle = ''
        if (not flight):
            if (t['horizkeys'] == 0):
                if (stationary == mobile):
                    toggle = self.actPower_name(1, stationary, mobile)
                else:
                    toggle = self.actPower_name(1, stationary) 
        else:
            if (t['totalkeys'] == 0):
                if (stationary == mobile):
                    toggle = self.actPower_name(1, stationary, mobile)
                else:
                    toggle = self.actPower_name(1, stationary) 

        curfile.SetBind(self.Data['Follow'],"follow" + toggle + t.U() + t['dow'] + t.F() + t.B() + t.L() + t.R() + bl + t.KeyState() + '.txt')


    def bindisused(self):
        return self.Data['Enable']

    def findconflicts(self):
        Utility.CheckConflict(self.Data,"Up","Up Key")
        Utility.CheckConflict(self.Data,"Down","Down Key")
        Utility.CheckConflict(self.Data,"Forward","Forward Key")
        Utility.CheckConflict(self.Data,"Back","Back Key")
        Utility.CheckConflict(self.Data,"Left","Strafe Left Key")
        Utility.CheckConflict(self.Data,"Right","Strafe Right Key")
        Utility.CheckConflict(self.Data,"TurnLeft","Turn Left Key")
        Utility.CheckConflict(self.Data,"TurnRight","Turn Right Key")
        Utility.CheckConflict(self.Data,"AutoRun","AutoRun Key")
        Utility.CheckConflict(self.Data,"Follow","Follow Key")

        if (self.Data['NonSoD'])                          : Utility.CheckConflict(self.Data,"NonSoDMode","NonSoD Key")
        if (self.Data['Sprint'])                            : Utility.CheckConflict(self.Data,"SprintMode","Sprint Mode Key")
        if (self.Data['SSSS'])                            : Utility.CheckConflict(self.Data,"RunMode","Speed Mode Key")
        if (self.Data['JumpCJ'] or self.Data['JumpSJ'])   : Utility.CheckConflict(self.Data,"JumpMode","Jump Mode Key")
        if (self.Data['FlyHover'] or self.Data['FlyFly']) : Utility.CheckConflict(self.Data,"FlyMode","Fly Mode Key")

        #if (self.Data['FlyQFly'] and (self.Profile.Data['Archetype'] == "Peacebringer")) : Utility.CheckConflict(self.Data,"QFlyMode","Q.Fly Mode Key")

        if (self.Data['TPMode'] and self.Data['TPEnable']):
            Utility.CheckConflict(self.Data['TPMode'],"ComboKey","TP ComboKey")
            Utility.CheckConflict(self.Data['TPMode'],"ResetKey","TP ResetKey")

            TPQuestion = "Teleport Bind"
            if (self.Profile.Data['Archetype'] == "Peacebringer"):
                TPQuestion = "Dwarf Step Bind"
            elif (self.Profile.Data['Archetype'] == "Warshade"):
                TPQuestion = "Shd/Dwf Step Bind"

            Utility.CheckConflict(self.Data['TPMode'],"BindKey", TPQuestion)

        if (self.Data['FlyGFly']): Utility.CheckConflict(self.Data,"GFlyMode","Group Fly Key")
        if (self.Data['TTPMode'] and self.Data['TTPEnable']):
            Utility.CheckConflict(self.Data['TTPMode'],"ComboKey","TTP ComboKey")
            Utility.CheckConflict(self.Data['TTPMode'],"ResetKey","TTP ResetKey")
            Utility.CheckConflict(self.Data['TTPMode'],"BindKey","Team TP Bind")

        if (self.Data['Temp']):
            Utility.CheckConflict(self.Data,"TempMode","Temp Mode Key")
            Utility.CheckConflict(self.Data['TempTrayToggle'],"TraySwitch","Tray Toggle Key") 

        if ((self.Profile.Data['Archetype'] == "Peacebringer") or (self.Profile.Data['Archetype'] == "Warshade")):
            if (self.Data['Nova']  and self.Data['NovaEnable']): Utility.CheckConflict(self.Data['Nova'], "Mode","Nova Form Bind")
            if (self.Data['Dwarf'] and self.Data['DwarfEnable']): Utility.CheckConflict(self.Data['Dwarf'],"Mode","Dwarf Form Bind")

    #  toggleon variation
    def actPower_toggle(self, unq, on, off):
        (s, traytest) = ('','')
        if isinstance(on, dict):
            #  deal with power slot stuff..
            traytest = on['trayslot']

        offpower = {}
        if isinstance(off, list):
            for w in off:
                if (w and w != 'on' and not (w in offpower)):
                    if isinstance(w, dict):
                        if (w['trayslot'] == traytest):
                            s = s + '$$powexectray ' + w['trayslot']
                            unq = 1
                    else:
                        offpower[w] = 1
                        s = s + '$$powexectoggleoff ' + w

        # TODO - I don't think there's ever 'trayslot' sent in here but sigh
        #    if (off['trayslot'] and off['trayslot'] == traytest):
        #        s = s + '$$powexectray ' + off['trayslot']
        #        unq = 1
        else:
            if (off and (off != 'on') and not offpower.get(off, '')):
                offpower[off] = 1
                s = s + '$$powexectoggleoff ' + off

        if (unq and s):
            s = s + '$$powexecunqueue'

        # lop off prelim $$ (used to be "if (start):" but start was always 1 in every call here
        s = s[2:]
        if (on):
            if isinstance(on, dict):
                #  deal with power slot stuff..
                s = s + '$$powexectray '.on['trayslot'] + '$$powexectray ' + on['trayslot']
            else:
                s = s + '$$powexectoggleon ' + on
        return s


    def actPower_name(self, start, unq, on = None, *args):
        (s, traytest) = ('','')
        if isinstance(on, dict):
            #  deal with power slot stuff..
            traytest = on['trayslot']

        for v in args:
            if isinstance(v, list):
                for item in v:
                    _, w = item
                    if (w and w != 'on'):
                        if isinstance(w, dict):
                            if (w['trayslot'] == traytest):
                                s = s + '$$powexectray ' + w['trayslot']
                        else:
                            s = s + '$$powexecname ' + w

                if (v['trayslot'] and v['trayslot'] == traytest):
                    s = s + '$$powexectray ' + v['trayslot']

            else:
                if (v and v != 'on'):
                    s = s + '$$powexecname ' + v

        if (unq and s):
            s = s + '$$powexecunqueue' 

        if (on and on != ''):
            if isinstance(on, dict):
                #  deal with power slot stuff..
                s = s + '$$powexectray ' + on['trayslot'] + '$$powexectray ' + on['trayslot']
            else:
                s = s + '$$powexecname ' + on + '$$powexecname ' + on 

        if (start): s = s[2:]
        return s


    # TODO - this isn't used anywhere, is it useful?
    #  updated hybrid binds can reduce the space used in SoD Bindfiles by more than 40KB per SoD mode generated
    def actPower_hybrid(self, start, unq, on, *args):
        (s, traytest) = ('','')
        if isinstance(on, dict): traytest = on['trayslot']

        for v in args:
            if isinstance(v, list):
                for pair in v:
                    _, w = pair
                    if (w and w != 'on'):
                        if isinstance(w, dict):
                            if (w['trayslot'] == traytest):
                                s = s + '$$powexectray ' + w['trayslot']
                        else:
                            s = s + '$$powexecname ' + w

                if (v['trayslot'] == traytest):
                    s = s + '$$powexectray ' + v['trayslot']
            else:
                if (v == 'on'): s = s + '$$powexecname ' + v

        if (unq and s): s = s + '$$powexecunqueue'

        if (on):
            if isinstance(on, dict):
                #  deal with power slot stuff..
                s = s + '$$powexectray ' + on['trayslot'] + '$$powexectray ' + on['trayslot']
            else:
                s = s + '$$powexectoggleon ' + on

        if start: s = s[2:]
        return s


    # local actPower = actPower_name
    # # local actPower = self.actPower_toggle
    def sodJumpFix(self, t, key, makeModeKey, suffix, bl, curfile, turnoff, autofollowmode, feedback):

        bindfile = self.Profile.GetBindFile(f"{autofollowmode}j", suffix)
        t['ini'] = '-down$$'
        makeModeKey(self.Profile, t, bl, str(bindfile), turnoff,None,1)
        curfile.SetBind(key,"+down" + feedback + self.actPower_name(1, t['cjmp']) + bindfile.BLF())


    def sodSetDownFix (self, t, key, makeModeKey, suffix, bl, curfile, turnoff, autofollowmode, feedback):
        pathsuffix = 'f' if autofollowmode else 'a'
        bindfile = self.Profile.GetBindFile(f"autofollowmode{pathsuffix}", suffix)
        t['ini'] = '-down$$'
        makeModeKey(self.Profile, t, bl, str(bindfile), turnoff,None,1)
        curfile.SetBind(key,'+down' + feedback + bindfile.BLF())

    UI.Labels.Add( {
        'Up'        : 'Up',
        'Down'      : 'Down',
        'Forward'   : 'Forward',
        'Back'      : 'Back',
        'Left'      : 'Strafe Left',
        'Right'     : 'Strafe Right',
        'TurnLeft'  : 'Turn Left',
        'TurnRight' : 'Turn Right',
        'AutoRun'   : 'Auto Run',
        'Follow'    : 'Follow Target',

        'DefaultMode'   : 'Default SoD Mode',
        'MousechordSoD' : 'Mousechord is SoD Forward',
        'AutoMouseLook' : 'Automatically Mouselook when moving',

        'SprintPower' : 'Power to use for Sprint',

        'ChangeCamdist'     : 'Change camera distance when moving',
        'CamdistBase'       : 'Base Camera Distance',
        'CamdistTravelling' : 'Travelling Camera Distance',

        'ChangeDetail'     : 'Change graphics detail level when moving',
        'DetailBase'       : 'Base Detail Level',
        'DetailTravelling' : 'Travelling Detail Level',

        'NonSoD'     : "Enable Non-SoD movement keys toggle",
        'NonSoDMode' : 'Non-SoD Mode',
        'ToggleSoD'  : 'SoD Mode Toggle',

        'JumpMode'   : 'Toggle Jump Mode',
        'SimpleSJCJ' : 'Simple Combat Jumping / Super Jump Toggle',
        'JumpCJ'     : "Player has Combat Jump?",
        'JumpSJ'     : "Player has Super Jump?",

        'RunMode'          : 'Toggle Super Speed Mode',
        'SSOnlyWhenMoving' : 'SuperSpeed only when moving',
        'SSSJModeEnable'   : 'Enable Super Speed / Super Jump Mode',

        'FlyMode'  : 'Toggle Fly Mode',
        'GFlyMode' : 'Toggle Group Fly Mode',

        'SelfTellOnChange' : 'Self-/tell when changing mode',

        'TPEnable'         : 'Enable Teleport Binds',
        'TPMode'           : 'Teleport Bind',
        'TPCombo'          : 'Teleport Combo Key',
        'TPReset'          : 'Teleport Reset Key',
        'HideWinsDuringTP' : 'Hide Windows when Teleporting',
        'AutoHoverTP'      : 'Automatically use Hover when Teleporting',

        'TTPEnable'   : 'Enable Team Teleport Binds',
        'TTPMode'     : 'Team Teleport Bind',
        'TTPCombo'    : 'Team Teleport Combo Key',
        'TTPReset'    : 'Team Teleport Reset Key',
        'AutoGFlyTTP' : 'Automatically use Group Fly when Team Teleporting',

        'Temp'           : 'Enable Temporary Travel Power binds',
        'TempMode'       : 'Toggle Temp Mode',
        'TempTray'       : 'Temporary Travel Power Tray',
        'TempTrayToggle' : 'Toggle Temporary Travel Power Tray',

        'NovaMode'  : 'Toggle Nova Form',
        'NovaTray'  : 'Nova Travel Power Tray',
        'DwarfMode' : 'Toggle Dwarf Form',
        'DwarfTray' : 'Dwarf Travel Power Tray',
        'HumanMode' : 'Human Form',
        'HumanTray' : 'Human Travel Power Tray',

        'Sprint' : 'Enable Sprint SoD',
    })

class SoD_Table(dict):

    def __init__(self, data):
        for k in data:
            self[k] = data[k]

            self.dirnames = { 'U' : 'up', 'D' : 'dow', 'F' : 'forw', 'B' : 'bac', 'L' : 'lef', 'R' : 'rig' }

    def KeyState(self, p = {'toggle':None}):
        ret = ''
        for key in ('space','X','W','S','A','D'):
            ret = ret + str(not self[key] if (key == p['toggle']) else self[key])
        return ret

    # These next two subs are terrible.  This stuff should all be squirreled away in BindFile.

    # This will return "$$bindloadfilesilent C:\path\CODE\CODE1010101<suffix>.txt"
    def bl(self, code, suffix = ''):
        return self['profile'].GetBindFile(code.upper(), code.upper() + self.KeyState() + suffix + '.txt').BLF()

    # This will return "CODE\CODE1010101<suffix>.txt" (without bindsdir prepended)
    def path(self, code, suffix = ''): 
        return Path(code.upper(), code.upper() + self.KeyState() + suffix + '.txt')

    def dirs(self, dirs):
        ret = ''
        for dir in list(dirs):
            ret = ret + self[ self.dirnames[dir] ]
        return ret

    def U(self): return self['up']
    def D(self): return self['dow']
    def F(self): return self['forw']
    def B(self): return self['bac']
    def L(self): return self['lef']
    def R(self): return self['rig']

