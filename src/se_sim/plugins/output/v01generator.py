from typing import Any

from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG


class Generator(PluginBase):
    def trans(self, outp: dict[str, Any]) -> dict[str, Any]:
        PLUGIN_LOG.debug("example_generator.Generator.trans()")
        outp['history'].append("generator 4711")
        simulation = outp['v0simulation']
        if hasattr(simulation, 'generate'):
            simulation.generate()
        return outp
