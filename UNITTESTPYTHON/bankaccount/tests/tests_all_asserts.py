import unittest

class AllAssertsTests(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true(self):
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("I_am_not_a_number")
    def test_assert_in(self):
        self.assertIn(10, [1, 2, 10])
        self.assertNotIn(10, ["a", 4])

    def test_assert_dicts(self):
        user = {
            "User_name": "Andres", 
            "user_last_name" : "Marquez"
        }
        self.assertDictEqual({
            "User_name": "Andres", 
            "user_last_name" : "Marquez"
        }, user)

    def test_assert_set(self):
        user = { 1,2,3}
        self.assertSetEqual({ 1,2,3}, user)