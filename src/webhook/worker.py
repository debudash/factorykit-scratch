def backoff_delays(max_attempts: int) -> list[float]:
    """Return one delay per attempt, doubling from 1.0 (3 -> [1.0, 2.0, 4.0])."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    return [float(2 ** i) for i in range(max_attempts)]
