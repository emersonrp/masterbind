from pathlib import Path

class BindFile:

    def __init__(self, profile, filename):
        self.binds    = {}
        self.filename = Path(filename)
        self.Profile  = profile

    def SetBind(self, key, bindtext):
        if not key:
            raise Exception(f"invalid key: { key }, bindtext { bindtext }")

        bindtext = bindtext.strip()

        # TODO -- how to call out the 'reset file' object as special?
        # if ($file eq $resetfile1 and $key eq $resetkey) {
            # $resetfile2->{$key} = $s
        # }

        self.binds[key] = bindtext

    def BaseReset(self):
        return '$$bindloadfilesilent ' + self.Profile.Data['BindsDir'] + "\\subreset.txt"

    # BLF == full "$$bindloadfilesilent path/to/file/kthx"
    def BLF(self):
        return '$$' + self.BLFs()

    # BLFs == same as above but no '$$' for use at start of binds.  Unnecessary?
    def BLFs(self):
        return 'bindloadfilesilent ' + str(self.BLFPath())

    # BLFPath == just the path to the file
    def BLFPath(self):
        # We re-calculate all this actual paths stuff each time
        # in case the user has changed the bindsdir in the meantime
        if self.Profile.Data.get('BindsDir', ''):
            bindsdir = Path(self.Profile.Data['BindsDir'])
        else:
            # TODO - do something more error-y
            print("ERROR!  BindsDir unset in General prefs!!!")
            return

        wholepath = bindsdir / self.filename
        return wholepath

    def Write(self):
        wholepath = self.BLFPath()
        # Get the full parent dir of the file
        filedir   = wholepath.parent

        # Make the dir if it doesn't exist already.
        try:
            filedir.mkdir(parents = True, exist_ok = True)
        except FileExistsError:
            raise Exception(f"{wholedir} already exists but is not a directory, aborting write of {wholepath}")

        contents = ''
        for bind in self.binds:
            contents = contents + f"{bind} {self.binds[bind]}\n"

        # TODO -- need to wholepath.unlink first?

        # TODO this is just debug
        #print(f"about to write to {wholepath}:\n{contents}")

        wholepath.write_text(contents)
