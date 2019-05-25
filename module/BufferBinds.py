import wx

from module.Module import Module
from UI.ControlGroup import ControlGroup

class BufferBinds(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'Buffer Binds')

    def InitKeys(self):
        self.Data = {
            'Enabled' : False,
        }

        self.BBinds = []

    def MakeTopSizer(self):
        topSizer = wx.BoxSizer(wx.VERTICAL)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        importbtn = wx.Button(self, label = "Import Bind")
        importbtn.Bind(wx.EVT_BUTTON, self.ImportBind)
        importbtn.SetToolTip("Import a Buffer Bind from file")
        importbtn.Disable()

        newbindbtn = wx.Button(self, label = "New Bind")
        newbindbtn.Bind(wx.EVT_BUTTON, self.AddNewBind)
        newbindbtn.SetToolTip("Create a new Buffer Bind")

        btnSizer.Add( importbtn , 0, wx.ALL, 10 )
        btnSizer.Add( newbindbtn, 0, wx.ALL, 10 )

        topSizer.Add(btnSizer, 1, wx.ALL, 10)

        sizer = ControlGroup(self, 'Buffer Binds')

        # TODO - when we load from an existing profile, we'll have some set up already maybe
        for i in range(1, len(self.Data.keys())):
            sizer.AddLabeledControl({
            })

        #bbinds.curset = bbinds.curset or 1

        #bbEnablePrev = "NO"
        #bbEnableNext = "NO"
        #if (bbinds.curset > 1) { bbEnablePrev = "YES" }
        #bbinds.prevbind = cbButton("<<",
        #    sub {
        #        my(self)
        #        bbinds.curset = bbinds.curset - 1
        #        if (bbinds.curset < 1) { bbinds.curset = 1 }
        #        bbinds.zbox.value = box[bbinds.curset]
        #        bbinds.poslabel.title = bbinds.curset.."/"..table.getn(bbinds)
        #        bbEnablePrev = "NO"
        #        if (bbinds.curset > 1) { bbEnablePrev = "YES" }
        #        bbinds.prevbind.active=bbEnablePrev
        #        bbEnableNext = "NO"
        #        if (bbinds.curset < table.getn(bbinds)) { bbEnableNext = "YES" }
        #        bbinds.nextbind.active=bbEnableNext
        #    },25,undef,{active=bbEnablePrev}
        #)
        #if (bbinds.curset < table.getn(bbinds)) { bbEnableNext = "YES" }
        #cbToolTip("Click this to go to the previous bind")
        #bbinds.nextbind = cbButton(">>",
        #    sub {
        #        my(self)
        #        bbinds.curset = bbinds.curset + 1
        #        if (bbinds.curset > table.getn(bbinds)) { bbinds.curset = table.getn(bbinds) }
        #        bbinds.zbox.value = box[bbinds.curset]
        #        bbinds.poslabel.title = bbinds.curset.."/"..table.getn(bbinds)
        #        bbEnablePrev = "NO"
        #        if (bbinds.curset > 1) { bbEnablePrev = "YES" }
        #        bbinds.prevbind.active=bbEnablePrev
        #        bbEnableNext = "NO"
        #        if (bbinds.curset < table.getn(bbinds)) { bbEnableNext = "YES" }
        #        bbinds.nextbind.active=bbEnableNext
        #    },25,undef,{active=bbEnableNext})
        #bbinds.poslabel = iup.label{title = bbinds.curset.."/"..table.getn(bbinds);rastersize="50x";alignment="ACENTER"}
        #box.value = box[bbinds.curset]
        #bbinds.zbox = iup.zbox(box)
        #bbinds.dlg  = iup.dialog{iup.vbox{bbinds.zbox,iup.hbox{bbinds.prevbind;newbindbtn;importbtn;bbinds.poslabel;bbinds.nextbind;alignment="ACENTER"};alignment="ACENTER"};title = "Gameplay : Buffer Binds",maxbox="NO",resize="NO",mdichild="YES",mdiclient=mdiClient}
        #bbinds.dlg_close_cb = sub {
        #    my(self)
        #    bbinds.dlg = undef
        #}

        topSizer.Add(sizer, 1, wx.ALL, 10)

        self.topSizer = topSizer


    def addBBind(binds, n, profile):
        print("Got into addBBind")
        #bbind = bbinds[n]
        #bbtitle = cbTextBox("Buffer Bind Name",bbind.title,cbTextBoxCB(profile,bbind,"title"),300,undef,100)
        #selchattext = cbToggleText("Select Chat",bbind.selchatenabled,bbind.selchat,
        #        cbCheckBoxCB(profile,bbind,"selchatenabled"),cbTextBoxCB(profile,bbind,"selchat"),100,undef,300)
        #selchattext = cbPowerBindBtn("Select Chat",bbind,"selchat",chatnogloballimit,300,undef,profile)
        #buffpower1 = cbTextBox("Buff Power",bbind.power1,cbTextBoxCB(profile,bbind,"power1"))
        #buffpower1 = cbPowerList("First Buff Power",profile.powerset,bbind,"power1",profile,200)
        #chat1text = cbPowerBindBtn("First Chat Command",bbind,"chat1",chatnogloballimit,300,undef,profile)
        #chat3text = cbPowerBindBtn("Third Chat Command",bbind,"chat3",chatnogloballimit,300,undef,profile)
        #if (not bbind.power3enabled) { chat3text.active = "NO" }
        #buffpower3 = cbTogglePower("Third Buff Power",profile.powerset,bbind.power3enabled,bbind,"power3",
        #        sub { my(_,v) profile.modified = true 
        #            if (v == 1) {
        #                bbind.power3enabled = true
        #                chat3text.active = "YES"
        #                } else {
        #                    bbind.power3enabled = undef
        #                    chat3text.active = "NO"
        #                    }
        #                },profile,undef,undef,200)
        #        if (not bbind.power2enabled) { buffpower3.active = "NO" }
        #chat2text = cbPowerBindBtn("Second Chat Command",bbind,"chat2",chatnogloballimit,300,undef,profile)
        #if (not bbind.power2enabled) { chat2text.active = "NO" }
        #buffpower2 = cbTogglePower("Second Buff Power",profile.powerset,bbind.power2enabled,bbind,"power2",
        #        sub { my(_,v) profile.modified = true 
        #            if (v == 1) {
        #                bbind.power2enabled = true
        #                chat2text.active = "YES"
        #                buffpower3.active = "YES"
        #                if (bbind.power3enabled) {
        #                    chat3text.active = "YES"
        #                    }
        #                } else {
        #                    bbind.power2enabled = undef
        #                    chat2text.active = "NO"
        #                    buffpower3.active = "NO"
        #                    chat3text.active = "NO"
        #                    }
        #                },profile,undef,undef,200)
        #        team1key = cbBindBox("Team 1 Key",bbind,"team1",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 1 Key"),profile)
        #team2key = cbBindBox("Team 2 Key",bbind,"team2",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 2 Key"),profile)
        #team3key = cbBindBox("Team 3 Key",bbind,"team3",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 3 Key"),profile)
        #team4key = cbBindBox("Team 4 Key",bbind,"team4",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 4 Key"),profile)
        #team5key = cbBindBox("Team 5 Key",bbind,"team5",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 5 Key"),profile)
        #team6key = cbBindBox("Team 6 Key",bbind,"team6",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 6 Key"),profile)
        #team7key = cbBindBox("Team 7 Key",bbind,"team7",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 7 Key"),profile)
        #team8key = cbBindBox("Team 8 Key",bbind,"team8",cbMakeDescLink("Buff Bind ",bbind,"title",": Team 8 Key"),profile)
        #usepetnames = cbCheckBox("Use Pet Names to Select?",bbind.usepetnames,cbCheckBoxCB(profile,bbind,"usepetnames"))
        #pet1key = cbBindBox("Pet 1 Key",bbind,"pet1",cbMakeDescLink("Buff Bind ",bbind,"title",": Pet 1 Key"),profile)
        #pet2key = cbBindBox("Pet 2 Key",bbind,"pet2",cbMakeDescLink("Buff Bind ",bbind,"title",": Pet 2 Key"),profile)
        #pet3key = cbBindBox("Pet 3 Key",bbind,"pet3",cbMakeDescLink("Buff Bind ",bbind,"title",": Pet 3 Key"),profile)
        #pet4key = cbBindBox("Pet 4 Key",bbind,"pet4",cbMakeDescLink("Buff Bind ",bbind,"title",": Pet 4 Key"),profile)
        #pet5key = cbBindBox("Pet 5 Key",bbind,"pet5",cbMakeDescLink("Buff Bind ",bbind,"title",": Pet 5 Key"),profile)
        #pet6key = cbBindBox("Pet 6 Key",bbind,"pet6",cbMakeDescLink("Buff Bind ",bbind,"title",": Pet 6 Key"),profile)
        ##  we use a custom listbox callback to enable/disable bufferbind UI elements based on the selection of this list.
        #target = cbListBox("Buffs affect...",{"Teammates","Pets","Both"},3,bbind.target,
        #        sub { my(_,str,i,v) profile.modified = true 
        #            if (v == 1) {
        #                bbind.target = i
        #                #  activate bind boxes based on the value of i.
        #                if (i == 1) {
        #                    team1key.active="YES"
        #                    team2key.active="YES"
        #                    team3key.active="YES"
        #                    team4key.active="YES"
        #                    team5key.active="YES"
        #                    team6key.active="YES"
        #                    team7key.active="YES"
        #                    team8key.active="YES"
        #                    pet1key.active="NO"
        #                    pet2key.active="NO"
        #                    pet3key.active="NO"
        #                    pet4key.active="NO"
        #                    pet5key.active="NO"
        #                    pet6key.active="NO"
        #                    } elsif (i == 2) {
        #                        team1key.active="NO"
        #                        team2key.active="NO"
        #                        team3key.active="NO"
        #                        team4key.active="NO"
        #                        team5key.active="NO"
        #                        team6key.active="NO"
        #                        team7key.active="NO"
        #                        team8key.active="NO"
        #                        pet1key.active="YES"
        #                        pet2key.active="YES"
        #                        pet3key.active="YES"
        #                        pet4key.active="YES"
        #                        pet5key.active="YES"
        #                        pet6key.active="YES"
        #                        } else {
        #                            team1key.active="YES"
        #                            team2key.active="YES"
        #                            team3key.active="YES"
        #                            team4key.active="YES"
        #                            team5key.active="YES"
        #                            team6key.active="YES"
        #                            team7key.active="YES"
        #                            team8key.active="YES"
        #                            pet1key.active="YES"
        #                            pet2key.active="YES"
        #                            pet3key.active="YES"
        #                            pet4key.active="YES"
        #                            pet5key.active="YES"
        #                            pet6key.active="YES"
        #                            }
        #                        }
        #            })
        #if (bbind.target == 1) {
        #        pet1key.active="NO"
        #        pet2key.active="NO"
        #        pet3key.active="NO"
        #        pet4key.active="NO"
        #        pet5key.active="NO"
        #        pet6key.active="NO"
        #        } elsif (bbind.target == 2) {
        #                team1key.active="NO"
        #                team2key.active="NO"
        #                team3key.active="NO"
        #                team4key.active="NO"
        #                team5key.active="NO"
        #                team6key.active="NO"
        #                team7key.active="NO"
        #                team8key.active="NO"
        #                }

        #        delbtn = cbButton("Delete this Bind",sub {
        #            if (iup.Alarm("Confirm Deletion","Are you sure you want to delete this bind?","Yes","No") == 1) {
        #                table.remove(bbinds,n)
        #                bbinds.curset = bbinds.curset - 1
        #                if (bbinds.curset == 0) { bbinds.curset = 1 }
        #                cbCleanDlgs(profile,bbinds.dlg)
        #                bbinds.dlg:hide()
        #                # bbinds.dlg:destroy()
        #                bbinds.dlg = undef
        #                module.createDialog(bbinds,profile)
        #                cbShowDialog(bbinds.dlg,218,10,profile,bbinds.dlg_close_cb)
        #                profile.modified = true 
        #                }
        #            })
        #        exportbtn = cbButton("Export...",sub { cbExportModuleSettings(profile,n,bbinds,"BuffBind") })

        #return iup.vbox{bbtitle,selchattext,buffpower1,chat1text,buffpower2,chat2text,buffpower3,chat3text,
        #        iup.hbox{iup.vbox{team1key,team2key,team3key,team4key,team5key,team6key,team7key,team8key},
        #            iup.vbox{target,iup.fill{},usepetnames,pet1key,pet2key,pet3key,pet4key,pet5key,pet6key,iup.fill{}}},
        #        iup.hbox{delbtn,exportbtn}

        #def bindsettings(profile):
        #    Buffer = profile.Buffer
        #    if Buffer == "None":
        #        profile.Buffer = Buffer = {}

        #    Buffer.number = Buffer.number or 0
        #    Buffer.curset = Buffer.curset or 0
        #    Buffer.set = Buffer.set or {}
        #    if (Buffer.dlg):
        #        Buffer.dlg.show()
    #        else:
    #           module.createDialog(buffer,profile)
    #           cbShowDialog(buffer.dlg,218,10,profile,buffer.dlg_close_cb)

    def PopulateBindFiles(self):

        profile = self.Profile

        ResetFile = profile.Data['ResetFile']
        (afile, bfile, cfile, dfile) = ('','','','')
        #  for each bindset, create the binds.
        for bbind in self.BBinds:

            selchat = cbPBindToString(bbind.selchat) if bbind.selchatenabled else ''
            chat1   = cbPBindToString(bbind.chat1)   if bbind.chat1enabled   else ''
            chat2   = cbPBindToString(bbind.chat2)   if bbind.chat2enabled   else ''
            chat3   = cbPBindToString(bbind.chat3)   if bbind.chat3enabled   else ''

            npow = 1
            if (bbind.power2enabled): npow = 2
            if (bbind.power3enabled): npow = 3

            if (bbind.target == 1 or bbind.target == 3):
                for j in range(1,8):
                    teamid = "team" + str(j)
                    filebase = f"profile.base\\buffi\\bufft{j}"
                    afile = profile.GetBindFile(f"{filebase}a.txt")
                    bfile = profile.GetBindFile(f"{filebase}b.txt")
                    afile.SetBind(    teamid,f'+down teamselect {j} {selchat}bindloadfile {filebase}b.txt')
                    ResetFile.SetBind(teamid,f'+down teamselect {j} {selchat}bindloadfile {filebase}b.txt')
                    if (npow == 1):
                        bfile.SetBind(teamid,f'-down{chat1}powexecname {bbind.power1} bindloadfile {filebase}a.txt')
                    else:
                        bfile.SetBind(teamid,f'-down {chat1}powexecname {bbind.power1} bindloadfile {filebase}c.txt')
                        cfile = profile.GetBindFile(f"{filebase}c.txt")
                    if (npow == 2):
                        cfile.SetBind(teamid,f'{chat2}powexecname {bbind.power2} bindloadfile {filebase}a.txt')
                    else:
                        dfile = profile.GetBindFile(f"{filebase}d.txt")
                        cfile.SetBind(teamid,f'+down {chat2}powexecname {bbind.power2}  bindloadfile {filebase}d.txt')
                        dfile.SetBind(teamid,f'-down {chat3}powexecname {bbind.power3}  bindloadfile {filebase}a.txt')
            if (bbind.target == 2 or bbind.target == 3):
                for j in range(1,6):
                    petid    = f"pet{j}"
                    filebase = f"profile.base\\buffi\\buffp{j}"
                    if bbind.usepetnames:
                        petaction = profile.petaction[f'pet{j}name']
                        ResetFile.SetBind(petid,f'+down petselectname {petaction} pet{j}name {selchat}bindloadfile {filebase}b.txt')
                    else:
                        petnum = j-1
                        ResetFile.SetBind(petid,f'+down petselect {petnum} {selchat}bindloadfile {filebase}b.txt')

                    afile = profile.GetBindFile(f"{filebase}a.txt")
                    bfile = profile.GetBindFile(f"{filebase}b.txt")
                    if bbind.usepetnames:
                        petaction = profile.petaction[f'pet{j}name']
                        afile.SetBind(petid,f'+down petselectname {petaction} {selchat}bindloadfile {filebase}b.txt')
                    else:
                        petnum = j-1
                        afile.SetBind(petid,f'+down petselect {petnum} {selchat}bindloadfile {filebase}b.txt')


                    if npow == 1:
                        bfile.SetBind(petid,f'-down {chat1}powexecname bbind.power1 bindloadfile {filebase}a.txt')
                    else:
                        bfile.SetBind(petid,f'-down {chat1}powexecname bbind.power1 bindloadfile {filebase}c.txt')
                        cfile = profile.GetBindFile("{filebase}c.txt")

                    if npow == 2:
                        cfile.SetBind(petid,f'{chat2}powexecname bbind.power2 bindloadfile {filebase}a.txt')
                    else:
                        dfile = profile.GetBindFile(f"{filebase}d.txt")
                        cfile.SetBind(petid,f'+down {chat2}powexecname bbind.power2 bindloadfile           {filebase}d.txt')
                        dfile.SetBind(petid,f'-down {chat3}powexecname bbind.power3 bindloadfile           {filebase}a.txt')

    def findconflicts(self):
        profile = self.Profile
        ResetFile = profile.Data['ResetFile']
        for bbind in self.BBinds:
            title = bbind.title or 'unknown'
            if (bbind.target == 1 or bbind.target == 3):
                for j in range(1,8):
                    cbCheckConflict(bbind,f"team{j}","Buff bind title: Team {j} Key")

            if (bbind.target == 2 or bbind.target == 3):
                for j in range(1,6):
                        cbCheckConflict(bbind,f"pet{j}","Buff bind title: Pet {j} Key")

    def bindisused(self):
        True if self.BBinds else False


    def AddNewBind(self):
        table.insert(bbinds,newBBind())
        bbinds.curbind = table.getn(bbinds)
        module.createDialog(bbinds,profile)
        cbShowDialog(bbinds.dlg,218,10,profile,bbinds.dlg_close_cb)
        profile.modified = true


    def ImportBind(self):
        pass
        # newbbind = newBBind() #  we will be filling this new BBind up.
        # table.insert(bbinds,newbbind)
        # newbbind_n = table.getn(bbinds)
        # if (cbImportModuleSettings(profile,newbbind_n,bbinds,"BuffBind")) {
        #         bbinds.curbind = table.getn(bbinds)
        #         #  Resolve Key COnflicts.
        #         cbResolveKeyConflicts(profile,true)
        #         module.createDialog(bbinds,profile)
        #         cbShowDialog(bbinds.dlg,218,10,profile,bbinds.dlg_close_cb)
        #         profile.modified = true
        # } else {
        #         #  user cancelled, remove the new table from bbinds.
        #         table.remove(bbinds)
        # }
