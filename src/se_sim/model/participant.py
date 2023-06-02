from typing import Any, Tuple
from se_sim.generator.participant import GenParticipant
from se_sim.model.simobject import SeObject
from se_sim.utils.log_loggers import MODEL_LOG


class Participant(SeObject, GenParticipant):
    """
    A general participant in the Smart Energy Simulation
    """

    def __init__(self, el_role: str, en_title: str, de_title: str,
                 lwh: Tuple[str, str, str]) -> None:
        SeObject.__init__(self)
        GenParticipant.__init__(self)
        self.el_role = el_role
        self.en_title = en_title
        self.de_title = de_title
        # Length Width Height
        self.lwh = lwh
        MODEL_LOG.debug(f"New '{el_role}' object (en:'{en_title}')")

    def as_dict(self) -> dict[str, Any]:
        return {
            "uuid": str(self.uuid),
            "el_role": self.el_role,
            "en_title": self.en_title,
            "de_title": self.de_title,
            "lwh": self.lwh,
        }
