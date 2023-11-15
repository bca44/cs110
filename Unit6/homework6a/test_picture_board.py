from byu_pytest_utils import max_score, dialog, test_files


@max_score(10)
@dialog(
    test_files / "board.dialog.txt",
    "picture_board.py"
)
def test_picture_board(): ...
