#Task 1
retail_file = open('c:/Users/jiang/Downloads/retail/retail.txt')# open the original txt file
retail_all = retail_file.read().splitlines() # read the file into a list retail_all
print(retail_all)

#Task 2
retail_eight = retail_all[5:13] # Choose 8 industries via slicing and create a new list
retail_faves = '|'.join(retail_eight) # create a new list with a delimiter separating all items
print(retail_faves)

#Task 3
new_item = input('enter a 9th item to be added onto the retail list?')

#Task 4
retail_faves = retail_faves.lower()
new_item = new_item.lower()

#Task 5
retail_faves = retail_faves + '|' + new_item
retail_faves

#Task 6 
retail_mylist = retail_faves.split('|')
retail_mylist

#Task 7
retail_subset = []
num = len(retail_all)
num
num2 = num // 4
for i in range(1, num2 + 1):
    retail_subset.append(retail_all[4*i - 1])
retail_subset

#Task 8
retail_other_read = open('retail.txt')
