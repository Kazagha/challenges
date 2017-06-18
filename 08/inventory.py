from item import Item

if __name__ == "__main__":

    room = Item(name='House', value=0)
    room = Item(name='Lounge Room', value=0, contents=[])
    room.add(Item('TV',value=4000, contents=[]))
    room.add(Item('Board Games',value=1000, contents=[Item('Dixit',value=250,contents=[])]))

    room.print()
    selected_room = room

    while(True):
        user_input = input('>>>  ').strip(' ')

        if(user_input == 'print'):
            selected_room.print()
        elif(user_input == 'add'):
            name = input('Item name: ')
            value = input('Item value: ')
            selected_room.contents.append(Item(name, value=int(value), contents=[]))
        elif(user_input[0:2] == 'cd'):
            if(user_input[3:] == '..'):
                selected_room = selected_room.parent
            else:
                selected_room = selected_room.get_item(user_input[3:])
        elif(user_input == 'exit'):
            break