#!/usr/bin/env python3

import wx
import os, sys

from Window.Main import Main

def run():
    app = wx.App(False)

    app.path = os.path.dirname(sys.argv[0])


    frame = Main(None, "MasterBind")
    frame.Show(True)

    app.MainLoop()

if __name__ == "__main__":
    run()

