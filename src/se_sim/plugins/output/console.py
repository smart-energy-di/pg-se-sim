import pprint
import sys
from typing import Any

from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG


class StdOut(PluginBase):
    def trans(self, outp: dict[str, Any]) -> dict[str, Any]:
        PLUGIN_LOG.debug("out.StdOut.trans()")
        if 'pretty' in self.call_params:
            pprint.pprint(outp, sys.stdout)
        else:
            print(outp, file=sys.stdout)
        return outp
