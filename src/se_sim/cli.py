#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""smart energy simulator CLI.
"""

import sys
from typing import Any

import click

from se_sim.utils import cli_utils
from se_sim.utils.log_loggers import PLUGIN_LOG
from se_sim.utils.log_utils import add_loggers


@click.command()
@click.version_option(version='0.0.1-alpha')
@click.argument('plugins', nargs=-1)
@click.option('--dm', default=0, count=True,
              help='Show model debug information (maybe multiple).')
@click.option('--dp', default=0, count=True,
              help='Show plugins debug information (maybe multiple).')
@click.option('--de', default=0, count=True,
              help='Show event debug information (maybe multiple).')
@click.option('--ds', default=0, count=True,
              help='Show simulation debug information (maybe multiple).')
def main(plugins: list[str], dm: int, dp: int, de: int, ds: int) -> int:
    add_loggers(dm, dp, de, ds)
    if len(plugins) < 2:
        PLUGIN_LOG.error("less than 2 plugins")
        exit(1)
    PLUGIN_LOG.info("Program start")
    runtime_infos: dict[str, Any] = {}
    data_out: dict[str, Any] = {'history': [],
                                'data': None,
                                'data_type': 'v0simulation'}

    for plugin in plugins:
        PLUGIN_LOG.debug("-" * 60)
        PLUGIN_LOG.debug(f"Plugin: '{plugin}'")
        data_inp = data_out
        first_plugin = plugins.index(plugin) == 0
        last_plugin = plugins.index(plugin) + 1 == len(plugins)
        # cast :
        plugin = plugin.replace('\\:', '##&&##')
        plugin_parsed = plugin.split(':')
        # cast back:
        plugin_parsed = [i.replace('##&&##', ':') for i in plugin_parsed]
        plugin_name = plugin_parsed[0]
        PLUGIN_LOG.debug("PLUGIN '{}'".format(plugin_name))
        plugin_params = cli_utils.get_plugin_params(plugin, plugin_parsed)
        PLUGIN_LOG.debug(f"   params '{plugin_params}'")
        plugin_obj = cli_utils.locate(plugin_name)
        if plugin_obj is None:
            PLUGIN_LOG.error("PLUGIN '{}' not found".format(plugin_name))
            exit(1)
        data_out = cli_utils.compute_plugin(data_inp, data_out, first_plugin,
                                            last_plugin, plugin, plugin_obj,
                                            plugin_params,
                                            runtime_infos)
        PLUGIN_LOG.debug("f:{} l:{} plugin_obj: {} / '{}'".format(
            first_plugin,
            last_plugin,
            type(plugin_obj),
            plugin
        ))
    PLUGIN_LOG.info("Program exit")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
