import unittest
import sys
import tempfile


class TestExitCode(unittest.TestCase):

    def setUp(self):
        # to be able to import mprof
        sys.path.append('.')
        from mprof import run_action
        self.run_action = run_action

    def test_exit_code_success(self):
        tmpfile = tempfile.NamedTemporaryFile('w', suffix='.py')
        with tmpfile as ofile:
            s = "1+1"
            ofile.write(s)
            ofile.flush()
            sys.argv = ['<ignored>', '--exit-code', tmpfile.name]
            self.assertRaisesRegexp(SystemExit, '0', self.run_action)

    def test_exit_code_fail(self):
        tmpfile = tempfile.NamedTemporaryFile('w', suffix='.py')
        with tmpfile as ofile:
            s = "raise RuntimeError('I am not working nicely')"
            ofile.write(s)
            ofile.flush()
            sys.argv = ['<ignored>', '--exit-code', tmpfile.name]
            self.assertRaisesRegexp(SystemExit, '1', self.run_action)

    def test_no_exit_code_success(self):
        tmpfile = tempfile.NamedTemporaryFile('w', suffix='.py')
        with tmpfile as ofile:
            s = "raise RuntimeError('I am not working nicely')"
            ofile.write(s)
            ofile.flush()
            sys.argv = ['<ignored>', tmpfile.name]
            self.run_action()

if __name__ == '__main__':
    unittest.main()
