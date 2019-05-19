import wx

from module.Module import Module
from UI.ControlGroup import ControlGroup

class ComplexBinds(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'Complex Binds')


    def InitKeys(self):
        self.Data = {
            'Enabled' : False,
        }

    def MakeTopSizer(self):
        self.topSizer = wx.BoxSizer(wx.VERTICAL)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        importbtn = wx.Button(self, label = "Import Bind")
        importbtn.Bind(wx.EVT_BUTTON, self.ImportBind)
        importbtn.SetToolTip("Import a Complex Bind from file")
        importbtn.Disable()

        newbindbtn = wx.Button(self, label = "New Bind")
        newbindbtn.Bind(wx.EVT_BUTTON, self.AddNewBind)
        newbindbtn.SetToolTip("Create a new Complex Bind")

        btnSizer.Add( importbtn , 0, wx.ALL, 10 )
        btnSizer.Add( newbindbtn, 0, wx.ALL, 10 )

        self.topSizer.Add(btnSizer, 1, wx.ALL, 10)

        sizer = ControlGroup(self, 'Complex Binds')

        self.topSizer.Add(sizer, 1, wx.ALL, 10)

    def AddNewBind(self): pass
    def ImportBind(self): pass

    def addCBind(cbinds,n,profile):
        pass
    #   my $cbind = cbinds[n]
    #   my $bindtext = iup.label{title = ""; SIZE = "100X"}
    #   sub matrix_value {
    #           my (_,l,c)
    #           if ( == 0) { #  return the titles of columns
    #                   if ( == 0) { return "" } elsif ( == 1) { return "Bindkey" } else { return "Cycle "..(c - 1) }
    #           } elsif ( > 0) { #  return the values of the bindkeys
    #                   if (bind[l] == nil) { return "" }
    #                   if ( == 1) { return cbind[l].bindkey or nil } else { return cbind[l][c-1] or nil }
    #           }
    #   }
    #   sub matrix_value_edit {
    #           my (_,l,c,newval)
    #           cbind[l] = cbind[l] or {}
    #           if (ewval == "") { newval = nil }
    #           if ( == 1) { cbind[l].bindkey = newval } else { cbind[l][c-1] = newval } profile.modified = true 
    #           return iup.DEFAULT
    #   }
    #   sub matrix_entercell {
    #           my (_,l,c)
    #           if (bind[l] == nil) { bindtext.title = "" } else {
    #                   if ( == 1) {
    #                           bindtext.title = cbind[l].bindkey or ""
    #                   } else {
    #                           bindtext.title = cbind[l][c-1] or ""
    #                   }
    #           }
    #           return iup.DEFAULT
    #   }
    #   my $matrix = iup.matrix{numcol="600";numlin="50";numcol_visible="5";numlin_visible="10"
    #           height0=8;value_cb = matrix_value; value_edit_cb = matrix_value_edit; enteritem_cb = matrix_entercell}
    #   for i = 2,600 do matrix["alignment"..i] = "ALEFT" }
    #   my $delbtn = cbButton("Delete this Bind",function()
    #           if (up.Alarm("Confirm Deletion","Are you sure you want to delete this bind?","Yes","No") == 1) {
    #                   table.remove(cbinds,n)
    #                   cbinds.curbind = cbinds.curbind - 1
    #                   if (binds.curbind == 0) { cbinds.curbind = 1 }
    #                   cbinds.dlg:hide()
    #                   # cbinds.dlg:destroy()
    #                   cbinds.dlg = nil
    #                   module.createDialog(cbinds,profile)
    #                   cbShowDialog(cbinds.dlg,218,10,profile,cbinds.dlg_close_cb)
    #                   profile.modified = true 
    #           } })
    #   my $exportbtn = cbButton("Export...",function() cbExportModuleSettings(profile,n,cbinds,"ComplexBind") })
    #   return iup.frame{iup.vbox{bindtext,matrix,iup.hbox{delbtn,exportbtn}},cx = 0, cy = 65 * (n-1)}

    #  this returns the default empty Simple Bind table to be inserted into SBinds
    def newCBind(*args): return args

    def createDialog(cbinds, profile):
        pass
    #   my $box = {}
    #   for i = 1,table.getn(cbinds) do
    #           table.insert(box,addCBind(cbinds,i,profile))
    #   }
    #   cbinds.curbind = cbinds.curbind or 1
    #   my $newbindbtn = cbButton("New Complex Bind",
    #           function()
    #                   table.insert(cbinds,newCBind())
    #                   cbinds.curbind = table.getn(cbinds)
    #                   cbinds.dlg:hide()
    #                   # cbinds.dlg:destroy()
    #                   cbinds.dlg = nil
    #                   module.createDialog(cbinds,profile)
    #                   cbShowDialog(cbinds.dlg,218,10,profile,cbinds.dlg_close_cb)
    #                   profile.modified = true 
    #           },100)
    #   my $importbtn = cbButton("Import Complex Bind",function()
    #           my $newcbind = newCBind() #  we will be filling this new BBind up.
    #           table.insert(cbinds,newcbind)
    #           my $newcbind_n = table.getn(cbinds)
    #           if (bImportModuleSettings(profile,newcbind_n,cbinds,"ComplexBind")) {
    #                   cbinds.curbind = table.getn(cbinds)
    #                   cbinds.dlg:hide()
    #                   cbinds.dlg = nil
    #                   #  Resolve Key COnflicts.
    #                   cbResolveKeyConflicts(profile,true)
    #                   module.createDialog(cbinds,profile)
    #                   cbShowDialog(cbinds.dlg,218,10,profile,cbinds.dlg_close_cb)
    #                   profile.modified = true
    #           } else {
    #                   #  user cancelled, remove the new table from bbinds.
    #                   table.remove(cbinds)
    #           }
    #   },100)
    #   my $sbEnablePrev = "NO"
    #   my $sbEnableNext = "NO"
    #   if (binds.curbind > 1) { sbEnablePrev = "YES" }
    #   cbinds.prevbind = cbButton("<<",function(self)
    #                   cbinds.curbind = cbinds.curbind - 1
    #                   cbinds.zbox.value = box[cbinds.curbind]
    #                   cbinds.poslabel.title = cbinds.curbind.."/"..table.getn(cbinds)
    #                   my $sbEnablePrev = "NO"
    #                   if (binds.curbind > 1) { sbEnablePrev = "YES" }
    #                   cbinds.prevbind.active=sbEnablePrev
    #                   my $sbEnableNext = "NO"
    #                   if (binds.curbind < table.getn(cbinds)) { sbEnableNext = "YES" }
    #                   cbinds.nextbind.active=sbEnableNext
    #           },25,nil,{active=sbEnablePrev})
    #   if (binds.curbind < table.getn(cbinds)) { sbEnableNext = "YES" }
    #   cbinds.nextbind = cbButton(">>",function(self)
    #                   cbinds.curbind = cbinds.curbind + 1
    #                   cbinds.zbox.value = box[cbinds.curbind]
    #                   cbinds.poslabel.title = cbinds.curbind.."/"..table.getn(cbinds)
    #                   my $sbEnablePrev = "NO"
    #                   if (binds.curbind > 1) { sbEnablePrev = "YES" }
    #                   cbinds.prevbind.active=sbEnablePrev
    #                   my $sbEnableNext = "NO"
    #                   if (binds.curbind < table.getn(cbinds)) { sbEnableNext = "YES" }
    #                   cbinds.nextbind.active=sbEnableNext
    #           },25,nil,{active=sbEnableNext})
    #   cbinds.poslabel = iup.label{title = cbinds.curbind.."/"..table.getn(cbinds);rastersize="50x";alignment="ACENTER"}
    #   box.value = box[cbinds.curbind]
    #   cbinds.zbox = iup.zbox(box)
    #   cbinds.dlg = iup.dialog{iup.vbox{cbinds.zbox,iup.hbox{cbinds.prevbind;newbindbtn;importbtn;cbinds.poslabel;cbinds.nextbind;alignment="ACENTER"};alignment="ACENTER"};title = "General : Complex Binds",maxbox="NO",resize="NO",mdichild="YES",mdiclient=mdiClient}
    #   cbinds.dlg_close_cb = function(self) cbinds.dlg = nil }

    def bindsetting(profile):
        cbinds = profile.cbinds
        if cbinds == None:
            profile.cbinds = cbinds = {}

        if cbinds.dlg:
            cbinds.dlg.show()
        else:
            module.createDialog(cbinds, profile)
            cbShowDialog(cbinds.dlg,218,10,profile,cbinds.dlg_close_cb)

    def maxKeys(cbind):
        maxK = 0
        for n in range(1, 600):
            k = cbind[n]
            if (k):
                if k.bindkey: maxK = n

        return maxK


    def maxCycles(cbind, maxK):
        maxC = 0
        for m in range(1, maxK):
            for n in range(2, 600):
                if cbind[m] and cbind[m][n]:
                    if (n > maxC): maxC = n
        return maxC+1

    def writeBind(bindfile, cbinds, key, cycle, bindset, maxC, profile):
        nextCycle = cycle+1
        if (nextCycle > maxC): nextCycle = 1

        keydef = cbinds[bindset][key]

        cmd = ''
        if (keydef[cycle]): cmd = keydef[cycle] + '$$'

        cmd = cmd + f"bindloadfile {profile.base}\cbinds\{bindset}-{nextCycle}.txt"
        bindfile.SetBind(keydef['bindkey'], cmd)


    def PopulateBindFiles(thing):
        profile = thing.Profile
        ResetFile = profile.Data['ResetFile']
        cbinds = profile['cbinds'] or []

        (cbindfile, maxK, maxC) = ('', 0, 0)
        for k in range(1, len(cbinds)):   # for each complex bind set...
            maxK = maxKeys(cbinds[k])
            maxC = maxCycles(cbinds[k], maxK)
            for j in range(1, maxC):  #  for each cycle in this bindset, counting the first one twice...
                    # ...create a new bindfile if cycle is 2+
                    if j > 1:
                        cbindfile = profile.GetBindFile(f'{profile["base"]}\cbinds\{k}-{j-1}.txt')
                    for i in range(1, maxK):
                        if j == 1:
                            writeBind(ResetFile, cbinds, i, j,   k, maxC-1, profile)
                        else:
                            writeBind(cbindfile, cbinds, i, j-1, k, maxC-1, profile)

    def findconflicts(profile):
        cbinds = profile.cbinds or []
        for k in cbinds:
            for i in range(1, maxKeys(k)):  #  for each key in the bindset
                cbCheckConflict(k[i], "bindkey", f"Complex Bind {k}")

    def bindisused(profile):
        return True if profile.cbinds else False
