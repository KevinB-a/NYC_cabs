"""
Source pour le calcul:
https://geodesie.ign.fr/contenu/fichiers/Distance_longitude_latitude.pdf
"""
import numpy as np
from math import sin, cos, acos, pi


#############################################################################
def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m / 60 + s / 3600

#############################################################################
def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd - d) * 60
    m = int(x)
    s = (x - m) * 60
    return d, m, s


#############################################################################
def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd / 180 * pi


#############################################################################
def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd / pi * 180


#############################################################################
def distanceGPS(latA, longA, latB, longB):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(abs(longB - longA)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S * RT


#############################################################################
def distKm(latStart, longStart, latDrop, longDrop):
    """
    return distance beetween the depart and the drop in km

    :param latStart:
    :param longStart:
    :param latDrop:
    :param longDrop:
    :return: distance in km
    """
    # cooordonnées GPS en radians du 1er point (ici, mairie de Tours)
    latA = deg2rad(latStart)  # Nord
    longA = deg2rad(longStart)  # Est

    # cooordonnées GPS en radians du 2ème point (ici, mairie de Limoges)
    latB = deg2rad(latDrop)  # Nord
    longB = deg2rad(longDrop)  # Est

    dist_km = (distanceGPS(latA, longA, latB, longB)) / 1000

    return int(dist_km)
################################################################################
def ft_haversine_distance(lat1, lng1, lat2, lng2):
    lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))
    AVG_EARTH_RADIUS = 6371 #km
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = np.sin(lat * 0.5) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * np.arcsin(np.sqrt(d))
    return h
##################################################################################
def ft_degree(lat1, lng1, lat2, lng2):
    AVG_EARTH_RADIUS = 6371 #km
    lng_delta_rad = np.radians(lng2 - lng1)
    lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))
    y = np.sin(lng_delta_rad) * np.cos(lat2)
    x = np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(lng_delta_rad)
    return np.degrees(np.arctan2(y, x))
