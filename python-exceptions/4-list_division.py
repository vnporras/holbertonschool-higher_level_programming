#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    correct_types = ["int", "float"]
    try:
        for i in range(0, list_length):
                      
    except:
        None
    finally:
        return result
    




def list_division_OLD(my_list_1, my_list_2, list_length):
    result = []
    correct_types = ["int", "float"]
    try:
        for index, value in enumerate(my_list_1):
            value2 = my_list_2[index]

            if (index == len(my_list_1) - 1 and len(my_list_1) < len(my_list_2)):
                exists_list_2_next_index = my_list_2[index + 1]

                if (exists_list_2_next_index != None):
                    print("out of range")
            
            if (value2 == None):
                print("out of range")
                result.append(0)
                continue

            if type(value).__name__ not in correct_types or type(value2).__name__ not in correct_types:
                print("wrong type")
                result.append(0)
                continue

            if value2 == 0:
                print("division by 0")
                result.append(0)
                continue

            result.append(value / value2)            
    except:
        None
    finally:
        return result


# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)


# print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)