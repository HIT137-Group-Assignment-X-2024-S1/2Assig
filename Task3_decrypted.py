global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}    #key names inconsistent
def process_numbers(numbers):
    local_variable = 5                                              #Remove global global_variable - not required
    # numbers = [1, 2, 3, 4, 5]                                     #Removed variable, function parsed through my_set
    while local_variable > 0:
        if local_variable % 2 == 0: 
            print('numbers-', numbers)
            numbers.remove(local_variable)                          #remove spacing
        local_variable -= 1                                         #endless loop for while statement withouth '-= 1'
    return numbers

my_set = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]                             #square brackets
result = process_numbers(my_set)                                    #formatting

def modify_dict(dict_variable):
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict(5)

def update_global():                                                #function not called
    global global_variable
    global_variable += 10


for i in range(5): 
    print(i)
    i += 1                                                          #should be i not c

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")                                         #Condition 

if 5 not in my_dict:
    print("5 not found in the dictionary!")


print(global_variable)
print(my_dict)
print(my_set) 