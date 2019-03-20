# This program is to show what all activity/functions can be done with LIST

if __name__ == '__main__':
    
    nk_list = []                        # Declare, not necessary everytime
    nk_list = [x for x in range(10)]    # It can be directly declared and used like this as well
    print('---------------------')
    print(nk_list)                      # Print the list
    print('---------------------')
    print(len(nk_list))                 # Print Length of List
    print('---------------------')
    nk_list.append(10)                  # Add/Append at the end - 1 new item to the list # Note: here we have added an INT
    print(nk_list)
    print('---------------------')
    nk_list.insert(0,'Mike')            # Insert at a specific INDEX
    print(nk_list)
    print('---------------------')
    nk_list.append('Nitin')             # Added a STRING into the same list
    print(nk_list)      
    print('---------------------')
    nk_list.append(0)                   # Added Duplicate Item
    nk_list.append('Nitin')             # Added Duplicate Item
    print('---------------------')
    print('The Item: 0 - is present',nk_list.count(0), 'times!')    # Count occurance of the same Item Value
    print('---------------------')
    print('The Item: "Nitin" - is present',nk_list.count('Nitin'), 'times!')    # Count occurance of the same Item Value
    print('---------------------')
    nk_list.clear()                     # Clear, deletes all Items in the list
    print(nk_list)
    print('---------------------')
    nk_list = [int(x) for x in input('\nEnter space seperated values:\t').split(' ')]   # Took userinput[STRING, seperated by ' '] - converted each of them into INT
    print('\n',nk_list)
    print('---------------------')
    temp_list = nk_list.copy()          # Copy the whole list
    print(temp_list)
    print('---------------------')
    print(nk_list.index(11))            # This gives you Index of a specific value that you are looking for, if not found -  Throws an Error
    print('---------------------')
    nk_list.pop(0)                      # Removes the Item placed at the specified INDEX
    print(nk_list)
    print('---------------------')
    nk_list.remove(12)                  # Removes the Item based on VALUE
    print(nk_list)
    print('---------------------')
    nk_list.sort()                      # Ascending Sort - Lowest to Highest
    print(nk_list)
    print('---------------------')
    nk_list.sort(reverse=True)          # Descending Sort - Highest to Lowest
    print(nk_list)
    print('---------------------')
    user_list = ['Test','Best']
    nk_list.extend(user_list)           # Merge 2 lists into 1 list
    print(nk_list)
    print('---------------------')