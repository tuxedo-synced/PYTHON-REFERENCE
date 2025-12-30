# format specifier = {value:flags} format a value based on what flags are inserted 

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that may spaces 
# :< = left justify
# :> = right justify 
# :^ = center align
# :+ = use a plus sign to indicate positive values 
# := = place sign to left most position 
# : = insert a space before positive numbers   # colon followed by a space !!!
# :, = comma separator 

pointer_value1 = 3.14159
pointer_value2 = -987.65
pointer_value3 = 12.34

print(f"Pointer val 1 {pointer_value1:.2f}")
print(f"Pointer val 2 {pointer_value2:.2f}")
print(f"Pointer val 3 {pointer_value3:.2f}")
print()
print(f"Pointer val 1 {pointer_value1}")
print(f"Pointer val 2 {pointer_value2}")
print(f"Pointer val 3 {pointer_value3}")
print()
print(f"Pointer val 1 {pointer_value1:10}") # set the value as len(space)+len(digits) = {number}
print(f"Pointer val 2 {pointer_value2:10}")
print(f"Pointer val 3 {pointer_value3:10}")
print()
print(f"Pointer val 1 {pointer_value1:010}") # set the value as len(space)+len(digits) = {number} 
print(f"Pointer val 2 {pointer_value2:010}") # also zero pads the empty spaces
print(f"Pointer val 3 {pointer_value3:010}")
print()
print(f"Pointer val 1 {pointer_value1:<10}")
print(f"Pointer val 2 {pointer_value2:<10}")
print(f"Pointer val 3 {pointer_value3:<10}")
print()
print(f"Pointer val 1 {pointer_value1:>10}")
print(f"Pointer val 2 {pointer_value2:>10}")
print(f"Pointer val 3 {pointer_value3:>10}")
print()
print(f"Pointer val 1 {pointer_value1:^10}")
print(f"Pointer val 2 {pointer_value2:^10}")
print(f"Pointer val 3 {pointer_value3:^10}")
print()
print(f"Pointer val 1 {pointer_value1:+10}")
print(f"Pointer val 2 {pointer_value2:+10}")
print(f"Pointer val 3 {pointer_value3:+10}")
print()
print(f"Pointer val 1 {pointer_value1:=10}")
print(f"Pointer val 2 {pointer_value2:=10}")
print(f"Pointer val 3 {pointer_value3:=10}")
print()
val = 3000000023114 
print(f"Pointer val  {val:,}")
print()

# combination of flags 
#[[fill]align][sign][#][0][width][,][.precision][type]
print(f"value {val:+,.2f}")
print(f"value {val:*<+30,.2f}")


# fill 
print(f"{5:*<5}")   # * left fill → "5****"
print(f"{5:*>5}")   # * right fill → "****5"
print(f"{5:*^5}")   # * center fill → "**5**"


