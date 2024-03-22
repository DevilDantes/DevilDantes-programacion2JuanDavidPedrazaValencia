lst= list()

Bandas = ['Queens','My Chemicals Romances','Kiss','Jackson Five','Evanescence']
print('Informacion:', lst)
print('Informacion:', len(lst))
print('Informacion:', Bandas)
print('Informacion:', len(Bandas))
print(Bandas.index('Queens'))
print(Bandas.index('Kiss'))
print(Bandas.index('Evanescence'))

Datos_personales = ["nombre" , "edad" , "altura" , "estado civil", "direccion"]
Datos_personales.append("telefono")
print(Datos_personales)
Datos_personales.append("Correo")
print(Datos_personales)

it_companies = ["Facebook" , "Google" , "Microsoft" , "Apple", "IBM" , "Oracle" , "Amazon"]
it_companies.insert(2, "Pollo Hermanos")
print(it_companies)
it_companies.insert(4, "Stark Industrie")
print(it_companies)
nose_existe= "Facebook" in it_companies
print(nose_existe)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
it_companies.remove("Facebook")
print(it_companies)
it_companies.pop(0)
print(it_companies)
it_companies.clear()
print(it_companies)