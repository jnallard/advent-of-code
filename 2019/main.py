import sys
import importlib
from datetime import datetime

selected_day = input("Select a day to run (1-25): ")
try:
  day_module = importlib.import_module('day' + selected_day, package=None)
except Exception as ex:
  print('Could not process day: ' + selected_day)
  sys.exit(0)

print('-------------------------------')
print('Running day', selected_day)
start_time = datetime.now()
print('Starting at:\t', start_time.strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print('-------------------------------')
result = day_module.compute_day()
end_time = datetime.now()
print('-------------------------------')
print('Results:\t', result)
print('Start time:\t', start_time.strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print('End time:\t', end_time.strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print('Duration:\t', (end_time - start_time))
