#!/usr/bin/python3 -OO
# Copyright 2007-2019 The SABnzbd-Team <team@sabnzbd.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
tests.test_misc - Testing functions in misc.py
"""

import unittest
import datetime

from sabnzbd import misc
from tests.testhelper import *


class MiscTest(unittest.TestCase):

    def assertTime(self, offset, age):
        self.assertEqual(offset, misc.calc_age(age, trans=True))
        self.assertEqual(offset, misc.calc_age(age, trans=False))

    def test_timeformat24h(self):
        self.assertEqual('%H:%M:%S', misc.time_format('%H:%M:%S'))
        self.assertEqual('%H:%M', misc.time_format('%H:%M'))

    @set_config({"ampm": True})
    def test_timeformatampm(self):
        misc.HAVE_AMPM = True
        self.assertEqual('%I:%M:%S %p', misc.time_format('%H:%M:%S'))
        self.assertEqual('%I:%M %p', misc.time_format('%H:%M'))

    def test_calc_age(self):
        date = datetime.datetime.now()
        m = date - datetime.timedelta(minutes=1)
        h = date - datetime.timedelta(hours=1)
        d = date - datetime.timedelta(days=1)
        self.assertTime('1m', m)
        self.assertTime('1h', h)
        self.assertTime('1d', d)

    def test_monthrange(self):
        min_date = datetime.date.today() - datetime.timedelta(days=350)
        self.assertEqual(12, len(list(misc.monthrange(min_date, datetime.date.today()))))

    def test_safe_lower(self):
        self.assertEqual("all caps", misc.safe_lower("ALL CAPS"))
        self.assertEqual("", misc.safe_lower(None))