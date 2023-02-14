from typing import Any

from se_sim.utils.log_loggers import PLUGIN_LOG


class PluginBase:
    def __init__(self, call_params: dict[str, str],
                 runtime_infos: dict[str, Any]) -> None:
        PLUGIN_LOG.debug("PluginBase '%s'", str(self))
        PLUGIN_LOG.debug("    call_params: '%s'", str(call_params))
        PLUGIN_LOG.debug("    runtime_infos: '%s'", str(runtime_infos))
        self.call_params = call_params
        self.runtime_infos = runtime_infos
