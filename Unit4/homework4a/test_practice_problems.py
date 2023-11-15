from byu_pytest_utils import with_import, max_score


@max_score(1)
@with_import("practice_problems")
def test_replace_digits_with_asterisk_short(replace_digits_with_asterisks):
    observed = replace_digits_with_asterisks("h311o my fr13nd")
    expected = "h***o my fr**nd"
    assert observed == expected


@max_score(1)
@with_import("practice_problems")
def test_replace_digits_with_asterisk_long(replace_digits_with_asterisks):
    observed = replace_digits_with_asterisks("Im 4 57ud3n7 47 8Yu 4ND I L0V3 70 c0D3!")
    expected = "Im * **ud*n* ** *Yu *ND I L*V* ** c*D*!"
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_remove_punctuation_short(remove_punctuation):
    observed = remove_punctuation("Hi! I really, really, really like pi! Do you?")
    expected = "Hi I really really really like pi Do you"
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_remove_punctuation_again(remove_punctuation):
    observed = remove_punctuation("2 * 3 = 6")
    expected = "2  3  6"
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_count_whitespace_short(count_whitespace):
    observed = count_whitespace("Hi my name is bob.")
    expected = 4
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_count_whitespace_all_kinds(count_whitespace):
    observed = count_whitespace("\n\n\t    :) \t\n  \t")
    expected = 13
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_most_punctuation(most_punctuation):
    observed = most_punctuation([
        ".",
        "2 + 2 = 5!",
        "Words. Words? Words?? Words!"
    ])
    expected = "Words. Words? Words?? Words!"
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_most_punctuation_again(most_punctuation):
    observed = most_punctuation([
        "..",
        "...!",
        "."
    ])
    expected = "...!"
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_keep_big_words(keep_big_words):
    observed = keep_big_words([
        'BYU Rocks!',
        'My name is Michaela Rachel Johnson.',
        'Nope.',
        'Almost. But not quite.'
    ])
    expected = [
        'BYU Rocks!',
        'My name is Michaela Rachel Johnson.'
    ]
    assert observed == expected


@with_import("practice_problems")
@max_score(1)
def test_keep_big_words_again(keep_big_words):
    observed = keep_big_words([
        'UofU',
        'My name is Inigo Montoya.',
        'Still nope.',
        'Almost. But not quite.'
    ])
    expected = []
    assert observed == expected
