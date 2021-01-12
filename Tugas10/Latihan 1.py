from datetime import *

def diffDate(y):
    hariini = datetime.date(datetime.now())
    print('Today date                  : ', hariini)
    
    y = y.split('-')
    y = date(int(y[0]), int(y[1]), int(y[2]))
    print('End date of the year        : ', y)
    
    selisih = (y - hariini).days
    print('Difference                  : ', selisih, 'today')
    return selisih

diffDate('2021-12-31')
