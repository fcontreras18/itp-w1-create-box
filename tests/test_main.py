import unittest

# For an extra challenge, make it so only the outer border of the box shows 
# and it is not filled in. Make this a separate function and add unit tests for it.

from create_box import create_box
from create_box import create_outer_border

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = """
$$$$$$
$    $
$    $
$    $
$    $
$$$$$$
""".lstrip()

fifth_box_expected = """
#####
#   #
#   #
#   #
#   #
#   #
#####
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_third_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)
        
        
class TestCreateBorderBox(unittest.TestCase):
    def test_border_box(self):
        self.assertEqual(create_outer_border(6, 6, '$'), fourth_box_expected)
    
    def test_border_box2(self):
        self.assertEqual(create_outer_border(7, 5, '#'), fifth_box_expected)
    # Add your own test using third_box_expected
