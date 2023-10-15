import json

cocktails = [{"name": "mojito", "ingredients": ['ice', 'mint', 'soda']}]

with open('cocktails.json', 'w', encoding='utf-8') as json_file:
    json.dump(cocktails, json_file, ensure_ascii=False, indent=2)
