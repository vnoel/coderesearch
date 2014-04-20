#!/usr/bin/env python
#encoding:utf-8

"""
Utility functions to find data files on Climserv or ICARE servers
Created by VNoel on 2014-02-27
"""

import socket

# server-dependent paths pointing to CALIOP level 1 and level 2 data

hostname = socket.gethostname()
if hostname == 'access.icare.univ-lille1.fr':
    # ICARE
    l1dir = ('/DATA/LIENS/CALIOP/CAL_LID_L1.v3.01',)
    l2dir = ('/DATA/LIENS/CALIOP/05kmCLay.v3.02',
             '/DATA/LIENS/CALIOP/05kmCLay.v3.01')
    l2adir = ('/DATA/LIENS/CALIOP/05kmALay.v3.01',)
else:
    # CLIMSERV
    l1dir = ('/bdd/CALIPSO/Lidar_L1/CAL_LID_L1.v3.30',
             '/bdd/CALIPSO/Lidar_L1/CAL_LID_L1.v3.02',
             '/bdd/CALIPSO/Lidar_L1/CAL_LID_L1.v3.01')
    l2dir = ('/bdd/CALIPSO/Lidar_L2/05kmCLay.v3.02',
             '/bdd/CALIPSO/Lidar_L2/05kmCLay.v3.01',
             '/bdd/CALIPSO/Lidar_L2/05kmCLay.v2.01',
             '/bdd/CALIPSO/Lidar_L2/05kmCLay.v2.01')