#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
codes = [18, 19, 20, 21, 22, 23, 24, 25, 26]

#Create a normal and comprehensive list that will display the codes.

#Normal List
normalCodes = []
for cd in codes:
    normalCodes.append(cd)

print("Programming related books in normal list: ", normalCodes)

#comprehensive list
comprehensiveCodes = [n for n in codes]
print("\nProgramming related books in comprehendive list: ", comprehensiveCodes)

#Create a normal and comprehensive list that will add the codes together for auditing purpose

#Adding normal list codes
totalNCode = []
sum = 0
for n in codes:
    sum += n

print("\nTotal codes for auditing in normsl list: ", sum)

#Adding comprehensive codes
sumCom = 0
totalcCode = [sumCom:= sumCom + n for n in codes]
print("\nTotal codes for auditing in comprehensive list: ", totalcCode)

#Create a normal and comprehensive list that will display only codes that are tracked by odd numbers.

#Normal list
oddNormal = []
for n in codes:
    if n % 2 != 0:
        oddNormal.append(n)

print("\nTracked odd numbers in normal list: ", oddNormal)

#Comprehensive List
oddComprehensive = [x for x in codes if x % 2 != 0]
print("\nTracked odd numbers in comprehensive list: ", oddComprehensive)

#Create a set to display the list of codes.
setList = set(codes)
print("\nSet list codes : ", setList)