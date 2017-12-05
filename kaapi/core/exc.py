"""Kaapi exception classes."""

class KaapiError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class KaapiConfigError(KaapiError):
    """Config related errors."""
    pass

class KaapiRuntimeError(KaapiError):
    """Generic runtime errors."""
    pass

class KaapiArgumentError(KaapiError):
    """Argument related errors."""
    pass
