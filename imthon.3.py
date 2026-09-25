
def raqamlar_soni(matn):
    soni = 0

    for son in matn:
        if son.isdigit():
           soni += 1

    return soni

print(raqamlar_soni("abc123"))

