"""Kaapi magic controller."""

#from cement.ext.ext_argparse import ArgparseController, expose
from cement.core.controller import CementBaseController, expose
from kaapi.core.temp import KaapiInstaller

"""
Class for Magic controller
"""
class KaapiMagicController(CementBaseController):
    """
    Class for Magic controller
    """
    class Meta:
        """
        Meta Class of Magic controller
        """
        label = 'magic'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'All stack related operations'
        arguments = [
            (
                ['--lite'], dict(help='mainline nginx installation', action='store_true')),
            (
                ['--add-pagespeed'], dict(help='build with add pagespeed', action='store_true')),
            (
                ['--no-pagespeed'], dict(help='build with everything except pagespeed',
                                         action='store_true')),
            (
                ['--add-libressl'], dict(help='build with add libressl', action='store_true')),
            (
                ['--no-libressl'], dict(help='build with everything except libressl',
                                        action='store_true')),
            (
                ['--add-brotli'], dict(help='build with add brotli', action='store_true')),
            (
                ['--no-brotli'], dict(help='build with everything except brotli',
                                      action='store_true')),
            (
                ['--add-ngxheaders'], dict(help='build with add ngx_headers',
                                             action='store_true')),
            (
                ['--no-ngxheaders'], dict(help='build with everything except ngx_headers',
                                           action='store_true')),
            (
                ['--add-naxsi'], dict(help='build with add naxsi WAF', action='store_true')),
            (
                ['--no-naxsi'], dict(help='build with everything except naxsi WAF',
                                     action='store_true')),
            (
                ['--no-tlspatch'], dict(help='build with add TLS Patch', action='store_true')),
            (
                ['--add-tlspatch'], dict(help='build with everything except TLS Patch',
                                           action='store_true')),
            ]

    @expose(hide=True)
    def default(self):
        """
        default function of the magic controler
        """
       # print self.app.pargs.__dict__
        arglist = self.app.pargs.__dict__
        arglist = {k: v for k, v in arglist.items() if v is True}
        addlist = []
        removelist = []
        print ("full list is", arglist.keys())
        if (len(arglist.keys()) == 0):
            print ("Only magic")
        else:
            if ('lite' in arglist.keys()) and (len(arglist.keys()) > 1):
                print ("Error: --lite cannot be mixed with other parameters")
            elif ('lite' in arglist.keys()):
                print ("Selected is only lite")
            else:
                for k in arglist.keys():
                    keyword,feature = k.split('_')
                    if keyword == 'no':
                        removelist.append(feature)
                    else:
                        addlist.append(feature)
                commonlist = list(set(addlist).intersection(removelist))
                addlist = [x for x in addlist if x not in commonlist]
                removelist = [x for x in removelist if x not in commonlist]
                if(len(addlist)>0):
                    print "Ignores all remove list & installs Lite + ", addlist
                else :
                    print "install fulllist excluding ", removelist        
        

       # else:
       #     print("builds and install nginx based stack with all modeules")

    @expose(help="Uninstall full stack")
    def remove(self):
        """
        remove function of the magic controler
        """
        print("removes whole stack")

    @expose(help="Display info on installed packages")
    def state(self):
        """
        State/Info function of the magic controler
        """
        print("Displays list of the current installed modules & plugins")
