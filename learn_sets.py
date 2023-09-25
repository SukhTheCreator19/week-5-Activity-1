def learn_sets():
  print("I am in sets")
   ###############################SETS########################################
 # Sets Practice #1
  # Join the following sets into one, called my_set_3:
  my_set = {1, 2, "three", "four"}
  my_set1 = {"three", 4, 5}
  my_set2 = {1, 2, "three", "four"}
  my_set0 = {"three", 4, 5}
  
  my_set3 = {f"{my_set},{my_set1}, {my_set2}, {my_set0}"}
  print(my_set3)
    # Sets Practice #2
    # Remove a random item from the following set, using set methods. 
  raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
  raffle.remove("Rachel")
  
    # Sets Practice #3
    # Add the name Gunther to the following set, using set methods:
    # 
  raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
  raffle.add("Gunther")