#!/usr/bin/env python

# THIS FILE IS PART OF THE CYLC SUITE ENGINE.
# Copyright (C) 2008-2015 NIWA
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

import gtk
from copy import deepcopy
from cylc.task_state import task_state


# TODO - make sizes consistent
empty = {}
empty['small'] = ["11 11 1 1", ". c None"]
empty['small'].extend(["..........."]*11)
empty['medium']= ["17 17 1 1", ". c None"]
empty['medium'].extend(["................."]*17)
empty['large'] = ["22 22 1 1", ". c None"]
empty['large'].extend(["......................"]*22)
empty['extra large'] = ["32 32 1 1", ". c None"]
empty['extra large'].extend(["................................"]*32)
  
stopped = {
        'small': [
                "10 10 3 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "+  c None",
                "+++++*****",
                "+++++*****",
                "+++++...**",
                "+++++...**",
                "+++++...**",
                "**...+++++",
                "**...+++++",
                "**...+++++",
                "*****+++++",
                "*****+++++" 
        ],
        'medium': [
                "14 14 3 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "+  c None",
                "+++++++*******",
                "+++++++*******",
                "+++++++*******",
                "+++++++....***",
                "+++++++....***",
                "+++++++....***",
                "+++++++....***",
                "***....+++++++",
                "***....+++++++",
                "***....+++++++",
                "***....+++++++",
                "*******+++++++",
                "*******+++++++",
                "*******+++++++"
        ], 
        'large': [
                "20 20 3 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "+  c None",
                "++++++++++**********",
                "++++++++++**********",
                "++++++++++**********",
                "++++++++++**********",
                "++++++++++......****",
                "++++++++++......****",
                "++++++++++......****",
                "++++++++++......****",
                "++++++++++......****",
                "++++++++++......****",
                "****......++++++++++",
                "****......++++++++++",
                "****......++++++++++",
                "****......++++++++++",
                "****......++++++++++",
                "****......++++++++++",
                "**********++++++++++",
                "**********++++++++++",
                "**********++++++++++",
                "**********++++++++++"
        ],
        'extra large': [
                "30 30 3 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "+  c None",
                "+++++++++++++++***************",
                "+++++++++++++++***************",
                "+++++++++++++++***************",
                "+++++++++++++++***************",
                "+++++++++++++++***************",
                "+++++++++++++++***************",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "+++++++++++++++.........******",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "******.........+++++++++++++++",
                "***************+++++++++++++++",
                "***************+++++++++++++++",
                "***************+++++++++++++++",
                "***************+++++++++++++++",
                "***************+++++++++++++++",
                "***************+++++++++++++++"
        ]
}

filtered = {
        'medium': [
                "10 20 3 1",
                "o	c <FILL>",
                "x	c <BRDR>",
                ".  c None",
                "..........",
                "..........",
                "..........",
                "...xxxx...",
                "...xoox...",
                "...xoox...",
                "...xoox...",
                "...xoox...",
                "...xoox...",
                "...xoox...",
                "...xoox...",
                "...xoox...",
                "...xxxx...",
                "..........",
                "..........",
                "..........",
                "...xxxx...",
                "...xoox...",
                "...xxxx...",
                "..........",
                "..........",
                ]
        }

live = {
        'small': [
                "11 11 4 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "b  c <FAM_BLACK>",
                "w  c <FAM_WHITE>",
                "***********",
                "***********",
                "**wwwww..**",
                "**wbbbw..**",
                "**wbbbw..**",
                "**wbbbw..**",
                "**wwwww..**",
                "**.......**",
                "**.......**",
                "***********",
                "***********"
        ],
        'medium': [
                "17 17 4 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "b  c <FAM_BLACK>",
                "w  c <FAM_WHITE>",
                "*****************",
                "*****************",
                "*****************",
                "***wwwwwww....***",
                "***wbbbbbw....***",
                "***wbbbbbw....***",
                "***wbbbbbw....***",
                "***wbbbbbw....***",
                "***wbbbbbw....***",
                "***wwwwwww....***",
                "***...........***",
                "***...........***",
                "***...........***",
                "***...........***",
                "*****************",
                "*****************",
                "*****************"
        ],
        'large': [
                "22 22 4 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "b  c <FAM_BLACK>",
                "w  c <FAM_WHITE>",
                "**********************",
                "**********************",
                "**********************",
                "**********************",
                "****wwwwwwww......****",
                "****wbbbbbbw......****",
                "****wbbbbbbw......****",
                "****wbbbbbbw......****",
                "****wbbbbbbw......****",
                "****wbbbbbbw......****",
                "****wwwwwwww......****",
                "****..............****",
                "****..............****",
                "****..............****",
                "****..............****",
                "****..............****",
                "****..............****",
                "****..............****",
                "**********************",
                "**********************",
                "**********************",
                "**********************"
        ],
        'extra large': [
                "32 32 4 1",
                ".	c <FILL>",
                "*	c <BRDR>",
                "b  c <FAM_BLACK>",
                "w  c <FAM_WHITE>",
                "********************************",
                "********************************",
                "********************************",
                "********************************",
                "********************************",
                "********************************",
                "*******wwwwwwwwww........*******",
                "*******wwwwwwwwww........*******",
                "*******wwbbbbbbww........*******",
                "*******wwbbbbbbww........*******",
                "*******wwbbbbbbww........*******",
                "*******wwbbbbbbww........*******",
                "*******wwbbbbbbww........*******",
                "*******wwbbbbbbww........*******",
                "*******wwwwwwwwww........*******",
                "*******wwwwwwwwww........*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "*******..................*******",
                "********************************",
                "********************************",
                "********************************",
                "********************************",
                "********************************",
                "********************************"
        ]

}


class DotMaker(object):

    """Make dot icons to represent task and family states."""

    def __init__(self, theme, size='medium'):
        self.theme = theme
        self.size = size

    def get_icon(self, state=None, is_stopped=False, is_family=False, is_filtered=False):
        """Generate a gtk.gdk.Pixbuf for a state.

        If is_stopped, generate a stopped form of the Pixbuf.
        If is_family, add a family indicator to the Pixbuf.
        """
        if state is None:
            # Empty icon.
            xpm = empty[self.size]
        elif state not in self.theme:
            # TODO - handle unknown state separately
            pass
            #if is_stopped:
            #    xpm = stopped_runahead[self.size]
            #elif is_filtered:
            #    size = 'medium'
            #    xpm = filtered_runahead[size]
            #else:
            #    xpm = deepcopy(runahead[self.size])
            #    if is_family:
            #        xpm[3] = xpm[3].replace('<FAM>', 'black')
            #    else:
            #        xpm[3] = xpm[3].replace('<FAM>', 'None')
        else:
            # Known state icon.
            color = self.theme[state]['color']
            if self.theme[state]['style'] == 'filled':
                fill_color = color
                brdr_color = color
            else:
                fill_color = 'None'
                brdr_color = color
            if is_stopped:
                xpm = deepcopy(stopped[self.size])
                xpm[1] = xpm[1].replace('<FILL>', fill_color)
                xpm[2] = xpm[2].replace('<BRDR>', brdr_color)
            elif is_filtered:
                size = 'medium'
                xpm = deepcopy(filtered[size])
                xpm[1] = xpm[1].replace('<FILL>', fill_color)
                xpm[2] = xpm[2].replace('<BRDR>', brdr_color)
            else:
                xpm = deepcopy(live[self.size])
                xpm[1] = xpm[1].replace('<FILL>', fill_color)
                xpm[2] = xpm[2].replace('<BRDR>', brdr_color)
                if is_family:
                    xpm[3] = xpm[3].replace('<FAM_BLACK>', brdr_color)
                    xpm[4] = xpm[4].replace('<FAM_WHITE>', 'None')
                else:
                    xpm[3] = xpm[3].replace('<FAM_BLACK>', fill_color)
                    xpm[4] = xpm[4].replace('<FAM_WHITE>', fill_color)

        # NOTE: to get a pixbuf from an xpm file, use:
        #    gtk.gdk.pixbuf_new_from_file('/path/to/file.xpm')
        return gtk.gdk.pixbuf_new_from_xpm_data(data=xpm)

    def get_image(self, state, is_stopped=False, is_filtered=False):
        """Returns a gtk.Image form of get_icon."""
        img = gtk.Image()
        img.set_from_pixbuf(self.get_icon(state, is_stopped=is_stopped, is_filtered=is_filtered))
        return img

    def get_dots(self):
        dots = {'task' : {}, 'family' : {}}
        for state in task_state.legal:
            dots['task'][state] = self.get_icon(state)
            dots['family'][state] = self.get_icon(state, is_family=True)
        dots['task']['empty'] = self.get_icon()
        dots['family']['empty'] = self.get_icon()
        return dots
