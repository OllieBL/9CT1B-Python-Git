def initials(name):
    initial = name[:1].upper()
    return initial

initials0 = []

initials0.append(initials(input('what is your first name? ')))
initials0.append(initials(input('what is your middle name? ')))
initials0.append(initials(input('what is your last name? ')))

print('you initials are:', initials0[0], initials0[1], initials0[2])