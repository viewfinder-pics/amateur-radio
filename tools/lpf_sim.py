#!/usr/bin/env python3
"""Simulation der Siebenpol-Tiefpassfilter (40 m / 20 m) fuer die Radioberry-PA.

Schaltung: Tschebyscheff-Tiefpass, 0,1 dB Welligkeit, 50 Ohm, 7 Elemente
(C1 - L2 - C3 - L4 - C5 - L6 - C7, Kondensatoren als Querglieder nach Masse).
Die Spulen werden auf Ringkernen T37-6 (AL ca. 3,0 nH/Wdg.^2) gewickelt.

Aufruf:  python3 tools/lpf_sim.py

Ausgabe: Grenzfrequenz (-3 dB) sowie Einfuegedaempfung im Band und bei den
Oberwellen, jeweils fuer ideale Spulen und fuer Spulenguete Q = 60.
Die Werte gelten fuer ideale Bauteile und muessen am fertigen Filter
nachgemessen werden (NanoVNA / LiteVNA).
"""
import numpy as np

R = 50.0  # Systemimpedanz in Ohm
AL = 3.0  # nH pro Windung^2 (T37-6)

# Normierte Tschebyscheff-Werte, 0,1 dB Welligkeit, n = 7
G = [1.1812, 1.4228, 2.0967, 1.5734, 2.0967, 1.4228, 1.1812]

# Gewaehlte Bauteile (E12-Kondensatoren, ganze Windungen)
FILTER = {
    "40 m": dict(C1=470, C3=820, N2=22, N4=23, fc_ziel=8.0,
                 band=(7.0, 7.2), harm=(14.0, 21.0)),
    "20 m": dict(C1=220, C3=390, N2=15, N4=16, fc_ziel=16.0,
                 band=(14.0, 14.35), harm=(28.0, 42.0)),
}


def ideal_werte(fc_mhz):
    """Ideale Bauteilwerte (pF / uH) fuer die Ziel-Grenzfrequenz."""
    w = 2 * np.pi * fc_mhz * 1e6
    c1 = G[0] / (w * R) * 1e12
    c3 = G[2] / (w * R) * 1e12
    l2 = G[1] * R / w * 1e6
    l4 = G[3] * R / w * 1e6
    return c1, c3, l2, l4


def daempfung_db(f_mhz, c1, c3, l2, l4, q=None):
    """Einfuegedaempfung in dB (Kettenmatrix, 50 Ohm Quelle und Last)."""
    w = 2 * np.pi * f_mhz * 1e6

    def quer(c_pf):
        return np.array([[1, 0], [1j * w * c_pf * 1e-12, 1]], dtype=complex)

    def laengs(l_nh):
        z = 1j * w * l_nh * 1e-9
        if q:
            z += w * l_nh * 1e-9 / q  # Verlustwiderstand der Spule
        return np.array([[1, z], [0, 1]], dtype=complex)

    m = np.eye(2, dtype=complex)
    for el in (quer(c1), laengs(l2), quer(c3), laengs(l4),
               quer(c3), laengs(l2), quer(c1)):
        m = m @ el
    a, b, c, d = m[0, 0], m[0, 1], m[1, 0], m[1, 1]
    s21 = 2 / (a + b / R + c * R + d)
    return -20 * np.log10(abs(s21))


def grenzfrequenz_3db(c1, c3, l2, l4):
    for f in np.arange(1.0, 60.0, 0.01):
        if daempfung_db(f, c1, c3, l2, l4) > 3.0:
            return f
    return None


def main():
    for name, p in FILTER.items():
        l2 = AL * p["N2"] ** 2  # nH
        l4 = AL * p["N4"] ** 2
        c1, c3 = p["C1"], p["C3"]
        ideal = ideal_werte(p["fc_ziel"])
        print(f"== {name} ==")
        print(f"C1 = C7 = {c1} pF, C3 = C5 = {c3} pF")
        print(f"L2 = L6 = {p['N2']} Wdg. = {l2 / 1000:.2f} uH, "
              f"L4 = {p['N4']} Wdg. = {l4 / 1000:.2f} uH")
        print(f"ideal fuer fc = {p['fc_ziel']} MHz: C1 {ideal[0]:.0f} pF, "
              f"C3 {ideal[1]:.0f} pF, L2 {ideal[2]:.2f} uH, L4 {ideal[3]:.2f} uH")
        print(f"-3 dB bei {grenzfrequenz_3db(c1, c3, l2, l4):.1f} MHz")
        for f in p["band"] + p["harm"]:
            ideal_db = daempfung_db(f, c1, c3, l2, l4)
            real_db = daempfung_db(f, c1, c3, l2, l4, q=60)
            print(f"  {f:6.2f} MHz: {ideal_db:6.2f} dB (ideal)  "
                  f"{real_db:6.2f} dB (Q=60)")
        print()


if __name__ == "__main__":
    main()
