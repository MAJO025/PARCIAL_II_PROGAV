from api import CountryAPI

if __name__ == "__main__":

    # MARIA : M-A-R-I-A

    nombres_maria = ["mexico", "austria", "romania", "india", "australia","ethiopia", "mongolia", "morocco", "angola", "nepal", "uganda", "ecuador", "lebanon"]

 

    api = CountryAPI()

    # ___ Países de Maria ___
    
    print("=" * 65)
    print("Países de MARIA (M·A·R·I·A)")
    print("=" * 65)
    paises_maria = api.by_names_concurrente(nombres_maria)

    for p in paises_maria:
        print(p)
        print()

    if len(paises_maria) >= 2:
        paises_maria[0].comparar(paises_maria[1:])

