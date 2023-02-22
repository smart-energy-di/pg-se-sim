import unittest
from uuid import UUID

from se_sim.plugins.json.pickle import UUIDHandler


class SimObjectTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.uuidHandler = UUIDHandler(context=None)
        self.test_uuid = UUID("7e233b2a-f915-4ec6-8f30-e5c9236bc164")
        self.test_str = "7e233b2a-f915-4ec6-8f30-e5c9236bc164"

    def test_str2uuid(self) -> None:
        self.assertEqual(
            self.uuidHandler.restore(self.test_str),
            self.test_uuid)

    def test_uuid2str(self) -> None:
        self.assertEqual(
            self.uuidHandler.flatten(self.test_uuid, data={}),
            self.test_str)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
