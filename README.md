# amateur-radio

Notizen, Bauanleitungen und kleine Werkzeuge rund um den Amateurfunk. Die Sammlung ist ein Praxisprojekt und wird nach und nach erweitert.

## Inhalt

| Thema | Datei |
| --- | --- |
| Tiefpassfilter 40 m / 20 m und 50-Ω-Dummy-Load (Bauanleitung, Prüfen, Einkaufsliste) | [docs/tiefpassfilter-und-dummy-load.md](docs/tiefpassfilter-und-dummy-load.md) |
| Radioberry V2.0 mit AURSINC Preamp/PA Board V2 (Daten, Warnungen, Fehlersuche) | [docs/radioberry-pa-v2.md](docs/radioberry-pa-v2.md) |
| Simulation der beiden Filter (Python) | [tools/lpf_sim.py](tools/lpf_sim.py) |

## Projekt im Überblick

Ziel ist ein möglichst günstiges Kurzwellengerät mit dem selbstgebauten Radioberry V2.0 und der aufgesteckten PA-Platine (3 bis 5 W). Vor der ersten Antenne gehören dazu:

1. ein Tiefpassfilter pro Band (hier 40 m und 20 m), damit keine Oberwellen abgestrahlt werden,
2. ein 50-Ω-Dummy-Load für Tests ohne Antenne,
3. ein VNA (NanoVNA oder LiteVNA) zum Nachmessen der fertigen Filter.

## Simulation ausführen

```bash
pip install numpy
python3 tools/lpf_sim.py
```

Das Skript gibt für beide Filter die Grenzfrequenz sowie die Dämpfung im Band und bei den Oberwellen aus, jeweils für ideale Spulen und für eine Spulengüte von 60.

## Hinweise

- Alle Werte der Simulation gelten für ideale Bauteile und müssen am fertigen Filter nachgemessen werden.
- Preise und Verfügbarkeiten in den Dokumenten stammen vom 12.10.2026 und können sich ändern.
- Das Senden ist nur im Rahmen der eigenen Amateurfunkbewilligung zulässig.

## Quellen

[1] QRP Labs, "Low Pass Filter kit", https://shop.qrp-labs.com/LPF (G-QRP-Design von W3NQN; Anleitung: https://www.qrp-labs.com/images/lpfkit/instructions2a.pdf)

[2] WiMo, "Eisenpulver-Ringkern T-37-6", https://www.wimo.com/de/40093-37-6

[3] WiMo, "SMA-Einbaubuchse", https://www.wimo.com/de/42903

[4] WiMo, "BNC-Buchse Einloch UG-1094", https://www.wimo.com/de/42025

[5] RS, "TE Connectivity ROX Metalloxid Widerstand 200 Ω 5 % / 5 W", https://de.rs-online.com/web/p/durchsteckwiderstande/1870069

[6] RS, "KYOCERA AVX SR Keramik-Vielschichtkondensator C0G 470 pF 100 V", https://de.rs-online.com/web/p/mlccs-multilayer-ceramic-capacitors/5373763

[7] RS, "Block CUL100 Kupferdraht emailliert 0,4 mm, Spule 345 m", https://de.rs-online.com/web/p/kupferdrahte/7790722

[8] Newegg-Listing "AURSINC Radioberry Preamp Board V2" mit Käuferberichten, https://www.newegg.com/global/om-en/p/3C6-02X3-00TE7 (Händlerangaben, nicht herstellerverifiziert)

[9] PiDIYLab, "Radioberry HAT Raspberry Pi", https://pidiylab.com/radioberry-hat-raspberry-pi/

[10] BG7IYN, "Radioberry PAv2 Test", https://jumbo5566.github.io/pro/rb/2024/04/17/rb016_025.html
