
lays=10                             #price of product
kurkure=12.5
doritos=15
LS=3                                #number of lays
KE=2                                #number of kurkure
DS=2                                #number of doritos
while LS>0:                            #just assigning while loop for lays to run the code for multiple times
    total=int(input('amount'))
    demand=input('need')
    if demand == 'lays':
        a=int(input('total_need'))
        remainder=total-(lays*a)
        LS=LS-a
        print(LS)
    elif demand == 'kurkure':
        remainder=total-kurkure
        KE=KE-1                     #subtracting by 1 as the code can be run only once here
        print(KE)
    elif demand == 'doritos':
        remainder=total-doritos
        DS=DS-1
        print(DS)
    print(remainder)