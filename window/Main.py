#!/usr/bin/env python3

import wx, wx.adv
import os, sys

from pathlib import Path
from Profile import Profile

###################
# Main Window Class
###################
class Main(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)

        self.about_info     = None

        self.SetBackgroundColour(wx.WHITE)

        h = 600
        w = 800
        #if prefs.get('save_window_size'):
        #    if prefs.get('window_width'):  w = int(prefs.get('window_width'))
        #    if prefs.get('window_height'): h = int(prefs.get('window_height'))
        self.SetSize((w, h))

        # "Profile" (File) menu
        ProfMenu = wx.Menu()

        self.Prof_new  = ProfMenu.Append(-1, "New Profile...", "Create a new profile")
        self.Prof_load = ProfMenu.Append(-1, "Load Profile...", "Load an existing profile")
        self.Prof_save = ProfMenu.Append(-1, "Save Profile", "Save the current profile")
        ProfMenu.AppendSeparator()
        self.Prof_prefs = ProfMenu.Append(-1, "Preferences...", "Edit Preferences")
        self.Prof_exit  = ProfMenu.Append(wx.ID_EXIT)

        self.Prof_new.Enable(0)
        self.Prof_load.Enable(0)
        self.Prof_save.Enable(0)
        self.Prof_prefs.Enable(0)

        # "Help" Menu
        HelpMenu = wx.Menu()

        self.Help_manual  = HelpMenu.Append(-1, "Manual","User's Manual")
        self.Help_faq     = HelpMenu.Append(-1, "FAQ","Frequently Asked Questions")
        self.Help_about   = HelpMenu.Append(wx.ID_ABOUT)

        self.Help_manual.Enable(0)
        self.Help_faq.Enable(0)

        # cram the separate menus into a menubar
        MenuBar = wx.MenuBar()
        MenuBar.Append(ProfMenu, 'Profile')
        MenuBar.Append(HelpMenu, 'Help')

        # glue the menubar into the main window
        self.SetMenuBar(MenuBar)

        # MENUBAR EVENTS
        self.Bind(wx.EVT_MENU, self.newProfile, self.Prof_new)
        self.Bind(wx.EVT_MENU, self.loadProfile, self.Prof_load)
        self.Bind(wx.EVT_MENU, self.saveProfile, self.Prof_save)
        self.Bind(wx.EVT_MENU, self.prefsWindow, self.Prof_prefs)
        self.Bind(wx.EVT_MENU, self.exitApplication, self.Prof_exit)

        self.Bind(wx.EVT_MENU, no_op, self.Help_manual)
        self.Bind(wx.EVT_MENU, no_op, self.Help_faq)
        self.Bind(wx.EVT_MENU, self.showAboutBox, self.Help_about)

        AppIcon = wx.Icon()
        AppIcon.LoadFile('MasterBind.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(AppIcon)

        # TODO - read in the config for the window (size, location, etc)
        # and apply it before .Show()

# TODO TODO TODO -- remove this once we actually start making and saving profiles
        profile = Profile(self)
# TODO TODO TODO

        writeBindsButton = wx.Button( self, label = 'Write Binds!' )
        writeBindsButton.Bind(wx.EVT_BUTTON, profile.WriteBindFiles)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(profile,  1, wx.EXPAND|wx.ALL, 3)
        sizer.Add(writeBindsButton, 0, wx.ALIGN_RIGHT|wx.ALL, 5)

        self.SetSizerAndFit(sizer)

    def newProfile(self, evt):
        pass

    def loadProfile(self, evt):
        pass

    def saveProfile(self, evt):
        pass

    def prefsWindow(self, evt):
        pass

    def exitApplication(self, evt):
        # TODO - prompt for save if profile is dirty.
        self.Close(1)

    def showAboutBox(self, evt):
        if self.about_info is None:
            info = wx.adv.AboutDialogInfo()
            info.AddDeveloper('R Pickett (emerson@hayseed.net)')
            info.AddDeveloper('\nbased on CityBinder, (c) 2005-2017 Jeff Sheets')
            info.AddDeveloper('\nspeed-on-demand binds originally created by Gnarley')
            info.AddDeveloper('\nadvanced teleport binds by DrLetharga')
            info.SetDescription("MasterBind can help you set up custom keybinds in City of Heroes, including speed-on-demand binds.")
            info.SetCopyright('(c) 2010-2019 R Pickett <emerson@hayseed.net>')
            info.SetWebSite('https://emersonrp.github.io/masterbind/')
            info.SetName('MasterBind')
            info.SetLicense(Path('LICENSE').read_text())
            info.SetVersion('0.1')
            self.about_info = info
        wx.adv.AboutBox(self.about_info)

def no_op():
    pass

1
