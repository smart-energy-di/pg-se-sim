from generator.participant import GenParticipant
from model.simobject import SeObject
from utils.log_loggers import MODEL_LOG


class Participant(SeObject, GenParticipant):
    """
    A general participant in the Smart Energy Simulation
    """

    def __init__(self, el_role, en_title, de_title):
        SeObject.__init__(self)
        GenParticipant.__init__(self)
        self._el_role = el_role
        self._en_title = en_title
        self._de_title = de_title
        MODEL_LOG.debug(f"New '{el_role}' object (en:'{en_title}')")

    @property
    def el_role(self):
        return self._el_role

    @property
    def en_title(self):
        return self._en_title
