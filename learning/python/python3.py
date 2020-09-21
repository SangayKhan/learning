#How to propose a girl?

def plz(ans2):
		if ans2 == "YES" or ans2 =="Yes" or ans2 == "yes":
			print("Yess...!!!I LOVE YOU...!!!")
		elif ans2 == "NO" or ans2 == "No" or ans2 == "no":
			print("OK...Thank you for your time")
		else:
			print("Answer only yes or no")

def Crush(ans2):
	if ans2 == "YES" or ans2 =="Yes" or ans2 == "yes":
		print("Yess...!!!I LOVE YOU...!!!")
	elif ans2 == "NO" or ans2 == "No" or ans2 == "no":
		print("Plzzz...!!!")
		plz(str(input("I ask you again Can i be you boyfriend? \n")))
	else:
		print("Answer only yes or no")

def crush(ans1):

	if (ans1 == "NO" or ans1 == "no" or ans1 == "No"):
		print("yes...!!!she don't have one")
		Crush(str(input("Can i be you boyfriend? \n")))	
	elif (ans1 == "YES" or ans1 == "Yes" or ans1 == "yes"):
		print("Sad...tell me when you break up...!!!")
	else:
		print("Answer only yes or no")

crush(str(input("Do you have a boyfriend? \n")))
