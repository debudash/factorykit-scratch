import sys, pathlib, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from webhook.worker import backoff_delays


class TestBackoffDelays(unittest.TestCase):
    def test_three_attempts_double_from_one(self):
        self.assertEqual(backoff_delays(3), [1.0, 2.0, 4.0])

    def test_one_attempt(self):
        self.assertEqual(backoff_delays(1), [1.0])

    def test_zero_attempts_raises(self):
        with self.assertRaises(ValueError):
            backoff_delays(0)


if __name__ == "__main__":
    unittest.main()
