list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
halfofplayers = len(list_players) // 2

first_team = list_players[:halfofplayers]
second_team = list_players[halfofplayers:]

print(first_team)
print(second_team)
