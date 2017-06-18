from item import Item

if __name__ == "__main__":

    room = Item(name='Lounge Room', value=0)
    room.contents.append(Item('TV',value=4000, contents=[]))
    room.contents.append(Item('Board Games',value=1000, contents=[Item('Dixit',value=250,contents=[])]))

    room.print()
    selected_room = room

    while(True):
        user_input = input('>>>  ').strip(' ')

        if(user_input == 'print'):
            selected_room.print()
        elif(user_input == 'new'):
            name = input('Item name: ')
            value = input('Item value: ')
            selected_room.contents.append(Item(name, value=int(value), contents=[]))
        elif(user_input[0:2] == 'cd'):
            print('Changing directory...')
            #print(f'{user_input[2:]}')
            selected_room = selected_room.get_item(user_input[3:])
        elif(user_input == 'exit'):
            break