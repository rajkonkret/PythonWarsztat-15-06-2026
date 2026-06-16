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
