import json

def read_intro_cutscene(file_path):
    with open(file_path, 'r') as file:
        game_data = json.load(file)
        for event in game_data['events']:
            if event['id'] == 'intro_cutscene':
                return event['sentences']
        return []

def introSequence():
    intro_cutscene_sentences = read_intro_cutscene('Whispering-Dark Updated.json') 

    print("Press Enter to display the next line of text")
    for sentence in intro_cutscene_sentences:
        print(sentence)
        user_input = input()
        if user_input.lower() == 'q':
            break


    