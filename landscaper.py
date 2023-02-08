## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "rusty scissors", "profit": 5, "cost": 5},
    {"name": "old lawnmower", "profit": 50, "cost": 50},
    {"name": "fancy lawnmower", "profit": 100, "cost": 250},
    {"name": "starving students", "profit": 250, "cost": 500}
    
]

## Game option function

def mow_lawn():
    tool = tools[game["tool"]]
    print(f"You mow the lawn with your {tool['name']} and make {tool['profit']} dollars")
    game["money"] += tool["profit"]
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game['money']} dollars and are using {tool['name']}")
# You win the game when you have a team of starving students and $1000. In this situation, send a message to the user telling them, they've won.

def upgrade():
    if game["tool"] >= len(tools) - 1):
        print("no more upgrades")
        return 0
    next_tool = tools[game["tool"]+1]
    if (next_tool == None): 
        print("There is no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("not enough money to buy tool")
        return 0
    print("you are upgrading your tool")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check():
    if(game["tool"] == 1 and game["money"] >= 1000):
        print("You win")
        return True
    return False

while (True):
    
    i = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")
    
    i = int(i)
    
    if (i == 1):
        mow_lawn()
        
    if (i == 2):
        check_stats()
        
    if (i == 3):
        upgrade()
        
    if (i == 4):
        print("You quit the game")
        break
    
    if (win_check()):
        break