def check_frequency(list_of_strings):
    frequency_dict = {}
    for entry in list_of_strings:
        if entry not in frequency_dict:
            frequency_dict[entry] = 1
        else:
            frequency_dict[entry] += 1
    return frequency_dict

if __name__ == "__main__":
    list_of_string = [
                    'India',
                    'China',
                    'United States of America',
                    'United Kingdom',
                    'Russia',
                    'India',
                    'China',
                    'United Kingdom',
                    'China',
                    'India'
                ]       
    print(check_frequency(list_of_string))