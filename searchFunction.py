# python yes

#manipulate lists
import random
# function definitions
#find minimum value function
def findMinVal(myList):
  print("Original values: ", myList)
  minVal=100
  for i in range(0,len(myList)):
    if myList[i]<minVal:
      minVal=myList[i]
  print("The smallest value in the list: ",minVal)

# a function count(l,val) that returned the number of times value val appears in list l.
def count(myList, val):
	count = 0
	for val in myList:
		if (val == highest):
			count = count + 1
	return count
highest=10

# define some lists
lotteryNumbers= []
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))
lotteryNumbers.append(random.randint(1,10))

#function calls
findMinVal(lotteryNumbers)
print(" ")
print("Number of times 10 shows up in the list: ", count(lotteryNumbers, highest))
