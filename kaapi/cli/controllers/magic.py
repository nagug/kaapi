"""Kaapi magic controller."""

#from cement.ext.ext_argparse import ArgparseController, expose
from cement.core.controller import CementBaseController, expose

class KaapiMagicController(CementBaseController):
    class Meta:
        label = 'magic'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'All stack related operations'
        arguments = [
            (['--lite'],
                dict(help='mainline nginx installation', action='store_true')),
            (['--only-pagespeed'],
                dict(help='build with only pagespeed', action='store_true')),
            (['--no-pagespeed'],
                dict(help='build with everything except pagespeed', action='store_true')),
            (['--only-libressl'],
                dict(help='build with only libressl', action='store_true')),
            (['--no-libressl'],
                dict(help='build with everything except libressl', action='store_true')),
            (['--only-brotli'],
                dict(help='build with only brotli', action='store_true')),
            (['--no-brotli'],
                dict(help='build with everything except brotli', action='store_true')),                
            (['--only-ngx_headers'],
                dict(help='build with only ngx_headers', action='store_true')),
            (['--no-ngx_headers'],
                dict(help='build with everything except ngx_headers', action='store_true')),
            (['--only-naxsi'],
                dict(help='build with only naxsi WAF', action='store_true')),
            (['--no-naxsi'],
                dict(help='build with everything except naxsi WAF', action='store_true')),
            (['--no-tls_patch'],
                dict(help='build with only TLS Patch', action='store_true')),
            (['--only-tls_patch'],
                dict(help='build with everything except TLS Patch', action='store_true')),
            ]

    @expose(hide=True)
    def default(self):
        print "builds and install everything"
        if(self.app.pargs.lite):
            print "builds and install nginx based stack, no additional modules"
        
  

    @expose(help="Uninstall full stack")
    def remove(self):
        print "removes whole stack"

    @expose(help="Display info on installed packages")
    def state(self):
        print "Displays list of the current installed modules & plugins"
