import re

alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
file_path = 'text.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
except Exception as e:
    print(f"Помилка: {e}")

def find_first_sentence(text):
    first_sentence = ''
    end_punctuation = ['.', '!', '?']

    for char in text:
        first_sentence += char

        if char in end_punctuation:
            break

    print(first_sentence)

def sort_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    sorted_words = sorted(words, key=lambda word: [alphabet.index(char) for char in word])
    for word in sorted_words:
        print(word)

find_first_sentence(text)
sort_text(text)
