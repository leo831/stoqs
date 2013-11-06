#!/usr/bin/env python
__author__    = 'Mike McCann,Duane Edgington,Reiko Michisaki'
__copyright__ = '2013'
__license__   = 'GPL v3'
__contact__   = 'duane at mbari.org'

__doc__ = '''

Master loader for all CANON activities in September 2013

Mike McCann; Modified from  Duane Edgington and Reiko Michisaki's work
MBARI 18 September 2013

@var __date__: Date of last svn commit
@undocumented: __doc__ parser
@status: production
@license: GPL
'''

import os
import sys
import datetime  # needed for glider data
import time      # for startdate, enddate args
import csv
import urllib2
os.environ['DJANGO_SETTINGS_MODULE']='settings'
project_dir = os.path.dirname(__file__)

# the next line makes it possible to find CANON
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))  # this makes it possible to find CANON, one directory up

from CANON import CANONLoader
       
# building input data sources object
#cl = CANONLoader('stoqs_september2011', 'CANON - September 2011')
cl = CANONLoader('stoqs_september2013', 'CANON - September 2013')

# Set start and end dates for all loads from sources that contain data 
# beyond the temporal bounds of the campaign
startdate = datetime.datetime(2013, 9, 9)                  # Fixed start
enddate = datetime.datetime(2013, 9, 30)                   # Fixed end

# default location of thredds and dods data:
cl.tdsBase = 'http://odss.mbari.org/thredds/'
cl.dodsBase = cl.tdsBase + 'dodsC/'

#####################################################################
#  DORADO 
#####################################################################
# special location for dorado data
cl.dorado_base = 'http://dods.mbari.org/opendap/data/auvctd/surveys/2013/netcdf/'
cl.dorado_files = [
                   'Dorado389_2013_259_00_259_00_decim.nc',
                   'Dorado389_2013_261_01_261_01_decim.nc',
                   'Dorado389_2013_262_00_262_00_decim.nc',
                   'Dorado389_2013_262_01_262_01_decim.nc',
                   'Dorado389_2013_268_00_268_00_decim.nc',
				   ]

#####################################################################
#  LRAUV 
#####################################################################

# From: M Jordan Stanway <mjstanway@mbari.org>
# Subject: Re: LRAUV netcdf files on OPeNDAP
# Date: September 18, 2013 1:15:01 PM PDT
# To: Mike McCann <mccann@mbari.org>
# 
# Not to my knowledge.
# 
# I've been discouraging people from using the .nc files because the decimation and interpolation can be misleading, and usually causes misunderstandings.
# 
# On Sep 18, 2013 12:33 PM, "Mike McCann" <mccann@mbari.org> wrote:
# Hi Jordan,
# 
# Are the netCDF files you have here:
# 
# http://aosn.mbari.org/TethysDash/data/daphne/realtime/sbdlogs/2013/201309/20130918T154456/
# 
# available on on OPeNDAP server?
# 
# If not, and the directory can be mounted on elvis, then I can set them up to be served with Hyrax.
# 
# -Mike


######################################################################
#  GLIDERS
######################################################################

# Glider data files from CeNCOOS thredds server
# L_662
cl.l_662_base = 'http://www.cencoos.org/thredds/dodsC/gliders/Line66/'
cl.l_662_files = ['OS_Glider_L_662_20130711_TS.nc']
cl.l_662_parms = ['TEMP', 'PSAL', 'FLU2']
cl.l_662_startDatetime = startdate
cl.l_662_endDatetime = enddate

# NPS_34
cl.nps34_base = 'http://www.cencoos.org/thredds/dodsC/gliders/Line66/'
cl.nps34_files = [ 'OS_Glider_NPS_G34_20130829_TS.nc']
cl.nps34_parms = ['TEMP', 'PSAL']
cl.nps34_startDatetime = startdate
cl.nps34_endDatetime = enddate

# NPS_29
cl.nps29_base = 'http://www.cencoos.org/thredds/dodsC/gliders/Line66/'
cl.nps29_files = [ 'OS_Glider_NPS_G29_20130829_TS.nc']
cl.nps29_parms = ['TEMP', 'PSAL', 'OPBS']
cl.nps29_startDatetime = startdate
cl.nps29_endDatetime = enddate


# Other gliders - served from campaign's TDS catalog
# Generic Glider ctd
cl.glider_ctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_Teledyne/'
cl.glider_ctd_files = [ 'nemesis_ctd.nc',
                        'ucsc260_ctd.nc',
                        'ucsc294_ctd.nc']
cl.glider_ctd_parms = ['TEMP', 'PSAL' ]
cl.glider_ctd_startDatetime = startdate
cl.glider_ctd_endDatetime = enddate

# Glider met 
cl.glider_met_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_Teledyne/'
cl.glider_met_files = [ 'nemesis_met.nc',
                        'ucsc260_met.nc',
                        'ucsc294_met.nc']
cl.glider_met_parms = ['meanu','meanv' ]
cl.glider_met_startDatetime = startdate
cl.glider_met_endDatetime = enddate

# Wavegliders
# WG OA
cl.wg_oa_ctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/WG_OA/NetCDF/'
cl.wg_oa_ctd_files = [ 'WG_OA_ctd.nc']
cl.wg_oa_ctd_parms = ['TEMP', 'PSAL','DENSITY','OXYGEN' ]
cl.wg_oa_ctd_startDatetime = startdate
cl.wg_oa_ctd_endDatetime = enddate

# WG Tex - load from both CTD and EcoPuck data files
cl.wg_tex_ctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/WG_Tex/NetCDF/'
cl.wg_tex_ctd_files = [ 'WG_Tex_ctd.nc', 'WG_Tex_eco.nc' ]
cl.wg_tex_ctd_parms = ['TEMP', 'PSAL','DENSITY', 'chlorophyll','backscatter650','backscatter470']
cl.wg_tex_ctd_startDatetime = startdate
cl.wg_tex_ctd_endDatetime = enddate

# WG OA
cl.wg_oa_met_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/WG_OA/NetCDF/'
cl.wg_oa_met_files = [ 'WG_OA_met.nc']
cl.wg_oa_met_parms = ['WINDSPEED','WINDDIRECTION','AIRTEMPERATURE','AIRPRESSURE']
cl.wg_oa_met_startDatetime = startdate
cl.wg_oa_met_endDatetime = enddate

# WG Tex
cl.wg_tex_met_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/WG_Tex/NetCDF/'
cl.wg_tex_met_parms = ['WINDSPEED','WINDDIRECTION','AIRTEMPERATURE','AIRPRESSURE']
cl.wg_tex_met_files = [ 'WG_Tex_met.nc']
cl.wg_tex_met_startDatetime = startdate
cl.wg_tex_met_endDatetime = enddate

# WG OA
cl.wg_oa_pco2_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/WG_OA/NetCDF/'
cl.wg_oa_pco2_files = [ 'WG_OA_pco2.nc']
cl.wg_oa_pco2_parms = ['pH','eqpco2','airco2','airtemp' ]
cl.wg_oa_pco2_startDatetime = startdate
cl.wg_oa_pco2_endDatetime = enddate









# nemesis ctd
cl.nemesis_ctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_Teledyne/'
cl.nemesis_ctd_files = [ 'nemesis_ctd.nc']
cl.nemesis_ctd_parms = ['TEMP', 'PSAL' ]
cl.nemesis_ctd_startDatetime = startdate
cl.nemesis_ctd_endDatetime = enddate

# nemesis met 
cl.nemesis_met_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_Teledyne/'
cl.nemesis_met_files = [ 'nemesis_met.nc']
cl.nemesis_met_parms = ['meanu', 'meanv' ]
cl.nemesis_met_startDatetime = startdate
cl.nemesis_met_endDatetime = enddate

# ucsc294 met 
cl.ucsc294_met_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_UCSC_2/'
cl.ucsc294_met_files = [ 'ucsc294_met.nc']
cl.ucsc294_met_parms = ['meanu', 'meanv' ]
cl.ucsc294_met_startDatetime = startdate
cl.ucsc294_met_endDatetime = enddate

# ucsc294 ctd 
cl.ucsc294_ctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_UCSC_2/'
cl.ucsc294_ctd_files = [ 'ucsc294_ctd.nc']
cl.ucsc294_ctd_parms = ['TEMP', 'PSAL' ,'oxygen','chla','backscatter']
cl.ucsc294_ctd_startDatetime = startdate
cl.ucsc294_ctd_endDatetime = enddate

# ucsc260 ctd 
cl.ucsc260_ctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/Slocum_UCSC_1/'
cl.ucsc260_ctd_files = [ 'ucsc294_ctd.nc']
cl.ucsc260_ctd_parms = ['TEMP', 'PSAL' ,'oxygen','chla','backscatter']
cl.ucsc260_ctd_startDatetime = startdate
cl.ucsc260_ctd_endDatetime = enddate



######################################################################
#  WESTERN FLYER: September 20-27
######################################################################
# UCTD
cl.wfuctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Ships/Western_Flyer/uctd/'
cl.wfuctd_parms = [ 'TEMP', 'PSAL', 'xmiss', 'wetstar' ]
cl.wfuctd_files = [ 
'canon13m01.nc', 'canon13m02.nc', 'canon13m03.nc', 'canon13m04.nc', 'canon13m05.nc', 'canon13m06.nc', 'canon13m07.nc', 'canon13m08.nc',
'canon13m09.nc', 'canon13m10.nc', 'canon13m11.nc', 
                      ]

# PCTD
cl.pctdDir = 'CANON_september2013/Platforms/Ships/Western_Flyer/pctd/'
cl.wfpctd_base = cl.dodsBase + cl.pctdDir
cl.wfpctd_parms = [ 'TEMP', 'PSAL', 'xmiss', 'ecofl' , 'oxygen']
cl.wfpctd_files = [ 
'canon13c01.nc', 'canon13c02.nc', 'canon13c03.nc', 'canon13c04.nc', 'canon13c05.nc', 'canon13c06.nc', 'canon13c07.nc',
'canon13c08.nc', 'canon13c09.nc', 'canon13c10.nc', 'canon13c11.nc', 'canon13c12.nc', 'canon13c13.nc', 'canon13c14.nc',
'canon13c15.nc', 'canon13c16.nc', 'canon13c17.nc', 'canon13c18.nc', 'canon13c19.nc', 
]

# BCTD
# SubSample data files from /mbari/BOG_Archive/ReportsForSTOQS/GOC12/ copied to local BOG_Data dir
cl.bctdDir = 'CANON_september2013/Platforms/Ships/Western_Flyer/netcdf/bctd/'
cl.subsample_csv_base = cl.dodsBase + cl.bctdDir
cl.subsample_csv_base = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'BOG_Data')
cl.subsample_csv_files = [
                            #'STOQS_canon13_CHL_1U.csv', 'STOQS_canon13_CHL_5U.csv', 'STOQS_canon13_NH4.csv', 'STOQS_canon13_NO2.csv',
                    		#'STOQS_canon13_NO3.csv','STOQS_canon13_OXY_ML.csv', 'STOQS_canon13_PHAEO_1U.csv', 'STOQS_canon13_PHAEO_5U.csv',
                            #'STOQS_canon13_PHAEO_GFF.csv', 'STOQS_canon13_PO4.csv', 'STOQS_canon13_SIO4.csv', #'STOQS_canon13_CARBON_GFF.csv
							#'STOQS_canon13_CHL_GFF.csv',
                         ]

######################################################################
#  RACHEL CARSON: September 16-20? (259-262) Sep 30 - Oct 3
######################################################################
# UCTD
cl.rcuctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Ships/Rachel_Carson/uctd/'
cl.rcuctd_parms = [ 'TEMP', 'PSAL', 'xmiss', 'wetstar' ]
cl.rcuctd_files = [ 
                    '25913RCm01.nc', '26013RCm01.nc', 
                      ]

# PCTD
cl.pctdDir = 'CANON_september2013/Platforms/Ships/Rachel_Carson/pctd/'
cl.rcpctd_base = cl.dodsBase + cl.pctdDir
cl.rcpctd_parms = [ 'TEMP', 'PSAL', 'xmiss', 'ecofl', 'oxygen' ]
cl.rcpctd_files = [ 
                    '25913RCc01.nc', '25913RCc02.nc', '25913RCc03.nc', '26013RCc01.nc', 
                      ]
# BCTD
# SubSample data files from /mbari/BOG_Archive/ReportsForSTOQS/GOC12/ copied to local BOG_Data dir
cl.bctdDir = 'CANON_september2013/Platforms/Ships/Rachel_Carson/bctd/'
cl.subsample_csv_base = cl.dodsBase + cl.bctdDir
cl.subsample_csv_base = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'BOG_Data')
cl.subsample_csv_files = [
#                            'STOQS_canon13_CHL_1U.csv', 'STOQS_canon13_CHL_5U.csv', 'STOQS_canon13_NH4.csv', 'STOQS_canon13_NO2.csv', 'STOQS_canon13_NO3.csv', 
			    'STOQS_canon13_OXY_ML.csv', 'STOQS_canon13_PHAEO_1U.csv', 'STOQS_canon13_PHAEO_5U.csv',
                            'STOQS_canon13_PHAEO_GFF.csv', 'STOQS_canon13_PO4.csv', 'STOQS_canon13_SIO4.csv', 'STOQS_canon13_CARBON_GFF.csv',
                            'STOQS_canon13_CHL_GFF.csv',
                         ]

#####################################################################
# JOHN MARTIN
#####################################################################
## No netcdf files as of 18 September 2013
##cl.JMuctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Ships/Martin/uctd/' 
##cl.JMuctd_parms = ['TEMP', 'PSAL', 'xmiss', 'wetstar' ]
##cl.JMuctd_files = [ '27710c01jm.nc',   '27910c06jm.nc',   '28410c02jm.nc',   '28710c03jm.nc',   '29810c01jm.nc', ]

cl.pctdDir = 'CANON_september2013/Platforms/Ships/Martin/pctd/'
cl.JMpctd_base = cl.dodsBase + 'CANON_september2013/Platforms/Ships/Martin/pctd/' 
cl.JMpctd_parms = ['TEMP', 'PSAL', 'xmiss', 'wetstar', 'oxygen' ]
cl.JMpctd_files = [ '25613JMC01.nc',
                    '25613JMC02.nc',
                    '25613JMC03.nc',
                    '25613JMC04.nc',
                    '25613JMC05.nc',
                    '26013JMC01.nc',
                    '26013JMC02.nc',
                    '26013JMC03.nc',
                    '26013JMC04.nc',

                  ]

######################################################################
#  MOORINGS
######################################################################
# Mooring M1 Combined file produced by DPforSSDS processing - for just the duration of the campaign
cl.m1_base = 'http://dods.mbari.org/opendap/data/ssdsdata/deployments/m1/'
cl.m1_files = [
                '201202/OS_M1_20120222hourly_CMSTV.nc', 
                '201309/OS_M1_20130918hourly_CMSTV.nc'
              ]
cl.m1_parms = [ 'eastward_sea_water_velocity_HR', 'northward_sea_water_velocity_HR',
                'SEA_WATER_SALINITY_HR', 'SEA_WATER_TEMPERATURE_HR', 'SW_FLUX_HR', 'AIR_TEMPERATURE_HR',
                'EASTWARD_WIND_HR', 'NORTHWARD_WIND_HR', 'WIND_SPEED_HR'
              ]
cl.m1_startDatetime = startdate
cl.m1_endDatetime = enddate


# Mooring OA1 CTD
cl.oaDir = 'CANON_september2013/Platforms/Moorings/OA_1/'
cl.OA1ctd_base = cl.dodsBase + cl.oaDir
cl.OA1ctd_files = ['OA1_ctd_2013.nc']
cl.OA1ctd_parms = ['TEMP', 'PSAL', 'conductivity' ]
cl.OA1ctd_startDatetime = startdate
cl.OA1ctd_endDatetime = enddate
# Mooring OA1 MET
cl.OA1met_base = cl.dodsBase + cl.oaDir
cl.OA1met_files = ['OA1_met_2013.nc']
cl.OA1met_parms = ['Wind_direction','Wind_speed','Air_temperature','Barometric_pressure']
cl.OA1met_startDatetime = startdate
cl.OA1met_endDatetime = enddate
# Mooring OA1 PH
cl.OA1pH_base = cl.dodsBase + cl.oaDir
cl.OA1pH_files = ['OA1_pH_2013.nc']
cl.OA1pH_parms = ['pH' ]
cl.OA1pH_startDatetime = startdate
cl.OA1pH_endDatetime = enddate
# Mooring OA1 PCO2
cl.OA1pco2_base = cl.dodsBase + cl.oaDir
cl.OA1pco2_files = ['OA1_pco2_2013.nc']
cl.OA1pco2_parms = ['pCO2' ]
cl.OA1pco2_startDatetime = startdate
cl.OA1pco2_endDatetime = enddate
# Mooring OA1 O2
cl.OA1o2_base = cl.dodsBase + cl.oaDir
cl.OA1o2_files = ['OA1_o2_2013.nc']
cl.OA1o2_parms = ['oxygen', 'oxygen_saturation' ]
cl.OA1o2_startDatetime = startdate
cl.OA1o2_endDatetime = enddate
# Mooring OA1 Fluorescence
cl.OA1fl_base = cl.dodsBase + cl.oaDir
cl.OA1fl_files = ['OA1_fl_2013.nc']
cl.OA1fl_parms = [ 'fluor' ]
cl.OA1fl_startDatetime = startdate
cl.OA1fl_endDatetime = enddate
 
# Mooring OA2 CTD
cl.oaDir = 'CANON_september2013/Platforms/Moorings/OA_2/'
cl.OA2ctd_base = cl.dodsBase + cl.oaDir
cl.OA2ctd_files = ['OA2_ctd_2013.nc']
cl.OA2ctd_parms = ['TEMP', 'PSAL', 'conductivity' ]
cl.OA2ctd_startDatetime = startdate
cl.OA2ctd_endDatetime = enddate
# Mooring OA2 MET
cl.OA2met_base = cl.dodsBase + cl.oaDir
cl.OA2met_files = ['OA2_met_2013.nc']
cl.OA2met_parms = ['Wind_direction','Wind_speed','Air_temperature','Barometric_pressure']
cl.OA2met_startDatetime = startdate
cl.OA2met_endDatetime = enddate
# Mooring OA2 PH
cl.OA2pH_base = cl.dodsBase + cl.oaDir
cl.OA2pH_files = ['OA2_pH_2013.nc']
cl.OA2pH_parms = ['pH' ]
cl.OA2pH_startDatetime = startdate
cl.OA2pH_endDatetime = enddate
# Mooring OA2 PCO2
cl.OA2pco2_base = cl.dodsBase + cl.oaDir
cl.OA2pco2_files = ['OA2_pco2_2013.nc']
cl.OA2pco2_parms = ['pCO2' ]
cl.OA2pco2_startDatetime = startdate
cl.OA2pco2_endDatetime = enddate
# Mooring OA2 O2
cl.OA2o2_base = cl.dodsBase + cl.oaDir
cl.OA2o2_files = ['OA2_o2_2013.nc']
cl.OA2o2_parms = ['oxygen', 'oxygen_saturation' ]
cl.OA2o2_startDatetime = startdate
cl.OA2o2_endDatetime = enddate
# Mooring OA2 Fluorescence
cl.OA2fl_base = cl.dodsBase + cl.oaDir
cl.OA2fl_files = ['OA2_fl_2013.nc']
cl.OA2fl_parms = [ 'fluor' ]
cl.OA2fl_startDatetime = startdate
cl.OA2fl_endDatetime = enddate
 

#######################################################################################
# DRIFTERS
#######################################################################################
# Stella drifters, requires input file stella_load.csv with the names of the 

cl.stella_base = cl.dodsBase + 'CANON_september2013/Platforms/Drifters/Stella_1/'
cl.stella_parms = [ 'TEMP', 'pH' ]
cl.stella_files = ['stella203_data.nc', 'stella204_data.nc', 'stella205_data.nc']



#######################################################################################
# ESPs
#######################################################################################
# MBARI ESPs Mack and Bruce
cl.espmack_base = cl.dodsBase + 'CANON_september2013/Platforms/Moorings/ESP_Mack/NetCDF/'
cl.espmack_parms = [ 'TEMP', 'PSAL', 'chl', 'chlini', 'no3' ]
cl.espmack_files = [ 
                        'ctd.nc',
                      ]

# add code for Bruce here. we think that all the plumbing is in place for Bruce, just need .nc file(s)

###################################################################################################################
# Execute the load
cl.process_command_line()

if cl.args.test:
    #cl.loadL_662(stride=100) 
    #cl.load_NPS29(stride=100) 
    #cl.load_NPS34(stride=100) 
    #cl.load_nemesis_ctd(stride=100) 
    #cl.load_ucsc294_ctd(stride=100) 
    #cl.load_glider_ctd(stride=100) 
    #cl.load_ucsc260_ctd(stride=100) 
    #cl.load_nemesis_met(stride=100) 

    #cl.load_wg_oa_pco2(stride=100) 
    #cl.load_wg_oa_ctd(stride=100) 
    #cl.load_wg_oa_met(stride=100) 
    #cl.load_wg_tex_ctd(stride=100)
    #cl.load_wg_tex_met(stride=100)
    #cl.load_glider_ctd(stride=100)
    #cl.load_glider_met(stride=100)

    #cl.loadDorado(stride=1000)
    ##cl.loadDaphne(stride=100)             # Someone needs to make good NetCDF files
    ##cl.loadTethys(stride=100)             # Someone needs to make good NetCDF files

    #cl.loadRCuctd(stride=10)
    #cl.loadRCpctd(stride=10)
    #cl.loadJMpctd(stride=10)
    #cl.loadWFuctd(stride=100)   
    #cl.loadWFpctd(stride=50)

    #cl.loadM1(stride=10)
    #cl.loadStella203(stride=10)
    #cl.loadStella204(stride=10)
    #cl.loadOA1ctd(stride=1)
    #cl.loadOA1met(stride=1)
    #cl.loadOA1pH(stride=1)
    #cl.loadOA1pco2(stride=1)
    #cl.loadOA1fl(stride=1)
    #cl.loadOA1o2(stride=1)
    #cl.loadOA2ctd(stride=1)
    #cl.loadOA2met(stride=1)
    #cl.loadOA2pH(stride=1)
    ##cl.loadOA2pco2(stride=1)
    #cl.loadOA2fl(stride=1)
    #cl.loadOA2o2(stride=1)
    cl.loadStella(stride=2)
    ##cl.loadESPmack()
    ##cl.loadESPbruce()
    ##cl.loadSubSamples()

elif cl.args.optimal_stride:
    cl.loadL_662(stride=1) 
    cl.load_NPS29(stride=1) 
    cl.load_NPS34(stride=1) 
    cl.load_nemesis_ctd(stride=1) 
    cl.load_ucsc294_ctd(stride=1) 
    cl.load_nemesis_met(stride=1) 

    cl.loadDorado(stride=2)
    ##cl.loadDaphne(stride=100)             # Someone needs to make good NetCDF files
    ##cl.loadTethys(stride=100)             # Someone needs to make good NetCDF files

    cl.loadRCuctd(stride=1)
    cl.loadRCpctd(stride=1)
    cl.loadJMpctd(stride=1)
    ##cl.loadWFuctd(stride=100)             # Not until 9/20/13
    ##cl.loadWFpctd(stride=50)

    cl.loadM1(stride=1)
    ##cl.load_ucsc294_met(stride=1)         # No method in CANON/__init__.py yet
    cl.loadStella203(stride=1)
    cl.loadStella204(stride=1)
    cl.loadOA1ctd(stride=1)
    cl.loadOA1met(stride=1)
    ##cl.loadOA1pH(stride=1)
    ##cl.loadOA1pco2(stride=1)
    ##cl.loadOA1fl(stride=1)
    ##cl.loadOA1o2(stride=1)
    ##cl.loadOA2ctd(stride=1)
    ##cl.loadOA2met(stride=1)
    ##cl.loadOA2pH(stride=1)
    ##cl.loadOA2pco2(stride=1)
    ##cl.loadOA2fl(stride=1)
    ##cl.loadOA2o2(stride=1)
    ##cl.loadESPmack()
    ##cl.loadESPbruce()

    cl.load_wg_tex_ctd(stride=1)
    ##cl.loadSubSamples()

else:
    cl.stride = cl.args.stride
    cl.loadL_662()
    cl.load_NPS29()
    cl.load_NPS34()
    cl.load_nemesis_ctd()
    cl.load_ucsc294_ctd() 
    cl.load_nemesis_met() 

    cl.loadDorado()
    ##cl.loadDaphne()             # Someone needs to make good NetCDF files
    ##cl.loadTethys()             # Someone needs to make good NetCDF files

    cl.loadRCuctd()
    cl.loadRCpctd()
    cl.loadJMpctd()
    ##cl.loadWFuctd()             # Not until 9/20/13
    ##cl.loadWFpctd()

    cl.loadM1()
    ##cl.load_ucsc294_met()         # No method in CANON/__init__.py yet
    cl.loadStella203()
    cl.loadStella204()
    cl.loadOA1ctd()
    cl.loadOA1met()
    ##cl.loadOA1pH()
    ##cl.loadOA1pco2()
    ##cl.loadOA1fl()
    ##cl.loadOA1o2()
    ##cl.loadOA2ctd()
    ##cl.loadOA2met()
    ##cl.loadOA2pH()
    ##cl.loadOA2pco2()
    ##cl.loadOA2fl()
    ##cl.loadOA2o2()
    ##cl.loadESPmack()
    ##cl.loadESPbruce()
    ##cl.loadSubSamples()
