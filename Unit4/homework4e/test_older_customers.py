from byu_pytest_utils import max_score, dialog, test_files


@max_score(3)
@dialog(
    test_files / "thirty.dialog.csv",
    "older_customers.py", test_files / "customers.csv", "thirty.observed.csv", "30",
    output_file="thirty.observed.csv"
)
def test_older_customers_30(): ...


@max_score(4)
@dialog(
    test_files / "fifteen.dialog.csv",
    "older_customers.py", test_files / "customers.csv", "fifteen.observed.csv", "15",
    output_file="fifteen.observed.csv"
)
def test_older_customers_15(): ...
