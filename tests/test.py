import unittest

from deflake import DeFlake


class DeflakeTestCase(unittest.TestCase):
    def _results_are_same_and_pass(self, results):
        return all(results[0] == result and result == "PASS" for result in results)

    def test_default_no_fail(self):
        flake = DeFlake("ls")
        results = flake.run()
        self.assertEqual(len(results), 10,
            "Program should have run 10 times but ran %s" % len(results))
        self.assertTrue(self._results_are_same_and_pass(results))

    def test_max_runs_no_fail(self):
        flake = DeFlake("ls", max_runs=21)
        results = flake.run()
        self.assertEqual(len(results), 21, 
            "Program should have run 21 times but ran %s" % len(results))
        self.assertTrue(self._results_are_same_and_pass(results))

    def test_mp(self):
        flake = DeFlake("ls", pool_size=4)
        results = flake.run()
        len_results = len(results)
        self.assertEqual(len_results, 10, 
            "Program should have run 10 times, but ran %s" % len_results)
        self.assertTrue(self._results_are_same_and_pass(results))


if __name__ == "__main__":
    unittest.main()
