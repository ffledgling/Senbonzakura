#Calling this oddity because we don't want to override the built-in expcetions module
from exceptions import Exception

class DownloadError(Exception):
    """ Class for errors raised when downloading a resource fails """
    pass

class DBError(Exception):
    """ Class for all Database related Errors """
    pass

class CacheMissError(Exception):
    """ Class for errors raised while trying to access non-existant cache
        resources """
    pass

class CacheCollisionError(Exception):
    """ Class for errors raised upon collisions in cache """
    pass

class CacheError(Exception):
    """ Class for generic cache related errors """
    pass

class NotImplementedError(Exception):
    """ Exception raised for functions/classes not implemented yet """
    pass

class ConfigError(Exception):
    """ Exception raised for missing or invalid configuration """
    pass
class ToolError(Exception):
    """ Exception raised for problems during tooling setup """
    pass
