values = [1,4,-5,10,-7,2,3,-1,'-','N/A','97']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

print [v for v in filter(is_int, values)]
