class Item:

    name = ''
    description = ''
    value = 0
    contents = []

    def __init__(self, name, description=None, value = 0, contents=[]):
        self.name = name
        self.description = description
        self.value = value
        self.contents = contents

    def get_value(self):

        #if len(self.contents) == 0:
        #    return self.value
        #else:

        #print(type(self.contents), len(self.contents), self.contents)

        return self.value + sum(item.get_value() for item in self.contents)

    def print(self):
        #print(len(self.contents))
        for item in self.contents:
            yield ('Item: ', item.name)

    def get_contents(self):
        for item in self.contents:
            yield item

    def __len__(self):
        print('len')
        return len(list(self.get_contents()))

    def __getitem__(self, pos):
        print(pos)
        return self.contents[pos]
