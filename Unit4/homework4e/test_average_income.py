from byu_pytest_utils import dialog, max_score, test_files


@max_score(3)
@dialog(test_files / "engineer.txt", "average_income.py", test_files / "customers.csv", "Engineer")
def test_average_income_engineer(): ...


@max_score(4)
@dialog(test_files / "lawyer.txt", "average_income.py", test_files / "customers.csv", "Lawyer")
def test_average_income_lawyer(): ...
