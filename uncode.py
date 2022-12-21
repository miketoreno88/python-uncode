# ru
# abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# word = "стретвоокуф"

# def code(text, step):
#     decryption = ""
#     for a in text:
#         for item in range(len(abc)):
#             if a == str(abc[item]):
#                 decryption += abc[item-step]
#     return(decryption)

# print(code(word, 2))

#eu
abc = "abcdefghijklmnopqrstuvwxyz"
word = "rtqitcoogt"

def code(text, step):
    decryption = ""
    for a in text:
        for item in range(len(abc)):
            if a == str(abc[item]):
                decryption += abc[item-step]
    return(decryption)

print(code(word, 2))