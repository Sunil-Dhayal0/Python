# count_vowels
text = input("type the word:  ")

vowels = "aeiou"
count  = 0

text = text.lower()

for char in text:
    if char in vowels:
        count+=1

print(f"number of vowels {count}")

