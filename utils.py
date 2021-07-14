def safe_convert_to_float(s):
    """Convert to float or return None.

        >>> safe_convert_to_float("1.2")
        1.2

        >>> safe_convert_to_float("hello") is None
        True
    """

    try:
        return float(s)

    except ValueError:
        return None
