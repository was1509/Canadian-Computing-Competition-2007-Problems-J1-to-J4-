count = -1
compressed = ["CU" , ":-)", ":-(" , ";-)" , ":-P" , "( ̃. ̃)" , "TA", "CCC", "CUZ", "TY" , "YW" , "TTYL"]
translation = ["see you","I’m happy","I’m unhappy","wink","stick out my tongue","sleepy","totally awesome","Canadian Computing Competition","because","thank-you","you’re welcome","talk to you later"]
phrase = str(input("Enter phrase>"))
if phrase in compressed:
	for i in compressed:
		count += 1
		if i == phrase:
			break
	print(translation[count])
else:
	print(phrase)
