from byu_pytest_utils import max_score, dialog, test_files


@max_score(6)
@dialog(
    test_files / "grades.dialog.txt",
    "grades.py"
)
def test_grades(): ...
