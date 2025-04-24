import unittest

SERVER = "server_b"
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
    
    @unittest.skip("Work in progress, we will enable soon")
    def test_skip(self):
        self.assertEqual("Hola", "bye")

    @unittest.skipIf(SERVER == "server_b", "Skipped because we are not in the server")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100 == 150)