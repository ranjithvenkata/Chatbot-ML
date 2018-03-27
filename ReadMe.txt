README


Domain choice - Library ChatBot

Used json format for database and objectpath for querying data from it.
We have used objectpath library for querying json data to get entities results.


Steps to run :
Please install objectpath library by pip install objectpath.

Attributes -  Author name, title of book, subject of book.
Database file name - BooksData.json 
100 entries made in DB 
Bonus-1: - Used context switch for conditional branching on the basis of attributes
Functionalities implemented - 
 pick a book 



General Domain implemented - Restaurant ChatBot

Attributes -  Cuisine name, location of restaurant, Cost of restaurant.
Database file name - restaurantsData.json 
100 entries made in DB 
Bonus-1: - Used context switch for conditional branching on the basis of attributes


Functionalities implemented - 
search a restaurant
Bonus-2: Error Handling done when resultset  is null or queried data is not present in database

Working Sample chat after execution--

Note: Extra debug details are for the sake of convenience.

Library chat

BOT: Hi! How may I assist you?
User: pick a book
pick a book
scores [('SearchRestaurant', 0.1617004048582996), ('PickBook', 0.29286858974358976)]
Intent loadedPickBook
Title context

BOT: What's the title of the book?
User: Fairy Tales
fairy tales
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedPickBook
in Author context

BOT: What's the author name?
User: Hans Christian Andersen
hans christian andersen
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedPickBook
in Subject context

BOT: What's the subject you want to search?
User: Italian
italian
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedPickBook
in Reg context

BOT: Please type your registration number
User: 234
234
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedPickBook

Database retrieval:
{'title': 'Fairy Tales', 'author': 'Hans Christian Andersen', 'RegNo': '234', 'subject': 'Italian'}
the current intent isPickBook
$.books['Hans Christian Andersen' in @.author  or  'Fairy Tales' in @.title or 'Italian' in @.subject]
{'country': 'Denmark', 'author': 'Hans Christian Andersen', 'pages': 784, 'subject': 'Danish', 'year': 1836, 'title': 'Fairy tales', 'link': 'https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n', 'imageLink': 'images/fairy-tales.jpg'}
{'country': 'Italy', 'author': 'Dante Alighieri', 'pages': 928, 'subject': 'Italian', 'year': 1315, 'title': 'The Divine Comedy', 'link': 'https://en.wikipedia.org/wiki/Divine_Comedy\n', 'imageLink': 'images/the-divine-comedy.jpg'}
{'country': 'Italy', 'author': 'Giovanni Boccaccio', 'pages': 1024, 'subject': 'Italian', 'year': 1351, 'title': 'The Decameron', 'link': 'https://en.wikipedia.org/wiki/The_Decameron\n', 'imageLink': 'images/the-decameron.jpg'}
{'country': 'Italy', 'author': 'Giacomo Leopardi', 'pages': 184, 'subject': 'Italian', 'year': 1818, 'title': 'Poems', 'link': '\n', 'imageLink': 'images/poems-giacomo-leopardi.jpg'}
{'country': 'Italy', 'author': 'Elsa Morante', 'pages': 600, 'subject': 'Italian', 'year': 1974, 'title': 'History', 'link': 'https://en.wikipedia.org/wiki/History_(novel)\n', 'imageLink': 'images/history.jpg'}
{'country': 'Italy', 'author': 'Italo Svevo', 'pages': 412, 'subject': 'Italian', 'year': 1923, 'title': 'Confessions of Zeno', 'link': 'https://en.wikipedia.org/wiki/Zeno%27s_Conscience\n', 'imageLink': 'images/confessions-of-zeno.jpg'}

BOT: action: BookPicked !!




2. Restaurant Chat

BOT: Hi! How may I assist you?
User: find restaurant
find restaurant
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.32064777327935223)]
Intent loadedSearchRestaurant
in Cuisine context

BOT: For which cuisine are you looking for ?
User: Indian
indian
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedSearchRestaurant
in Location context

BOT: Please mention the location name such as east,west,north,south.
User: south
south
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedSearchRestaurant
in Cost context

BOT: Please mention the cost of the restaurant you are looking for?
User: medium
medium
scores [('PickBook', 0.06690705128205128), ('SearchRestaurant', 0.08477732793522268)]
Intent loadedSearchRestaurant
{'cuisine': 'Indian', 'cost': 'medium', 'location': 'south'}
the current intent isSearchRestaurant

Database retrieval:
$.restaurants['Indian' in @.cuisine  and  'south' in @.location and 'medium' in @.cost]
{'cuisine': 'Indian', 'cost': 'medium', 'name': 'Junoon', 'location': 'south'}
{'cuisine': 'Indian', 'cost': 'medium', 'name': 'Darbar Indian Cuisine', 'location': 'south'}
{'cuisine': 'Indian', 'cost': 'medium', 'name': 'Mantra', 'location': 'south'}
{'cuisine': 'Indian', 'cost': 'medium', 'name': 'Janta', 'location': 'south'}
{'cuisine': 'Indian', 'cost': 'medium', 'name': 'Hyderabad House', 'location': 'south'}

BOT: action: Restaurant is available


