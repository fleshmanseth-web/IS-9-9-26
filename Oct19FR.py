# Object orineted programming
from Oct19FortniteBot import FortniteBot

bots = []

bot1 = FortniteBot("Ron") #stamps out an instance of the bot, passing in the name as an argument
bot2 = FortniteBot("Harry")
bot3 = FortniteBot("Hermione")

#Change health for every bot
bot1.take_damage(50) #Calls the take damage method to the bot1 object
bot2.take_damage(10)
print(bot1.health)
print(bot2.health)
print(bot3.health)
print(bot1.name)

FortniteBot.max_health = 200 #Changes the class level variable of max_health
bot2.max_health = 100 #Changes the max health of bot2

print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)