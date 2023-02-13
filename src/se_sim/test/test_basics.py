import unittest
from uuid import UUID

from se_sim.model.simobject import SeObject


class SimObjectTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.seObject = SeObject()

    def test_01(self) -> None:
        self.assertEqual(type(self.seObject), SeObject)
        self.assertEqual(str(type(self.seObject)),
                         "<class 'se_sim.model.simobject.SeObject'>")

    def test_obj_has_valid_uuid(self) -> None:
        uuid_obj = UUID(str(self.seObject._uuid))  # direct
        self.assertEqual(str(uuid_obj),
                         str(self.seObject.uuid))  # getter


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
