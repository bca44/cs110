from byu_pytest_utils import dialog, max_score, test_files


@max_score(2)
@dialog(
    test_files / 'ooooo_small.dialog.txt',
    'ooooo.py', test_files / "ooooo_small.input.txt", "ooooo_small.observed.txt",
    output_file="ooooo_small.observed.txt"
)
def test_ooooo_small(): ...


@max_score(3)
@dialog(
    test_files / 'ooooo_large.dialog.txt',
    'ooooo.py', test_files / "ooooo_large.input.txt", "ooooo_large.observed.txt",
    output_file="ooooo_large.observed.txt"
)
def test_ooooo_large(): ...
