def input_str (text):
	n = input(text)
	return n

def phrase(text):
    vowel_letters = "ауоыиэяюёе"
    text = list(text.split())
    list_count = []
    for word in text:
        count = 0
        for i in word:
            if i in vowel_letters:
                count += 1
        list_count.append(count)
    return len(list_count) == list_count.count(list_count[0])


if phrase(input_str("Введите фразу: ")):
     print ("парам пам-пам")
else:
     print ("пам парам")
