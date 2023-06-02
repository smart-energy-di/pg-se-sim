from typing import Any

from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


class Volume(PluginBase):
    def trans(self, env: dict[str, Any]) -> dict[str, Any]:
        inp_key = self.call_params.get('inp_key', 'data')
        outp_key = self.call_params.get('outp_key', 'data')
        PLUGIN_LOG.debug("calc.Volume.trans()")
        result = dict()
        for p in env[inp_key]:
            (length_str, width_str, height_str) = p.lwh
            volume = Q_(length_str) * Q_(width_str) * Q_(height_str)
            result[str(p.uuid)] = str(volume.to_base_units())
        env[outp_key] = result
        env[f"{outp_key}_type"] = "calc.Volume"
        return env
