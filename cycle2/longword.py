words=input("enter a list of words(comma-seperated):").split(',')
longlen=0
for word in words:
    word=word.strip()
    currlen=len(word)
    if currlen>longlen:
        longlen=currlen
        longword=word
print(f"longest word:'{longword}'with length{longlen}")
