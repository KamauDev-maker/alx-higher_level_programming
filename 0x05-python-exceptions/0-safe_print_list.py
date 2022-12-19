#!usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    #initialize a counter to track the elements printed
    count = 0
    #iterate through the elements in my_list
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            #increment the count
            count += 1
        except IndexError:
            break
    print("")
    return (count)
