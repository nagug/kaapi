"""Kaapi base controller."""

from cement.ext.ext_argparse import ArgparseController, expose

VERSION = '0.1b'

BANNER = """
Kaapi v%s 
Copyright (c) 2017 Nimidam.com
""" % VERSION

class KaapiBaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'Kaapi is a CLI based LNMP installer for debian based systems.'
        arguments = [
            (['-v', '--version'], dict(action='version', version=BANNER)),
            ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()