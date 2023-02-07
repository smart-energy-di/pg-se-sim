#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""smart energy simulator CLI.
"""

import sys

import click

from simulation.create_objects import createSimObjects
from simulation.statistics import debug_general_statistic, debug_roles
from utils.log_loggers import PLUGIN_LOG
from utils.log_utils import add_loggers

AllSimObjects = set()


@click.command()
@click.version_option(version='0.0.1-alpha')
@click.option('--dm', default=0, count=True,
              help='Show model debug information (maybe multiple).')
@click.option('--dp', default=0, count=True,
              help='Show plugins debug information (maybe multiple).')
@click.option('--de', default=0, count=True,
              help='Show event debug information (maybe multiple).')
@click.option('--ds', default=0, count=True,
              help='Show simulation debug information (maybe multiple).')
def main(dm, dp, de, ds):
    add_loggers(dm, dp, de, ds)
    createSimObjects(AllSimObjects)
    debug_general_statistic(AllSimObjects)
    debug_roles(AllSimObjects)
    PLUGIN_LOG.info("Program exit")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
