#creating a new list from exisiting list of string which hava not more than 3 character
stationaries=['box','pen','pencil','tip','bottle','note']
three_char=[word.upper() for word in stationaries if len(word)<=3]
print(three_char)