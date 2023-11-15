from byu_pytest_utils import dialog, max_score, test_files

@max_score(2)
@dialog(
    test_files / 'add_bullets_one_line.dialog.txt',
    'add_bullets.py', test_files / "add_bullets_one_line.input.txt", "add_bullets_one_line.observed.txt", "*",
    output_file="add_bullets_one_line.observed.txt"
)
def test_add_bullets_one_line(): ...


@max_score(3)
@dialog(
    test_files / 'add_bullets_multiple_lines.dialog.txt',
    'add_bullets.py', test_files / "add_bullets_multiple_lines.input.txt", "add_bullets_multiple_lines.observed.txt", "o",
    output_file="add_bullets_multiple_lines.observed.txt"
)
def test_add_bullets_multiple_lines(): ...
