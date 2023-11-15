from byu_pytest_utils import dialog, max_score, test_files


@max_score(2)
@dialog(
    test_files / 'nan_small.dialog.txt',
    'filter_nan.py', test_files / "nan_small.input.txt", "nan_small.observed.txt", "*",
    output_file="nan_small.observed.txt"
)
def test_filter_nan_small(): ...


@max_score(3)
@dialog(
    test_files / 'nan_large.dialog.txt',
    'filter_nan.py', test_files / "nan_large.input.txt", "nan_large.observed.txt", "*",
    output_file="nan_large.observed.txt"
)
def test_filter_nan_large(): ...