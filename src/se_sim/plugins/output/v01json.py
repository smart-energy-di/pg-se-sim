import json
from typing import Any

from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG


def SimJsonDefault(obj: Any) -> Any:
    if hasattr(obj, 'as_dict'):
        return obj.as_dict()
    return str(obj)


class Json(PluginBase):
    def trans(self, env: dict[str, Any]) -> dict[str, Any]:
        if 'key' in self.call_params:
            key = self.call_params['key']
            PLUGIN_LOG.debug(f"out.Json.trans(key={key})")
            out_dict = {
                key: env[key]
            }
        else:
            PLUGIN_LOG.debug("out.Json.trans()")
            out_dict = env
        print(json.dumps(out_dict, default=SimJsonDefault, indent=2))
        return env
