class Context(object):

	def __init__(self,name):
		self.lifespan = 2
		self.name = name
		self.active = False

	def activate_context(self):
		self.active = True

	def deactivate_context(self):
		self.active = False

		def decrease_lifespan(self):
			self.lifespan -= 1
			if self.lifespan==0:
				self.deactivate_context()

class FirstGreeting(Context):

	def __init__(self):
		self.lifespan = 1
		self.name = 'FirstGreeting'
		self.active = True
    
class GetTitle(Context):

	def __init__(self):
		print('Title context')
		self.lifespan = 1
		self.name = 'GetTitle'
		self.active = True

class GetAuthor(Context):

	def __init__(self):
		print('in Author context')
		self.lifespan = 1
		self.name = 'GetAuthor'
		self.active = True


class GetSubject(Context):

	def __init__(self):
		print('in Subject context')
		self.lifespan = 1
		self.name = 'GetSubject'
		self.active = True
        
class GetCuisine(Context):

	def __init__(self):
		print('in Cuisine context')
		self.lifespan = 1
		self.name = 'GetCuisine'
		self.active = True

class GetLocation(Context):

	def __init__(self):
		print('in Location context')
		self.lifespan = 1
		self.name = 'GetLocation'
		self.active = True

class GetRegNo(Context):

	def __init__(self):
		print('in Reg context')
		self.lifespan = 1
		self.name = 'GetRegNo'
		self.active = True
        
class GetCost(Context):

	def __init__(self):
		print('in Cost context')
		self.lifespan = 1
		self.name = 'GetCost'
		self.active = True
class IntentComplete(Context):

	def __init__(self):
		self.lifespan = 1
		self.name = 'IntentComplete'
		self.active = True

class SpellConformation(Context):

	def __init__(self,index,CorrectWord,user_input,context):
		self.lifespan = 1
		self.name = 'SpellConformation'
		self.active = True
		self.index = index
		self.correct = CorrectWord
		self.tobecorrected = user_input
		self.contexttobestored = context
