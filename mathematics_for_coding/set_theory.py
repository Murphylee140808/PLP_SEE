admins = {"Dedan", "Chakin"}
editors = {"Chakin", "Aaron"}

# Combine both groups
# all_users = admins.union(editors)
#print("All Users", all_users)

# Who is both admin and editors?
# both_roles = admins.intersection(editors)
#print("Users with both roles: ", both_roles)

# Admin only
admins_only = admins.difference(editors)
print("Admins Only: ", admins_only)

# Redo
# Define two sets
A = {1, 2, 3, 4, "Akin", "Ade", "Tunji"}
B = {3, 4, 5, 6, "Wale", "Akin", "Kunle"}

#Set operations in action
union_set = A.union(B)
intersecton_set = A.intersection(B)
diff_set = A.difference(B)

# print ("Set A:", A)
# print("Unity of A and B Children: ", union_set)
# print("Those that appears on both side: ", intersecton_set)
print("The ones that are unique: ", diff_set)