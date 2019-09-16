# Emoji Converter
meg = input("> ")
words = meg.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😞"
}
output = ""
for word in words:
   output += emojis.get(word, word) + " "
print(output)
