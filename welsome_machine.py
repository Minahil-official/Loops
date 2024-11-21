def welsome_machine():
    affirmation = ("I am capable of doing anything I put my mind to. Hmmm That was not the affirmation.")
    user_input = input("please enter the affirmation:")
    while True:
        if user_input == affirmation:
            print("congratulations! you have wrote it successfully")
            break
        else:     
          print("please enter correct afirmation")
          break
welsome_machine()
        