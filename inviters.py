persons=input("how many user ")
if(persons<10):
    for i in range(persons):
      persons=input(f"enter the {i} invitor")
      print(persons)
elif(persons>=10):
    print("too many  pepole")
    
