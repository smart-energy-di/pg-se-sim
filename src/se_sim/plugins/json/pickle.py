import json
import sys
import uuid
from typing import IO, Any

import jsonpickle

from se_sim.model.participant import ParticipantEncoder
from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG

class DDD(jsonpickle.handlers.UUIDHandler):
    def flatten(self, obj, data):
        return str(obj)

    def restore(self, data):
        return uuid.UUID(data)


jsonpickle.handlers.registry.register(uuid.UUID, DDD)



class StdOut(PluginBase):
    def output(self, outp: Any, fp: IO) -> None:
        jsonpickle.handlers.register(DDD)
        simulation = outp['v0simulation']
        if 'pretty' in self.call_params:
            print(jsonpickle.encode(simulation, indent=2, unpicklable=False),
                  file=fp)
        else:
            print(jsonpickle.encode(simulation), file=fp)

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
