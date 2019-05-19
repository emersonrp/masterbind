import wx
from module.Module import Module

from UI.ControlGroup import ControlGroup
import UI.Labels

class TeamPetSelect(Module):
    def __init__(self, parent):
        Module.__init__(self, parent, 'Team / Pet Select Binds')

    def InitKeys(self):
        if not self.Data:
            self.Data = {
                'Enabled'     : True,

                'TPSEnable'   : 1,
                'TPSSelMode'  : '',
                'TeamSelect1' : 'UNBOUND',
                'TeamSelect2' : 'UNBOUND',
                'TeamSelect3' : 'UNBOUND',
                'TeamSelect4' : 'UNBOUND',
                'TeamSelect5' : 'UNBOUND',
                'TeamSelect6' : 'UNBOUND',
                'TeamSelect7' : 'UNBOUND',
                'TeamSelect8' : 'UNBOUND',
                'EnablePet' : 1,
                'SelNextPet' : 'UNBOUND',
                'SelPrevPet' : 'UNBOUND',
                'IncPetSize' : 'UNBOUND',
                'DecPetSize' : 'UNBOUND',
                'EnableTeam' : 1,
                'SelNextTeam' : 'A',
                'SelPrevTeam' : 'G',
                'IncTeamSize' : 'P',
                'DecTeamSize' : 'H',
                'IncTeamPos'  : '4',
                'DecTeamPos'  : '8',
                'Reset'       : '',
                'mode'        : 1,
            }

    def makeTopSizer(self):
        for i in range(1,8):
            self.Data[f"sel{i}"] = self.Data.get(f"sel{i}", "UNBOUND")

        topSizer = wx.BoxSizer(wx.VERTICAL)

        ##### direct-select keys
        TPSDirectBox = ControlGroup(self, 'Direct Team/Pet Select')

        TPSDirectBox.AddLabeledControl({
            'value' : 'TPSSelMode',
            'type' : 'combo',
            'parent' : self,
            'contents' : ['Teammates, then pets','Pets, then teammates','Teammates Only','Pets Only'],
            'tooltip' : 'Choose the order in which teammates and pets are selected with sequential keypresses',
        })
        for selectid in range(1,8):
            TPSDirectBox.AddLabeledControl({
                'value' : f"TeamSelect{selectid}",
                'type' : 'keybutton',
                'parent' : self,
                'tooltip' : f"Choose the key that will select team member / pet {selectid}",
            })

        topSizer.Add(TPSDirectBox, 0, wx.EXPAND)


        ##### Pet Select Binds
        PetSelBox = ControlGroup(self, 'Pet Select')

        PetSelBox.AddLabeledControl({
            'value' : 'SelNextPet',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will select the next pet from the currently selected one',
        })
        PetSelBox.AddLabeledControl({
            'value' : 'SelPrevPet',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will select the previous pet from the currently selected one',
        })
        PetSelBox.AddLabeledControl({
            'value' : 'IncPetSize',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will increase the size of your pet/henchman group rotation',
        })
        PetSelBox.AddLabeledControl({
            'value' : 'DecPetSize',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will decrease the size of your pet/henchman group rotation',
        })
        topSizer.Add(PetSelBox, 0, wx.EXPAND)

        ##### Team Select Binds
        TeamSelBox = ControlGroup(self, 'Team Select')
        TeamSelBox.AddLabeledControl({
            'value' :'SelNextTeam',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will select the next teammate from the currently selected one',
        })
        TeamSelBox.AddLabeledControl({
            'value' :'SelPrevTeam',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will select the previous teammate from the currently selected one',
        })
        TeamSelBox.AddLabeledControl({
            'value' :'IncTeamSize',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will increase the size of your teammate rotation',
        })
        TeamSelBox.AddLabeledControl({
            'value' :'DecTeamSize',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will decrease the size of your teammate rotation',
        })
        TeamSelBox.AddLabeledControl({
            'value' :'IncTeamPos',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will move you to the next higher slot in the team rotation',
        })
        TeamSelBox.AddLabeledControl({
            'value' :'DecTeamPos',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will move you to the next lower slot in the team rotation',
        })
        TeamSelBox.AddLabeledControl({
            'value' :'Reset',
            'type' : 'keybutton',
            'parent' : self,
            'tooltip' : 'Choose the key that will reset your team rotation to solo',
        })
        topSizer.Add(TeamSelBox, 0, wx.EXPAND)

        self.topSizer = topSizer

    def PopulateBindFiles(self):
        profile    = self.Profile
        ResetFile  = profile.General['ResetFile']
        if self.Data['TPSSelMode'] < 3:
            selmethod = "teamselect"
            selnummod = 0
            selmethod1 = "petselect"
            selnummod1 = 1
            if self.Data['TPSSelMode'] == 2:
                selmethod = "petselect"
                selnummod = 1
                selmethod1 = "teamselect"
                selnummod1 = 0
            selresetfile = profile.GetBindFile("tps","reset.txt")
            for i in range(1, 8):
                selfile = profile.GetBindFile("tps",f"sel{i}.txt")
                ResetFile.   SetBind(self.Data[f"TeamSelect{i}"],f"{selmethod} {i - selnummod}" + BindFile.BLF(profile,'tps',f"sel{i}.txt"))
                selresetfile.SetBind(self.Data[f"TeamSelect{i}"],f"{selmethod} {i - selnummod}" + BindFile.BLF(profile,'tps',f"sel{i}.txt"))
                for j in range(1, 8):
                    if (i == j):
                        selfile.SetBind(self.Data[f"TeamSelect{j}"], f"{selmethod1} {j - selnummod1}" + BindFile.BLF(profile,'tps',"reset.txt"))
                    else:
                        selfile.SetBind(self.Data[f"TeamSelect{j}"], f"{selmethod} {j - selnummod}"  + BindFile.BLF(profile,'tps',f"sel{j}.txt"))
        else:
            selmethod = "teamselect"
            selnummod = 0
            if self.Data['TPSSelMode'] == 4:
                selmethod = "petselect"
                selnummod = 1
            for i in range(1, 8):
                ResetFile.SetBind(self.Data['sel1'],f"{selmethod} {i - selnummod}")

        if self.Data['PetSelEnable']:
            tpsCreatePetSet(profile,1,0,profile.General['ResetFile'])
            for size in range(1, 8):
                for sel in range(0, size):
                    outfile = profile.GetBindFile("tps",f"pet{size}{sel}.txt")
                    tpsCreatePetSet(profile, size, sel, outfile)


        if self.Data['TeamSelEnable']:
            tpsCreateTeamSet(profile,1,0,0,profile.General['ResetFile'])
            for size in range(1, 8):
                for pos in range(0, size):
                    for sel in range(0, size):
                        if (sel != pos or sel == 0):
                            outfile = profile.GetBindFile("tps", f"team{size}{pos}{sel}.txt")
                            tpsCreateTeamSet(profile, size, pos, sel, outfile)


    def tpsCreatePetSet(self, profile, tsize, tset, outfile):
        # tsize is the size of the team at the moment
        # tpos is the position of the player at the moment, or 0 if unknown
        # tsel is the currently selected team member as far as the bind knows, or 0 if unknown
        #file.SetBind(TPS.reset,'tell $name, Re-Loaded Single Key Team Select Bind.' . BindFile::BLF($profile, 'petsel', '10.txt')
        if (tsize < 8):
            outfile.SetBind(self.Data['IncPetSize'],'tell $name, ' + formatPetConfig(tsize+1) + BindFile.BLF(profile, 'tps', (tsize+1) + f"{tsel}.txt"))
        else:
            outfile.SetBind(self.Data['DecPetSize'],'nop')

        if tsize == 1:
            outfile.SetBind(self.Data['DecPetSize'],'nop')
            outfile.SetBind(self.Data['SelNextPet'],'petselect 0' . BindFile.BLF(profile, 'tps', f'{tsize}1.txt'))
            outfile.SetBind(self.Data['SelPrevPet'],'petselect 0' . BindFile.BLF(profile, 'tps', f'{tsize}1.txt'))
        else:
            (selnext, selprev) = (tsel+1, tsel-1)
            if selnext > tsize: selnext = 1
            if selprev < 1:     selprev = tsize

            newsel = tsel
            if tsize-1 < tsel: newsel = tsize-1
            if tsize == 2:     newsel = 0
            outfile.SetBind(self.Data['DecPetSize'],'tell $name, ' + formatPetConfig(tsize-1) + BindFile.BLF(profile, 'tps', f'{tsize-1}{newsel}.txt'))
            outfile.SetBind(self.Data['SelNextPet'],'petselect ' + (selnext-1) + BindFile.BLF(profile, 'tps', f'{tsize}{selnext}.txt'))
            outfile.SetBind(self.Data['SelPrevPet'],'petselect ' + (selprev-1) + BindFile.BLF(profile, 'tps', f'{tsize}{selprev}.txt'))

    def formatPetConfig(self, num):
        return "[" + ('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth')[num - 1] + " Pet ]"

    def tpsCreateTeamSet(self, profile, tsize, tpos, tset, outfile):
        #  tsize is the size of the team at the moment
        #  tpos is the position of the player at the moment, or 0 if unknown
        #  tsel is the currently selected team member as far as the bind knows, or 0 if unknown
        outfile.SetBind(self.Data['Reset'],'tell $name, Re-Loaded Single Key Team Select Bind' . BindFile.BLF(profile, 'teamsel2', '100.txt'))
        if tsize < 8:
            outfile.SetBind(self.Data['IncTeamSize'],'tell $name, ' . formatTeamConfig(tsize+1, tpos) . BindFile.BLF(profile, 'teamsel2',f'{tsize+1}{tpos}{tsel}.txt'))
        else:
            outfile.SetBind(self.Data['IncTeamSize'],'nop')

        if tsize == 1:
            outfile.SetBind(self.Data['DecTeamSize'],'nop')
            outfile.SetBind(self.Data['IncTeamPos'], 'nop')
            outfile.SetBind(self.Data['DecTeamPos'], 'nop')
            outfile.SetBind(self.Data['SelNextTeam'],'nop')
            outfile.SetBind(self.Data['SelPrevTeam'],'nop')
        else:
            (selnext, selprev) = (tsel+1, tsel-1)
            if selnext > tsize: selnext = 1
            if selprev < 1:     selprev = tsize
            if selnext == tpos: selnext = selnext + 1
            if selprev == tpos: selprev = selprev - 1
            if selnext > tsize: selnext = 1
            if selprev < 1:     selprev = tsize

            (tposup, tposdn) = (tpos+1, tpos-1)
            if tposup > tsize: tposup = 0
            if tposdn < 0:     tposdn = tsize

            (newpos, newsel) = (tpos, tsel)
            if tsize-1 < tpos: newpos = tsize-1
            if tsize-1 < tsel: newsel = tsize-1
            if tsize == 2:      newpos = newsel = 0

            outfile.SetBind(self.Data['DecTeamSize'],'tell $name, ' + formatTeamConfig(tsize-1,newpos) . BindFile.BLF(profile, 'teamsel2', f'{tsize-1}{newpos}{newsel}.txt'))
            outfile.SetBind(self.Data['IncTeamPos'], 'tell $name, ' + formatTeamConfig(tsize,  tposup) . BindFile.BLF(profile, 'teamsel2', f'{tsize}{tposup}{tsel}.txt'))
            outfile.SetBind(self.Data['DecTeamPos'], 'tell $name, ' + formatTeamConfig(tsize,  tposdn) . BindFile.BLF(profile, 'teamsel2', f'{tsize}{tposdn}{tsel}.txt'))

            outfile.SetBind(self.Data['SelNextTeam'],f'teamselect {selnext}' + BindFile.BLF(profile, 'teamsel2', f'{tsize}{tpos}{selnext}.txt'))
            outfile.SetBind(self.Data['SelPrevTeam'],f'teamselect {selprev}' + BindFile.BLF(profile, 'teamsel2', f'{tsize}{tpos}{selprev}.txt'))

    post = ('Zeroth','First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth'); # damn zero-based arrays
    def formatTeamConfig(self, size, pos):
        sizetext = f"{size}-Man"
        postext = ", No Spot"
        if pos > 0:     postext  = f", {post[pos]} Spot"
        if size == 1:
            sizetext = "Solo"
            postext  = ""
        if size == 2:
            sizetext = "Duo"
        if size == 3:
            sizetext = "Trio"
        return f"[{sizetext}{postext}]"

    def findconflicts(self):
        for i in range(1, 8):
            cbCheckConflict(self,f"TeamSelect{i}",f"Team/Pet {i} Key")

        cbCheckConflict(self,"SelNextPet","Select next henchman")
        cbCheckConflict(self,"SelPrevPet","Select previous henchman")
        cbCheckConflict(self,"IncPetSize","Increase Henchman Group Size")
        cbCheckConflict(self,"DecPetSize","Decrease Henchman Group Size")

    def bindisused(self):
        return True if profile.TeamPetSelect['Enable'] else False

    def HelpText(self):
        """

Team/Pet Direct Selection binds contributed by ShieldBearer.

Single Key Team Selection binds based on binds from Weap0nX.

        """


    UI.Labels.Add({
        'TPSSelMode' : "Team/Pet selection mode",
        'TeamSelect1' : "Select First Team Member/Pet",
        'TeamSelect2' : "Select Second Team Member/Pet",
        'TeamSelect3' : "Select Third Team Member/Pet",
        'TeamSelect4' : "Select Fourth Team Member/Pet",
        'TeamSelect5' : "Select Fifth Team Member/Pet",
        'TeamSelect6' : "Select Sixth Team Member/Pet",
        'TeamSelect7' : "Select Seventh Team Member/Pet",
        'TeamSelect8' : "Select Eighth Team Member/Pet",
        'SelNextPet' : 'Select Next Pet',
        'SelPrevPet' : 'Select Previous Pet',
        'IncPetSize' : 'Increase Pet Group Size',
        'DecPetSize' : 'Decrease Pet Group Size',
        'SelNextTeam' : 'Select Next Team Member',
        'SelPrevTeam' : 'Select Previous Team Member',
        'IncTeamSize' : 'Increase Team Size',
        'DecTeamSize' : 'Decrease Team Size',
        'IncTeamPos'  : 'Increase Team Position',
        'DecTeamPos'  : 'Decrease Team Position',
        'Reset'       : 'Reset to Solo',
    })
