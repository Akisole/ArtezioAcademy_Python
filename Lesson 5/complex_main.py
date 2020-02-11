"""main.py for complex numbers"""

from complex import Complex


def test_complex(num_a: Complex, num_b: Complex):
    """Tests for two complex numbers"""

    print(num_a + num_b)
    print(num_a - num_b)
    print(num_a * num_b)
    print(num_a / num_b)
    print(abs(num_a))
    print(abs(num_b))


NUMBER_ONE = input()
NUMBER_TWO = input()

NUMBER_ONE = Complex(int(NUMBER_ONE[:NUMBER_ONE.find(' ')]),
                     int(NUMBER_ONE[NUMBER_ONE.find(' '):]))
NUMBER_TWO = Complex(int(NUMBER_TWO[:NUMBER_TWO.find(' ')]),
                     int(NUMBER_TWO[NUMBER_TWO.find(' '):]))

test_complex(NUMBER_ONE, NUMBER_TWO)
