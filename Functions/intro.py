import json
from Functions.engine import set_event_happened, check_event_happened
from Functions.fight import fightFunc

def read_intro_cutscene(file_path, sequence):
    with open(file_path, 'r') as file:
        game_data = json.load(file)
        for event in game_data['events']:
            if event['id'] == sequence:
                return event['sentences']
        return []

def sequence(sequenceName, events, player='', enemy='', dialogue='', items=''):

    if not check_event_happened(sequenceName, events):
        intro_cutscene_sentences = read_intro_cutscene('assets/Whispering-Dark Updated.json', sequenceName) 
        print("\nPress Enter to display the next line of text")
        print("\nEnter 's' to skip")
        for sentence in intro_cutscene_sentences:
            print(sentence)
            user_input = input()
            if user_input.lower() == 's':
                set_event_happened(sequenceName, events)
                break

        set_event_happened(sequenceName, events)
        
        if (sequenceName) == 'basement_confrontation' or sequenceName == 'wendigo_confrontation':
            fightFunc(player, enemy, dialogue, items)
                    




    