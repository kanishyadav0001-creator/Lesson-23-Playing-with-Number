numberLarget = int(input("Enter Largest number :"))
numberSmallest = int(input("Enter smallest number :"))

while (numberSmallest):
    numberstore = numberSmallest
    numberSmallest = numberLarget % numberSmallest
    numberLargest = numberstore

print("HCF IS :",numberLargest)    