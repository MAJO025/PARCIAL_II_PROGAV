from api import CountryAPI

if __name__ == "__main__":

    # MARIA : M-A-R-I-A

    nombres_maria = ["mexico", "austria", "romania", "india", "australia"]

    # EMMANUEL: E-M-M-A-N-U-E-L
    nombres_emmanuel = ["ethiopia", "mongolia", "morocco", "angola", "nepal", "uganda", "ecuador", "lebanon"]

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


    # ── Países de Emmanuel ──
    print("\n" + "=" * 65)
    print(" Países de EMMANUEL (E·M·M·A·N·U·E·L)")
    print("=" * 65)
    paises_emmanuel = api.by_names_concurrente(nombres_emmanuel)

    for p in paises_emmanuel:
        print(p)
        print()

    if len(paises_emmanuel) >= 2:
        paises_emmanuel[0].comparar(paises_emmanuel[1:])