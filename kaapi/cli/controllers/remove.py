"""Kaapi magic controller."""

#from cement.ext.ext_argparse import ArgparseController, expose
from cement.core.controller import CementBaseController, expose

class KaapiRemoveController(CementBaseController):
    class Meta:
        label = 'remove'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Removes/Unistall/cleans Kaapi'


    @expose(hide=True)
    def default(self):
        print "removes the entire stack"