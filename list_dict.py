# # list
# thislist=[1,"23",4,"wassa",69]
#
# thislist[3]
# print(len(thislist))
# thislist[1]
# # nested lists
# L=[["Apple","Google","Microsoft"],["Java","Python",["Ruby", "On Rail"],"PHP"],["Adam","Bart","Lisa"]]
# print(L[1][2][1])
#
# AFC_east=["New England Patriots","Bufallo Bills","Miami Dolphins","New York Jets"]
# AFC_west=["Chargers","Raiders","Broncos","Chiefs"]
# AFC=AFC_east+AFC_west
# print(AFC)
# print(AFC[1:4:2])
#
# #split single string
#
# name="Maddison"
# print(list(name))
# list(name[3])
#
# # split and join back
#
# str_team="New England Patriots"
# t=str_team.split()
# print(t)
#
# team_name="$$".join(t)
# print(team_name)
#
# # rename
# AFC_east[3]="New York Giants"
# print(AFC_east)
# AFC_east[3]="New York Jets"

# Dictionaries
names=["Bailey","Maddison","Aob"]
scores=[60,90,100]
grades=dict(zip(names, scores))
# for i in names:
#     value=scores[i]
#     key=names[i]
#     grades[i]={str(key):int(value)}



print(grades)