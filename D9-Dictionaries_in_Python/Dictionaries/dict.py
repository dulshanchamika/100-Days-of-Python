programming_dictionary = {
    "Bug":"An Error in a program that prevent it from running as expected",
    "Function":"A piece of code that you can call over and over again",
}

#Retrieve an item
# Accessing using the key
print(programming_dictionary["Bug"])

# If we try to use a key that doesn't exist then it will show Key Error
# If the kwy is a number like 123 then we should give the key as 123

# Adding new entry
programming_dictionary["Loop"] = "The definition of the loop"
print(programming_dictionary)

#Empty Dictionary
empty_dictionary = {}
#It's good to create empty dictionary first and then add items to it
#empty_dictionary[]

#Wipe a existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#To edit a item in dictionary
#Change the value of Bug
# programming_dictionary["Bug"] = "Error"
# print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])