dyrektor = [41,27,35,33,25,47,38,53,43,35,36]
wizytator = [38,24,34,29,27,47,43,52,39,31,29]

def nadawanie_rang(wartosci):
    wartosci_sorted = wartosci.copy()
    wartosci_sorted.sort(reverse=True)
    rangi = [0]*len(wartosci)
    for i in range(len(wartosci_sorted)):
        ile = wartosci.count(wartosci_sorted[i]) 
        if ile == 1:
            ind = wartosci.index(wartosci_sorted[i])
            rangi[ind] = i + 1
        else:
            ind_sum = ile
            inds = []
            for j in range(len(wartosci)):
                if wartosci_sorted[i] == wartosci[j]:
                    inds.append(j)

            for k in range(len(wartosci_sorted)):
                if wartosci_sorted[i] == wartosci_sorted[k]:
                    ind_sum += k
                    
            ranga = ind_sum/ile
            for ind in inds:
                rangi[ind] = ranga
    return rangi

print(nadawanie_rang(dyrektor))