"""
🔥 Challenge 1: Swap Halves
Input: "CodeMaster"
Expected Output: "MasterCode"
💡 Hint: Use length and split the string in half, then reverse the order.
"""

Input = "CodeMaster"
val = len(Input)//2
inx1 = Input[(val-1):]
inx2 = Input[:val-1]
print(inx1+inx2)

"""
🔥 Challenge 2: Keep only consonants using slicing
Input: "beautiful"
Expected Output: "btfl"
💡 Hint: Manually remove vowels using index-based slicing.
"""

s = "beautiful"
result = s[0] + s[4] + s[6] + s[8]
print(result)

"""
🔥 Challenge 3: Palindrome Check (Ignore loops and reversed)
Input: "madam"
Expected Output: "Palindrome"
Input: "python"
Expected Output: "Not Palindrome"
💡 Hint: Use slicing and comparison.
"""

def myslice(name):
    name = name
    rv = name[::-1]
    if name == rv:
        print("Palindrome")
    else:
        print("Not Palindrome")

myslice("madam")

"""
🔥 Challenge 4: Remove characters at odd indexes
Input: "IndexingIsFun"
Expected Output: "IdeigsFn"
💡 Hint: Use slice steps creatively.
"""

Input = "IndexingIsFun"
for i in range(len(Input)):
    if i % 2 == 0:
        print(Input[i], end="")

print()

"""
🔥 Challenge 5: Hide everything except first 2 and last 2 characters
Input: "Confidential"
Expected Output: "Co********al"
💡 Hint: Use len() and slicing + * repeat.
"""

Input = "Confidential"
stars = "*"
inx1 = Input.index("n")
inx2 = Input.index("a")
dev = Input[inx1:inx2]
print(Input[:inx1]+stars.ljust(len(dev), '*')+Input[inx2:])

"""
🔥 Challenge 6: Interchange first 3 and last 3 characters
Input: "Incredible"
Expected Output: "bleredInci"
💡 Hint: Use slices: first 3, middle, last 3.
"""
Input = "Incredible"
inx = len(Input)//3
i = Input[(Input.index("i"))]
rd = Input[inx:-(inx+1)]
rv1 = Input[:inx]
rvm = len(Input[:-inx])
rv2 = Input[rvm:]
print(rv2+rd+rv1+i)

"""
🔥 Challenge 7: Remove every 3rd character
Input: "abcdefghijklmn"
Expected Output: "abdefhijkmn"
💡 Hint: Manually reconstruct skipping indexes 2, 5, 8...
"""
Input = "abcdefghijklmn"
print(Input[0:2]+Input[3:6]+Input[7:9]+Input[9:11]+Input[11:])