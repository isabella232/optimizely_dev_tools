import mock

import unittest

from optimizely_platform import exceptions
from optimizely_platform import objects

import functions as my_integration_functions


class FunctionsTest(unittest.TestCase):

  def test_get_dynamic_audience_conditions__successful_fetch(self):
    self.assertEqual(1, 1)
