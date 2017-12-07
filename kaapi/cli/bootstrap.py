"""Kaapi bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as KaapiBaseController.

from kaapi.cli.controllers.base import KaapiBaseController
from kaapi.cli.controllers.magic import KaapiMagicController
from kaapi.cli.controllers.remove import KaapiRemoveController
from kaapi.cli.controllers.update import KaapiUpdateController

def load(app):
    app.handler.register(KaapiBaseController)
    app.handler.register(KaapiMagicController)
    app.handler.register(KaapiRemoveController)
    app.handler.register(KaapiUpdateController)