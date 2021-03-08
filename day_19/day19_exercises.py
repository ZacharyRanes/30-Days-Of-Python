import json


# Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words

def count_line_word(file_path):
    with open(file_path) as f:
        text = f.read()
        lines = text.splitlines()
        words = text.split()
    return [len(lines), len(words)]


files_to_count = ['obama_speech.txt', 'michelle_obama_speech.txt',
                  'donald_speech.txt', 'melina_trump_speech.txt']
for file_name in files_to_count:
    count = count_line_word('./day_19/'+file_name)
    print(f'The file {file_name} has {count[0]} lines and {count[1]} words.')


# Read the countries_data.json data file in data directory,
# create a function that finds the ten most spoken languages

def most_spoken_languages(filename, top_count):
    with open(filename) as file_ob:
        top_lang = {}
        json_ob = json.load(file_ob)
        for country in json_ob:
            for lang in country['languages']:
                if lang in top_lang:
                    top_lang[lang] += 1
                else:
                    top_lang[lang] = 1
    top_lang_list = (list(top_lang.items()))
    top_lang_list.sort(key=lambda a: a[1], reverse=True)
    return top_lang_list[:top_count]


print(most_spoken_languages('./day_19/countries_data.json', 10))


# Read the countries_data.json data file in data directory,
# create a function that creates a list of the ten most populated countries

def most_pop_countries(filename, top_count):
    with open(filename) as file_ob:
        countries_pop = []
        json_ob = json.load(file_ob)
        for country in json_ob:
            countries_pop.append((country['name'], country['population']))
    countries_pop.sort(key=lambda a: a[1], reverse=True)
    return countries_pop[:top_count]


print(most_pop_countries('./day_19/countries_data.json', 10))


# Read the hacker news csv file and find out:
# a) Count the number of lines containing python or Python
# b) Count the number lines containing JavaScript, javascript or Javascript
# c) Count the number lines containing Java and not JavaScript
