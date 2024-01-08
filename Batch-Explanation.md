## So what do I do with this batch file?
The batch file provided is a template and must be edited to fit your dataset.  First, make sure pydro is installed on your computer.  The batch file allows you to operate Pydro through the command line, it is not a substitute for Pydro itself.  The following values correspond to what you would enter into Pydro if you were trying to calculate tides manually for your project.

- The location of your Python.exe
- The location of your rsd.py
- pred - specifies that you are calculating a prediction (not to be confused with the predicted/residual input later)
- -t the location of your .tcari
- -f the location of your .wpt
- -o where you want your output to be saved
- -gmt specifies Grenwich Mean Time for your project, do not change
- -# the hour relative to gmt (ex. -5 for EST)
- -m indicates that you want to calculate Mean High Water and Mean Lower Low Water datums.  Alternatively, you can use -b for Below MHW
- -a is the degrees below the horizon that the sun must be for the time window calculated to be terminated.  25 is standard.
- -s start time in the format of YYYY-MM-DDT000:00
- -e end time in the same format as the start time
- -n leave as 1
- -p if you want predicted tide values (no environmental effects)
- -r if you want residual tide values (with environmental effects)
- Note* -p or -r must be selected but not both.
