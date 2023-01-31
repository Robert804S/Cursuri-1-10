# bancomat
# verificam user-ul si parola
# userul are 2 incercari de a-si introduce username-ul
# daca user-ul poate scoate o suma mai mica sau egala cu soldul curent
# daca introducem o suma prea mare poate sa aleaga daca vrea sa reincerce sau nu
# daca userul introduce o suma prea mare se iese din program

expected_user_name = 'user-name'
expected_password = 'password'
sold = 5000
username = 'user-name'
if username == expected_user_name:
    print('username corect')
else:
    print('username incorect!')
    username = input('introduceti username: ')
    assert username == expected_user_name,      'username gresit a doua oara'
password = 'password'
if len(password) != len(expected_password):
    print('parola gresita!')
    password = input('introduceti parola: ')
    assert password == expected_password,       'parola gresita a doua oara'
elif password == expected_password:
    print('parola corecta')
else:
    print('parola gresita!')
    password = input('introduceti parola: ')
    assert password == expected_password,          'parola gresita a doua oara'
suma_extrasa = int(input('introduceti suma: '))
if suma_extrasa <= sold:
    print('tranzactie reusita')
else:
    print('suma dorita depaseste soldul curent')
    reincerare = input('doresti sa incerci din nou?')
    if reincerare == 'da':
        suma_extrasa = int(input('introduceti suma: '))
        assert suma_extrasa <= sold,         'suma dorita e prea mare'
        print('tranzactie acceptata!')
    elif reincerare == 'nu':
        print('multumesc, o zi buna!')
