from byu_pytest_utils import dialog, max_score, test_files


@max_score(1)
@dialog(
    test_files / "redaction_small_picked.dialog.txt",
    "redaction.py", test_files / "redaction_small.input.txt", "redaction_small.observed.txt", "picked",
    output_file="redaction_small.observed.txt"
)
def test_redaction_small_picked(): ...


@max_score(1)
@dialog(
    test_files / "redaction_small_peter.dialog.txt",
    "redaction.py", test_files / "redaction_small.input.txt", "redaction_small.observed.txt", "Peter",
    output_file="redaction_small.observed.txt"
)
def test_redaction_small_peter(): ...


@max_score(1)
@dialog(
    test_files / "redaction_large_the.dialog.txt",
    "redaction.py", test_files / "redaction_large.input.txt", "redaction_large.observed.txt", "the",
    output_file="redaction_large.observed.txt"
)
def test_redaction_large_the(): ...


@max_score(2)
@dialog(
    test_files / "redaction_large_and.dialog.txt",
    "redaction.py", test_files / "redaction_large.input.txt", "redaction_large_and.observed.txt", "and",
    output_file="redaction_large_and.observed.txt"
)
def test_redaction_large_and(): ...
