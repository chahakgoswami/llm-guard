import pytest

from llm_guard.output_scanners.reading_time import ReadingTime


@pytest.mark.parametrize(
    "prompt,output,expected_output,expected_valid,expected_score",
    [
        (
            "All humans are vegetarians.",
            "Many people around the world eat meat and fish as part of their diet. Therefore, the statement that all "
            "humans are vegetarians is incorrect.",
            "Many people around the world eat meat and fish as part of their diet. Therefore, the statement that all "
            "humans are vegetarians is incorrect.",
            False,
            1.0,
        ),  # Long
        (
            "Birds can fly",
            "Birds cannot fly.",
            "Birds cannot fly.",
            True,
            0.0,
        ),  # Short
    ],
)
def test_scan(prompt, output, expected_output, expected_valid, expected_score):
    scanner = ReadingTime(max_time=0.1)
    sanitized_output, valid, score = scanner.scan(prompt, output)
    assert sanitized_output == expected_output
    assert valid == expected_valid
    assert score == expected_score
