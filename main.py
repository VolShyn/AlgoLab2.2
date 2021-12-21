import PySimpleGUI as sg


def display_hash(hashTable):
    for i in range(len(hashTable)):
        sg.Print(i, end=" ")

        for j in hashTable[i]:
            sg.Print("-->", end=" ")
            sg.Print(j, end=" ")

        sg.Print()


HashTable = [[] for _ in range(10)]


def Hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

sg.theme('BluePurple')

layout = [[sg.Text('You have hast table with chain method with keys from 0 to 9')],
          [sg.Text('KeyValue  ----  Value')],
          [sg.Input(key='-IN-', size=(5, 1)), sg.Input(key='-IN1-', size=(10, 1)),
           sg.Button('Insert')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Hash-table with chain method', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        display_hash(HashTable)
    if event == 'Insert':
        insert(HashTable, int(values['-IN-']), values['-IN1-'])
window.close()
