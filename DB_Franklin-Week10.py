#NAME: Matthew Franklin
#DATE: March 27, 2023
#Assignment: Week 3

numberList = [1, 2, 3, 4, 5]
evenList = []
print(numberList)
print(evenList)

for number in numberList:
  #print(number)
  evenList.append(number * 2)

print(evenList)

evenList.pop(3)

print(evenList)
