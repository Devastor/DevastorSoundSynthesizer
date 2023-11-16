import time

from synthesizer import Player, Synthesizer, Waveform
import random
import csv

# player init
player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

notes_light_sounds = []
notes_hard_sounds = []


with open('notes.csv', 'r', newline='') as csvfile:
    notes_data = csv.reader(csvfile, delimiter=',')

    for row in notes_data:
        notes_hard_sounds.append({})
        if not ('#' in row[0]):
            notes_light_sounds.append({})
            if 'субк' in row[1]: notes_light_sounds[-1]['subcontr'] = row
            if 'контр' in row[1] and not ('субк' in row[1]): notes_light_sounds[-1]['subcontr'] = row
            if 'боль' in row[1]: notes_light_sounds[-1]['large'] = row
            if 'мал' in row[1]: notes_light_sounds[-1]['small'] = row
            if 'перв' in row[1]: notes_light_sounds[-1]['first'] = row
            if 'втор' in row[1]: notes_light_sounds[-1]['second'] = row
            if 'трет' in row[1]: notes_light_sounds[-1]['third'] = row
            if 'четв' in row[1]: notes_light_sounds[-1]['forth'] = row
            if 'пят' in row[1]: notes_light_sounds[-1]['fifth'] = row

        if 'субк' in row[1]: notes_hard_sounds[-1]['subcontr'] = row
        if 'контр' in row[1] and not ('субк' in row[1]): notes_hard_sounds[-1]['subcontr'] = row
        if 'боль' in row[1]: notes_hard_sounds[-1]['large'] = row
        if 'мал' in row[1]: notes_hard_sounds[-1]['small'] = row
        if 'перв' in row[1]: notes_hard_sounds[-1]['first'] = row
        if 'втор' in row[1]: notes_hard_sounds[-1]['second'] = row
        if 'трет' in row[1]: notes_hard_sounds[-1]['third'] = row
        if 'четв' in row[1]: notes_hard_sounds[-1]['forth'] = row
        if 'пят' in row[1]: notes_hard_sounds[-1]['fifth'] = row

print(notes_light_sounds)

TIME_PLAY = 1

play_1_2 = []

for el in notes_light_sounds:
    if 'first' in el or 'second' in el:
        try:
            player.play_wave(synthesizer.generate_constant_wave(float(el['first'][2]), TIME_PLAY / 2))
        except:
            player.play_wave(synthesizer.generate_constant_wave(float(el['second'][2]), TIME_PLAY / 2))
        play_1_2.append(el)

play_1_2_rev = play_1_2.copy()
play_1_2_rev.reverse()

for el in play_1_2_rev:
    if 'first' in el or 'second' in el:
        try:
            player.play_wave(synthesizer.generate_constant_wave(float(el['first'][2]), TIME_PLAY / 2))
        except:
            player.play_wave(synthesizer.generate_constant_wave(float(el['second'][2]), TIME_PLAY / 2))


while True:
    # random choice
    choice = int(random.random() * 14)

    index = 0

    for nota in play_1_2:
        if index == choice:
            try:
                player.play_wave(synthesizer.generate_constant_wave(float(nota['first'][2]), TIME_PLAY))
                a = input('Какая нота?')
                print(nota['first'][1])
            except:
                player.play_wave(synthesizer.generate_constant_wave(float(nota['second'][2]), TIME_PLAY))
                a = input('Какая нота?')
                print(nota['second'][1])



        index += 1

    time.sleep(1)

    #notes_light_sounds

# play
#player.play_wave(synthesizer.generate_constant_wave(440.0, 1.0))

