from src.compute_failure_rate import failure_rate

def test_failure_rate():
    assert failure_rate(100, 5) == 5.0
    assert failure_rate(0, 0) == 0