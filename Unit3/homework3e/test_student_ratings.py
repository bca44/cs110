from byu_pytest_utils import max_score, dialog, test_files


@max_score(6)
@dialog(
    test_files / "student_ratings.dialog.txt",
    "student_ratings.py"
)
def test_student_ratings(): ...