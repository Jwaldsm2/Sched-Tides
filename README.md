# Sched-Tides
An automated process to calculate tide conditions for defined projects on a daily basis

## Motivation
Predicting the tides has been an effort of mankind for millennia.  NOAA's proprietary **Pydro** software has made it a simpler effort for those looking to estimate tidal stages along specified flight lines designated for tide-coordinated aerial photogrammetry data collection.

## Inputs
 - NOAA-supplied TCARI (.tc) file
 - Flight line plan in the format of (.wpt) file with the following fields per line <RECORD,LINE,FEET,SCALE,MILES,FAZI,BAZI,SWP,LAT1,LON1,EWP,LAT2,LON2,EMULSION,LAP,PHOTOS,GRND_EL,MAGDEC,LAT3,LON3,FocalLength(M),FormatX(FT),FormatY(FT)>
 - User selected options for time zone, tidal datum to observe, sun above horizon (degrees), start time, end time, predicted or residual (includes recent environmental effects into tide calculation)

## Outputs
 - .csv and .txt
 - .geojson 
 - shapefiles and .gpkg

## How it works
The user will have to have Pydro running on their system.  From the batch file template, the user can fill the inputs corresponding for their project.  The batch file allows for several projects to be run in series without the user having to input all the data manually.  Even better, when managed with a scheduling program like Window's Task Scheduler, the batch file will be run automatically according to the schedule specified.  This is ideal for users calculating the tide residual (subject to environmental effects) on a frequent basis.  For this option to work, read on.

## How can I get this to run without me?
The next step is running scheduler tool mentioned in the paragraph above in conjunction with a short python script which automatically changes the date, since the user will probably want this to run daily at least.  That can be done by running UpDateBetter.py with the scheduler tool in the morning, prior to running the tide residual batch file.  
