def backoff_delays(max_attempts: int) -> list[float]:
    """Return one delay per attempt, doubling from 1.0 (3 -> [1.0, 2.0, 4.0])."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    return [float(2 ** i) for i in range(max_attempts)]


def is_permanent_failure(status: int) -> bool:
    """True for 4xx responses except 429 (those are not worth retrying)."""
    return 400 <= status < 500 and status != 429
