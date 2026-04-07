# TODO Напишите функцию find_common_participants
def find_common_participants (q , w, separator=','):
    x=set(q.split(separator))
    y=set(w.split(separator))
    common=x.intersection(y)
    return sorted(list(common))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
