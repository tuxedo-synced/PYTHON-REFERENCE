import numpy as np 

# Filtering - Refers to the process of selecting elements
#             from an array that match a given condition 

ages = np.array([
                    [21,17,19,20,16,30,18,65],
                    [39,22,15,99,18,19,20,21]
                ])
teenagers = ages[ages < 18]
print(ages)
print("The participants participate are: ", end = " ")
print(teenagers)
print("Number of participants are: ", end = " ")
print(len(teenagers))

teenagers = ages[(ages > 18) & (ages < 100)]    # numpy is of C language style so use &,|,^
print("The participants disqualified are: ", end = " ")
print(teenagers)

# np.where(condition , variable_name_of_array , replicated_value_for_valuees_whose_value_is_false)
adults = np.where(ages >= 18 , ages , 0)
print(adults)


