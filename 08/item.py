class Item:

    name = ''
    description = ''
    value = 0
    contents = []
    parent = None

    def __init__(self, name, description=None, value = 0, contents=[], parent=None):
        self.name = name
        self.description = description
        self.value = value
        self.contents = contents

    def add(self, item):
        item.parent = self
        self.contents.append(item)

    def get_value(self):

        return self.value + sum(item.get_value() for item in self.contents)

    def print(self, num_spaces=0):
        if(num_spaces == 0):
            print(f'{self.name.ljust(20)}${str(self.value).rjust(5)}')
        else:
            print(f'{self.repChar("|",num_spaces)}-{self.name.ljust(19 - num_spaces)}${str(self.get_value()).rjust(5)}')

        for item in self.contents:
            item.print(num_spaces=num_spaces + 1)

    def print_summary(self, num_spaces=0):
        if(num_spaces == 0):
            print(f'{self.name.ljust(20)}${str(self.get_value()).rjust(5)}')
        else:
            print(f'{self.repChar("|",num_spaces)}-{self.name.ljust(19 - num_spaces)}${str(self.get_value()).rjust(5)}')

        for item in self.contents:
            item.print(num_spaces=num_spaces + 1)

    def get_item(self, name):
        for item in self.contents:
            if str(item.name) == str(name):
                return item
        else:
            print(f'{name} not found')
            return self

    def get_contents(self):
        for item in self.contents:
            yield item

    def repChar(self, char, num):
        return char * num

    def __len__(self):
        print('len')
        return len(list(self.get_contents()))

    def __getitem__(self, pos):
        print(pos)
        return self.contents[pos]
