import math_utils as mt   # import all in the file
from django_course.fundamentals import my_packages
from django_course.fundamentals.math_utils import addition #import specifics functions (is more fast if the module is too big)
from my_packages import messages

# a module is an only file
# a package is a directory with some modules files

result = mt.addition(1, 2)
print(result)

print(messages.greet("Daniel"))
print(messages.bye("Daniel"))