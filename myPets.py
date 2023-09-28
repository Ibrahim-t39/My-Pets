myPets = ['zophie', 'pooka', 'fat-tail']
while True:
    print('Enter a pet name:')
    name = input().lower()
    if name not in myPets:
        print('I do not have a pet named ' + name + ', but i\'ll add it. :)')
        myPets.append(name)
    else:
        print(name + ' is my pet.')
        