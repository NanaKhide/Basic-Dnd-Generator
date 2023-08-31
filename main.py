import json
import random

# Load the JSON object
# the keyword with allows us to ignore a closing statement so we gonna use that.
with open("quests.json") as f:
    data = json.load(f)

# Gets the entries in Quests
quests = data["Quests"]

# Picks a random quest from the list
random_quest = random.choice(quests)

# Prints the random quest
print(random_quest)
