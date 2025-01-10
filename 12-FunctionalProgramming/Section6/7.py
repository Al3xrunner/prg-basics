points = lambda competitor: sum(sorted(competitor)[1:-1])
results =  [(17,15,16,17,15),
            (16,18,19,17,19),
            (19,15,15,19,18),
            (18,17,19,15,16)]

print(list(map(points, results)))
