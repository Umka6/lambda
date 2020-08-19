spisok = [-4,6,-10,9,-3,1,543,87,55,45]
#a = [x for x in spisok if x < 0] + [x for x in spisok if x >= 0]
print(sorted(spisok,key=lambda a:a))
