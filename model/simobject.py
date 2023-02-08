import uuid


class SeObject:
    """
    A base object for simulation tasks in the smart-energy-di framework
    """

    def __init__(self):
        self._uuid = uuid.uuid4()
