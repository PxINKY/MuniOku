import json
import operator

x = "./Settings/moderators.json"
f = open(x, "r")
data = json.load(f)
f.close()
data2 = data["Moderators"]
# Legend:
# 0 = Owner
# 1 = Co-Owner
# 2 = Super Admin
# 3 = Executive Admin
# 4 = Executive Moderator
# 5 = World Admin
# 6 = Discord Admin
# 7 = Discord Moderator


