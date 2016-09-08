import dis
def f():
    x = 2
    return x


print dis.dis(f)
print help(dis)
