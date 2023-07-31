name = "Saurabh Kandekar"
print(name.upper())

# When character is not available that time Return value -1
print(name.find('S'))

# string
print(name.replace("Saurabh Kandekar", "Shankar Kandekar"))

# string specific
print(name.replace("Saurabh", "Shankar"))

# Change Character
print(name.replace("S", "H"))

# This String exist or not 
print("Saurabh" in name)

#
name = "Arbaz"
saurabh = f'''
hello {name}
how are you??
all good!!
'''
print(saurabh)

#
name = "Arbaz"
saurabh = '''
hello {}
how are you??
all good!!
'''
print(saurabh.format(name))
