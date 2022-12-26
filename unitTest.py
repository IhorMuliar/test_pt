import unittest
import functionAS as app

class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = app
    
    def test_function(self):
        self.assertEqual(app.functionAS(1), 4)
        self.assertEqual(app.functionAS(2), 11)
        self.assertEqual(app.functionAS(3), 21)

if __name__ == '__main__':
    unittest.main()