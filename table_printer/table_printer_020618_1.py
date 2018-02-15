# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# STATUS:  unsolved

# Table Printer

#####################################
# TABLE DATA IMPORT
#####################################

# TODO:  alter the program to take an input file that is imported with the table data
tableDataSet_1 = [
	['apples','oranges','cherries','banana'],
	['Alice','Bob','Carol','David'],
	['dogs','cats','moose','goose'],
	['black','white','red','grey'],
	['jump','fall']
]

#####################################
# END TABLE DATA IMPORT
#####################################

# colWidthList = []
colWidthList = [0] * len(tableDataSet_1) # meaning you have to alter the way you set the lengths within the list, use set_colWidthList()
colStruct = []

# find the longest string in each of the inner lists

def find_long_string_1(list):
	longest_item = '' # to store the longest string item
	for item in list:
		if len(item) > len(longest_item):
			longest_item = item
		else:
			pass
	return (len(longest_item)) # return the value for use outside of the function
	# find the number length of the longest_item to set a width value for that column
	# colWidthList.append(len(longest_item))

def set_colWidthList(colWidthList):
	for num in range(0,len(colWidthList)):
		colWidthList[num] = find_long_string_1(tableDataSet_1[num]) # find the length of the longest string in 1st list and set the 1st position in colWidthList to the returned value

	print(colWidthList) # for testing

def get_longest_inner_list(parent_list):
	# return the length value of the longest list
	list_size = 0
	for inner_list in parent_list:
		if len(inner_list) > list_size:
			list_size = len(inner_list)
	# print (list_size) # for testing
	return list_size # return the value for use outside of loop

# def construct_table_1(parent_list,list_size):
# 	# a function to help with arranging and constructing the columns of the table used in arrange_table_1()

# 	for x in range(0,list_size): # note that the length of the longest list may exceed the number of columns (length of the parent_list) which may throw an error
# 		# current_inner_list = 0
# 		# current_inner_list_index = 0
# 		current_inner_list_index = x # should start at 0
# 		current_inner_list = 0
# 		row_unit = []

# 		# we want to cycle through all the inner lists to construct the new row
# 		# the upper limit of the range should be the number of inner_lists in parent_list rather than the length of the longest inner list
# 		for x in range(0,list_size):
# 			if parent_list[current_inner_list]: # if the inner_list exists
# 				target_value = parent_list[current_inner_list][current_inner_list_index]
# 				# add target_value to the row_unit
# 				row_unit.append(target_value)
# 				current_inner_list += 1 # move to the next inner list
# 			# elif parent_list[current_inner_list][current_inner_list_index]:
# 			# 	row_unit.append(target_value)
# 			elif not parent_list[current_inner_list]:
# 				pass
# 			else:
# 				pass

# 		# once you finish constructing the row unit, add it to the colStruct holding list
# 		colStruct.append(row_unit)

def arrange_table_1(parent_list):
	
	longest_list_sz = get_longest_inner_list(parent_list)
	# print(longest_list_sz) # for testing

	# if longest_list_sz > len(parent_list):
	# 	construct_table_1(parent_list,longest_list_sz)
	# else:
	# 	construct_table_1(parent_list,len(parent_list))

	# once you finish constructing the row unit, add it to the colStruct holding list
	# colStruct.append(row_unit)
	
	# current_inner_list = 0 # this is handled by the while loop
	current_inner_list_index = 0
	row_unit = []

	if longest_list_sz >= len(parent_list):
		while current_inner_list_index <= longest_list_sz: # while we haven't reached the length of the longest inner list
			for inner_list in parent_list: # cycle through all inner lists
				if inner_list[current_inner_list_index]:
					insert_value = inner_list[current_inner_list_index]
					# print(insert_value) # testing
					# row_unit.append(inner_list[current_inner_list_index])
					row_unit.append(insert_value)
					# print(row_unit) # testing
				else:
					pass
			current_inner_list_index += 1 # move to the next index position
	else:
		while current_inner_list_index <= len(parent_list): # while we haven't reached the length of the longest inner list
			for inner_list in parent_list: # cycle through all inner lists
				if inner_list[current_inner_list_index]:
					insert_value = inner_list[current_inner_list_index]
					print(insert_value) # testing
					# row_unit.append(inner_list[current_inner_list_index])
					row_unit.append(insert_value)
					# print(row_unit) # testing
				else:
					pass
			current_inner_list_index += 1 # move to the next index position

	

	# once you finish constructing the row unit, add it to the colStruct holding list
	colStruct.append(row_unit)

	# at this point you've went through all possible positions on all inner lists and created a list with the columns stored in colStruct


def display_table_1(colStruct,colWidthList):	
	for row in colStruct:
		for item in row:
			print(item) # testing by printing to a new line for every item

def printTable():	
	set_colWidthList(colWidthList)
	arrange_table_1(tableDataSet_1)
	display_table_1(colStruct,colWidthList)

# execute function

printTable()



