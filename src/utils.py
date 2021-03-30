"""
Source pour le calcul:
https://geodesie.ign.fr/contenu/fichiers/Distance_longitude_latitude.pdf
"""

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
