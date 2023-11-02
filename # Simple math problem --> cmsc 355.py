# Simple math problem --> cmsc 355

# pieces of gum adrianna has to begin with
initial_gumA = 10

strawberry_gum = 70
bubble_gum = 10

total_gum = initial_gumA + strawberry_gum + bubble_gum
print('Adrianna has a total of:',total_gum, 'pieces of gum!')


## two unit tests for the code above


import unittest

def calculate_total_gum(initial_gum, strawberry_gum, bubble_gum):
    return initial_gum + strawberry_gum + bubble_gum

class TestCalculateTotalGum(unittest.TestCase):
    def test_total_gum_with_positive_values(self):
        result = calculate_total_gum(10, 70, 10)
        self.assertEqual(result, 90)

    def test_total_gum_with_zero_values(self):
        result = calculate_total_gum(0, 0, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()

