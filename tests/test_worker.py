import sys, pathlib, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from webhook.worker import backoff_delays, is_permanent_failure


class TestBackoffDelays(unittest.TestCase):
    def test_three_attempts_double_from_one(self):
        self.assertEqual(backoff_delays(3), [1.0, 2.0, 4.0])

    def test_one_attempt(self):
        self.assertEqual(backoff_delays(1), [1.0])

    def test_zero_attempts_raises(self):
        with self.assertRaises(ValueError):
            backoff_delays(0)


class TestIsPermanentFailure(unittest.TestCase):
    def test_client_errors_are_permanent(self):
        for status in (400, 404, 499):
            self.assertTrue(is_permanent_failure(status), status)

    def test_429_is_retryable(self):
        self.assertFalse(is_permanent_failure(429))

    def test_server_errors_are_retryable(self):
        self.assertFalse(is_permanent_failure(500))
        self.assertFalse(is_permanent_failure(503))

    def test_redirect_and_success_are_not_permanent(self):
        for status in (200, 204, 302, 399):
            self.assertFalse(is_permanent_failure(status), status)


if __name__ == "__main__":
    unittest.main()
