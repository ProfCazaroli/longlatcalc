# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LongLatCalc
                                 A QGIS plugin
 LongLatCalc
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-07-17
        copyright            : (C) 2024 by Prof Cazaroli
        email                : prof.cazaroli@geoone.com.br
 ***************************************************************************/
"""

def classFactory(iface): 
    from .LongLatCalc import LongLatCalc
    return LongLatCalc(iface)
