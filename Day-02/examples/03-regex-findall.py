# Method1 using re-search twice
import re

print("Using Method 1 ")
text = "The quick brown fox"

if re.search(r"quick", text) and re.search(r"brown", text):
    print("Both patterns found")
else:
    print("One or both patterns not found")

# Method 2: Using re.findall and sets
# import re

print("Using Method 2 ")
text = "The quick brown fox"
words = ["quick", "brown"]

matches = re.findall(r"\b(?:quick|brown)\b", text)
if set(words).issubset(matches):
    print("Both patterns found")
else:
    print("One or both patterns not found")
