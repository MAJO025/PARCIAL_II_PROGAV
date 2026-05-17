from api import CountryAPI

if __name__ == "__main__":

    # EMMANUEL: E-M-M-A-N-U-E-L
    nombres_emmanuel = ["ethiopia", "mongolia", "morocco", "angola", "nepal", "uganda", "ecuador", "lebanon"]

    api = CountryAPI()



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