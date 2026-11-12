import Lab2.bmi as bmi

print("Test_bmi")

def test_bmi_normal_weight():
    result = ()
    test = (19.531249999999996, 0)

    result = bmi.calculate_bmi(height=1.60, weight=50)

    assert (result == test)

def test_bmi_over_weight():
    result = ()
    test = (27.343749999999996, 1)

    result = bmi.calculate_bmi(height=1.60, weight=70)

    assert (result == test)

def test_bmi_under_weight():
    result = ()
    test = (15.624999999999996, -1)

    result = bmi.calculate_bmi(height=1.60, weight=40)

    assert (result == test)
