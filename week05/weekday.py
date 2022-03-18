
# importing Pandas module
import pandas as pd
  
# Creating a Function
def check_weekday(date):
      
    # computing the parameter date
    # with len function
    res=len(pd.bdate_range(date,date))
      
    if res == 0 :
        print("It is the weekend, yay!")
    else:
        print("Yes, unfortunately today is a weekday.") 
  
# user input
date = "2022-03-01"
check_weekday(date)
  
date = "2022-03-05"
check_weekday(date)