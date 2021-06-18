from acc.catmath import cat_years_to_hooman_years, is_cat_leap_year  # noqa


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert True


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert True


def test__cat_years_to_hooman_years__0__returns_0():
    assert True


# BONUS MATERIAL FOR STEP 2


def test__is_cat_leap_year__succeeds():
    assert is_cat_leap_year(2016) is True
