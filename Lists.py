last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

# zip(sucjects, grades) takes the two lists and creteas a zip object where the twoo lists have been merged together.
# surrounding zip with list() essentially just converts the object back into a list
gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))
#print(gradebook)

# the way you combine two lists together in python is to add them together using '+'
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
