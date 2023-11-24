import csv
from itertools import product
import random
from gtts import gTTS

buchstabieralphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}


def csv_to_list(file_path):
    callsign_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            callsign_list.append(row[0])
    return callsign_list


# callsign generator
def callsign_generator():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    permutation = product(alphabet, repeat=3)
    all_free_callsigns = [''.join(list(p)) for p in permutation]
    return random.sample(all_free_callsigns, 1)[0]


# TODO create callsign with exactly 3 chars
# Filter list and check if callsign exits

def write_available_callsign_to_file(callsign):
    f = open("listOfAvailableCall.txt", "a")
    f.write(callsign + '\n')
    f.close()


def callsign_to_alphabet(callsign: str):
    return "" + buchstabieralphabet[callsign[0]] + " " + buchstabieralphabet[callsign[1]] + " " + buchstabieralphabet[
        callsign[2]]


reserved_callsigns = csv_to_list('Rufzeichenliste_AT.csv')

free_callsigns = []

while len(free_callsigns) < 5:
    callsign_candidate = callsign_generator()
    if callsign_candidate not in reserved_callsigns:
        free_callsigns.append(callsign_candidate)
        gTTS(text="Oscar Echo One " + callsign_to_alphabet(callsign_candidate), lang='en', slow=False).save(
            callsign_candidate + ".mp3")

print("Here are five callsigns not in use yet:")
print(free_callsigns)
