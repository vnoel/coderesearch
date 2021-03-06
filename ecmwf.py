#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import netCDF4
from localpath import eradir


# FIXME:la classe ecmwf ne correspond pas a un fichier
# mais a un des sous-ensembles ecmwf dispos sur climserv
# ce n'est pas bien.

class Ecmwf:

    # pour initialiser la classe, il faut passer
    # une chaine de caractere contenant la resolution
    # voulue pour les fichiers ECMWF
    # e.g. '075' ou '1125'
    def __init__(self, deg_res):
        self.path = eradir + 'GLOBAL_' + deg_res + '/4xdaily'
        if deg_res=='1125':
            self.identifier = ''
            self.desc = 'OPERA Global dataset, 1.125° res'
            res = 1.125
        elif deg_res=='075':
            self.identifier = 'ei'
            self.desc = 'ERA-Interim Global dataset, 0.75° res'
            res = 0.75
        else:
            raise NameError('Unknown resolution: ' + deg_res)
        self.res = deg_res
        self.lat = np.r_[90.:-90.-res:-res]
        self.lon = np.r_[0:360:res]
                
    def pl_file(self, year, month, varname):
        # aph = era40 pressure level files
        # aphei = era-interim pressure level files
        identifier = 'aph' + self.identifier
        filename = varname + '.%04d%02d.%s.GLOBAL_%s.nc' % (year, month, identifier, self.res)
        path = self.path + 'AN_PL/' + '%04d' % year + '/'
        name = path + filename
        return name

    def pl_var(self, year, month, varname,level=-1, lon180=None):
        f = self.pl_file (year, month, varname)
        print('Reading ' + f)
        try:
            nc = netCDF4.Dataset(f)
        except:
            raise NameError('No such ECMWF file: ' + f)

        lon = nc.variables['lon'][:]
        lat = nc.variables['lat'][:]
        if not(all(self.lon == lon) and all(lat==self.lat)):
            raise NameError('Longitude or latitude vectors not of expected size')
        
        levels = nc.variables['level'][:]

        if level > -1:
            levels = levels[level]

        # passer de 0->360 a -180->180 (comme ds fichiers calipso)
        if lon180:
            lon[lon >= 180] -= 360.

        add_offset = 0.
        scale_factor = 1.

        # getattr ne marche pas avec les structures netCDF, pfff
        if hasattr(nc.variables[varname], 'add_offset'):
            add_offset = nc.variables[varname].add_offset

        if hasattr(nc.variables[varname], 'scale_factor'):
            scale_factor = nc.variables[varname].scale_factor

        if level==-1:
            data = (nc.variables[varname][:] * scale_factor) + add_offset
        else:
            data = (nc.variables[varname][:,level,:,:] * scale_factor) + add_offset

        nc.close()
        return lon, lat, levels, data
    