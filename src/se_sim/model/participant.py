from json import JSONEncoder

from se_sim.generator.participant import GenParticipant
from se_sim.model.simobject import SeObject
from se_sim.utils.log_loggers import MODEL_LOG


class Participant(SeObject, GenParticipant):
    """
    A general participant in the Smart Energy Simulation
    """

    def __init__(self, el_role: str, en_title: str, de_title: str) -> None:
        SeObject.__init__(self)
        GenParticipant.__init__(self)
        self._el_role = el_role
        self._en_title = en_title
        self._de_title = de_title
        MODEL_LOG.debug(f"New '{el_role}' object (en:'{en_title}')")

    @property
    def el_role(self) -> str:
        return self._el_role

    @property
    def de_title(self) -> str:
        return self._de_title

    @property
    def en_title(self) -> str:
        return self._en_title


class ParticipantEncoder(JSONEncoder):
    def default(self, o):
        return {
            'uuid': str(o.uuid),
            'el_role': o.el_role,
            'de_title': o.de_title,
            'en_title': o.en_title,
        }
