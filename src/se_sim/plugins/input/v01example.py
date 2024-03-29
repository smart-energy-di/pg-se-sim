from typing import Any

from se_sim.simulation.simulation import Simulation
from se_sim.utils.log_loggers import PLUGIN_LOG


def read(data_inp: dict[str, Any], plugin_params: dict[str, str],
         runtime_infos: dict[str, Any]) -> dict[str, Any]:
    PLUGIN_LOG.debug(f'example_objs.import_objs params:{plugin_params}')
    simulation = Simulation()
    simulation.create_objects()
    data_inp['history'].append("created data 0815")
    data_inp['data'] = simulation
    data_inp['data_type'] = 'v0simulation'
    return data_inp


def fileread(data_inp: dict[str, Any], plugin_params: dict[str, str],
             runtime_infos: dict[str, Any]) -> dict[str, Any]:
    PLUGIN_LOG.debug(f'v01example.fileread params:{plugin_params}')
    if 'filename' in plugin_params:
        filename = plugin_params['filename']
        simulation = Simulation()
        simulation.create_from_json(filename)
        data_inp['history'].append(
            f"created by fileread with file:'{filename}'")
        data_inp['data'] = simulation
        data_inp['data_type'] = 'v0simulation'
    return data_inp
