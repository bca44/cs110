from byu_pytest_utils import dialog, max_score, test_files


@max_score(2)
@dialog(
    test_files / "replace_word_sells_to_sold.dialog.txt",
    "replace_word.py", test_files / "replace_word.input.txt", "replace_word_sells_to_sold.observed.txt", "sells", "sold",
    output_file="replace_word_sells_to_sold.observed.txt"
)
def test_replace_word_sells_sold(): ...


@max_score(2)
@dialog(
    test_files / "replace_word_seashells_to_lemonade.dialog.txt",
    "replace_word.py", test_files / "replace_word.input.txt", "replace_word_seashells_to_lemonade.observed.txt", "seashells", "lemonade",
    output_file="replace_word_seashells_to_lemonade.observed.txt"
)
def test_replace_word_seashells_lemonade(): ...