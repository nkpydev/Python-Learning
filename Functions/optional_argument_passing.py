def process_info(pass_dict = None,organization=None):
    user_info = {}
    user_info['First Name'] = pass_dict['First Name']
    user_info['Last Name'] = pass_dict['Last Name']
    user_info['Email ID'] = pass_dict['Email']
    user_info['Organization'] = 'Python Tweakers Inc'
    return user_info

if __name__ == "__main__":
    print('\nEnter your Details:\t')
    input_dict = {}
    input_dict['First Name'] = input('\nEnter your First Name:\t')
    input_dict['Last Name'] = input('\nEnter your Last Name:\t')
    input_dict['Email'] = input('\nEnter your Email-ID:\t')
    print(process_info(input_dict))