# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : September 2014
    Copyright            : (C) 2014 by NextGIS
    Email                : info at nextgis dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alexander Bruy'
__date__ = 'September 2014'
__copyright__ = '(C) 2014, NextGIS'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'


def classFactory(iface):
    from publish2ngw_plugin import Publish2NGWPlugin
    return Publish2NGWPlugin(iface)
