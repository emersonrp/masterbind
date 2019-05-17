import wx
import re
from module.Module import Module

import GameData
import UI.Labels
from UI.ControlGroup import ControlGroup

class SoD(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'SoD')

    def InitKeys(self):
        self.Data = {
            'Up' : "SPACE",
            'Down' : "X",
            'Forward' : "W",
            'Back' : "S",
            'Left' : "A",
            'Right' : "D",
            'TurnLeft' : "Q",
            'TurnRight' : "E",
            'AutoRun' : "R",
            'Follow' : "TILDE",
            'DefaultMode' : '',
            'MousechordSoD' : 1,
            'AutoMouseLook' : 0,

            'SprintPower' : 'Sprint',

            'ChangeCamera' : 1,
            'CamdistBase' : 15,
            'CamdistTravelling' : 60,

            'ChangeDetail' : 1,
            'DetailBase' : 100,
            'DetailTravelling' : 50,

            'NonSoDMode' : 1,
            'ToggleSoD' : 'CTRL-M',
            'JumpMode' : "T",
            'SimpleSJCJ' : 1,

            'RunMode' : "C",
            'SSOnlyWhenMoving' : 0,
            'SSSJModeEnable' : 1,

            'FlyMode' : "F",
            'GFlyMode' : "G",

            'SelfTellOnChange' : 1,

            'TPMode' : 'SHIFT-LBUTTON',
            'TPCombo' : 'SHIFT',
            'TPReset' : 'CTRL-T',

            'TTPMode' : 'SHIFT-CTRL-LBUTTON',
            'TTPCombo' : 'SHIFT-CTRL',
            'TTPReset' : 'SHIFT-CTRL-T',

            'AutoHoverTP' : 1,
            'HideWinsDuringTP' : 1,
            'AutoGFlyTTP' : 1,

            'RunPrimary' : "Super Speed",
            'RunPrimaryNumber' : 2,
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
        }

        if self.Profile.General.Data['Archetype'] == "Peacebringer":
            self.Data['NovaNova'] = "Bright Nova"
            self.Data['DwarfDwarf'] = "White Dwarf"
            self.Data['HumanFormShield'] = self.Data.get('HumanFormShield', "Shining Shield")

        elif self.Profile.General.Data['Archetype'] == "Warshade":
            self.Data['NovaNova'] = "Dark Nova"
            self.Data['DwarfDwarf'] = "Black Dwarf"
            self.Data['HumanFormShield'] = self.Data.get('HumanFormShield', "Gravity Shield")

        self.Data['HumanMode']       = self.Data.get('HumanMode'       , "UNBOUND")
        self.Data['HumanTray']       = self.Data.get('HumanTray'       , "1")
        self.Data['HumanHumanPBind'] = self.Data.get('HumanHumanPBind' , "nop")
        self.Data['HumanNovaPBind']  = self.Data.get('HumanNovaPBind'  , "nop")
        self.Data['HumanDwarfPBind'] = self.Data.get('HumanDwarfPBind' , "nop")

        #  Temp Travel Powers
        self.Data['TempTray']       = self.Data.get('TempTray'       , "6")
        self.Data['TempTraySwitch'] = self.Data.get('TempTraySwitch' , "UNBOUND")
        self.Data['TempMode']       = self.Data.get('TempMode'       , "UNBOUND")

    def FillTab(self):

        topSizer = wx.FlexGridSizer(0,2,10,10)

        enablecb = wx.CheckBox( self, -1, "Enable Speed On Demand" )
        enablecb.SetToolTip('Check this to enable Speed On Demand Binds')

        topSizer.Add( enablecb, 0, wx.ALL, 10)
        topSizer.AddSpacer(1)

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
            'contents' : ['No SoD','Sprint','Super Speed','Jump','Fly'],
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

        for cmd in ("AutoRun","Follow","NonSoDMode"): # TODO - lost "Sprint-Only SoD Mode" b/c couldn't find the name in %$Labels
            generalSizer.AddLabeledControl({
                'value' : cmd,
                'type' : 'keybutton',
                'parent' : self,
            })
        generalSizer.AddLabeledControl({
            'value' : 'ToggleSoD',
            'type' : 'keybutton',
            'parent' : self,
        })
        #generalSizer.AddLabeledControl({
        #    'value' : 'SprintSoD',
        #    'type' : 'checkbox',
        #    'parent' : self,
        #})
        generalSizer.AddLabeledControl({
            'value' : 'ChangeCamera',
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

        # if (player has team-tp):
        teleportSizer.AddLabeledControl({
            'value' : "TTPMode",
            'type' : 'keybutton',
            'parent' : self,
        })
        teleportSizer.AddLabeledControl({
            'value' : "TTPCombo",
            'type' : 'keybutton',
            'parent' : self,
        })
        teleportSizer.AddLabeledControl({
            'value' : "TTPReset",
            'type' : 'keybutton',
            'parent' : self,
        })

            # if (player has group fly):
        teleportSizer.AddLabeledControl({
            'value' : 'AutoGFlyTTP',
            'type' : 'checkbox',
            'parent' : self,
        })
            #
        #
        rightColumn.Add(teleportSizer, 0, wx.EXPAND)

        ##### TEMP TRAVEL POWERS
        tempSizer = ControlGroup(self, 'Temp Travel Powers')
        # if (temp travel powers exist)?  Should this be "custom"?
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

        self.SetSizer(topSizer)

        self.TabTitle = "Speed On Demand"

    def makeSoDFile(self, p):
        t = p['t']

        profile = t['profile']

        bl   = t.bl(p['bl'])   if p['bl']   else ''
        bla  = t.bl(p['bla'])  if p['bla']  else ''
        blf  = t.bl(p['blf'])  if p['blf']  else ''
        blbo = t.bl(p['blbo']) if p['blbo'] else ''
        blsd = t.bl(p['blsd']) if p['blsd'] else ''

        path   = t.path(p['path'])   if p['path']   else ''
        pathr  = t.path(p['pathr'])  if p['pathr']  else ''
        pathf  = t.path(p['pathf'])  if p['pathf']  else ''
        pathbo = t.path(p['pathbo']) if p['pathbo'] else ''
        pathsd = t.path(p['pathsd']) if p['pathsd'] else ''

        mobile     = p['mobile']     or ''
        stationary = p['stationary'] or ''
        modestr    = p['modestr']    or ''
        flight     = p['flight']     or ''
        fix        = p['fix']        or ''
        turnoff    = p['turnoff']    or ''
        sssj       = p['sssj']       or ''

        SoD = profile.SoD

        # this wants to be $turnoff ||= mobile, stationary once we know what those are.  arrays?  hashes?
        turnoff = turnoff or (mobile, stationary)

        if self.Data['Default'] == modestr and t['totalkeys'] == 0:

            curfile = profile.General['ResetFile']
            sodDefaultResetKey(mobile, stationary)

            sodUpKey     (t, bl, curfile, SoD, mobile, stationary, flight,'','','', sssj)
            sodDownKey   (t, bl, curfile, SoD, mobile, stationary, flight,'','','', sssj)
            sodForwardKey(t, bl, curfile, SoD, mobile, stationary, flight,'','','', sssj)
            sodBackKey   (t, bl, curfile, SoD, mobile, stationary, flight,'','','', sssj)
            sodLeftKey   (t, bl, curfile, SoD, mobile, stationary, flight,'','','', sssj)
            sodRightKey  (t, bl, curfile, SoD, mobile, stationary, flight,'','','', sssj)

            if (modestr == "NonSoD"): makeNonSoDModeKey(profile, t,"r",  curfile,(mobile, stationary))
            if (modestr == "Base")  : makeBaseModeKey  (profile, t,"r",  curfile, turnoff, fix)
            if (modestr == "Fly")   : makeFlyModeKey   (profile, t,"bo", curfile, turnoff, fix)
            if (modestr == "GFly")  : makeGFlyModeKey  (profile, t,"gf", curfile, turnoff, fix)
            if (modestr == "Run")   : makeSpeedModeKey (profile, t,"s",  curfile, turnoff, fix)
            if (modestr == "Jump")  : makeJumpModeKey  (profile, t,"j",  curfile, turnoff, path)
            if (modestr == "Temp")  : makeTempModeKey  (profile, t,"r",  curfile, turnoff, path)
            if (modestr == "QFly")  : makeQFlyModeKey  (profile, t,"r",  curfile, turnoff, modestr)

            sodAutoRunKey(t, bla, curfile, SoD, mobile, sssj)

            sodFollowKey(t, blf, curfile, SoD, mobile)


        if (flight == "Fly") and pathbo:
            #  blast off
            curfile = profile.GetBindFile(pathbo)
            sodResetKey(curfile, profile, path, actPower_toggle(None, 1, stationary, mobile), '')

            sodUpKey     (t, blbo, curfile,SoD, mobile, stationary, flight, '', '', "bo", sssj)
            sodDownKey   (t, blbo, curfile,SoD, mobile, stationary, flight, '', '', "bo", sssj)
            sodForwardKey(t, blbo, curfile,SoD, mobile, stationary, flight, '', '', "bo", sssj)
            sodBackKey   (t, blbo, curfile,SoD, mobile, stationary, flight, '', '', "bo", sssj)
            sodLeftKey   (t, blbo, curfile,SoD, mobile, stationary, flight, '', '', "bo", sssj)
            sodRightKey  (t, blbo, curfile,SoD, mobile, stationary, flight, '', '', "bo", sssj)

            # if (modestr == "Base"): makeBaseModeKey(profile, t, "r", curfile, turnoff, fix)
            t['ini'] = '-down$$'

            if self.Data['Default'] == "Fly":
                if self.Data['NonSoD']                     : t['FlyMode'] = t['NonSoDMode']
                if self.Data['Base']                       : t['FlyMode'] = t['BaseMode']
                if t['canss']                        : t['FlyMode'] = t['RunMode']
                if t['canjmp']                       : t['FlyMode'] = t['JumpMode']
                if self.Data['Temp'] and self.Data['TempEnable'] : t['FlyMode'] = t['TempMode']
            makeFlyModeKey(profile, t, "a", curfile, turnoff, fix)

            t['ini'] = ''
            # if modestr == "GFly" : makeGFlyModeKey  (profile, t, "gbo", curfile, turnoff, fix)
            # if modestr == "Run"  : makeSpeedModeKey (profile, t, "s",   curfile, turnoff, fix)
            # if modestr == "Jump" : makeJumpModeKey  (profile, t, "j",   curfile, turnoff, path)

            sodAutoRunKey(t, bla, curfile, SoD, mobile, sssj)

            sodFollowKey(t, blf, curfile, SoD, mobile)

            # curfile = profile.GetBindFile(pathsd)

            sodResetKey(curfile, profile, path,actPower_toggle(None,1, stationary, mobile),'')

            sodUpKey     (t, blsd, curfile,SoD, mobile, stationary, flight,'','',"sd", sssj)
            sodDownKey   (t, blsd, curfile,SoD, mobile, stationary, flight,'','',"sd", sssj)
            sodForwardKey(t, blsd, curfile,SoD, mobile, stationary, flight,'','',"sd", sssj)
            sodBackKey   (t, blsd, curfile,SoD, mobile, stationary, flight,'','',"sd", sssj)
            sodLeftKey   (t, blsd, curfile,SoD, mobile, stationary, flight,'','',"sd", sssj)
            sodRightKey  (t, blsd, curfile,SoD, mobile, stationary, flight,'','',"sd", sssj)

            t['ini'] = '-down$$'
            # if (modestr == "Base") : makeBaseModeKey(profile, t, "r",   curfile, turnoff, fix)
            # if (modestr == "Fly")  : makeFlyModeKey (profile, t, "a",   curfile, turnoff, fix)
            # if (modestr == "GFly") : makeGFlyModeKey(profile, t, "gbo", curfile, turnoff, fix)
            t['ini'] = ''
            # if (modestr == "Jump") : makeJumpModeKey(profile, t,"j", curfile, turnoff, path)

            sodAutoRunKey(t, bla, curfile,SoD, mobile, sssj)
            sodFollowKey(t, blf, curfile,SoD, mobile)

        curfile = profile.GetBindFile(path)

        sodResetKey(curfile, profile, path,actPower_toggle(None,1, stationary, mobile),'')

        sodUpKey     (t, bl, curfile,SoD, mobile, stationary, flight,'','','', sssj)
        sodDownKey   (t, bl, curfile,SoD, mobile, stationary, flight,'','','', sssj)
        sodForwardKey(t, bl, curfile,SoD, mobile, stationary, flight,'','','', sssj)
        sodBackKey   (t, bl, curfile,SoD, mobile, stationary, flight,'','','', sssj)
        sodLeftKey   (t, bl, curfile,SoD, mobile, stationary, flight,'','','', sssj)
        sodRightKey  (t, bl, curfile,SoD, mobile, stationary, flight,'','','', sssj)

        if (flight == "Fly") and pathbo:
            #  Base to set down
            if (modestr == "NonSoD") : makeNonSoDModeKey(profile, t,"r", curfile,(mobile, stationary), sodSetDownFix)
            if (modestr == "Base")   : makeBaseModeKey  (profile, t,"r", curfile, turnoff, sodSetDownFix)
            # if (t['BaseMode']):
                # curfile.SetBind(t['BaseMode'],"+down$$down 1" + actPower_name(None,1, mobile) + t['detailhi'] + t['runcamdist'] + t['blsd'])
            #
            if (modestr == "Run")     : makeSpeedModeKey (profile, t,"s",  curfile, turnoff, sodSetDownFix)
            if (modestr == "Fly")     : makeFlyModeKey   (profile, t,"bo", curfile, turnoff, fix)
            if (modestr == "Jump")    : makeJumpModeKey  (profile, t,"j",  curfile, turnoff, path)
            if (modestr == "Temp")    : makeTempModeKey  (profile, t,"r",  curfile, turnoff, path)
            if (modestr == "QFly")    : makeQFlyModeKey  (profile, t,"r",  curfile, turnoff, modestr)
        else:
            if (modestr == "NonSoD")  : makeNonSoDModeKey(profile, t,"r",  curfile, (mobile, stationary))
            if (modestr == "Base")    : makeBaseModeKey  (profile, t,"r",  curfile, turnoff, fix)
            if (flight == "Jump"):
                if (modestr == "Fly") : makeFlyModeKey   (profile, t,"a",  curfile, turnoff, fix,None,1)
            else:
                if (modestr == "Fly") : makeFlyModeKey   (profile, t,"bo", curfile, turnoff, fix)
            if (modestr == "Run")     : makeSpeedModeKey (profile, t,"s",  curfile, turnoff, fix)
            if (modestr == "Jump")    : makeJumpModeKey  (profile, t,"j",  curfile, turnoff, path)
            if (modestr == "Temp")    : makeTempModeKey  (profile, t,"r",  curfile, turnoff, path)
            if (modestr == "QFly")    : makeQFlyModeKey  (profile, t,"r",  curfile, turnoff, modestr)

        sodAutoRunKey(t, bla, curfile,SoD, mobile, sssj)

        sodFollowKey(t, blf, curfile,SoD, mobile)

        # AutoRun Binds
        curfile = profile.GetBindFile(pathr)

        sodResetKey(curfile, profile, path,actPower_toggle(None,1, stationary, mobile),'')

        sodUpKey     (t, bla, curfile,SoD, mobile, stationary, flight,1,'','', sssj)
        sodDownKey   (t, bla, curfile,SoD, mobile, stationary, flight,1,'','', sssj)
        sodForwardKey(t, bla, curfile,SoD, mobile, stationary, flight, bl, '','', sssj)
        sodBackKey   (t, bla, curfile,SoD, mobile, stationary, flight, bl, '','', sssj)
        sodLeftKey   (t, bla, curfile,SoD, mobile, stationary, flight,1,'','', sssj)
        sodRightKey  (t, bla, curfile,SoD, mobile, stationary, flight,1,'','', sssj)

        if (flight == "Fly") and pathbo:
            if modestr == "NonSoD" : makeNonSoDModeKey(profile, t,"ar", curfile, (mobile, stationary), sodSetDownFix)
            if modestr == "Base"   : makeBaseModeKey  (profile, t,"gr", curfile, turnoff, sodSetDownFix)
            if modestr == "Run"    : makeSpeedModeKey (profile, t,"as", curfile, turnoff, sodSetDownFix)
        else:
            if modestr == "NonSoD" : makeNonSoDModeKey(profile, t,"ar", curfile, (mobile, stationary))
            if modestr == "Base"   : makeBaseModeKey  (profile, t,"gr", curfile, turnoff, fix)
            if modestr == "Run"    : makeSpeedModeKey (profile, t,"as", curfile, turnoff, fix)

        if modestr == "Fly"        : makeFlyModeKey   (profile, t,"af", curfile, turnoff, fix)
        if modestr == "Jump"       : makeJumpModeKey  (profile, t,"aj", curfile, turnoff, pathr)
        if modestr == "Temp"       : makeTempModeKey  (profile, t,"ar", curfile, turnoff, path)
        if modestr == "QFly"       : makeQFlyModeKey  (profile, t,"ar", curfile, turnoff, modestr)

        sodAutoRunOffKey(t, bl, curfile,SoD, mobile, stationary, flight)

        curfile.SetBind(self.Data['Follow'],'nop')

        # FollowRun Binds
        curfile = profile.GetBindFile(pathf)

        sodResetKey(curfile, profile, path, actPower_toggle(None,1, stationary, mobile),'')

        sodUpKey     (t, blf, curfile,SoD, mobile, stationary, flight,'', bl,'', sssj)
        sodDownKey   (t, blf, curfile,SoD, mobile, stationary, flight,'', bl,'', sssj)
        sodForwardKey(t, blf, curfile,SoD, mobile, stationary, flight,'', bl,'', sssj)
        sodBackKey   (t, blf, curfile,SoD, mobile, stationary, flight,'', bl,'', sssj)
        sodLeftKey   (t, blf, curfile,SoD, mobile, stationary, flight,'', bl,'', sssj)
        sodRightKey  (t, blf, curfile,SoD, mobile, stationary, flight,'', bl,'', sssj)

        if (flight == "Fly") and pathbo:
            if modestr == "NonSoD" : makeNonSoDModeKey   (profile, t,"fr", curfile, (mobile, stationary), sodSetDownFix)
            if modestr == "Base"   : makeBaseModeKey     (profile, t,"fr", curfile, turnoff, sodSetDownFix)
            if modestr == "Run"    : makeSpeedModeKey    (profile, t,"fs", curfile, turnoff, sodSetDownFix)
        else:
            if modestr == "NonSoD" : makeNonSoDModeKey   (profile, t,"fr", curfile, (mobile, stationary))
            if modestr == "Base"   : makeBaseModeKey     (profile, t,"fr", curfile, turnoff, fix)
            if modestr == "Run"    : makeSpeedModeKey    (profile, t,"fs", curfile, turnoff, fix)

        if modestr == "Fly"        : makeFlyModeKey   (profile, t,"ff", curfile, turnoff, fix)
        if modestr == "Jump"       : makeJumpModeKey  (profile, t,"fj", curfile, turnoff, pathf)
        if modestr == "Temp"       : makeTempModeKey  (profile, t,"fr", curfile, turnoff, path)
        if modestr == "QFly"       : makeQFlyModeKey  (profile, t,"fr", curfile, turnoff, modestr)

        curfile.SetBind(self.Data['AutoRun'],'nop')

        sodFollowOffKey(t, bl, curfile,SoD, mobile, stationary, flight)

    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeNonSoDModeKey(self, p, t, bl, cur, toff, fix, fb):
        key = t['NonSoDMode']
        if (not key) or key == 'UNBOUND' : return

        feedback = ''
        if p.self.Data['Feedback']:
            feedback = fb or '$$t $name, Non-SoD Mode'

        if bl == "r":
            bindload = t.bl('n')
            if fix:
                fix(p, t, key, makeNonSoDModeKey,"n", bl, cur, toff,'', feedback)
            else:
                cur.SetBind(key, t['ini'] + actPower_toggle(None,1,None, toff) + t.dirs('UDFBLR') + t['detailhi'] + t['runcamdist'] + feedback + bindload)

        elif bl == "ar":
            bindload = t.bl('an')
            if fix:
                fix(p, t, key, makeNonSoDModeKey,"n", bl, cur, toff,"a", feedback)
            else:
                cur.SetBind(key, t['ini'] + actPower_toggle(None,1,None, toff) + t['detailhi'] + t['runcamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload)

        else:
            if fix:
                fix(p, t, key, makeNonSoDModeKey,"n", bl, cur, toff,"f", feedback)
            else:
                cur.SetBind(key, t['ini'] + actPower_toggle(None,1,None, toff) + t['detailhi'] + t['runcamdist'] + '$$up 0' + feedback + t.bl('fn'))
        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeTempModeKey(self, p, t, bl, cur, toff):
        key = t['TempMode']
        if (not key) or key == "UNBOUND": return

        feedback = '$$t $name, Temp Mode' if p.self.Data['Feedback'] else ''
        trayslot = "1 " + p.self.Data['TempTray']

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
    def makeQFlyModeKey(self, p, t, bl, cur, toff, modestr):
        key = t['QFlyMode']
        if (not key) or key == "UNBOUND": return

        if modestr == "NonSoD":
            cur.SetBind(key, "powexecname Quantum Flight")
            return

        feedback = '$$t $name, QFlight Mode' if p.self.Data['Feedback'] else ''

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
    def makeBaseModeKey(self, p, t, bl, cur, toff, modestr):
        key = t['BaseMode']
        if (not key) or key == "UNBOUND": return

        feedback = (fb or '$$t $name, Sprint-SoD Mode') if p.self.Data['Feedback'] else ''

        if bl == "r":
            bindload  = t.bl()

            ton = actPower_toggle(1, 1, (t['sprint'] if t['horizkeys'] else ''), toff)

            if fix:
                fix(p, t, key, makeBaseModeKey,"r", bl, cur, toff, '', feedback)
            else:
                cur.SetBind(key, t['ini'] + ton + t.dirs('UDFBLR') + t['detailhi'] + t['runcamdist'] + feedback + bindload)


        elif bl == "ar":
            bindload  = t.bl('gr')

            if fix:
                fix(p, t, key, makeBaseModeKey,"r", bl, cur, toff,"a", feedback)
            else:
                cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['sprint'], toff) + t['detailhi'] +  t['runcamdist'] + '$$up 0' + t.dirs('DLR') + feedback + bindload)

        else:
            if fix:
                fix(p, t, key, makeBaseModeKey,"r", bl, cur, toff,"f", feedback)
            else:
                cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['sprint'], toff) + t['detailhi'] + t['runcamdist'] + '$$up 0' + fb + t.bl('fr'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeSpeedModeKey(self, p, t, bl, cur, toff, fix, fb):
        key = t['RunMode']
        feedback = (fb or '$$t $name, Superspeed Mode') if p.self.Data['Feedback'] else ''

        if t['canss']:
            if bl == 's':
                bindload = t.bl('s')
                if fix:
                    fix(p, t, key, makeSpeedModeKey,"s", bl, cur, toff,'', feedback)
                else:
                    cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['speed'], toff) + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            elif bl == "as":
                bindload = t.bl('as')
                if fix:
                    fix(p, t, key, makeSpeedModeKey,"s", bl, cur, toff,"a", feedback)
                elif not feedback:
                    cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['speed'], toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)
                else:
                    bindload  = t.bl('as')
                    bindload2 = t.bl('as','_s')
                    tgl = p.GetBindFile(bindload2)
                    cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['speed'], toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload2)
                    tgl.SetBind(key, t['ini'] + actPower_toggle(1,1, t['speed'], toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            else:
                if fix:
                    fix(p, t, key, makeSpeedModeKey,"s", bl, cur, toff,"f", feedback)
                else:
                    cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['speed'], toff) + '$$up 0' +  t['detaillo'] + t['flycamdist'] + feedback + t.bl('fs'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeJumpModeKey(self, p, t, bl, cur, toff, fbl):
        key = t['JumpMode']
        if (t['canjmp'] and not p.self.Data['JumpSimple']):

            feedback = '$$t $name, Superjump Mode' if p.self.Data['Feedback'] else ''
            tgl = p.GetBindFile(fbl)

            if bl == "j":
                if (t['horizkeys'] + t['space'] > 0):
                    a = actPower(None,1, t['jump'], toff) + '$$up 1'
                else:
                    a = actPower(None,1, t['cjmp'], toff)

                bindload = t.bl('j')
                tgl.SetBind(key, '-down' + a + t['detaillo'] + t['flycamdist'] + bindload)
                cur.SetBind(key, '+down' + feedback + BindFile.BLF(p, fbl))
            elif bl == "aj":
                bindload = t.bl('aj')
                tgl.SetBind(key, '-down' + actPower(None,1, t['jump'], toff) + '$$up 1' + t['detaillo'] + t['flycamdist'] + t.dirs('DLR') + bindload)
                cur.SetBind(key, '+down' + feedback + BindFile.BLF(p, fbl))
            else:
                tgl.SetBind(key, '-down' + actPower(None,1, t['jump'], toff) + '$$up 1' + t['detaillo'] + t['flycamdist'] + t.bl('fj'))
                cur.SetBind(key, '+down' + feedback + BindFile.BLF(p, fbl))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeFlyModeKey(self, p, t, bl, cur, toff, fix, fb, fb_on_a):
        key = t['FlyMode']
        if (not key) or key == "UNBOUND": return

        feedback = (fb or '$$t $name, Flight Mode') if p.self.Data['Feedback'] else ''

        if t['canhov'] + t['canfly'] > 0:
            if bl == "bo":
                bindload = t.bl('bo')
                if fix:
                    fix(p, t, key, makeFlyModeKey,"f", bl, cur, toff,'', feedback)
                else:
                    cur.SetBind(key,'+down$$' + actPower_toggle(1,1, t['flyx'], toff) + '$$up 1$$down 0' + t.dirs('FBLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            elif bl == "a":
                if (not fb_on_a): feedback = ''

                bindload = t.bl('a')
                ton = t['flyx'] if t['tkeys'] else t['hover']
                if fix:
                    fix(p, t, key, makeFlyModeKey,"f", bl, cur, toff,'', feedback)
                else:
                    cur.SetBind(t['FlyMode'], t['ini'] + actPower_toggle(1,1, ton , toff) + t.dirs('UDLR') + t['detaillo'] + t['flycamdist'] + feedback + bindload)

            elif bl == "af":
                bindload = t.bl('af')
                if fix:
                    fix(p, t, key, makeFlyModeKey,"f", bl, cur, toff,"a", feedback)
                else:
                    cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['flyx'], toff) + t['detaillo'] + t['flycamdist'] + t.dirs('DLR') + feedback + bindload)

            else:
                if fix:
                    fix(p, t, key, makeFlyModeKey,"f", bl, cur, toff,"f", feedback)
                else:
                    cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['flyx'], toff) + t.dirs('UDFBLR') + t['detaillo'] + t['flycamdist'] + feedback + t.bl('ff'))

        t['ini'] = ''


    # TODO -- seems like these subs could get consolidated but stab one at that was feeble
    def makeGFlyModeKey (self, p, t, bl, cur, toff, fix):
        key = t['GFlyMode']

        if t['cangfly'] > 0:
            if bl == "gbo":
                bindload = t.bl('gbo')
                if fix:
                    fix(p, t, key, makeGFlyModeKey,"gf", bl, cur, toff,'','')
                else:
                    cur.SetBind(key, t['ini'] + '$$up 1$$down 0' + actPower_toggle(None,1, t['gfly'], toff) + t.dirs('FBLR') + t['detaillo'] + t['flycamdist'] .bindload)

            elif bl == "gaf":
                bindload = t.bl('gaf')
                if fix:
                    fix(p, t, key, makeGFlyModeKey,"gf", bl, cur, toff,"a")
                else:
                    cur.SetBind(key, t['ini'] + t['detaillo'] + t['flycamdist'] + t.dirs('UDLR') + bindload)

            else:
                if fix:
                    fix(p, t, key, makeGFlyModeKey,"gf", bl, cur, toff,"f")
                else:
                    if bl == "gf":
                        cur.SetBind(key, t['ini'] + actPower_toggle(1,1, t['gfly'], toff) + t['detaillo'] + t['flycamdist'] + t.bl('gff'))
                    else:
                        cur.SetBind(key, t['ini'] + t['detaillo'] + t['flycamdist'] + t.bl('gff'))
        t['ini'] = ''


    def iupMessage(self):
            print("ZOMG SOMEBODY IMPLEMENT A WARNING DIALOG!!!\n")

    def PopulateBindFiles(self):

        ResetFile = self.profile.General.Data['ResetFile']

        # $ResetFile.SetBind(petselect['sel5'] + ' "petselect 5')
        if (self.Data['Default'] == "NonSoD"):
            if (not self.Data['NonSoD']): iupMessage("Notice","Enabling NonSoD mode, since it is set as your default mode.")
            self.Data['NonSoD'] = 1

        if (self.Data['Default'] == "Base" and not self.Data['Base']):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Sprint SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['Default'] = "NonSoD"

        if (self.Data['Default'] == "Fly" and not (self.Data['FlyHover'] or self.Data['FlyFly'])):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Flight SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['Default'] = "NonSoD"

        if (self.Data['Default'] == "Jump" and not (self.Data['JumpCJ'] or self.Data['JumpSJ'])):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Superjump SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['Default'] = "NonSoD"

        if (self.Data['Default'] == "Run" and self.Data['RunPrimaryNumber'] == 1):
            iupMessage("Notice","Enabling NonSoD mode and making it the default, since Superspeed SoD, your previous Default mode, is not enabled.")
            self.Data['NonSoD'] = 1
            self.Data['Default'] = "NonSoD"


        t = Module.SoD.Table({
            profile : profile,
            sprint : '',
            speed : '',
            hover : '',
            fly : '',
            flyx : '',
            jump : '',
            cjmp : '',
            canhov : 0,
            canfly : 0,
            canqfly : 0,
            cangfly : 0,
            cancj : 0,
            canjmp : 0,
            canss : 0,
            tphover : '',
            ttpgrpfly : '',
            on : '$$powexectoggleon ',
            # on : '$$powexecname ',
            off : '$$powexectoggleoff ',
            mlon : '',
            mloff : '',
            runcamdist : '',
            flycamdist : '',
            detailhi : '',
            detaillo : '',
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


        if (profile.General['Archetype'] == "Peacebringer"):
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

        elif (not (profile.General['Archetype'] == "Warshade")):
            if (self.Data['FlyHover'] and not self.Data['FlyFly']):
                t['canhov'] = 1
                t['hover'] = "Hover"
                t['flyx'] = "Hover"
                if (self.Data['TPTPHover']): t['tphover'] = '$$powexectoggleon Hover'

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
                if (self.Data['TPTPHover']): t['tphover'] = '$$powexectoggleon Hover'


        if ((profile.General['Archetype'] == "Peacebringer") and self.Data['FlyQFly']):
            t['canqfly'] = 1

        if (self.Data['FlyGFly']):
            t['cangfly'] = 1
            t['gfly'] = "Group Fly"
            if (self.Data['TTPTPGFly']): t['ttpgfly'] = '$$powexectoggleon Group Fly'

        if (self.Data['RunPrimaryNumber'] == 1):
            t['sprint'] = self.Data['RunSecondary']
            t['speed']  = self.Data['RunSecondary']
        else:
            t['sprint'] = self.Data['RunSecondary']
            t['speed']  = self.Data['RunPrimary']
            t['canss'] = 1

        t['unqueue'] = '$$powexecunqueue' if self.Data['Unqueue'] else ''
        if (self.Data['AutoMouseLook']):
            t['mlon']  = '$$mouselook 1'
            t['mloff'] = '$$mouselook 0'

        if (self.Data['RunUseCamdist']):
            t['runcamdist'] = '$$camdist ' + self.Data['RunCamdist']

        if (self.Data['FlyUseCamdist']):
            t['flycamdist'] = '$$camdist ' + self.Data['FlyCamdist']

        if (self.Data['Detail'] and self.Data['DetailEnable']):
            t['detailhi'] = '$$visscale ' + self.Data['DetailNormalAmt'] + '$$shadowvol 0$$ss 0'
            t['detaillo'] = '$$visscale ' + self.Data['DetailMovingAmt'] + '$$shadowvol 0$$ss 0'

        windowhide = windowshow = ''
        if self.Data['HideWinsDuringTP']:
            windowhide = '$$windowhide health$$windowhide chat$$windowhide target$$windowhide tray'
            windowshow = '$$show health$$show chat$$show target$$show tray'

        # turn = "+zoomin$$-zoomin"  # a non functioning bind used only to activate the keydown/keyup functions of +commands
        t['turn'] = "+down";  # a non functioning bind used only to activate the keydown/keyup functions of +commands

        #  temporarily set self.Data['Default'] to "NonSoD"
        # self.Data['Default'] = "Base"
        #  set up the keys to be used.
        if (self.Data['Default'] == "NonSoD"): t['NonSoDMode'] = self.Data['NonSoDMode']
        if (self.Data['Default'] == "Base"): t['BaseMode'] = self.Data['BaseMode']
        if (self.Data['Default'] == "Fly"): t['FlyMode'] = self.Data['FlyMode']
        if (self.Data['Default'] == "Jump"): t['JumpMode'] = self.Data['JumpMode']
        if (self.Data['Default'] == "Run"): t['RunMode'] = self.Data['RunMode']
    #   if (self.Data['Default'] == "GFly"): t['GFlyMode'] = self.Data['GFlyMode']
        t['TempMode'] = self.Data['TempMode']
        t['QFlyMode'] = self.Data['QFlyMode']

        for space in (0,1):
            t['space'] = space
            t['up'] = '$$up ' + space
            t['upx'] = '$$up ' + (1-space)

            for X in (0,1):
                t['X'] = X
                t['dow'] = '$$down ' + X
                t['dowx'] = '$$down ' + (1-X)

                for W in (0,1):
                    t['W'] = W
                    t['forw'] = '$$forward ' + W
                    t['forx'] = '$$forward ' + (1-W)

                    for S in (0,1):
                        t['S'] = S
                        t['bac'] = '$$backward ' + S
                        t['bacx'] = '$$backward ' + (1-S)

                        for A in (0,1):
                            t['A'] = A
                            t['lef'] = '$$left ' + A
                            t['lefx'] = '$$left ' + (1-A)

                            for D in (0,1):
                                t['D'] = D
                                t['rig'] = '$$right ' + D
                                t['rigx'] = '$$right ' + (1-D)

                                t['totalkeys'] = space+X+W+S+A+D;  # total number of keys down
                                t['horizkeys'] = W+S+A+D;          # total # of horizontal move keys.  So Sprint isn't turned on when jumping
                                t['vertkeys'] = space+X
                                t['jkeys'] = t['horizkeys']+t['space']

                                if self.Data['NonSoD'] or t['canqfly']:
                                    t[self.Data['Default'] + "Mode"] = t['NonSoDMode']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 'n',
                                        bla        : 'an',
                                        blf        : 'fn',
                                        path       : 'n',
                                        pathr      : 'an',
                                        pathf      : 'fn',
                                        mobile     : '',
                                        stationary : '',
                                        modestr    : "NonSoD",
                                    })
                                    t[self.Data['Default'] + "Mode"] = None

                                if self.Data['Base']:
                                    t[self.Data['Default'] + "Mode"] = t['BaseMode']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 'r',
                                        bla        : 'gr',
                                        blf        : 'fr',
                                        path       : 'r',
                                        pathr      : 'ar',
                                        pathf      : 'fr',
                                        mobile     : t['sprint'],
                                        stationary : '',
                                        modestr    : "Base",
                                    })
                                    t[self.Data['Default'] + "Mode"] = None

                                if t['canss']:
                                    t[self.Data['Default'] + "Mode"] = t['RunMode']
                                    if self.Data['SSSSSJModeEnable']:
                                        sssj = t['jump']
                                    if self.Data['SSMobileOnly']:
                                        makeSoDFile({
                                            t          : t,
                                            bl         : 's',
                                            bla        : 'as',
                                            blf        : 'fs',
                                            path       : 's',
                                            pathr      : 'as',
                                            pathf      : 'fs',
                                            mobile     : t['speed'],
                                            stationary : '',
                                            modestr    : "Run",
                                            sssj       : sssj,
                                        })
                                    else:
                                        makeSoDFile({
                                            t          : t,
                                            bl         : 's',
                                            bla        : 'as',
                                            blf        : 'fs',
                                            path       : 's',
                                            pathr      : 'as',
                                            pathf      : 'fs',
                                            mobile     : t['speed'],
                                            stationary : t['speed'],
                                            modestr    : "Run",
                                            sssj       : sssj,
                                        })

                                    t[self.Data['Default'] + "Mode"] = None

                                if (t['canjmp'] > 0) and (not self.Data['JumpSimple']):
                                    t[self.Data['Default'] + "Mode"] = t['JumpMode']
                                    if (t['jump'] == t['cjmp']):
                                        jturnoff = t['jumpifnocj']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 'j',
                                        bla        : 'aj',
                                        blf        : 'fj',
                                        path       : 'j',
                                        pathr      : 'aj',
                                        pathf      : 'fj',
                                        mobile     : t['jump'],
                                        stationary : t['cjmp'],
                                        modestr    : "Jump",
                                        flight     : "Jump",
                                        fix        : sodJumpFix,
                                        turnoff    : jturnoff,
                                    })
                                    t[self.Data['Default'] + "Mode"] = None

                                if (t['canhov'] + t['canfly'] > 0):
                                    t[self.Data['Default'] + "Mode"] = t['FlyMode']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 'r',
                                        bla        : 'af',
                                        blf        : 'ff',
                                        path       : 'r',
                                        pathr      : 'af',
                                        pathf      : 'ff',
                                        mobile     : t['flyx'],
                                        stationary : t['hover'],
                                        modestr    : "Fly",
                                        flight     : "Fly",
                                        pathbo     : 'bo',
                                        pathsd     : 'sd',
                                        blbo       : 'bo',
                                        blsd       : 'sd',
                                    })
                                    t[self.Data['Default'] + "Mode"] = None

                                if t['canqfly'] > 0:
                                    t[self.Data['Default'] + "Mode"] = t['QFlyMode']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 'q',
                                        bla        : 'aq',
                                        blf        : 'fq',
                                        path       : 'q',
                                        pathr      : 'aq',
                                        pathf      : 'fq',
                                        mobile     : "Quantum Flight",
                                        stationary : "Quantum Flight",
                                        modestr    : "QFly",
                                        flight     : "Fly",
                                    })
                                    t[self.Data['Default'] + "Mode"] = None

                                if t['cangfly']:
                                    t[self.Data['Default'] + "Mode"] = t['GFlyMode']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 'a',
                                        bla        : 'af',
                                        blf        : 'ff',
                                        path       : 'ga',
                                        pathr      : 'gaf',
                                        pathf      : 'gff',
                                        mobile     : t['gfly'],
                                        stationary : t['gfly'],
                                        modestr    : "GFly",
                                        flight     : "GFly",
                                        pathbo     : 'gbo',
                                        pathsd     : 'gsd',
                                        blbo       : 'gbo',
                                        blsd       : 'gsd',
                                    })
                                    t[self.Data['Default'] + "Mode"] = None

                                if (self.Data['Temp'] and self.Data['TempEnable']):
                                    trayslot = "1 " + self.Data['TempTray']
                                    t[self.Data['Default'] + "Mode"] = t['TempMode']
                                    makeSoDFile({
                                        t          : t,
                                        bl         : 't',
                                        bla        : 'at',
                                        blf        : 'ft',
                                        path       : 't',
                                        pathr      : 'at',
                                        pathf      : 'ft',
                                        mobile     : trayslot,
                                        stationary : trayslot,
                                        modestr    : "Temp",
                                        flight     : "Fly",
                                    })
                                    t[self.Data['Default'] + "Mode"] = None


        t['space'] = t['X'] = t['W'] = t['S'] = t['A'] = t['D'] = 0

        t['up']   = '$$up '       +    t['space']
        t['upx']  = '$$up '       + (1-t['space'])
        t['dow']  = '$$down '     +    t['X']
        t['dowx'] = '$$down '     + (1-t['X'])
        t['forw'] = '$$forward '  +    t['W']
        t['forx'] = '$$forward '  + (1-t['W'])
        t['bac']  = '$$backward ' +    t['S']
        t['bacx'] = '$$backward ' + (1-t['S'])
        t['lef']  = '$$left '     +    t['A']
        t['lefx'] = '$$left '     + (1-t['A'])
        t['rig']  = '$$right '    +    t['D']
        t['rigx'] = '$$right '    + (1-t['D'])

        if (self.Data['TLeft']  == "UNBOUND"): ResetFile.SetBind(self.Data['TLeft'], "+turnleft")
        if (self.Data['TRight'] == "UNBOUND"): ResetFile.SetBind(self.Data['TRight'],"+turnright")

        if self.Data['Temp'] and self.Data['TempEnable']:
            temptogglefile1 = profile.GetBindFile("temptoggle1.txt")
            temptogglefile2 = profile.GetBindFile("temptoggle2.txt")
            temptogglefile2.SetBind(self.Data['TempTraySwitch'],'-down$$gototray 1'                  + BindFile.BLF(profile, 'temptoggle1.txt'))
            temptogglefile1.SetBind(self.Data['TempTraySwitch'],'+down$$gototray ' + self.Data['TempTray'] + BindFile.BLF(profile, 'temptoggle2.txt'))
            ResetFile.      SetBind(self.Data['TempTraySwitch'],'+down$$gototray ' + self.Data['TempTray'] + BindFile.BLF(profile, 'temptoggle2.txt'))


        (dwarfTPPower, normalTPPower, teamTPPower) = ('','','')
        if (profile.General['Archetype'] == "Warshade"):
            dwarfTPPower  = "powexecname Black Dwarf Step"
            normalTPPower = "powexecname Shadow Step"
        elif (profile.General['Archetype'] == "Peacebringer"):
            dwarfTPPower = "powexecname White Dwarf Step"
        else:
            normalTPPower = "powexecname Teleport"
            teamTPPower   = "powexecname Team Teleport"

        (dwarfpbind, novapbind, humanpbind, humanBindKey) = ('','','','')
        if (self.Data['Human'] and self.Data['HumanEnable']):
            humanBindKey = self.Data['HumanMode']
            humanpbind = cbPBindToString(self.Data['HumanHumanPBind'], profile)
            novapbind  = cbPBindToString(self.Data['HumanNovaPBind'],  profile)
            dwarfpbind = cbPBindToString(self.Data['HumanDwarfPBind'], profile)

        if ((profile.General['Archetype'] == "Peacebringer") or (profile.General['Archetype'] == "Warshade")):
            if (humanBindKey):
                ResetFile.SetBind(humanBindKey, humanpbind)



        #  kheldian form support
        #  create the Nova and Dwarf form support files if enabled.
        Nova  = self.Data['Nova']
        Dwarf = self.Data['Dwarf']

        fullstop = '$$up 0$$down 0$$forward 0$$backward 0$$left 0$$right 0'

        if Nova['Enable']:
            ResetFile.SetBind(Nova['Mode'],f"t $name, Changing to {Nova['Nova']} Form{fullstop}{t['on']}{Nova['Nova']}$$gototray {Nova['Tray']}" + BindFile.BLF(profile, 'nova.txt'))

            novafile = profile.GetBindFile("nova.txt")

            if Dwarf['Enable']:
                novafile.SetBind(Dwarf['Mode'],f"t $name, Changing to {Dwarf['Dwarf']} Form{fullstop}{t['off']}{Nova['Nova']}{t['on']}{Dwarf['Dwarf']}$$gototray {Dwarf['Tray']}" + BindFile.BLF(profile, 'dwarf.txt'))

            humanBindKey = humanBindKey or Nova['Mode']

            humpower = '$$powexectoggleon ' if (self.Data['UseHumanFormPower'] + self.Data['HumanFormShield']) else ''

            novafile.SetBind(humanBindKey,"t \$name, Changing to Human Form, SoD Mode{fullstop}$$powexectoggleoff {Nova['Nova']} {humpower}$$gototray 1" + BindFile.BLF(profile, 'reset.txt'))

            if humanBindKey == Nova['Mode']: humanBindKey = None

            if novapbind: novafile.SetBind(Nova['Mode'], novapbind)

            if t['canqfly']: makeQFlyModeKey(profile, t,"r", novafile, Nova['Nova'],"Nova")

            novafile.SetBind(self.Data['Forward'],"+forward")
            novafile.SetBind(self.Data['Left'],"+left")
            novafile.SetBind(self.Data['Right'],"+right")
            novafile.SetBind(self.Data['Back'],"+backward")
            novafile.SetBind(self.Data['Up'],"+up")
            novafile.SetBind(self.Data['Down'],"+down")
            novafile.SetBind(self.Data['AutoRun'],"++forward")
            novafile.SetBind(self.Data['FlyMode'],'nop')
            if (self.Data['FlyMode'] != self.Data['RunMode']):
                novafile.SetBind(self.Data['RunMode'],'nop')
            if (self.Data['MouseChord']):
                novafile.SetBind('mousechord "' + "+down$$+forward")

            if (self.Data['TP'] and self.Data['TPEnable']):
                novafile.SetBind(self.Data['TPComboKey'],'nop')
                novafile.SetBind(self.Data['TPBindKey'],'nop')
                novafile.SetBind(self.Data['TPResetKey'],'nop')

            novafile.SetBind(self.Data['Follow'],"follow")
            # novafile.SetBind(self.Data['ToggleKey'],'t $name, Changing to Human Form, Normal Mode$$up 0$$down 0$$forward 0$$backward 0$$left 0$$right 0$$powexectoggleoff ' + Nova['Nova'] + '$$gototray 1' + BindFile.BLF(profile, 'reset.txt'))


        if Dwarf['Enable']:
            ResetFile.SetBind(Dwarf['Mode'],f"t $name, Changing to {Dwarf['Dwarf']} Form{fullstop}$$powexectoggleon {Dwarf['Dwarf']}$$gototray {Dwarf['Tray']}" + BindFile.BLF(profile, 'dwarf.txt'))
            dwrffile = profile.GetBindFile("dwarf.txt")
            if Nova['Enable']:
                dwrffile.SetBind(Nova['Mode'],f"t \$name, Changing to {Nova['Nova']} Form{fullstop}$$powexectoggleoff {Dwarf['Dwarf']}$$powexectoggleon {Nova['Nova']}$$gototray {Nova['Tray']}" + BindFile.BLF(profile, 'nova.txt'))


            humanBindKey = humanBindKey or Dwarf['Mode']
            humpower = '$$powexectoggleon ' + self.Data['HumanFormShield'] if self.Data['UseHumanFormPower'] else ''

            dwrffile.SetBind(humanBindKey,f"t \$name, Changing to Human Form, SoD Mode{fullstop}$$powexectoggleoff {Dwarf['Dwarf']}{humpower}$$gototray 1" + BindFile.BLF(profile, 'reset.txt'))

            if dwarfpbind:   dwrffile.SetBind(Dwarf['Mode'], dwarfpbind)
            if t['canqfly']: makeQFlyModeKey(profile, t,"r", dwrffile, Dwarf['Dwarf'],"Dwarf")

            dwrffile.SetBind(self.Data['Forward'],"+forward")
            dwrffile.SetBind(self.Data['Left'],"+left")
            dwrffile.SetBind(self.Data['Right'],"+right")
            dwrffile.SetBind(self.Data['Back'],"+backward")
            dwrffile.SetBind(self.Data['Up'],"+up")
            dwrffile.SetBind(self.Data['Down'],"+down")
            dwrffile.SetBind(self.Data['AutoRun'],"++forward")
            dwrffile.SetBind(self.Data['FlyMode'],'nop')
            dwrffile.SetBind(self.Data['Follow'],"follow")
            if (self.Data['FlyMode'] != self.Data['RunMode']):
                dwrffile.SetBind(self.Data['RunMode'],'nop')
            if (self.Data['MouseChord']):
                dwrffile.SetBind('mousechord "' + "+down$$+forward")

            if self.Data['TP'] and self.Data['TPEnable']:
                dwrffile.SetBind(self.Data['TPComboKey'],'+down$$' + dwarfTPPower + t['detaillo'] + t['flycamdist'] + windowhide + BindFile.BLF(profile, 'dtp','tp_on1.txt'))
                dwrffile.SetBind(self.Data['TPBindKey'],'nop')
                dwrffile.SetBind(self.Data['TPResetKey'],substr(t['detailhi'],2) + t['runcamdist'] + windowshow + BindFile.BLF(profile, 'dtp','tp_off.txt'))
                #  Create tp_off file
                tp_off = profile.GetBindFile("dtp","tp_off.txt")
                tp_off.SetBind(self.Data['TPComboKey'],'+down$$' + dwarfTPPower + t['detaillo'] + t['flycamdist'] + windowhide + BindFile.BLF(profile, 'dtp','tp_on1.txt'))
                tp_off.SetBind(self.Data['TPBindKey'],'nop')

                tp_on1 = profile.GetBindFile("dtp","tp_on1.txt")
                tp_on1.SetBind(self.Data['TPComboKey'],'-down$$powexecunqueue' + t['detailhi'] + t['runcamdist'] + windowshow + BindFile.BLF(profile, 'dtp','tp_off.txt'))
                tp_on1.SetBind(self.Data['TPBindKey'],'+down' + BindFile.BLF(profile, 'dtp','tp_on2.txt'))

                tp_on2 = profile.GetBindFile("dtp","tp_on2.txt")
                tp_on2.SetBind(self.Data['TPBindKey'],'-down$$' + dwarfTPPower + BindFile.BLF(profile, 'dtp','tp_on1.txt'))

            # dwrffile.SetBind(self.Data['ToggleKey'],f"t \$name, Changing to Human Form, Normal Mode{fullstop}$$powexectoggleoff {Dwarf['Dwarf']}$$gototray 1" + BindFile.BLF(profile, 'reset.txt'))


        if (self.Data['JumpSimple']):
            if (self.Data['JumpCJ'] and self.Data['JumpSJ']):
                ResetFile.SetBind(self.Data['JumpMode'],'powexecname Super Jump$$powexecname Combat Jumping')
            elif (self.Data['JumpSJ']):
                ResetFile.SetBind(self.Data['JumpMode'],'powexecname Super Jump')
            elif (self.Data['JumpCJ']):
                ResetFile.SetBind(self.Data['JumpMode'],'powexecname Combat Jumping')

        if (self.Data['TP'] and self.Data['TPEnable'] and not normalTPPower):
            ResetFile.SetBind(self.Data['TPComboKey'],'nop')
            ResetFile.SetBind(self.Data['TPBindKey'],'nop')
            ResetFile.SetBind(self.Data['TPResetKey'],'nop')

        if (self.Data['TP'] and self.Data['TPEnable'] and not (profile.General['Archetype'] == "Peacebringer") and normalTPPower):
            tphovermodeswitch = ''
            if not t['tphover']:
                # TODO hmm can't get this from .KeyState directly?
                tphovermodeswitch = t.bl('r') + "000000.txt"
                #($tphovermodeswitch = t.bl('r')) =~ s/\d\d\d\d\d\d/000000/

            ResetFile.SetBind(self.Data['TPComboKey'],'+down$$' + normalTPPower + t['detaillo'] + t['flycamdist'] + windowhide + BindFile.BLF(profile, 'tp','tp_on1.txt'))
            ResetFile.SetBind(self.Data['TPBindKey'],'nop')
            ResetFile.SetBind(self.Data['TPResetKey'],substr(t['detailhi'],2) + t['runcamdist'] + windowshow + BindFile.BLF(profile, 'tp','tp_off.txt') + tphovermodeswitch)
            #  Create tp_off file
            tp_off = profile.GetBindFile("tp","tp_off.txt")
            tp_off.SetBind(self.Data['TPComboKey'],'+down$$' + normalTPPower + t['detaillo'] + t['flycamdist'] + windowhide + BindFile.BLF(profile, 'tp','tp_on1.txt'))
            tp_off.SetBind(self.Data['TPBindKey'],'nop')

            tp_on1 = profile.GetBindFile("tp","tp_on1.txt")
            zoomin = '' if t['tphover'] else (t['detailhi'] + t['runcamdist'])
            tp_on1.SetBind(self.Data['TPComboKey'],'-down$$powexecunqueue' + zoomin + windowshow + BindFile.BLF(profile, 'tp','tp_off.txt') + tphovermodeswitch)
            tp_on1.SetBind(self.Data['TPBindKey'],'+down' + t['tphover'] + BindFile.BLF(profile, 'tp','tp_on2.txt'))

            tp_on2 = profile.GetBindFile("tp","tp_on2.txt")
            tp_on2.SetBind(self.Data['TPBindKey'],'-down$$' + normalTPPower + BindFile.BLF(profile, 'tp','tp_on1.txt'))

        if (self.Data['TTP'] and self.Data['TTPEnable'] and not (profile.General['Archetype'] == "Peacebringer") and teamTPPower):
            tphovermodeswitch = ''
            ResetFile.SetBind(self.Data['TTPComboKey'],'+down$$' + teamTPPower + t['detaillo'] + t['flycamdist'] + windowhide + BindFile.BLF(profile, 'ttp','ttp_on1.txt'))
            ResetFile.SetBind(self.Data['TTPBindKey'],'nop')
            # TODO does this substr dtrt?
            ResetFile.SetBind(self.Data['TTPResetKey'],substr(t['detailhi'],2) + t['runcamdist'] + windowshow + BindFile.BLF(profile, 'ttp','ttp_off') + tphovermodeswitch)
            #  Create tp_off file
            ttp_off = profile.GetBindFile("ttp","ttp_off.txt")
            ttp_off.SetBind(self.Data['TTPComboKey'],'+down$$' + teamTPPower + t['detaillo'] + t['flycamdist'] + windowhide + BindFile.BLF(profile, 'ttp','ttp_on1.txt'))
            ttp_off.SetBind(self.Data['TTPBindKey'],'nop')

            ttp_on1 = profile.GetBindFile("ttp","ttp_on1.txt")
            ttp_on1.SetBind(self.Data['TTPComboKey'],'-down$$powexecunqueue' + t['detailhi'] + t['runcamdist'] + windowshow + BindFile.BLF(profile, 'ttp','ttp_off') + tphovermodeswitch)
            ttp_on1.SetBind(self.Data['TTPBindKey'],'+down' + BindFile.BLF(profile, 'ttp','ttp_on2.txt'))

            ttp_on2 = profile.GetBindFile("ttp","ttp_on2.txt")
            ttp_on2.SetBind(self.Data['TTPBindKey'],'-down$$' + teamTPPower + BindFile.BLF(profile, 'ttp','ttp_on1.txt'))


    def sodResetKey(self, curfile, p, path, turnoff, moddir):
        re.sub(r'\d\d\d\d\d\d', '000000', path) # ick ick ick

        (u, d) = (0, 0)
        if (moddir == 'up')  : u = 1
        if (moddir == 'down'): d = 1
        curfile.SetBind(p.General['Reset Key'],
                'up ' + u + '$$down ' + d + '$$forward 0$$backward 0$$left 0$$right 0' .
                turnoff + '$$t $name, SoD Binds Reset' + BindFile.BaseReset(p) + BindFile.BLF(p, path))


    def sodDefaultResetKey(self, mobile, stationary):
        pass
        # TODO -- decide where to keep 'resetstring' and make this def update it.
        #cbAddReset('up 0$$down 0$$forward 0$$backward 0$$left 0$$right 0'.actPower_name(None,1, stationary, mobile) + '$$t $name, SoD Binds Reset')



    # TODO TODO TODO -- the s/\d\d\d\d\d\d/$newbits/ scheme in the following six subs is a vile evil (live veil ilve vlie) hack.
    def sodUpKey(self, t, bl, curfile, SoD, mobile, stationary, flight, autorun, followbl, bo, sssj):

        (upx, dow, forw, bac, lef, rig) = (t['upx'], t.D, t.F, t.B, t.L, t.R)

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
            toggle = actPower_name(None,1, toggleon, toggleoff, toggleoff2)

        newbits = t.KeyState({toggle : 'space'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['space'] == 1) else '+down'

        if followbl:
            move = ''
            if (t['space'] != 1):
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = upx + dow + forw + bac + lef + rig

            curfile.SetBind(self.Data['Up'], ini + move + bl)
        elif (not autorun):
            curfile.SetBind(self.Data['Up'], ini + upx + dow + forw + bac + lef + rig + ml + toggle + bl)
        else:
            if (not sssj):
                toggle = '' #  returns the following line to the way it was before sssj
            curfile.SetBind(self.Data['Up'], ini + upx + dow + '$$backward 0' + lef + rig + toggle + t['mlon'] + bl)

    def sodDownKey(self, t, bl, curfile, SoD, mobile, stationary, flight, autorun, followbl, bo, sssj):

        (up, dowx, forw, bac, lef, rig) = (t.U, t['dowx'], t.F, t.B, t.L, t.R)

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
            toggle = actPower_name(None,1, toggleon, toggleoff)

        newbits = t.KeyState({toggle : 'X'})
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

    def sodForwardKey(self, t, bl, curfile,SoD, mobile, stationary, flight, autorunbl, followbl, bo, sssj):

        (up, dow, forx, bac, lef, rig) = (t.U, t.D, t['forx'], t.B, t.L, t.R)
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
            toggle = actPower_name(None,1, toggleon, toggleoff)


        newbits = t.KeyState({toggle : 'W'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['W'] == 1) else '+down'

        if (followbl):
            move
            if (t['W'] == 1):
                move = ini
            else:
                bl = followbl
                re.sub(r'\d\d\d\d\d\d', newbits, bl)
                move = ini + up + dow + forx + bac + lef + rig

            curfile.SetBind(self.Data['Forward'], move + bl)
            if (self.Data['MouseChord']):
                if (t['W'] == 1): move = ini + up + dow + forx + bac + rig + lef
                curfile.SetBind('mousechord', move + bl)

        elif (not autorunbl):
            curfile.SetBind(self.Data['Forward'], ini + up + dow + forx + bac + lef + rig + ml + toggle + bl)
            if (self.Data['MouseChord']):
                curfile.SetBind('mousechord', ini + up + dow + forx + bac + rig + lef + ml + toggle + bl)

        else:
            if (t['W'] == 1):
                bl = autorunbl
                re.sub('\d\d\d\d\d\d', newbits, bl)

            curfile.SetBind(self.Data['Forward'], ini + up + dow + '$$forward 1$$backward 0' + lef + rig + t['mlon'] + bl)
            if (self.Data['MouseChord']):
                curfile.SetBind('mousechord', ini + up + dow + '$$forward 1$$backward 0' + rig + lef + t['mlon'] + bl)




    def sodBackKey(self, t, bl, curfile,SoD, mobile, stationary, flight, autorunbl, followbl, bo, sssj):
        (up, dow, forw, bacx, lef, rig) = (t.U, t.D, t.F, t['bacx'], t.L, t.R)

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
            toggle = actPower_name(None,1, toggleon, toggleoff)


        newbits = t.KeyState({toggle : 'S'})
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



    def sodLeftKey (self, t, bl, curfile,SoD, mobile, stationary, flight, autorun, followbl, bo, sssj):

        (up, dow, forw, bac, lefx, rig) = (t.U, t.D, t.F, t.B, t['lefx'], t.R)

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
            toggle = actPower_name(None,1, toggleon, toggleoff)


        newbits = t.KeyState({toggle : 'A'})
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



    def sodRightKey(self, t, bl, curfile,SoD, mobile, stationary, flight, autorun, followbl, bo, sssj):
        (up, dow, forw, bac, lef, rigx) = (t.U, t.D, t.F, t.B, t.L, t['rigx'])

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
            toggle = actPower_name(None,1, toggleon, toggleoff)

        newbits = t.KeyState({toggle : 'D'})
        re.sub(r'\d\d\d\d\d\d', newbits, bl)

        ini = '-down' if (t['D'] == 1) else '+down'

        if (followbl):
            move
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



    def sodAutoRunKey(self, t, bl, curfile,SoD, mobile, sssj):
        if (sssj and t['space'] == 1):
            curfile.SetBind(self.Data['AutoRun'],'forward 1$$backward 0' + t.dirs('UDLR') + t['mlon'] + actPower_name(None,1, sssj, mobile) + bl)
        else:
            curfile.SetBind(self.Data['AutoRun'],'forward 1$$backward 0' + t.dirs('UDLR') + t['mlon'] + actPower_name(None,1, mobile) + bl)

    def sodAutoRunOffKey(self, t, bl, curfile,SoD, mobile, stationary, flight, sssj):
        if (not flight and not sssj):
            if (t['horizkeys'] > 0):
                toggleon = t['mlon'] + actPower_name(None,1, mobile)
            else:
                toggleon = t['mloff'] + actPower_name(None,1, stationary, mobile)

        elif (sssj):
            if (t['horizkeys'] > 0 or t['space'] == 1):
                toggleon = t['mlon'] + actPower_name(None,1, mobile, toggleoff)
            else:
                toggleon = t['mloff'] + actPower_name(None,1, stationary, mobile, toggleoff)

        else:
            if (t['totalkeys'] > 0):
                toggleon = t['mlon'] + actPower_name(None,1, mobile)
            else:
                toggleon = t['mloff'] + actPower_name(None,1, stationary, mobile)


        bindload = bl + t.KeyState + '.txt'
        curfile.SetBind(self.Data['AutoRun'], t.dirs('UDFBLR') + toggleon + bindload)


    def sodFollowKey(self, t, bl, curfile,SoD, mobile):
        curfile.SetBind(self.Data['Follow'],'follow' + actPower_name(None,1, mobile) + bl + t.KeyState + '.txt')


    def sodFollowOffKey(self, t, bl, curfile,SoD, mobile, stationary, flight):
        if (not flight):
            if (t['horizkeys'] == 0):
                if (stationary == mobile):
                    toggle = actPower_name(None,1, stationary, mobile)
                else:
                    toggle = actPower_name(None,1, stationary)


        else:
            if (t['totalkeys'] == 0):
                if (stationary == mobile):
                    toggle = actPower_name(None,1, stationary, mobile)
                else:
                    toggle = actPower_name(None,1, stationary)



        curfile.SetBind(self.Data['Follow'],"follow" + toggle + t.U + t['dow'] + t.F + t.B + t.L + t.R + bl + t.KeyState + '.txt')


    def bindisused(self):
        return profile.self.Data['Enable']

    def findconflicts(self):
        Utility.CheckConflict(self.Data,"Up","Up Key")
        Utility.CheckConflict(self.Data,"Down","Down Key")
        Utility.CheckConflict(self.Data,"Forward","Forward Key")
        Utility.CheckConflict(self.Data,"Back","Back Key")
        Utility.CheckConflict(self.Data,"Left","Strafe Left Key")
        Utility.CheckConflict(self.Data,"Right","Strafe Right Key")
        Utility.CheckConflict(self.Data,"TLeft","Turn Left Key")
        Utility.CheckConflict(self.Data,"TRight","Turn Right Key")
        Utility.CheckConflict(self.Data,"AutoRun","AutoRun Key")
        Utility.CheckConflict(self.Data,"Follow","Follow Key")

        if (self.Data['NonSoD'])                                                            : Utility.CheckConflict(SoD,"NonSoDMode","NonSoD Key")
        if (self.Data['Base'])                                                              : Utility.CheckConflict(SoD,"BaseMode","Sprint Mode Key")
        if (self.Data['SSSS'])                                                              : Utility.CheckConflict(SoD,"RunMode","Speed Mode Key")
        if (self.Data['JumpCJ'] or self.Data['JumpSJ'])                                           : Utility.CheckConflict(SoD,"JumpMode","Jump Mode Key")
        if (self.Data['FlyHover'] or self.Data['FlyFly'])                                         : Utility.CheckConflict(SoD,"FlyMode","Fly Mode Key")
        if (self.Data['FlyQFly'] and (self.profile.General['Archetype'] == "Peacebringer")) : Utility.CheckConflict(SoD,"QFlyMode","Q.Fly Mode Key")

        if (self.Data['TP'] and self.Data['TPEnable']):
            Utility.CheckConflict(self.Data['TP'],"ComboKey","TP ComboKey")
            Utility.CheckConflict(self.Data['TP'],"ResetKey","TP ResetKey")

            TPQuestion = "Teleport Bind"
            if (profile.General['Archetype'] == "Peacebringer"):
                TPQuestion = "Dwarf Step Bind"
            elif (profile.General['Archetype'] == "Warshade"):
                TPQuestion = "Shd/Dwf Step Bind"

            Utility.CheckConflict(self.Data['TP'],"BindKey", TPQuestion)

        if (self.Data['FlyGFly']): Utility.CheckConflict(SoD,"GFlyMode","Group Fly Key")
        if (self.Data['TTP'] and self.Data['TTPEnable']):
            Utility.CheckConflict(self.Data['TTP'],"ComboKey","TTP ComboKey")
            Utility.CheckConflict(self.Data['TTP'],"ResetKey","TTP ResetKey")
            Utility.CheckConflict(self.Data['TTP'],"BindKey","Team TP Bind")

        if (self.Data['Temp'] and self.Data['TempEnable']):
            Utility.CheckConflict(SoD,"TempMode","Temp Mode Key")
            Utility.CheckConflict(self.Data['Temp'],"TraySwitch","Tray Toggle Key")


        if ((profile.General['Archetype'] == "Peacebringer") or (profile.General['Archetype'] == "Warshade")):
            if (self.Data['Nova']  and self.Data['NovaEnable']): Utility.CheckConflict(self.Data['Nova'], "Mode","Nova Form Bind")
            if (self.Data['Dwarf'] and self.Data['DwarfEnable']): Utility.CheckConflict(self.Data['Dwarf'],"Mode","Dwarf Form Bind")

    #  toggleon variation
    def actPower_toggle(self, start, unq, on, *args):
        (s, traytest) = ('','')
        if isinstance(on, dict):
            #  deal with power slot stuff..
            traytest = on['trayslot']

        offpower = {}
        for v in (args):
            if isinstance(v, list):
                for pair in v:
                    j, w = pair
                    if (w and w != 'on' and not offpower[w]):
                        if isinstance(w, dict):
                            if (w['trayslot'] == traytest):
                                s = s + '$$powexectray ' + w['trayslot']
                                unq = 1
                        else:
                            offpower['w'] = 1
                            s = s + '$$powexectoggleoff ' + w

                if (v['trayslot'] and v['trayslot'] == traytest):
                    s = s + '$$powexectray ' + v['trayslot']
                    unq = 1
            else:
                if (v and (v != 'on') and not offpower[v]):
                    offpower[v] = 1
                    s = s + '$$powexectoggleoff ' + v

        if (unq and s):
            s = s + '$$powexecunqueue'

        # if start then s = string.sub(s,3,string.len(s)) end
        if (on):
            if isinstance(on, dict):
                #  deal with power slot stuff..
                s = s + '$$powexectray '.on['trayslot'] + '$$powexectray ' + on['trayslot']
            else:
                s = s + '$$powexectoggleon ' + on
        return s


    def actPower_name(self, start, unq, on, *args):
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


        if (start): s = substr(s, 2)
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

        if start: s = substr(s, 2)
        return s


    # local actPower = actPower_name
    # # local actPower = actPower_toggle
    def sodJumpFix(self, t, key, makeModeKey, suffix, bl, curfile, turnoff, autofollowmode, feedback):

        filename = t.path("${autofollowmode}j", suffix)
        tglfile = self.Profile.GetBindFile(filename)
        t['ini'] = '-down$$'
        makeModeKey(self.Profile, t, bl, tglfile, turnoff,None,1)
        curfile.SetBind(key,"+down" + feedback + actPower_name(None,1, t['cjmp']) + BindFile.BLF(self.Profile, filename))


    def sodSetDownFix (self, t, key, makeModeKey, suffix, bl, curfile, turnoff, autofollowmode, feedback):
        pathsuffix = 'f' if autofollowmode else 'a'
        filename = t.path("autofollowmode$pathsuffix", suffix)
        tglfile = self.Profile.GetBindFile(filename)
        t['ini'] = '-down$$'
        makeModeKey(self.Profile, t, bl, tglfile, turnoff,None,1)
        curfile.SetBind(key,'+down' + feedback + BindFile.BLF(self.Profile, filename))

    UI.Labels.Add( {
        'Up' : 'Up',
        'Down' : 'Down',
        'Forward' : 'Forward',
        'Back' : 'Back',
        'Left' : 'Strafe Left',
        'Right' : 'Strafe Right',
        'TurnLeft' : 'Turn Left',
        'TurnRight' : 'Turn Right',
        'AutoRun' : 'Auto Run',
        'Follow' : 'Follow Target',

        'DefaultMode' : 'Default SoD Mode',
        'MousechordSoD' : 'Mousechord is SoD Forward',
        'AutoMouseLook' : 'Automatically Mouselook when moving',

        'SprintPower' : 'Power to use for Sprint',

        'ChangeCamera' : 'Change camera distance when moving',
        'CamdistBase' : 'Base Camera Distance',
        'CamdistTravelling' : 'Travelling Camera Distance',

        'ChangeDetail' : 'Change graphics detail level when moving',
        'DetailBase' : 'Base Detail Level',
        'DetailTravelling' : 'Travelling Detail Level',

        'NonSoDMode' : 'Non-SoD Mode',
        'ToggleSoD' : 'SoD Mode Toggle',
        'JumpMode' : 'Toggle Jump Mode',
        'SimpleSJCJ' : 'Simple Combat Jumping / Super Jump Toggle',

        'RunMode' : 'Toggle Super Speed Mode',
        'SSOnlyWhenMoving' : 'SuperSpeed only when moving',
        'SSSJModeEnable' : 'Enable Super Speed / Super Jump Mode',

        'FlyMode' : 'Toggle Fly Mode',
        'GFlyMode' : 'Toggle Group Fly Mode',

        'SelfTellOnChange' : 'Self-/tell when changing mode',

        'TPMode'  : 'Teleport Bind',
        'TPCombo' : 'Teleport Combo Key',
        'TPReset' : 'Teleport Reset Key',
        'HideWinsDuringTP' : 'Hide Windows when Teleporting',
        'AutoHoverTP' : 'Automatically use Hover when Teleporting',

        'TTPMode'  : 'Team Teleport Bind',
        'TTPCombo' : 'Team Teleport Combo Key',
        'TTPReset' : 'Team Teleport Reset Key',
        'AutoGFlyTTP' : 'Automatically use Group Fly when Team Teleporting',

        'TempMode' : 'Toggle Temp Mode',
        'TempTray' : 'Temporary Travel Power Tray',

        'NovaMode' : 'Toggle Nova Form',
        'NovaTray' : 'Nova Travel Power Tray',
        'DwarfMode' : 'Toggle Dwarf Form',
        'DwarfTray' : 'Dwarf Travel Power Tray',
        'HumanMode' : 'Human Form',
        'HumanTray' : 'Human Travel Power Tray',

        'SprintSoD' : 'Enable Sprint SoD',
    })

class SoD_Table:

    dirnames = { 'U' : 'up', 'D' : 'dow', 'F' : 'forw', 'B' : 'bac', 'L' : 'lef', 'R' : 'rig' }

    def KeyState(self, t, p):
        for key in ('space','X','W','S','A','D'):
            ret = ret + (not t[key]) if (key == p['toggle']) else t[key]
        return ret

    # These next two subs are terrible.  This stuff should all be squirreled away in BindFile.

    # This will return "$bindloadfilesilent C:\path\CODE\CODE1010101<suffix>.txt"
    def bl(self, code, suffix = ''):
        p = self['profile']
        return BindFile.BLF(p, code.upper(), code.upper() + self.KeyState + suffix + '.txt')

    # This will return "CODE\CODE1010101<suffix>.txt"
    def path(self, code, suffix = ''):
        # TODO TODO TODO XXX File Spec catpath what is the actual plan here?
        return File.Spec.catpath(None, code.upper(), code.upper() + self.KeyState + suffix + '.txt')

    def dirs(self, dirs):
        for dir in dirs.split(''):
            ret = ret + self[ dirnames[dir] ]
        return ret

    def U(self): return self['up']
    def D(self): return self['dow']
    def F(self): return self['forw']
    def B(self): return self['bac']
    def L(self): return self['lef']
    def R(self): return self['rig']

