# Sets are Lists with no Duplicate entries.

country_input_a = [
                'India',
                'China',
                'United States of America',
                'India',
                'China',
                'United Kingdom',
                'Uganda',
                'United States of America'
            ]

country_input_b = [
                    'India',
                    'South Africa',
                    'Russia',
                    'United Kingdom'
                ]

# 1] Now we want to know - the unique Countries. [SET]
unique_country_list_a = set(country_input_a)
unique_country_list_b = set(country_input_b)
print('----------------------------------------------------------------')
print(unique_country_list_a) # This will show us the unique entries in input_a
print(unique_country_list_b) # This will show us the unique entries in input_b
print('----------------------------------------------------------------')
# 2] Now if we want to see - the common entries, 
# which are present in both the inputs [INTERSECTION]
print(unique_country_list_a.intersection(unique_country_list_b))
print(unique_country_list_b.intersection(unique_country_list_a))
print('----------------------------------------------------------------')
# 3] Now if we want to see - the entries which are present in only 1 of the inputs - 
# ignoring the common ones, who are present in both inputs [SYMMETRIC_DIFFERENCE]
print(unique_country_list_a.symmetric_difference(unique_country_list_b))
print(unique_country_list_b.symmetric_difference(unique_country_list_a))
print('----------------------------------------------------------------')
# 4] Now of we want to see - only the unique entries in either of the list - 
# ignoring the common ones [DIFFERENCE]
print(unique_country_list_a.difference(unique_country_list_b))
print(unique_country_list_b.difference(unique_country_list_a))
print('----------------------------------------------------------------')
# 5] Now we want to see a common list of all entries from both inputs
print(unique_country_list_a.union(unique_country_list_b))
print('----------------------------------------------------------------')