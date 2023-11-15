from byu_pytest_utils import max_score, test_files, dialog, with_import


@max_score(20)
@dialog(
    test_files / "grid_game.dialog.txt",
    "grid_game.py",
    test_files / "world.txt"
)
def test_grid_game(): ...

