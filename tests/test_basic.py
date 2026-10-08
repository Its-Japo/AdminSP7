import pytest

from mathlib import square, factorial, is_prime, gcd, lcm


class TestSquare:
    def test_positive_integer(self):
        assert square(4) == 16

    def test_negative_integer(self):
        assert square(-3) == 9

    def test_float(self):
        assert square(1.5) == pytest.approx(2.25)

    def test_zero(self):
        assert square(0) == 0

    @pytest.mark.parametrize("bad", ["4", None, [2], True])
    def test_invalid_type_raises(self, bad):
        with pytest.raises(TypeError):
            square(bad)


class TestFactorial:
    def test_small_number(self):
        assert factorial(5) == 120

    def test_larger_number(self):
        assert factorial(10) == 3628800

    def test_zero_and_one(self):
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)

    @pytest.mark.parametrize("bad", [2.5, "5", None])
    def test_invalid_type_raises(self, bad):
        with pytest.raises(TypeError):
            factorial(bad)


class TestIsPrime:
    @pytest.mark.parametrize("n", [2, 3, 5, 13, 97, 7919])
    def test_primes(self, n):
        assert is_prime(n) is True

    @pytest.mark.parametrize("n", [4, 9, 15, 25, 100, 7917])
    def test_composites(self, n):
        assert is_prime(n) is False

    @pytest.mark.parametrize("n", [1, 0, -7])
    def test_less_than_two_is_not_prime(self, n):
        assert is_prime(n) is False

    @pytest.mark.parametrize("bad", [7.0, "7", None])
    def test_invalid_type_raises(self, bad):
        with pytest.raises(TypeError):
            is_prime(bad)


class TestGcd:
    def test_common_divisor(self):
        assert gcd(12, 18) == 6

    def test_coprime(self):
        assert gcd(17, 5) == 1

    def test_with_zero(self):
        assert gcd(0, 9) == 9

    def test_negative_numbers(self):
        assert gcd(-12, 18) == 6

    def test_both_zero_raises(self):
        with pytest.raises(ValueError):
            gcd(0, 0)

    def test_invalid_type_raises(self):
        with pytest.raises(TypeError):
            gcd(12.0, 18)


class TestLcm:
    def test_common_multiple(self):
        assert lcm(4, 6) == 12

    def test_coprime(self):
        assert lcm(7, 5) == 35

    def test_negative_numbers(self):
        assert lcm(-4, 6) == 12

    def test_zero_raises(self):
        with pytest.raises(ValueError):
            lcm(0, 5)

    def test_invalid_type_raises(self):
        with pytest.raises(TypeError):
            lcm("4", 6)
