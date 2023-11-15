from byu_pytest_utils import dialog, max_score, test_files


@max_score(5)
@dialog(test_files / "grapefruit_game.txt", "word_guess.py", test_files / "grapefruit.txt")
def test_word_guess_grapefruit(): ...


@max_score(5)
@dialog(test_files / "apple_game.txt", "word_guess.py", test_files / "apple.txt")
def test_word_guess_apple(): ...
