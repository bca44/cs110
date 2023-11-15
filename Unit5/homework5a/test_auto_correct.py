from byu_pytest_utils import max_score, test_files, dialog


@max_score(5)
@dialog(
    test_files / "neat.dialog.txt",
    "auto_correct.py", test_files / "sloppy.txt", "neat.observed.txt",
    output_file="neat.observed.txt"
)
def test_auto_correct(): ...


@max_score(5)
@dialog(
    test_files / "neat_again.dialog.txt",
    "auto_correct.py", test_files / "another_sloppy.txt", "neat_again.observed.txt",
    output_file="neat_again.observed.txt"
)
def test_auto_correct_again(): ...
