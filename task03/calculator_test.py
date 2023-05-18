import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def testAddPositive(self):
        # print("testAddPositive")
        a = 5
        b = 6
        expected = 11

        calc = Calculator()
        actual = calc.add(a, b)

        self.assertEqual(expected, actual)

    def testSubPositive(self):
        print("testSubPositive")
        a = 5
        b = 6
        expected = -1

        calc = Calculator()
        actual = calc.sub(a, b)

        self.assertEqual(expected, actual)

    def testMulPositive(self):
        print("testMulPositive")
        a = 5
        b = 6
        expected = 30

        calc = Calculator()
        actual = calc.mul(a, b)

        self.assertEqual(expected, actual)

    def testDivPositive(self):
        # print("testDivPositive")
        a = 10
        b = 2
        expected = 5

        calc = Calculator()
        actual = calc.div(a, b)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
