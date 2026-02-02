import math_utils
import string_utils
import Shop_package.discuount as disc
from Shop_package.billing import calculate_total

print(math_utils.add(10, 20))
print(math_utils.subs(30,20))
print(math_utils.square(10))

from math_utils import add
print(add(100, 200))

print(string_utils.capitilize_word("india"))
print(string_utils.reverse_string("india"))
print(string_utils.word_count("india"))

print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))
print(calculate_total([1000, 200,4000,5000]))
