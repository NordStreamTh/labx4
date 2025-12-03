import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
        
    def test_area_positive(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        
    def test_area_negative(self):
        self.assertEqual(area(-3), 9)
        
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3), -12)

if __name__ == "__main__":
    unittest.main()
