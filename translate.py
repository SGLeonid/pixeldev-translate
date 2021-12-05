import requests
import json

history = []

# получение списка языков для перевода

url = "https://google-translate53.p.rapidapi.com/Google/GetLanguages"

headers = {
    'x-rapidapi-host': "google-translate53.p.rapidapi.com",
    'x-rapidapi-key': "f8f68316d2msh1cf4a3eac3bcab1p1dc879jsn9acc423c44c8"
    }

languages = requests.request("GET", url, headers=headers).json()

# Получение списка языков для перевода

def getlanguages():
    for lang in languages:
            print(lang + " : " + languages[lang])

# Функция непосредственного перевода текста
# Если всё ок - возвращает строку с переведённым текстом, иначе - None

def translate(text, language):

    if language in languages:

        url = "https://google-translate53.p.rapidapi.com/Google/Translate"

        querystring = {"text":text,"language":language}

        headers = {
            'x-rapidapi-host': "google-translate53.p.rapidapi.com",
            'x-rapidapi-key': "f8f68316d2msh1cf4a3eac3bcab1p1dc879jsn9acc423c44c8"
            }

        translated = requests.request("GET", url, headers=headers, params=querystring).json()

        if len(translated["text"]) > 0:
            history.append({"text":text, "language":language})

            return translated["text"]
        else:
            return None

    else:
        print ("Incorrect language key!")
        return None

# Ввод текста для перевода

def translateinp():
    print("Note: View list of language keys before translating!")
    text = input("Text: ")
    lang = input("Language to translate (key):")
    print(translate(text, lang))

# Вывод истории переводов

def gethistory():
    print("History of translate: ")
    for each in history:
        print ("Text: " + each["text"] + ", language: " + each["language"])

# Обработка не существующей функции

def funcerr(): print("Function change error!")

# Код для главной функции (Main)

mainmenu = ("Main menu", "1) Translate", "2) Language keys", "3) History", "4) Exit")
menuswitch = { 1:translateinp, 2:getlanguages, 3:gethistory }

while True:
    for each in mainmenu:
        print(each)

    func = int(input("Action: "))
    if func == 4: break;
    else: menuswitch.get(func, funcerr)()



