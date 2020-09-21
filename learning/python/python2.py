'''def function():

	def function1():
		result_str1 = ""
		for row in range(0,7):    
		    for column in range(0,7):     
		        if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):  
		            result_str1 = result_str1 +"|"    
		        else:      
		            result_str1 =result_str1 +" "    
		    result_str1 =result_str1 +"\n"    
		return result_str1 
	#function1()		

	def function2():
		result_str2 = ""    
		for row in range(0,7):    
		    for column in range(0,7):     
		        if ((column == 3 and (0 < row < 6 )) or (row == 0 and column > 0 and column <6)):  
		            result_str2 =result_str2 +"|"    
		        else:      
		            result_str2 =result_str2 +" "    
		    result_str2 =result_str2 +"\n"    
		return result_str2	
	#function2()	

	def function3():
		result_str3 = ""
		for row in range (0, 7):
			for column in range(0, 7):
				if (((column == 1 or column ==5) and row != 0 ) or ((row == 0 or row ==3) and (column > 1 and column < 5))):
					result_str3 = result_str3 +"|"
				else:
					result_str3  = result_str3 +" "
			result_str3 = result_str3 +"\n"
		return result_str3
	#function3()		

	def function4():
		result_str4 = ""
		for row in range (0, 7):
			for column in range(0, 7):
				if (( row == 0 and (column == 0 or column == 6 ) )  or ( row == 1 and (column == 1 or column == 5 )) or ( row == 2 and (column == 2 or column == 4 )) or (column ==3 and row > 2)):
					result_str4 = result_str4 +"|"
				else:
					result_str4 = result_str4 +" "
			result_str4 = result_str4 +"\n"
		return result_str4	
	#function4()	
		
	def function5():
		result_str5 = " "
		for row in range (0, 10):
			for column in range(0, 10):
				if (row == 1 and ( column == 1 or column == 6 )):
					result_str5 = result_str5 +"__"
				elif (row == 2 and ( column == 0 or column == 9 )):
					result_str5 = result_str5 +"|"
				elif (row == 2 and ( column == 2 or column == 7 )):
					result_str5 = result_str5 +"o"
				elif (row == 3 and column == 4):
					result_str5 = result_str5 +"||"
				elif (row == 4 and column == 4):
					result_str5 = result_str5 +"__"
				else:
					result_str5 = result_str5 +" "
			result_str5 = result_str5 +"\n"
		return result_str5
	#function5()

	x = "{} {} {} {} HELLO SONAM! {}".format(function1(),function2(),function3(),function4(),function5())
	#y = x.format(result_str1, result_str2, result_str3, result_str4, result_str5)

	print(function1())
	print(function2())
	print(function3())
	print(function4())
	print(function5())

	print(x)

function()'''

def print_alpha_A(size):
    for m in range(size):
        for n in range((size // 2) + 1):  
            if ((n == 0 or n == size // 2) and m != 0 or m == 0 and n != 0 and n != size // 2 or m == size // 2):
                print("*", end = "") 
            else:
                print(" ", end = "")         
        print()
print_alpha_A(7)