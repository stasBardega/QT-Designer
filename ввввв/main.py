#Відкриваємо для читання
with open("quotes.txt", "r",encoding = "UTF-8") as file:
    for line in file:
        print(line)

answer = input("Хто написав ці рядки")

#Відкриваємо для дописання
with open("quotes.txt", "a",encoding = "UTF-8") as file:
    file.write("\n(Шевченко Т. Г.)")

while True:
    #Запитуємо у користувача, чи хоче він додати ще одну цитату
    answer = input("Бажаєте додати ще одну цитату? (так / ні)")
    answer = answer.lower()

    if answer == "так":
        quote = input("Введіть цитату: ")
        author = input("Введіть автора: ")
        with open("quotes.txt", "a",encoding = "UTF-8") as file:
            file.write("\n, quote")
            file.write("\n, author")
            file.close()
    else:
        break

with open("quotes.txt", "r",encoding = "UTF-8") as file:
    for line in file:
        print(line)
