"""Kaapi base controller."""

from cement.core.controller import CementBaseController, expose
from kaapi.core.variables import KaapiVariables

BANNER = KaapiVariables.BANNER

class KaapiBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Kaapi is a CLI based LNMP installer for debian based systems.'
        arguments = [
            (['-v', '--version'], dict(action='version', version=BANNER)),
            ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()