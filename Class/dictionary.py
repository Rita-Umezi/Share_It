# """
# dictionaries are used to stores an unordered collection of data values and also key words 
# first_dict={"key":"value"}
# """
# first_dict={"24/0474": 59, #dictionary to store student scores
#             "24/1070": 99,
#             "24/2070": 29
#             }
# print(first_dict)#print the dictionary

student_deet={"name":"Grace", "age":19, "height": 5.5, "attendance": True}
print("Student name is", student_deet["name"])
print("Student attendance is", student_deet["attendance"])
print(student_deet.get("height"))# the .get method can be used to get/fetch a value
print(student_deet.get("matric", "key unknown"))#the string after is to print what will happen if the matric is not found

student_deet["matric_no"]="24/0494"
student_deet["age"]="24" #used to replace the age from 19 to 24
print(student_deet)
print(student_deet.keys())
print(student_deet.items())
print(student_deet.values())

#making a dictionary from a list
number=[1,2,3,4]
square_num={num:num**2 for num in number}
print(square_num)

alpha=["a", "b", "c", "d"]
number=[2,4,6,8]
new_dic={letter:num for letter, num in zip(alpha, number)} #normal syntax=={key: value for item in iterable}
print(new_dic)

student_name={"Timi", "Rita", "Ola", "Omo"}
attendance={student_name:"present" if student_name!="Rita"
            else "Absent" for student_name in student_name}
print(attendance)