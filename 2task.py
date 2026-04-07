# TODO Найдите количество книг, которое можно разместить на дискете
page=100
line=50
sim=25
mem=1.44
mem1=4
to=1024
res=int((mem * to * to) // (page * line * sim * mem1))
print("Количество книг, помещающихся на дискету:", res)
