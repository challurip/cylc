#!/usr/bin/env python2

# THIS FILE IS PART OF THE CYLC SUITE ENGINE.
# Copyright (C) 2008-2018 NIWA
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
"""Load custom variables for template processor."""


def load_template_vars(template_vars=None, template_vars_file=None):
    """Load template variables from key=value strings."""
    res = {}
    if template_vars_file:
        for line in open(template_vars_file):
            line = line.strip().split("#", 1)[0]
            if not line:
                continue
            key, val = line.split("=", 1)
            res[key.strip()] = val.strip()
    if template_vars:
        for pair in template_vars:
            key, val = pair.split("=", 1)
            res[key.strip()] = val.strip()
    return res
