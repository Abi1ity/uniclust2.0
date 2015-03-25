from flask.ext.wtf import Form
from table import ItemTable, Item
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from flask.ext.babel import gettext
from app.models import User

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    
class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname
        
    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        if self.nickname.data != User.make_valid_nickname(self.nickname.data):
            self.nickname.errors.append(gettext('This nickname has invalid characters. Please use letters, numbers, dots and underscores only.'))
            return False
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append(gettext('This nickname is already in use. Please choose another one.'))
            return False
        return True
        
class PostForm(Form):
    post = TextField('post', validators = [Required()])
    
class SearchForm(Form):
    search = TextField('search', validators = [Required()])

class TasksForm(Form):
	your_tasks = TextField('tasks', validators = [Required()])#@@Table@@
	
	def fill_in_table(self):
		items = [Item('Name1', 'Description1'),
				 Item('Name2', 'Description2'),
				 Item('Name3', 'Description3')]

		items = [dict(name='Name1', description='Description1'),
				 dict(name='Name2', description='Description2'),
				 dict(name='Name3', description='Description3')]

		table = ItemTable(items)
		return table

class AllTasksForm(Form):
	all_tasks = TextField('all_tasks', validators = [Required()])#@@Table@@
	
	def fill_in_table1(self):
		items = [Item('User1Task', 'Description1'),
				 Item('User2Task', 'Description2'),
				 Item('User3Task', 'Description3')]

		items = [dict(name='User1Task', description='Description1'),
				 dict(name='User2Task', description='Description2'),
				 dict(name='User3Task', description='Description3')]

		table = ItemTable(items)
		return table


class NewTaskForm(Form):
	new_task = TextField('tasks', validators = [Required()])#@@Table@@
	
	def show(self):
		items = [Item('User1Task', 'Description1'),
				 Item('User2Task', 'Description2'),
				 Item('User3Task', 'Description3')]

		items = [dict(name='draft', description='Description1'),
				 dict(name='draft', description='Description2'),
				 dict(name='draft', description='Description3')]

		table = ItemTable(items)
		return table
		
"""
class AllTasks(Form):
	all_tasks = @@Table
	interface_gen = @@Interface Editor
	script_connection = @@Script Editor
	source_parce = @@Catalogue&Buttons
"""
