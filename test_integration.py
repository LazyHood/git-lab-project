import unittest
import os

# Загружаем calculator.py напрямую
calc_path = os.path.join(os.path.dirname(__file__), 'calculator.py')
with open(calc_path) as f:
    exec(f.read(), globals())

class TestIntegration(unittest.TestCase):
    
    def test_complex_calculation(self):
        # (10 + 5) * 2 - 6 / 3
        step1 = add(10, 5)
        step2 = multiply(step1, 2)
        step3 = divide(6, 3)
        result = subtract(step2, step3)
        self.assertEqual(result, 28)
    
    def test_average_calculation(self):
        numbers = [10, 20, 30, 40, 50]
        total = sum([add(0, num) for num in numbers])
        average = divide(total, len(numbers))
        self.assertEqual(average, 30)
    
    def test_operation_chain(self):
        result = 100
        result = subtract(result, 20)
        result = multiply(result, 2)
        result = divide(result, 4)
        result = add(result, 10)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
