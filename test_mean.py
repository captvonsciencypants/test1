
from mean import calc_mean


# Test functions

def test_int():
	num_list = [1, 2, 3, 4, 5]

	observed = calc_mean(num_list)
	expected = 3

	assert observed == expected


def test_zero():
	num_list = [0]

	observed = calc_mean(num_list)
	expected = 0

	assert observed == expected


def test_double():
	num_list = [1, 2, 3, 4]

	observed = calc_mean(num_list)
	expected = 2.5

	assert observed == expected


def test_long():
    big_number = 100000

    observed = calc_mean(range(1,big_number))
    expected = big_number/2.0

    assert observed == expected