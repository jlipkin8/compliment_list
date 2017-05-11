""" This is a Terminal-based program that allows a user to create, view the entire, or view a 
random compliment from the compliment list """

import ranint from random 

def add_compliment_list(my_list):
    """takes user input and adds it as a new item to the end of the list"""
    compliment = raw_input("Give a compliment: ")
    my_list.append(compliment)
    return my_list 

def view_all_compliments(my_list): 
    """iterates though the list containing compliments and prints each item out""" 
    for compliment in my_list: 
        print compliment 

def view_random_compliment(my_list): 
    end = my_list - 1 
    random = randint(0,end)
    print my_list[random]
    