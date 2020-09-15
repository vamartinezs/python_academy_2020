from week2.simple_promo_class_exercise.Promo import *
from unittest.mock import patch


# Mocking Exercises
def test_product_has_expirated():
    # Returns true in case the product has expired
    with patch.object(Promo, 'has_expired', return_value="True"):
        assert instantiate_promo() == "True"


def test_product_name():
    # Returns true if both names are equal
    with patch.object(Promo, 'get_name', return_value="Candy"):
        assert instantiate_promo_name() == "Candy"


def test_product_expiration_date():
    # Returns the comparison among two dates in datetime objects
    with patch.object(Promo, 'get_expiration_date', return_value=datetime(month=3, year=2020, day=1)):
        assert not instantiate_promo_expiration_date() == datetime(year=2019, day=14, month=2)


if __name__ == '__main__':
    test_product_has_expirated()
    test_product_name()
    test_product_expiration_date()
