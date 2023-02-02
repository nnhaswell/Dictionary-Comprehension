import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

#print(data)

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

name = input('Please enter your name: ').upper()

phonetic_name = [phonetic_dict[letter] for letter in name]


print(phonetic_name)
