import sys
import uuid
from typing import IO, Any

import jsonpickle  # type: ignore

from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG


class UUIDHandler(jsonpickle.handlers.UUIDHandler):  # type: ignore
    def flatten(self, obj: uuid.UUID, data: dict[str, Any]) -> str:
        """
        Flatten `obj` into a json-friendly form and write result to `data`.

        :param object obj: The object to be serialized.
        :param dict data: A partially filled dictionary which will contain the
            json-friendly representation of `obj` once this method has
            finished.
        """
        return str(obj)

    def restore(self, data: str) -> uuid.UUID:
        return uuid.UUID(data)


jsonpickle.handlers.registry.register(uuid.UUID, UUIDHandler)


class StdOut(PluginBase):
    def output(self, outp: Any, fp: IO[str]) -> None:
        jsonpickle.handlers.register(UUIDHandler)
        simulation = outp['data']
        if 'pretty' in self.call_params:
            print(jsonpickle.encode(simulation, indent=2, unpicklable=False),
                  file=fp)
        else:
            print(jsonpickle.encode(simulation), file=fp)

    def trans(self, outp: dict[str, Any]) -> dict[str, Any]:
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
