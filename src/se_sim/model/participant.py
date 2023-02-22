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
        self.el_role = el_role
        self.en_title = en_title
        self.de_title = de_title
        MODEL_LOG.debug(f"New '{el_role}' object (en:'{en_title}')")
