try:
    with open("test.txt", mode ="w") as myfile:
        myfile.write('testing write lines in a file :v')
    with open("test.txt", mode ="r") as myfile:
        print(myfile.readlines())
except FileNotFoundError:
    print("File not found or not exist")
except Exception as e:
    print(f"An error has occured: {type(e)}")
