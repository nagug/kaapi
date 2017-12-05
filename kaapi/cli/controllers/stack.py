"""Kaapi stack controller."""

from cement.ext.ext_argparse import ArgparseController, expose

class KaapiStackController(ArgparseController):
    class Meta:
        label = 'stack'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Install the stack components as requested'
        arguments = [
            (['--all'],
                dict(help='Install all stack', action='store_true')),
            (['--lite'],
                dict(help='Install just nginx without php or mysql', action='store_true')),
            (['--php55'],
                dict(help='Install all stack but force php 5.5', action='store_true')),
            (['--mainline'],
                dict(help='Install all mainline nginx stack', action='store_true')),
            ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(help="install packages", hide=True)
    def install(self):
        print "Inside install package"
        if(self.app.pargs.all):
            print "Inside install package"