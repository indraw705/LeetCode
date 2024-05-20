# Print maximum apreared character in a line

text = "Pranita Indrajit Narvekar / Pimple nilakh "

dict_map = {}

for _ in text:
    if _ == " ":
        pass
    elif _ in dict_map:
        dict_map[_] +=1
    else:
        dict_map[_] = 1

res = max(dict_map, key=dict_map.get)

print(f"max sting is {str(res)}")