import json
import sys
from typing import IO, Any

from se_sim.model.participant import ParticipantEncoder
from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG


class StdOut(PluginBase):
    def output(self, outp: Any, fp: IO) -> None:
        simulation = outp['v0simulation']
        if 'pretty' in self.call_params:
            print(
                json.dumps(simulation, cls=ParticipantEncoder, sort_keys=True,
                           indent=2,
                           ensure_ascii=False),
                file=fp)
        else:
            print(json.dumps(simulation, cls=ParticipantEncoder), file=fp)

    def trans(self, outp):
        try:
            if 'out' in self.call_params:
                f = open(self.call_params['out'], "w")
                self.output(outp, f)
                f.close()
            else:
                self.output(outp, sys.stdout)
        except OSError as err:
            PLUGIN_LOG.error(err)
            exit(1)
        return outp
