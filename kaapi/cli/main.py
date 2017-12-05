"""Kaapi main application entry point."""
import os

from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from kaapi.core import exc

# Application default.  Should update config/kaapi.conf to reflect any
# changes, or additions here.
defaults = init_defaults('kaapi')

# All internal/external plugin configurations are loaded from here
defaults['kaapi']['plugin_config_dir'] = '/etc/kaapi/plugins.d'

# External plugins (generally, do not ship with application code)
defaults['kaapi']['plugin_dir'] = '/var/lib/kaapi/plugins'

# External templates (generally, do not ship with application code)
defaults['kaapi']['template_dir'] = '/var/lib/kaapi/templates'

class KaapiApp(CementApp):
    class Meta:
        label = 'kaapi'
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = 'kaapi.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = 'kaapi.cli.plugins'

        # Internal templates (ship with application code)
        template_module = 'kaapi.cli.templates'

        # Adding extensions, using mustache for simplicity
        #extensions = ['mustache']

        # call sys.exit() when app.close() is called
        exit_on_close = True



class KaapiTestApp(KaapiApp):
    """A test app that is better suited for testing."""
    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = KaapiApp()

def main():
    with app:
        try:

            # Disable not root access here itself
            if not os.geteuid() == 0:
                print("\nroot or sudo access required \n for running this program \n")
                # Consider this is as an uncaught error and exist with code 1
                app.close(1)
            
            app.run()
        
        except exc.KaapiError as e:
            # Catch our application errors and exit 1 (error)
            print('KaapiError > %s' % e)
            app.exit_code = 1
            
        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1
            
        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
