def emoji_convertor(message):
    words = message.split(" ")
    emoji = {
        ':)' : "😀",
        '):' : "😪"
    }
    output = ""
    for word in words:
        output+=emoji.get(word, word) + ""
    return output

m=input('>')
final = emoji_convertor(m)
print(final)
