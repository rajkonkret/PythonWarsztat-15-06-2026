def procent_na_ulamek(fn):
    def wrapper(transport, nocleg, rabat, *args, **kwargs):
        rate = rabat / 100
        return fn(transport, nocleg, rate, *args, **kwargs)

    return wrapper


@procent_na_ulamek
def oblicz_rabat(transport, nocleg, rabat):
    return (transport + nocleg) * rabat


def kwota(transport, nocleg, wyzywienie, wycieczki, ubezpieczenie, inne, rabat=0.0):
    rabat_kwota = oblicz_rabat(transport, nocleg, rabat)
    koszt_rabatowany = (transport + nocleg) - rabat_kwota
    koszt_pelny = wyzywienie + wycieczki + ubezpieczenie + inne
    suma = koszt_rabatowany + koszt_pelny
    return round(suma, 2)


print(__name__)

if __name__ == '__main__':

    print(kwota(
        transport=500,
        nocleg=800,
        wyzywienie=300,
        wycieczki=300,
        ubezpieczenie=100,
        inne=90
    ))
    # 2090.0

    rabaty = [0, 5, 10, 15, 20]

    for r in rabaty:
        kw = kwota(
            transport=500,
            nocleg=800,
            wyzywienie=300,
            wycieczki=300,
            ubezpieczenie=100,
            inne=90,
            rabat=r
        )
        print(f"Rabat: {r:>3} -> {kw:.2f} zł")
        # r:>3 - wyrównaj do prawej, szerokosc 3 znaki
    # Rabat:   0 -> 2090.00 zł
    # Rabat:   5 -> 2025.00 zł
    # Rabat:  10 -> 1960.00 zł
    # Rabat:  15 -> 1895.00 zł
    # Rabat:  20 -> 1830.00 zł
