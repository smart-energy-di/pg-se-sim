import uuid

from se_sim.utils.log_loggers import MODEL_LOG


class SeObject:
    """
    A base object for simulation tasks in the smart-energy-di framework
    """

    def __init__(self) -> None:
        self._uuid = uuid.uuid4()
        MODEL_LOG.debug(f"create base object (uuid:'{self._uuid}')")

    @property
    def uuid(self) -> uuid.UUID:
        return self._uuid
