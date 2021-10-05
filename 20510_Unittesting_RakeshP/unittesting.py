import unittest
from validate import validateUP


class Validtest(unittest.TestCase):
    def testval1(self):
        self.assertEqual(validateUP('Rakesh', 'Rakesh@123'), True)

    def testval2(self):
        self.assertEqual(validateUP(22, 'Rakesh@123'), False)

    def testval3(self):
        self.assertEqual(validateUP('RakeshP', 'Rakesh12'), False)

    def testval4(self):
        self.assertEqual(validateUP('Rake', 'R'), False)

    def testval5(self):
        self.assertEqual(validateUP('Rakesh', 'rakesh@123'), False)

    def testval6(self):
        self.assertEqual(validateUP('Rakesh', 21325), False)

    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Teardown")

    @classmethod
    def setUpClass(self) -> print("setup class"):
        pass

    @classmethod
    def tearDownClass(self) -> print("teardown"):
        pass

    if __name__ == '__main__':
        unittest.main()
