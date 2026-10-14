string=input("enter a string:")
if string.endswith('ing'):
    mod_str=string+'ly'
else:
    mod_str=string+'ing'
print("modified string:",mod_str)
