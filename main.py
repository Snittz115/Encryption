def encrypt(phrase):
    encryption = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            encryption = encryption + "g%$"
        else:
            encryption = encryption + letter
    return (encryption)


print(encrypt(input("Type in a phrase: ")))