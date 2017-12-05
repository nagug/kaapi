"""Kaapi bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as KaapiBaseController.

from kaapi.cli.controllers.base import KaapiBaseController

def load(app):
    app.handler.register(KaapiBaseController)
