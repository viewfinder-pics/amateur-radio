# Notizen: Radioberry V2.0 mit AURSINC Preamp/PA Board V2

Stand: 12.10.2026

Diese Notizen fassen zusammen, was in den Händlerangaben und Erfahrungsberichten zur Endstufenplatine für den Radioberry zu finden war. Die Angaben stammen aus Händler-Listings und sind teils widersprüchlich. Verbindlich sind nur Schaltplan und Messung am eigenen Gerät.

## Was die Platine laut Händler leistet

- Aufsteckplatine für den Radioberry, macht daraus ein kleines QRP-Radio. Die Händlerangaben nennen 3 bis 5 W Ausgangsleistung im Bereich 1 bis 50 MHz [8].
- Versorgung 6 bis 8 V, 8,4 V bevorzugt; ein Anschlusskabel für eine 8-V-Batterie liegt bei [8]. Eine zu hohe Spannung kann das Board zerstören, deshalb vor dem Einschalten nachmessen.
- Ein- und Ausgang als SMA, drei SMA-Kabel liegen bei (Rx, Tx, Antenne) [8].
- Eingebautes T/R-Relais: Mit einer einzigen Antenne lässt sich senden und empfangen. Das nennt ein Käufer als einen der größten Vorteile gegenüber dem Radioberry ohne Platine [8].
- Verschiedene Listings geben abweichende Ausgangsleistungen an (1,5 bis 3 W bzw. 3 bis 5 W). Die Platine kann ihrerseits eine weitere PA mit 10 bis 100 W ansteuern.

## Rohausgang des Radioberry

Der Radioberry selbst liefert nur etwa 20 mW (13 dBm) und hat laut dem Bericht auf [9] erheblichen Oberwellenanteil. Er läuft unter Raspberry Pi OS Bookworm (64 Bit) auf einem Raspberry Pi 4. Beim Installationsskript wird für die AURSINC-Platine die Variante **CL025** gewählt [9]. Das Netzteil für den Pi sollte mindestens 5 V / 3 A liefern.

## Warnungen aus Erfahrungsberichten

- **Dauerbetrieb:** Ein Käufer berichtet, dass die Endstufentransistoren nach etwa 20 Minuten fast dauerndem WSPR-Senden auf mehreren Bändern ausgefallen sind [8]. Daher Kühlung beachten, kurze Sendezeiten wählen und bei FT8 oder WSPR nicht mit voller Leistung fahren.
- **Lötstellen:** Ein Käufer berichtet, dass bei der SMA-Buchse die Lötstellen so groß sind, dass sie beim Aufstecken die Radioberry-Platine berühren können.
- **Dokumentation:** Mehrere Rezensenten bemängeln die dünne Dokumentation.
- **Oberwellen:** In den Listings steht nichts zu Tiefpassfiltern auf der Platine. Vor dem Anschluss an eine Antenne deshalb mit externem Tiefpass und Messung arbeiten (siehe [Bauanleitung](tiefpassfilter-und-dummy-load.md)).

## Inbetriebnahme und Fehlersuche (BG7IYN)

Ein Blogeintrag zum PA-Board V2 [10] beschreibt die Inbetriebnahme in SparkSDR und eine einfache Fehlersuche. Die Einstellungen stehen dort als Screenshots, die Messwerte lassen sich so zusammenfassen:

1. In SparkSDR die PA aktivieren und die passende Radio-Einstellung wählen.
2. Wenn die PA nicht sendet: Leuchtet die TX-LED rot?
3. Eingangsspannung (Vpp) sollte mindestens 7 V betragen.
4. Der Messpunkt für den PA-Strom sollte mindestens 2 V zeigen, das entspricht etwa 1 A (Strommessung über einen 40-mΩ-Widerstand mit INA199).
5. Sind Spannung und Strom in Ordnung, aber es kommt keine Leistung, ist laut Autor der Leistungs-MOSFET defekt.

## Sicherer erster Sendetest

1. 50-Ω-Dummy-Load und SWR-Meter oder VNA bereithalten (Bauanleitung siehe [Tiefpassfilter und Dummy Load](tiefpassfilter-und-dummy-load.md)).
2. Tiefpassfilter zwischen PA und Dummy Load schalten, mit wenig Leistung beginnen.
3. Oberwellen und Anpassung messen.
4. Erst danach eine Antenne anschließen (Dipol oder EFHW für 40 m und 20 m).

## Quellen

Siehe [README](../README.md#quellen).
