"""
🔹 1. Extract domain name from email
Input: "user@example.com"
Expected Output: "example.com"
💡 Hint: Use slicing and .index("@") or find position of '@'.
"""

user_input = "user@example.com"

user_input_num = user_input.index("@")
print(user_input[(user_input_num+1):])

"""
🔹 2. Get the middle character(s)
Input: "Python"
Expected Output: "th"
💡 Hint: Use len() to find the middle two letters for even-length strings.
"""

s = "Python"
first = s[(len(s)//2)-1]
second = s[len(s)//2]
print(first+second)

"""
🔹 3. Replace the last 4 characters with "****"
Input: "mysecret1234"
Expected Output: "mysecret****"
💡 Hint: Use negative indexing and string concatenation.
"""

Input = "mysecret1234"
stars = '*'
Inputs = Input[:-4]
ms = len(Input)-len(Inputs)
print(Inputs+stars.ljust(ms, '*'))

"""
🔹 4. Remove every vowel using slicing only (no loops)
Input: "education"
💡 Hint: If string is known, manually slice out non-vowel segments.
"""

s = "education"
result = s[1] + s[3] + s[5] + s[8]
print(result)

"""
🔹 5. Keep only characters at even positions
Input: "Programming"
Expected Output: "Pormig"
💡 Hint: Use slicing with step 2.
"""
Input = "Programming"
print(Input[::2])

"""
🔹 6. Reverse the first and last three characters separately
Input: "HelloWorld123"
Expected Output: "lleoWorl321"
💡 Hint: Use slice + reverse each part individually, then join.
"""

Input = "HelloWorld123"
indx = Input.index("1")
ch = Input[:indx]
num = Input[indx:]
chrv = ch[::-1]
numrv = num[::-1]
print(chrv+numrv)

"""
🔹 7. Mask phone number except last 4 digits
Input: "9876543210"
Expected Output: "******3210"
💡 Hint: Use * * * * * * + slice the last 4 digits.
"""

Input = "9876543210"
stars = '*'
inx1 = Input[:-4]
inx2 = Input[len(inx1):]
print(inx2)
print(stars.ljust(len(inx1), '*')+inx2)