def reverse_words(s):
    return " ".join(s.split()[::-1])

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

s = "Madam in Eden Im Adam"
print("Original:", s)
print("Reversed words:", reverse_words(s))
print("Vowel count:", count_vowels(s))
print("Is palindrome:", is_palindrome(s))
