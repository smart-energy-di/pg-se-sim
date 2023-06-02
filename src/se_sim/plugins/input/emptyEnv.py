from typing import Any

from se_sim.utils.log_loggers import PLUGIN_LOG


def initialize(data_inp: dict[str, Any], plugin_params: dict[str, str],
               runtime_infos: dict[str, Any]) -> dict[str, Any]:
    PLUGIN_LOG.debug(f'none.none params:{plugin_params}')
    initDict: dict[str, Any] = {'history': [],
                                'data': None,
                                'data_type': None}
    return initDict
