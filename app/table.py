from flask_table import Table, Col

class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

