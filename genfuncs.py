def generate_sum_function(input):
        if type(input) == list:
                def list_sum():
                        total = 0
                        for element in input:
                                total += element
                        return total
                return list_sum
        elif type(input) == dict:
                def dict_sum():
                        total = 0
                        for value in input.values():
                                total += value
                        return total
                return dict_sum
        else:
                def error_message():
                        return "You cannot sum this type!"
                return error_message def generate_sum_function(input):



        if type(input) == list:
                def list_sum():
                        total = 0
                        for element in input:
                                total += element
                        return total
                return list_sum
        elif type(input) == dict:
                def dict_sum():
                        total = 0
                        for value in input.values():
                                total += value
                                return total
                return dict_sum
        else:
                def error_message():
                        return "You cannot sum this type!"
                        return error_message

sumlist = sum_generator([])
sumdict = sum_generator({})
sumint = sum_generator(12)
sumfloat = sum_generator(1.23)