""" Abhiyaan Application Section B.1 Programming

    Problem statement: Input will be an array of 0's and 1's,
    output the minimum number of steps required to bring all the
    1's together.

    SAMPLE 
    INPUT:
    7
    1 1 0 1 0 0 1
    
    OUTPUT:
    4

    Solution by:
    Akhil Reddy
    CH20B076
    """
    

n = int(input()) # Just for formality, no use in python code
arr1 = list(map(int,input().split()))
# arr1 is the input list of 0's and 1's
arr2 = [] # Array of indices of ones of input array

count = 0
while(1 in arr1):
  arr2.append(arr1.index(1)+count)
  arr1.remove(1)
  count += 1
# In this while loop, we are creating arr2 by noting and appending the index of each 1 in arr1 and removing the 1 from arr1.

num = 0
if (len(arr2))%2 == 0:
  num = int((len(arr2))/2)-1
else:
  num = int((len(arr2)+1)/2)-1
fix = arr2[num]
# Here we are choosing the middle element of arr2 and storing it in the variable called fix.

tot = 0
for x in arr2:
  if x == fix:
    continue
  tot += (abs(fix - x) - 1)
#In this loop we take each element of arr2, calculate the number of elements between the fix and that element (abs(fix - x) - 1) and add it into the total.

num2 = len(arr2)-3

if num2 < 1:
  correction = 0
elif num2 % 2 == 0:
  correction = num2*(num2 + 2)/4
elif num2 % 2 != 0:
  correction = ((num2 + 1)**2)/4
else:
  print("Error")

final_tot = int(tot - correction)

print(final_tot)