import random
# Player state
player = {
    'location': 'forest_entrance',
    'inventory': [],
    'energy': 10
}
def show_status():
    print('\nCurrent Location:', player['location'])
    print('Inventory:', player['inventory'])
    print('Energy:', player['energy'])
def forest_entrance():
    print('\nYou stand at the forest edge, where the misty path splits ....\n')
    print('Do you:\n'
          ' 1) Follow the glowing trail\n'
          ' 2) Head to the stone archway\n'
          ' 3) Climb a tall tree\n'
          ' 4) Check the humming bush\n')
    answer = int(input('Choose your path (1-4): '))
    if answer == 1:
        player['location'] = 'faerie_circle'
    elif answer == 2:
        player['location'] = 'ancient_ruins'
    elif answer == 3:
        player['location'] = 'treetop_view'
    elif answer == 4:
        print('You approach the humming bush cautiously....')
        if random.random() < 0.5:
            print('You found a glowing Moonberry! It shimmers with a soft light. You move on to the Faerie Circle.')
            player['inventory'].append('moonberry')
            player['location'] = 'faerie_circle'
        else:
            print('Just rustling leaves... nothing special this time. You move on to the Ancient Ruins.')
            player['location'] = 'ancient_ruins'
def faerie_circle():
    print('\nA ring of glowing mushrooms pulses with magic. Mischievous faeries giggle, offering a deal to guide you to the Crystal.\n')
    print('Do you:\n'
          '1) Accept their riddle for a shortcut\n'
          '2) Politely decline and backtrack\n'
          '3) Sneak past the faeries')
    answer = int(input('Choose your path (1-3): '))
    if answer == 1:
        print('\nThe faeries whisper a riddle and vanish into sparkles...')
        if random.random() < 0.5:
            print('You solve the riddle! A shimmering path opens to the Crystal Glade.')
            player['location'] = 'crystal_glade'
        else:
            print('You hesitate on the answer... vines snatch your feet! You’ve fallen into the Bramble Maze!')
            player['location'] = 'bramble_maze'
    elif answer == 2:
        print('\nYou bow respectfully and backtrack to the forest entrance.')
        player['location'] = 'forest_entrance'
        forest_entrance()
    elif answer == 3:
        print('\nYou try to sneak past the faeries...')
        if random.random() < 0.5:
            print('You slip past undetected and find the Crystal Glade!')
            player['location'] = 'crystal_glade'
        else:
            print('You trip! The faeries giggle as you tumble into the Bramble Maze!')
            player['location'] = 'bramble_maze'
def ancient_ruins():
    print('\nCrumbling pillars surround a stone altar. A rusty amulet lies in the dust, and a narrow tunnel leads deeper.\n')
    print('Do you:\n'
          '1) Take the amulet\n'
          '2) Enter the tunnel\n'
          '3) Search the ruins for clues')
    answer = int(input('Choose your path (1-3): '))
    if answer == 1:
        print('You have found an amulet! You move to the Altar Chamber.')
        player['inventory'].append('Amulet')
        player['location'] = 'altar_chamber'
    elif answer == 2:
        print('You enter the dark, narrow tunnel. It leads deeper into the ruins... You have exhausted yourself and lost some energy.')
        player['location'] = 'underground_chamber'
        player['energy'] -= 4
    elif answer == 3:
        print('You carefully search the ruins...')
        if random.random() < 0.5:
            print('You find a Map! You move on to enter the tunnel.')
            player['inventory'].append('Map')
            player['location'] = 'underground_chamber'
        else:
            print('You search everywhere... only to find cobwebs. That cost you some energy.')
            player['energy'] -= 5
def treetop_view():
    print('\nFrom a high branch, you see a distant tower, a glowing glade, and smoke rising from a camp. The branch creaks under your weight.\n')
    print('Do you:\n'
          '1) Climb toward the tower\n'
          '2) Descend and head to the glade\n'
          '3) Investigate the smoke')
    answer = int(input('Choose your path (1-3): '))
    if answer == 1:
        print('You find yourself in an abandoned tower. All that climbing has exhausted you. You lose some energy.')
        player['location'] = 'abandoned_tower'
        player['energy'] -= 6
    elif answer == 2:
        print('You journey on to the Crystal Glade.')
        player['location'] = 'crystal_glade'
    elif answer == 3:
        print('You carefully approach the smoke and come across a Wanderer’s Camp.')
        if random.random() < 0.5:
            print('You meet a kind villager who offers you a map. You part ways and head down a mysterious path.')
            player['inventory'].append('Map')
            player['location'] = 'mystery_path'
        else:
            print('Uh oh... the villager seems upset and throws you into the Bramble Maze.')
            player['energy'] -= 4
            player['location'] = 'bramble_maze'
def crystal_glade():
    print('\nYou arrive at a radiant glade. The Crystal of Dawn glows atop a pedestal, guarded by a spectral stag.\n')
    print('The stag speaks: "Prove your worth, traveler. Show your trust, your wisdom, or your will."\n')
    print('Do you:\n'
          '1) Offer the Amulet\n'
          '2) Use the Map to find a hidden path\n'
          '3) Plead with the stag\n'
          '4) Attempt to steal the Crystal')
    answer = int(input('Choose your path (1-4): '))
    if answer == 1:
        if 'Amulet' in player['inventory']:
            print('The stag bows its head. "Your heart is true." The path clears, and you retrieve the Crystal of Dawn!\nYOU WIN!')
            exit()
        else:
            print('You have no Amulet. The stag snorts, disappointed, and vines drag you into the Bramble Maze.')
            player['location'] = 'bramble_maze'
    elif answer == 2:
        if 'Map' in player['inventory']:
            print('Using the map, you navigate around the glade and retrieve the Crystal without disturbing the stag. A secret passage reveals ancient lore.\nYOU WIN!')
            exit()
        else:
            print('You fumble through the bushes, lost without a map. The stag notices and banishes you to the Bramble Maze.')
            player['location'] = 'bramble_maze'
    elif answer == 3:
        if random.random() < 0.5:
            print('Your sincerity moves the stag. It allows you to take the Crystal of Dawn.\nYOU WIN!')
            exit()
        else:
            print('The stag turns away, unconvinced. Vines trap you and drag you into the Bramble Maze.')
            player['location'] = 'bramble_maze'
    elif answer == 4:
        if random.random() < 0.3:
            print('You leap for the Crystal and grab it before the stag can react. You race away with it!\nYOU WIN by risk!')
            exit()
        else:
            print('You reach for the Crystal, but the stag rears back and strikes you down.\nGAME OVER.')
            exit()
def bramble_maze():
    print('\nThorns and shadows close around you. You are trapped in the Bramble Maze. You have a chance to escape but it will not be easy.\n')
    print('Do you:\n'
          '1) Use a Moonberry to regain strength\n'
          '2) Push through the thorns\n'
          '3) Rest and hope for rescue')
    answer = int(input('Choose your path (1-3): '))
    if answer == 1:
        if 'moonberry' in player['inventory']:
            print('You eat the Moonberry. Your strength recovers and you are able to climb out of the Bramble Maze. The forest guides you back to the entrance.')
            player['energy'] = 2
            player['inventory'].remove('moonberry')
            player['location'] = 'forest_entrance'
            forest_entrance()
        else:
            print('You have no Moonberry. The thorns grow tighter.\nGAME OVER!')
            exit()
    elif answer == 2:
        print('You push through the thorns... it costs you a lot of energy.')
        player['energy'] -= 8
        if player['energy'] <= 0:
            print('Exhausted and bleeding, you collapse.\nGAME OVER!')
            exit()
        else:
            print('You fight your way free and stumble back to the forest entrance.')
            player['location'] = 'forest_entrance'
            forest_entrance()
    elif answer == 3:
        if random.random() < 0.5:
            print('A gentle sprite finds you and guides you out. You return to the forest entrance.')
            player['location'] = 'forest_entrance'
            forest_entrance()
        else:
            print('The maze grows darker. No one comes. You are lost forever.\nGAME OVER!')
            exit()
# Start the game
print('Welcome to Mystic Forest Quest! Find the Crystal of Dawn to save your village.')
forest_entrance()
# Main game loop
while True:
    show_status()
    if player['energy'] <= 0:
        print('\nYou have no energy left. The forest consumes the unworthy.\nGAME OVER!')
        break
    if player['location'] == 'faerie_circle':
        faerie_circle()
    elif player['location'] == 'ancient_ruins':
        ancient_ruins()
    elif player['location'] == 'treetop_view':
        treetop_view()
    elif player['location'] == 'crystal_glade':
        crystal_glade()
    elif player['location'] == 'bramble_maze':
        bramble_maze()
    elif player['location'] == 'forest_entrance':
        forest_entrance()
    else:
        print('\nYou wander into unknown territory and vanish...\nGAME OVER!')
        break
