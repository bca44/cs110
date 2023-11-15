from byu_pytest_utils import max_score, test_files, dialog


@max_score(5)
@dialog(
    test_files / "postal_bins.dialog.txt",
    "postal_routing.py", test_files / "addresses.txt", "postal_bins.observed.txt",
    output_file="postal_bins.observed.txt"
)
def test_postal_routing_unknown_bin(): ...


@max_score(5)
@dialog(
    test_files / "postal_bins_again.dialog.txt",
    "postal_routing.py", test_files / "more_addresses.txt", "postal_bins_again.observed.txt",
    output_file="postal_bins_again.observed.txt"
)
def test_postal_routing_again(): ...
