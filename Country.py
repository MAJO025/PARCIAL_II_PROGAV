class Country:
    def __init__(self, datos: dict):
        self.nombre    = datos["name"]["common"]
        self.capital   = datos.get("capital", ["—"])[0]
        self.poblacion = datos.get("population", 0)
        self.area      = datos.get("area", 0)
        self.region    = datos.get("region", "—")

    def __str__(self):
        return (
            f"{self.nombre} ({self.region})\n"
            f"  Capital:   {self.capital}\n"
            f"  Población: {self.poblacion:,}\n"
            f"  Densidad:  {self.densidad():.2f} hab/km²"
        )

    def densidad(self):
        return self.poblacion / self.area if self.area else 0

    def comparar(self, otros: list):
        todos = [self] + otros

        print(f"\n{'País':<20} {'Población':>15} {'Área':>12} {'Densidad':>15}")
        print("-" * 65)

        for p in todos:
            print(
                f"{p.nombre:<20} "
                f"{p.poblacion:>15,} "
                f"{p.area:>12,.0f} "
                f"{p.densidad():>12.2f} hab/km²"
            )

        print()
        print(f"  Mayor población : {max(todos, key=lambda p: p.poblacion).nombre}")
        print(f"  Mayor área      : {max(todos, key=lambda p: p.area).nombre}")
        print(f"  Mayor densidad  : {max(todos, key=lambda p: p.densidad()).nombre}")