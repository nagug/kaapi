"""Kaapi stack controller."""

#from cement.ext.ext_argparse import ArgparseController, expose
from cement.core.controller import CementBaseController, expose

class KaapiStackController(CementBaseController):
    class Meta:
        label = 'stack'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'All stack related operations'
        arguments = [
            (['--all'],
                dict(help='full installation of nginx with php7 and mariadb', action='store_true')),
            (['--nginx'],
                dict(help='full installation of nginx', action='store_true')),
            (['--pagespeed'],
                dict(help='add pagespeed to nginx', action='store_true')),
            (['--libressl'],
                dict(help='add libressal as default ssl ', action='store_true')),
            (['--brotli'],
                dict(help='add brotli to nginx', action='store_true')),
            (['--ngx_headers'],
                dict(help='add ngx_headers_more to nginx', action='store_true')),
            (['--naxsi'],
                dict(help='add naxsi to nginx', action='store_true')),
            (['--tls_patch'],
                dict(help='add cloudflare TLS patch to nginx', action='store_true')),
            (['--php'],
                dict(help='specify php version: Supported are 7,7.1,5.6 & NONE (NONE - does not install php at all', action='store', dest='php')),
            (['--mysql'],
                dict(help='specify mysql type: Supported are percona, mariadb and NONE', action='store',dest='mysql')),
            ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(help="Full stack install")
    def install(self):
        print "Default selection and hence installs full blown nginx along with php7 and mariadb"
        if(self.app.pargs.all):
            print "builds and install all packages"
        if(self.app.pargs.nginx):
            print "builds and install nginx only with only give options, if none full installation"
        if(self.app.pargs.pagespeed):
            print "add pagespeed option"
        if(self.app.pargs.libressl):
            print "add libressl as default SSL"
        if(self.app.pargs.brotli):
            print "add brotli option"
        if(self.app.pargs.ngx_headers):
            print "add ngx_headers_more option"
        if(self.app.pargs.naxsi):
            print "add naxsi option"
        if(self.app.pargs.tls_patch):
            print "add tls_patch option"
        if(self.app.pargs.php):
            print "set php version to:%s" % self.app.pargs.php
        if(self.app.pargs.mysql):
            print "set mysql version to:%s" % self.app.pargs.mysql        

    @expose(help="Uninstall full stack")
    def remove(self):
        print "removes whole stack"

    @expose(help="Display info on installed packages")
    def remove(self):
        print "Displays info on installed packages"
