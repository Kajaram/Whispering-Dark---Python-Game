import json

def read_intro_cutscene(file_path, sequence):
    with open(file_path, 'r') as file:
        game_data = json.load(file)
        for event in game_data['events']:
            if event['id'] == sequence:
                return event['sentences']
        return []

def sequence(sequenceName):
    intro_cutscene_sentences = read_intro_cutscene('assets/Whispering-Dark Updated.json', sequenceName) 
    print("\nPress Enter to display the next line of text")
    print("\nEnter 's' to skip")
    for sentence in intro_cutscene_sentences:
        print(sentence)
        user_input = input()
        if user_input.lower() == 's':
            break


    