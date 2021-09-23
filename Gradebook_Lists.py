# last semester gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#current semester gradebook
gradebook = [["physics", 98],["calculus", 97],["poetry", 85],["history",88]]

#add classes to gradebook list

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])


# replace grades with new numbers
gradebook[-1][1] = 98
gradebook[2].remove(85)

#change number grade to 'pass'

gradebook[2].append("Pass")


full_gradebook = last_semester_gradebook + gradebook

print("The full gradebook is:")
print(full_gradebook)
