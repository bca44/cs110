from byu_pytest_utils import max_score, test_files, dialog


@max_score(7)
@dialog(
    test_files/"true-blue.dialog.txt",
    "blue_score.py"
)
def test_blue_score(): ...

