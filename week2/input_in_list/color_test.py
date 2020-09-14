from unittest.mock import patch

from week2.input_in_list.Colors import instantiate_color
from week2.input_in_list.Colors import Colors


def test_color_blue():
    # mock an object of class
    with patch.object(Colors, 'get_color', return_value="blue"):
        assert instantiate_color() == "blue"

def test_color_yellow():
    with patch.object(Colors, 'get_color', return_value="yellow"):
        assert instantiate_color() == "yellow"

def test_color_black():
    with patch.object(Colors, 'get_color', return_value="Not a valid color"):
        assert instantiate_color() == "Not a valid color"

def test_exit_option():
    with patch.object(Colors, 'get_color', return_value="bye"):
        assert instantiate_color() == "bye"


if __name__ == '__main__':
    test_color_blue()
    test_color_yellow()
    test_color_black()
    test_exit_option()
