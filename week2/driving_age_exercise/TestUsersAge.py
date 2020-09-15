import unittest
from week2.driving_age_exercise.Register import Register


class TestUsersAge(unittest.TestCase):

    UNIVERSAL_MINIMAL_DRIVING_AGE = 16

    def setUp(self): # Load drivers registers
        self.driver_register = Register()
        self.driver_register.load()

    def test_user_driving_record_1(self): # Juan López - 33 - Can drive
         self.assertEqual(self.driver_register.people[0].is_allowed_to_drive(self.UNIVERSAL_MINIMAL_DRIVING_AGE), True)

    def test_user_driving_record_2(self): # Ana Méndez - 40 - Can drive
        self.assertEqual(self.driver_register.people[1].is_allowed_to_drive(self.UNIVERSAL_MINIMAL_DRIVING_AGE), True)

    def test_user_driving_record_3(self): # Juan López - 33 - Can drive
        self.assertEqual(self.driver_register.people[2].is_allowed_to_drive(self.UNIVERSAL_MINIMAL_DRIVING_AGE), True)

    def test_user_driving_record_4(self): # Sara Castano - 18 -Can drive
        self.assertEqual(self.driver_register.people[3].is_allowed_to_drive(self.UNIVERSAL_MINIMAL_DRIVING_AGE), True)

    def test_user_driving_record_5(self): # Pepito Perez - 5 - Can't drive
        self.assertEqual(self.driver_register.people[4].is_allowed_to_drive(self.UNIVERSAL_MINIMAL_DRIVING_AGE), False)


if __name__ == '__main__':
    unittest.main()