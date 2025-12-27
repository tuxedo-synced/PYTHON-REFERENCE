# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]  ->  [start,end)

credit_number = "1234-5678-9101"
print(len(credit_number))
print(credit_number[2])
print(credit_number[0 : 4 : 1])
print(credit_number[ : 4 : 1])      # if  nothing is given it asumes start is 0 .
print(credit_number[5 : 9 : 1])
print(credit_number[14 :  : -1])    # if nothing is given it assumes end is 0 .
print(credit_number[ : : -1])       # here as step = -1 , it itself adjust start to -1 and end to -15 
print(credit_number[ : : 1])        # here as step = 1 , it itself adjust start to 0 and end to 14

#       1    2   3   4   -   5   6   7   8   -   9    1   0   1
#      -14  -13 -12 -11 -10  -9  -8  -7 -6   -5  -4   -3  -2  -1
last_four_digits = credit_number[-4::1]
print(f"XXXX-XXXXX-XXXXX-{last_four_digits}")
last_four_digits = credit_number[-4:]
print(f"XXXX-XXXXX-XXXXX-{last_four_digits}")
entire_string_by_negative_indexing = credit_number[::-1]
print(entire_string_by_negative_indexing)