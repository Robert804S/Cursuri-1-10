lista_jucatori_teren = ['Andrei', 'Alin', 'Mirel', 'Sorin', 'Ovidiu']
lista_jucatori_rezerva = ['Jucator1', 'Jucator2', 'Jucator3', 'Jucator4', 'Jucator5']
lista_jucatori_scosi = []
SCHIMBARI_MAX = 3
# Jucator_ce_iasa = input('Introduceti nume jucator ce iasa: ')
# Jucator_ce_intra = input('Introduceti nume jucator ce intra: ')
# index_j_ce_iasa = lista_jucatori_teren.index(Jucator_ce_iasa)
# index_j_ce_intra = lista_jucatori_rezerva.index(Jucator_ce_intra)

while SCHIMBARI_MAX > 0:
    Jucator_ce_iasa = input('Introduceti nume jucator ce iasa: ')
    if Jucator_ce_iasa not in lista_jucatori_teren:
        print(f'nu se poate efectua schimbarea deoarece jucatorul {Jucator_ce_iasa} nu e in teren')
    Jucator_ce_intra = input('Introduceti nume jucator ce intra: ')
    if Jucator_ce_intra not in lista_jucatori_rezerva:
        print(f'nu se poate efectua schimbarea deoarece jucatorul {Jucator_ce_intra} nu esta rezerva')
        print(f'Mai aveti {SCHIMBARI_MAX} schimbari')
    if Jucator_ce_iasa in lista_jucatori_teren and Jucator_ce_intra in lista_jucatori_rezerva:
        index_j_ce_iasa = lista_jucatori_teren.index(Jucator_ce_iasa)
        index_j_ce_intra = lista_jucatori_rezerva.index(Jucator_ce_intra)
        SCHIMBARI_MAX = SCHIMBARI_MAX -1
        print(f'A iesit din teren jucatorul {Jucator_ce_iasa}, a intrat in teren {Jucator_ce_intra}, mai aveti {SCHIMBARI_MAX} schimbari')
        lista_jucatori_teren.pop(index_j_ce_iasa) and lista_jucatori_scosi.append(Jucator_ce_iasa)
        lista_jucatori_rezerva.pop(index_j_ce_intra) and lista_jucatori_teren.append(Jucator_ce_intra)
        print(f'Jucatorii din teren sunt: {lista_jucatori_teren}')
        print(f'Jucatori rezerve: {lista_jucatori_rezerva}')
        print(f'Jucatori scosi pe banca: {lista_jucatori_scosi}')
print('Nu se mai pot face alte modificati in acest meci')
