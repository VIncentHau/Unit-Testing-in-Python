import datetime
symbol = input("Please Enter a Symbol (all caps): ") 
if symbol.isalpha() == True and len(symbol) <= 7 and symbol.isupper() == True:
  print("Symbol Is Valid") 
else:
  print("Symbol Is Not Valid") 

try:
  chart_type = int(input("Enter Chart Type (1 OR 2): ")) 
  if chart_type == 1 or chart_type == 2:  
    print("Chart Type Is Valid") 
  else:
    print("Chart Type Is Not Valid")  
except ValueError:
  print("Chart Type Is Not Valid")  

try:
  time_series = int(input("Enter Time Series (1-4): ")) 
  if time_series > 0 and time_series < 5:  
    print("Time Series Is Valid") 
  else:
    print("Time Series Is Not Valid") 
except ValueError:
  print("Time Series Is Not Valid") 

date_string = input("Enter start date in the format YYYY-MM-DD: ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print("Date Format Is Valid") 
except ValueError:
  print("Date Format Is Not valid, Please Enter In YYYY-MM-DD Format")

date_string = input("Enter End Date In The Format YYYY-MM-DD: ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format) 
  print("Date Format Is Valid") 
except ValueError:
  print("Date Format Is Not Valid, Please Enter In YYYY-MM-DD Format")