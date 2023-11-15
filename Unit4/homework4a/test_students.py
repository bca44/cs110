from byu_pytest_utils import dialog, test_files, max_score


@max_score(10)
@dialog(test_files / "students.txt", "students.py")
def test_students(): ...
