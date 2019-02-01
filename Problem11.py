def largestProductGrid(number):
    result = 0
    calc = 0
    liste = []
    strNumber = str(number)
    for i in range(0,800,40):
        zwischenliste = []
        for y in range(0,40,2):
            zwischenliste.append(int(strNumber[i+y:i+y+2]))

        liste.append(zwischenliste)
    for x in range(0,20):
        for y in range(0,20):
            if y < 17:
                calc = liste[x][y] * liste[x][y+1] * liste[x][y+2] * liste[x][y+3]
                if calc > result:
                    result = calc
            if x < 17:
                calc = liste[x][y] * liste[x+1][y] * liste[x+2][y] * liste[x+3][y]
                if calc > result:
                    result = calc
            if x < 17 and y < 17:
                calc = liste[x][y] * liste[x+1][y+1] * liste[x+2][y+2] * liste[x+3][y+3]
                if calc > result:
                    result = calc
            if x > 2 and y < 17:
                calc = liste[x][y] * liste[x-1][y+1] * liste[x-2][y+2] * liste[x-3][y+3]
                if calc > result:
                    result = calc
    return result


number= "08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748"

print(largestProductGrid(number))
