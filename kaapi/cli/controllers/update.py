"""Kaapi update controller."""

#from cement.ext.ext_argparse import ArgparseController, expose
from cement.core.controller import CementBaseController, expose

class KaapiUpdateController(CementBaseController):
    class Meta:
        label = 'update'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'updates kaapi with latest version with all modules'


    @expose(hide=True)
    def default(self):
        print "rebuild with updated source"