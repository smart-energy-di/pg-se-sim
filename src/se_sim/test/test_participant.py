import unittest
from uuid import UUID

from se_sim.model.participant import Participant


class SimObjectTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.participant = Participant(el_role='no_role',
                                       en_title='en_title',
                                       de_title='de_title',
                                       lwh=("1m", "1m", "1m"))

    def test_01(self) -> None:
        self.assertEqual(type(self.participant), Participant)
        self.assertEqual(str(type(self.participant)),
                         "<class 'se_sim.model.participant.Participant'>")

    def test_obj_has_valid_uuid(self) -> None:
        uuid_obj = UUID(str(self.participant._uuid))
        self.assertEqual(str(uuid_obj),
                         str(self.participant._uuid))

    def test_obj_has_role(self) -> None:
        self.assertEqual(self.participant.el_role, 'no_role')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
