class BindFile:

    BindFiles = {}

    def __init__(self, filename):

        if BindFiles[filename]:
            self = BindFiles[filename]
            return

        self.binds = {}

    def SetBind(self, key, bindtext):
        if not key:
            print(f"invalid key: { key }, bindtext { bindtext }")
            return

        bindtext = bindtext.strip()

        # TODO -- how to call out the 'reset file' object as special?
        # if ($file eq $resetfile1 and $key eq $resetkey) {
            # $resetfile2->{$key} = $s
        # }

        self.binds[key] = bindtext

    def BaseReset(self, profile):
        return '$$bindloadfilesilent ' + profile.General['BindsDir'] + "\\subreset.txt"

    # BLF == full "$$bindloadfilesilent path/to/file/kthx"
    def BLF(self, *args):
        return '$$' + self.BLFs(args)

    # BLFs == same as above but no '$$' for use at start of binds.  Unnecessary?
    def BLFs(self, *args):
        return 'bindloadfilesilent ' + self.BLFPath(args)

    # BLFPath == just the path to the file
    def BLFPath(self, profile, *args):
        pass
        #my $file = pop @bits
        #my ($vol, $bdir, undef) = File::Spec->splitpath( $profile->General->{'BindsDir'}, 1 )
        #my $dirpath = File::Spec->catdir($bdir, @bits)
        #return File::Spec->catpath($vol, $dirpath, $file)

    def Write(self, profile):
        # Pick apart the binds directory
        # TODO XXX all this File::Spec stuff
        (vol, bdir, _) = File.Spec.splitpath( profile.General['BindsDir'], 1 )

        # Pick apart the filename into component bits.
        (_, dir, file) = File.Spec.splitpath( self['filename'] )

        # mash together the two 'directory' parts:
        dir = File.Spec.catdir(bdir, dir)

        # now we want the fully-qualified dir name so we can make sure it exists...
        newpath = File.Spec.catpath( vol, dir, '' )
        # and the fully-qualified filename so we can write to it.
        fullname = File.Spec.catpath( vol, dir, file )
        # Make the dir if it doesn't exist already.
        # if ( ! -d $newpath ) {
        #     File::Path::make_path( $newpath, {verbose=>1} ) or warn "can't make dir $newpath: $!"
        # }

        # open the file and blast the poop into it.  whee!
        # open (my $fh, '>', $fullname ) or warn "can't write to $fullname: $!"
        # for my $k (sort keys %{ $self->{'binds'} }) {
        #     print $fh qq|$k "$self->{'binds'}->{$k}"\n|
        # }
        # print STDERR "Done $fullname!\n"
