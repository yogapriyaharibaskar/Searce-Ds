# Python3 code to demonstrate
# to check if list is sorted
# using naive method

# initializing list
test_list = [1, 6, 5, 8, 10]

# printing original list
print ("Original list : " + str(test_list))


# check sorted list
flag = 0
i = 1
while i < len(test_list):
	if(test_list[i] < test_list[i - 1]):
		flag = 1
	i += 1
	
# printing result
if (not flag) :
	print ("Yes, List is sorted.")
else :
	print ("No, List is not sorted.")
