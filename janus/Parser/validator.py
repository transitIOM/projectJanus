import json
from loguru import logger


def row_lengths(file: str) -> bool:

    # Load JSON data from the file
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Get the rows for the first table
    rows = data["tables"][0]["rows"]
    expected_len = len(rows[0])

    is_valid = True

    for i, row in enumerate(rows):
        if len(row) != expected_len:
            logger.error(
                "Row {index} has length {actual}, expected {expected}",
                index=i,
                actual=len(row),
                expected=expected_len,
            )
            is_valid = False

    return is_valid
