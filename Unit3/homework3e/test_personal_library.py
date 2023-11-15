from byu_pytest_utils import max_score, dialog, test_files


@max_score(4)
@dialog(
    test_files / "personal_library1.dialog.txt",
    "personal_library.py"
)
def test_personal_library1(): ...

@max_score(4)
@dialog(
    test_files / "personal_library2.dialog.txt",
    "personal_library.py"
)
def test_personal_library2(): ...