from pojistenec import Pojistenec
import display_logic as dl
import database_logic as db

data = {}
while True:
    dl.show_hint()
    choice = input()
    
    match choice:
        case '1':
            dl.clear_screen()
            name = input('Vlozte jmeno: ')
            surname = input('Vlozte prijmeni: ')
            age = input('Vlozte vek: ')
            phone = input('Vlozte telefonni cislo: ')

            pojistenec = Pojistenec(name, surname, age, phone)
            data = db.add_to_database(data, pojistenec, name)
        case '2':
            dl.show_all(data)
        case '3':
            key = input('Zadejte jmeno: ')
            dl.show_one(data, key)
        case '4':
            break
        case _:
            print('Neplatny input!')

