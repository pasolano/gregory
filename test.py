# One test program to rule them all...

import unittest

from test_french    import French_Test
from test_gregorian import Gregorian_Test
from test_shire     import Shire_Test

# Run all of the unit tests.
french_test    = French_Test()
gregorian_test = Gregorian_Test()
shire_test     = Shire_Test()
unittest.main()
