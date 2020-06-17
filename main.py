## Program to check for Coronavirus symptoms and advise actions
is_temperature_high_string = input ("Do you have a high temperature? (Yes/No) ")
## Selection 
if is_temperature_high_string == "Yes":
  print("Please contact 111.nhs.uk")
else:
  is_cough_continuous_string = input ("Do you have a continuous cough? (Yes/No) ")
  ## Nested selection
  if is_cough_continuous_string == "Yes":
    print("Please contact 111.nhs.uk")
  else:
    print("You do not have the main Coronavirus symptoms")
