#
# libms5803 - MS5803 pressure sensor library
#
# Copyright (C) 2014 by Artur Wroblewski <wrobell@pld-linux.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import time
from datetime import datetime

import ms5803

sensor = ms5803.Sensor()
while True:
    pressure, temp = sensor.read()
    print('{}: {}bar {}C'.format(datetime.now(), pressure / float(10000), temp / float(100)))

    time.sleep(0.5)

# vim: sw=4:et:ai
