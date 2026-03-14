#palindrom str
text = input("enter the text you want to check palindrom: ")

reversed_str = ''

for char in text:
    reversed_str = char + reversed_str

if text == reversed_str:
    print("text is palindrom")
else:
    print("text is not palindrom")