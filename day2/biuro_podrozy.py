import wycieczka

print(25 * "-")

rabaty = [0, 5, 10, 15, 20]

for r in rabaty:
    kw = wycieczka.kwota(
        transport=500,
        nocleg=800,
        wyzywienie=300,
        wycieczki=300,
        ubezpieczenie=100,
        inne=90,
        rabat=r
    )
    print(f"Rabat: {r:>3} -> {kw:.2f} zł")

# -------------------------
# Rabat:   0 -> 2090.00 zł
# Rabat:   5 -> 2025.00 zł
# Rabat:  10 -> 1960.00 zł
# Rabat:  15 -> 1895.00 zł
# Rabat:  20 -> 1830.00 zł
