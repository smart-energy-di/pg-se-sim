import builtins
import inspect
import json
import os
import sys
from types import ModuleType
from typing import Any, Optional
from urllib.parse import unquote

import yaml

from se_sim.utils.log_loggers import PLUGIN_LOG


class ErrorDuringImport(Exception):
    """Errors that occurred while trying to import something to document it."""

    def __init__(self, filename: Optional[str],
                 exc_info: tuple[Any, Any, Any]) -> None:
        self.filename = filename
        self.exc, self.value, self.tb = exc_info

    def __str__(self) -> str:
        exc = self.exc.__name__
        return 'problem in %s - %s: %s' % (self.filename, exc, self.value)


# flake8: noqa: C901
def safeimport(path: str, forceload: int = 0,
               cache: dict[str, ModuleType] = {}) -> Any:
    """Import a module; handle errors; return None if the module isn't found.

    If the module *is* found but an exception occurs, it's wrapped in an
    ErrorDuringImport exception and reraised.  Unlike __import__, if a
    package path is specified, the module at the end of the path is returned,
    not the package at the beginning.  If the optional 'forceload' argument
    is 1, we reload the module from disk (unless it's a dynamic extension)."""
    # noinspection PyPep8
    try:
        # If forceload is 1 and the module has been previously loaded from
        # disk, we always have to reload the module.  Checking the file's
        # mtime isn't good enough (e.g. the module could contain a class
        # that inherits from another module that has changed).
        if forceload and path in sys.modules:
            if path not in sys.builtin_module_names:
                # Remove the module from sys.modules and re-import to try
                # and avoid problems with partially loaded modules.
                # Also remove any submodules because they won't appear
                # in the newly loaded module's namespace if they're already
                # in sys.modules.
                subs = [m for m in sys.modules if m.startswith(path + '.')]
                for key in [path] + subs:
                    # Prevent garbage collection.
                    cache[key] = sys.modules[key]
                    del sys.modules[key]
        module = __import__(path)
    except:  # noqa
        # Did the error occur before or after the module was found?
        (exc, value, tb) = info = sys.exc_info()
        if path in sys.modules:
            # An error occurred while executing the imported module.
            raise ErrorDuringImport(sys.modules[path].__file__, info)
        elif exc is SyntaxError:
            # A SyntaxError occurred before we could execute the module.
            raise ErrorDuringImport(value.filename, info)  # type: ignore
        elif issubclass(exc,  # type: ignore
                        ImportError) and value.name == path:  # type: ignore
            # No such module in the path.
            return None
        else:
            # Some other error occurred during the importing process.
            raise ErrorDuringImport(path, sys.exc_info())
    for part in path.split('.')[1:]:
        try:
            module = getattr(module, part)
        except AttributeError:
            return None
    return module


def locate(path: str, forceload: int = 0) -> Any:
    """Locate an object by name or dotted path, importing as necessary."""
    parts = [part for part in path.split('.') if part]
    module, n = None, 0
    while n < len(parts):
        nextmodule = safeimport('.'.join(parts[:n + 1]), forceload)
        if nextmodule:
            module, n = nextmodule, n + 1
        else:
            break
    if module:
        l_object = module
    else:
        l_object = builtins
    for part in parts[n:]:
        try:
            l_object = getattr(l_object, part)
        except AttributeError:
            return None
    return l_object


def compute_files(data_out: dict[str, Any], first_plugin: bool,
                  last_plugin: bool, plugin: Any) -> dict[str, Any]:
    if first_plugin and os.path.isfile(plugin):
        f = open(plugin, "r")
        plugin_raw = f.read()
        if plugin[-5:] == '.json':
            data_out['data'] = json.loads(plugin_raw)
        if plugin[-5:] == '.yaml':
            data_out['data'] = yaml.load(plugin_raw, yaml.SafeLoader)
        PLUGIN_LOG.debug('first data_out: {}'.format(data_out))
    elif last_plugin:
        PLUGIN_LOG.debug('last data_out: {}'.format(data_out))
        f = open(plugin, "w")
        if plugin[-5:] == '.json':
            json.dump(data_out['data'], f,
                      indent=4,
                      sort_keys=True)
        if plugin[-5:] == '.yaml':
            yaml.dump_all(data_out['data'], f,
                          indent=4,
                          default_flow_style=False)
            f.close()
        else:
            PLUGIN_LOG.error("plugin or file '{}' not correct".format(plugin))
    return data_out


def compute_class(data_inp: dict[str, Any],
                  data_out: dict[str, Any],
                  plugin_obj: Any,
                  plugin_params: dict[str, str],
                  runtime_infos: dict[str, Any]) -> dict[str, Any]:
    converter = plugin_obj(plugin_params, runtime_infos)
    PLUGIN_LOG.debug('new plugin: {}'.format(converter))
    data_out = converter.trans(data_inp)
    return data_out


def compute_plugin(data_inp: dict[str, Any],
                   data_out: dict[str, Any],
                   first_plugin: bool,
                   last_plugin: bool, plugin: Any,
                   plugin_obj: Any, plugin_params: dict[str, str],
                   runtime_infos: dict[str, Any]) -> dict[str, Any]:
    if inspect.isclass(plugin_obj):
        data_out = compute_class(data_inp, data_out, plugin_obj,
                                 plugin_params,
                                 runtime_infos)
    elif inspect.isfunction(plugin_obj):
        data_out = plugin_obj(data_inp, plugin_params, runtime_infos)
    elif type(plugin_obj) is dict:
        data_out = plugin_obj
        PLUGIN_LOG.debug('first data_out: {}'.format(data_out))
    if plugin_obj is None:
        data_out = compute_files(data_out, first_plugin, last_plugin,
                                 plugin)
    return data_out


def get_plugin_params(plugin: str, plugin_parsed: list[str]) -> dict[str, str]:
    plugin_params = {}
    try:
        if len(plugin_parsed) > 1:
            params_list = plugin_parsed[1].split(',')
            for param_string in params_list:
                p_key, p_value = param_string.split('=')
                plugin_params[p_key] = unquote(p_value)
    except ValueError:
        PLUGIN_LOG.error(
            "plugin param should be in form of:  plugin:key1=value1,key2=value2")
        PLUGIN_LOG.error("your plugin param: '%s'", plugin)
        exit(1)
    PLUGIN_LOG.debug("your plugin params: '%s'", plugin_params)
    return plugin_params
