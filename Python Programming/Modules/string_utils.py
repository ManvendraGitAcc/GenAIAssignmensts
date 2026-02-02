def capitilize_word(w : str):
    capital = ""
    for ch in range(len(w)):
        capital += chr(ord(w[ch]) - 32)
    return capital

def reverse_string(w : str):
    count = len(w)
    capital = ""
    for ch in range(count, 0, -1):
        capital += w[ch - 1]
    return capital

def word_count(w : str):
    count = 0
    for ch in w:
        count += 1
    return count