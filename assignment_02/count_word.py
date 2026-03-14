# count word
sentence = input("type the sentence: ")
count = 0

for num in sentence.split():
    count+=1

print(f"number of words in sentence is:  {count}")

