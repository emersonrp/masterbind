#!/usr/bin/env python3

import wx
import os, sys

#use About
#use Profile
#use StdDefault
#
#use Powerbinder
#use PowerBindCmds
#
#our $profile
#
#BCApp.new.MainLoop

###################
# Application class
###################
def run():
    app = wx.App(False)

    app.path = os.path.dirname(sys.argv[0])

    from window.Main import Main

    frame = Main(None, "MasterBind")
    frame.Show(True)

    app.MainLoop()

if __name__ == "__main__":
    run()

