simple_string = "This is a string"
multiline_string = """
This is a multiline
string.
"""
first_name = "Ruthvik "
last_name = "Madavaram"
full_name = first_name + last_name
print(full_name)

#slicing
substring = full_name[2:6]
print(substring, len(substring))

upper_case = full_name.upper()
lower_case = full_name.lower()
print(upper_case, lower_case)

text = "    abcd    "
print(text.strip())

list = full_name.split(" ")
print(list)

print(",".join(list))