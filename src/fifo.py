try:
    # read file with automatic close
    with open("test.txt", 'r+') as file:
        line1 = file.readline()
        print(line1)
        file.write("bla3")
        # not needed if file is in with block file.close()
except IOError as exception:
    print(exception)
else:
    print("everything done")
finally:
    file.close()

import urllib.request

full_url = 'https://www.google.ch'
try:
    response = urllib.request.urlopen(full_url)
except Exception:
    print("Couldn't connect to the google service.", full_url)
else:
    print(response.read())

import json

# define a dictionary
phonebook = {'jess': '079-777-8899', 'pete': '079-777-9988'}
print(json.dumps(phonebook, indent=4, separators=(';', ' --> ')))
with open("test.json", 'w') as jsonfile:
    jsonfile.write(json.dumps(phonebook, indent=4))

with open("test.json", "r") as newjsonfile:
    print("reading the file")
    file = json.load(newjsonfile)
    print(file["jess"])
