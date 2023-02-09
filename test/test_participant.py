import unittest
from uuid import UUID

from model.participant import Participant


class SimObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.participant = Participant(el_role='no_role',
                                       en_title='en_title',
                                       de_title='de_title')

    def test_01(self):
        self.assertEqual(type(self.participant), Participant)
        self.assertEqual(str(type(self.participant)),
                         "<class 'model.participant.Participant'>")

    def test_obj_has_valid_uuid(self):
        uuid_obj = UUID(str(self.participant._uuid))
        self.assertEqual(str(uuid_obj),
                         str(self.participant._uuid))

    def test_obj_has_role(self):
        self.assertEqual(self.participant.el_role, 'no_role')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
