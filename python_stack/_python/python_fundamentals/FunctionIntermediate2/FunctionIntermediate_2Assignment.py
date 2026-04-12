# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15

students[0]['last_name'] = 'Bryant'

sports_directory['soccer'][0] = 'Andres'

z[0]['y'] = 30

print("--- Task 1: Updated Values ---")
print(f"x: {x}")
print(f"First Student: {students[0]}")
print(f"Sports Directory: {sports_directory}")
print(f"z: {z}\n")


# 2. Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for curr_dict in some_list:
        output_line = []
        for key, val in curr_dict.items():
            output_line.append(f"{key} - {val}")
        
        print(", ".join(output_line))

students_list = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print("--- Task 2: Iterate Dictionary ---")
iterateDictionary(students_list)

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for curr_dict in some_list:
        if key_name in curr_dict:
            print(curr_dict[key_name])
print("\n--- Task 3: Get Values ---")
iterateDictionary2('first_name', students_list)
iterateDictionary2('last_name', students_list)

# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(val)} {key.upper()}")
        for item in val:
            print(item)
        print()
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}   
print("--- Task 4: Print Info ---")
printInfo(dojo)