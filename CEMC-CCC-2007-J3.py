value = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
num_list = [1,2,3,4,5,6,7,8,9,10]
n_list = []
new_li = []
total = 0
num = int(input(""))
if num >= 1 and num < 10:
	for i in range(num):
		n = int(input(""))
		n_list.append(n)
	new = int(input(""))
	for j in num_list:
		if j not in n_list:
			new_li.append(j)
	for k in new_li:
		total += value[k-1]
	average = total/num
	if new > average:
		print("deal")
	else:
		print("no deal")
