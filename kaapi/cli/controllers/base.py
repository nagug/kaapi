"""Kaapi base controller."""

from cement.ext.ext_argparse import ArgparseController, expose

class KaapiBaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'Kaapi is a CLI based LNMP installer for debian based systems.'
        arguments = [
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        print("Inside KaapiBaseController.default().")

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``kaapi.cli.templates``, or ``/var/lib/kaapi/templates/``.
        #
