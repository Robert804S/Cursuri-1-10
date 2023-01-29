# simulare unui bancomat

'''
sa definim un user si o parola
sa definim un sold al contului de tipul int
sa putem introduce de la tastatura userul si parola contului
daca username sau password este gresita sa se opreasca executarea programului
'''

user = 'username'
expected_password = '1234'
sold = 100
username = input('username: ')
assert user == username, 'username gresit!'
print('username corect')
parola = input('parola: ')
assert expected_password == parola, 'parola gresita'
print('parola este corecta')
suma = int(input('introduceti suma dorita: '))
assert suma <= sold, 'fonduri insuficiente'
print(f'suma dorita este: {suma}')
print('plata efectuata')