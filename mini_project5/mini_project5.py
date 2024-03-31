import statistics

def squares (*args):   
    if len(args) == 0:
        return
    m = statistics.mean(args)
    for i in args:
        yield (i - m) ** 2        


for i in squares(3, 4, 5):
    print(i)
