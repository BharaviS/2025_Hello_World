"""
🔹 1. Extract the last 3 characters
Input: "PythonMastery"
Expected Output: "ery"

💡 Hint: Use negative indexing with a slice.
"""

inp = "PythonMastery"
inp = inp[10:]
print(inp)

"""
🔹 2. Get every third character
Input: "ABCDEFGHIJKLMNO"
Expected Output: "ADGJMO"

💡 Hint: Use [::3] pattern.
"""
inp = "ABCDEFGHIJKLMNO"
print(inp[::3])

"""
 🔹 3. Reverse only the middle part
Input: "StartMiddleEnd"
Expected Output: "StartelddiMEnd"

💡 Hint: Slice the middle and reverse it separately.
"""

inp = "StartMiddleEnd"
inpv = len(inp)
print(inp[1:12:2])

"""
🔹 4. Trim first and last characters
Input: "!Hello!"
Expected Output: "Hello"

💡 Hint: Use s[1:-1].
"""

inp = "!Hello!"
print(inp[1:-1])

"""
🔹 5. Slice using input length
Ask user for a string. Return the first half using slicing.

💡 Hint: Use len() and s[:len(s)//2].
"""

inp = input("Enter your name: ")
print(inp[:len(inp)//2])

"""
🔹 6. Slice-based vowel extraction (no loop)
Input: "education"
Expected Output: "euaio" (Hint: manually build the vowel slice positions if known.)

💡 Hint: Find a creative way using fixed positions if string is known.
"""

inp = "education"
print(inp[::2])