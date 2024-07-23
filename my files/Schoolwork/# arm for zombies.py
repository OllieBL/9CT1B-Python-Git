# arm for zombies
# add new weapon
def addWeapon(arsenal):
    approval = input('do you want to add a weapon? ')
    if approval != 'yes':
        return
    weapon = input('what weapon? ')
    amount = input('how many? ')
    weapon = {weapon: amount}
    arsenal.update(weapon)

# display weapons
def displayWeapons(arsenal):
    approval = input('do you want to display weapons? ')
    if approval != 'yes':
        return
    for key, value in arsenal.items():
        print(key, ':', value)

# search for weapon
def search(arsenal):
    approval = input('do you want to search for a weapon? ')
    if approval != 'yes':
        return
    item = input('what weapon? ')
    if item in arsenal:
        print(arsenal[item])

# remove weapon
def deleteWeapon(arsenal):
    approval = input('do you want to delete a weapon? ')
    if approval != 'yes':
        return
    item = input('what weapon? ')
    del arsenal[item]

# final code
anti_zombie_arsenal = {
    'Shotgun': 10,
    'Machete': 5,
    'Crossbow': 8,
    'Hand Grenade': 3
}
while True:
    search(anti_zombie_arsenal)
    displayWeapons(anti_zombie_arsenal)
    addWeapon(anti_zombie_arsenal)
    deleteWeapon(anti_zombie_arsenal)