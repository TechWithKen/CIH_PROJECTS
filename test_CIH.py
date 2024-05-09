import unittest
import CIH

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(CIH.add(10, 89), 99)

	def test_subtract(self):
		self.assertEqual(CIH.subtract(89, 10), 79)

	def test_multiply(self):
		self.assertEqual(CIH.multiply(10, 89), 890)

	def test_divide(self):
		self.assertEqual(CIH.divide(90, 10), 9)



if __name__ == "__main__":
	unittest.main()