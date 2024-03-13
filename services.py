import requests
from difflib import get_close_matches

api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition(word):
    meaning =''

    try:
        response = requests.get(api_url + word)
        data = response.json()[0]
        if data:
            meaning = str(word).upper() + '\n'
            for i in range(len(data['meanings'][0]["definitions"])):
                meaning = meaning + f"Definition {i+1} : " +(data['meanings'][0]['definitions'][i]['definition']) +"\n"#+ "Example :  "+ (data['meanings'][0]['definitions'][i]['example']) +"\n\n"
            #meaning = meaning + (data['meanings'][0]['definitions'][0]['definition'])
        return meaning
    except (requests.exceptions.RequestException, KeyError):
            return "Word not found."


#while True:
#  word = input("Enter a word (or 'q' to quit): ")
#  if word.lower() == 'q':
#    break
#  meaning = get_definition(word)
#  print(meaning)