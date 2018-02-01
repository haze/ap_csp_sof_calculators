# our loop conditonal
continued = True

print('This program calculates mpg.')
# while the user wants to calculate
while continued:
  # get our variables
  milesDriven = int(input("Enter Miles Driven: "))
  gallonsUsed = int(input("Enter Gallons Used: "))
  # calculate mpg
  mpg = milesDriven / gallonsUsed
  print('Miles per gallon: {}'.format(mpg))
  # parse result into continued
  continued = str(input("Would you like to start a new calculation? [y/n]: ")).lower() == "y"
print("cya.")
