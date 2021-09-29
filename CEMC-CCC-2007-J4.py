phrase1_list = []
phrase2_list = []
phrase1 = str(input("Enter first phrase>"))
phrase2 = str(input("Enter second phrase>"))
for i in phrase1:
	if i != " ":
		phrase1_list.append(i)
for j in phrase2:
	if j != " ":
		phrase2_list.append(j)
if sorted(phrase1_list) == sorted(phrase2_list):
	print("Is an anagram.")
else:
	print("Is not an anagram")
