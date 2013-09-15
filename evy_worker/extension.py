import logging
import functools
import stevedore

def extensions_is_enable(config, logger, ext):
    enable = True
    if enable:
        logger.info('loading extension: %s', ext.name)
    return enable

config = {}
logger = logging.getLogger()



def invoke_plugin(name, *args, **kwargs):
    em = stevedore.enabled.EnabledExtensionManager(
        'evy.extensions',
        functools.partial(extensions_is_enable, config, logger),
        invoke_on_load=True
    )
    extensions = {}
    for ext in em:
        extensions[ext.name] = ext.obj

    print extensions

    extensions[name].run(*args, **kwargs)

    print name, args, kwargs
    return True
