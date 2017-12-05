"""CLI tests for kaapi."""

from kaapi.utils import test

class CliTestCase(test.KaapiTestCase):
    def test_kaapi_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
