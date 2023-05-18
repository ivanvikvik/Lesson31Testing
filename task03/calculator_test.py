import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        # print("***** setUp *****")
        self.calc = Calculator()

    def tearDown(self):
        # print("***** tearDown *****")
        del self.calc

    def testAddPositive(self):
        # print("testAddPositive")
        a = 5
        b = 6
        expected = 11

        actual = self.calc.add(a, b)

        self.assertEqual(expected, actual)

    def testSubPositive(self):
        # print("testSubPositive")
        a = 5
        b = 6
        expected = -1

        actual = self.calc.sub(a, b)

        self.assertEqual(expected, actual)

    def testMulPositive(self):
        # print("testMulPositive")
        a = 5
        b = 6
        expected = 30

        actual = self.calc.mul(a, b)

        self.assertEqual(expected, actual)

    def testDivPositive(self):
        # print("testDivPositive")
        a = 10
        b = 2
        expected = 5

        actual = self.calc.div(a, b)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
