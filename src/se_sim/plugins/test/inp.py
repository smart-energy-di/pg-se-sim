from typing import Any

from se_sim.model.participant import Participant
from se_sim.plugins.base import PluginBase
from se_sim.utils.log_loggers import PLUGIN_LOG


class Test01(PluginBase):
    def trans(self, outp: dict[str, Any]) -> dict[str, Any]:
        PLUGIN_LOG.debug("test.inp.Test01.trans()")
        objList: list[Any] = [
            Participant(
                el_role='consumer',
                en_title='oven',
                de_title='Backofen',
                lwh=("0.57 m", "0.59 m", "0.595 m"))
        ]
        testDict: dict[str, Any] = {'history': [],
                                    'data': objList,
                                    'data_type': 'v0simulation'}
        outp.update(testDict)
        return outp
