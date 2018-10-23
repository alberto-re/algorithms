import os
import unittest

loader = unittest.TestLoader()
suite = loader.discover(os.getcwd())

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
