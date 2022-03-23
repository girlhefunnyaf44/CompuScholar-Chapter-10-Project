class Validator:

  def get_integer(prompt, min, max):

    # loop until correct input received
    while True:
      try:
        inputString = input(prompt)  # get user input
        inputInt = int(inputString)  # try to convert to int

        if (inputInt >= min) and (inputInt <= max):  # verify range
          return inputInt            # success!
      except:
         continue                    # try again

  def get_float(prompt, min, max):

    # loop until correct input received
    while True:
      try:
        inputString = input(prompt)      # get user input
        inputFloat = float(inputString)  # try to convert to float

        if (inputFloat >= min) and (inputFloat <= max):  # verify range
          return inputFloat          # success!
      except:
           print("Has to be betwen $0 - $1,000; Try again.")
      else:
          print("Has to be betwen $0 - $1,000; Try again.")
