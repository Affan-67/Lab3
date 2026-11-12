import employee_info as ei

def test_get_employees_by_age_range():
    test = []
    result = ei.get_employees_by_age_range(45,55)

    assert(result == test)

def test_calculate_average_salary():
    test = 60166.666666666664
    result = ei.calculate_average_salary()

    assert(result == test)

def test_get_employees_by_dept():
    test = ["Chloe", "Mike"]
    result = ei.get_employees_by_dept("Engineering")
    names = [item["name"] for item in result]

    assert (names == test)