from reactions import react

def start():
    print('Welcome to use the plasma chemistry generator')
    print('Please insert input gases, separated by comma')
    print('example: NH,CF2,N2H2+')
    inputs = input(':')
    inputs = inputs.split(',')

    go_to_processes = True

    print('Do you want a full reaction list?')
    print('Y for full reations, N for only species list')
    only_spe = input('Y or N?:')

    if only_spe == 'N' or only_spe == 'n':
        only_spe = True
    elif only_spe == 'Y' or only_spe == 'y':
        only_spe = False
    else:
        go_to_processes = False
        print('Wrong insert')
    
    print('Please insert the species scale you want or leave it blank to use the default value:')
    # Give limitation on species scale
    C = False
    N = False
    S = False
    Si = False
    O = False
    
    for i in inputs:
        if 'C' in i:
            C = True
        if 'N' in i:
            N = True
        if 'Si' in i:
            Si = True
        if 'S' in i:
            S = True
        if 'O' in i:
            O = True
    # Manually input the limitations
    # Limit the number of carbon atoms
    if C:
        max_C = input('Please input maximun number of C:')
        if max_C != int:
            max_C = 1
    else:
        max_C = 1
    # Limit the number of nitrogen atoms
    if N:
        max_N = input('Please input maximun number of N:')
        if max_N != int:
            max_N = 2
    else:
        max_N = 2
    # Limit the number of sulfur atoms
    if S:
        max_S = input('Please input maximun number of S:')
        if max_S != int:
            max_S = 1
    else:
        max_S = 1
    # Limit the number of silicon atoms
    if Si:
        max_Si = input('Please input maximun number of Si:')
        if max_Si != int:
            max_Si = 1
    else:
        max_Si = 1
    # Limit the number of oxygen atoms
    if O:
        max_O = input('Please input maximun number of Si:')
        if max_O != int:
            max_O = 1
    else:
        max_O = -1
    
    print('Do you want to limit the overall scale of molecules (Sum of all those elements you insert above)')
    print('Please input the number below, leave it blank for using the default value:')
    scale = input(':')
    if type(scale) == int:
        tot = scale
    else:
        tot = -1
    
    # go to processes
    if go_to_processes:

        try:
            react(inputs, only_spe, '', max_C, max_N, max_S, max_Si, max_O, tot)
        except:
            print('Sorry, there is an error occuring')
            print('please check the input gases and try again')

q = False
while not q:
    start()
    print('Completed!')
    print('inset C to continue or leave it blank to exit')
    c = input(':')
    if c == 'C' or c == 'c':
        q = False
    else:
        q = True