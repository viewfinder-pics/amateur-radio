# Bauanleitung: Tiefpassfilter 40/20 m und Dummy Load

Stand: 12.10.2026

Zwei Siebenpol-Tiefpässe (40 m und 20 m) dämpfen die 2. Oberwelle rechnerisch um etwa 48 dB bzw. 44 dB, dazu kommt ein 50-Ω-Dummy-Load für bis zu 5 W. Die Werte stammen aus einer Simulation mit idealen Bauteilen ([`tools/lpf_sim.py`](../tools/lpf_sim.py)); im Aufbau werden sie schlechter und müssen gemessen werden.

Hintergrund: Der Radioberry sendet roh nur etwa 20 mW mit deutlichem Oberwellenanteil [9]. Die PA-Platine hebt das auf 3 bis 5 W an. In den Händlerangaben steht nichts zu Tiefpassfiltern auf der Platine (siehe [Notizen zur PA-Platine](radioberry-pa-v2.md)). Deshalb gehört vor die Antenne ein Tiefpass.

## Auf einen Blick

Beide Filter haben dieselbe Schaltung: vier Kondensatoren (C1, C3, C5, C7) und drei Spulen (L2, L4, L6), 50 Ω Ein- und Ausgang, ausgelegt als Tschebyscheff-Tiefpass mit 0,1 dB Welligkeit. Die Spulen werden auf Ringkernen T37-6 (AL ca. 3,0 nH/Wdg.²) gewickelt. Das Konzept entspricht dem 7-Element-Filter nach dem G-QRP-Design von W3NQN, das auch QRP Labs als Bausatz anbietet [1].

| Bauteil | 40 m | 20 m |
| --- | --- | --- |
| C1 = C7 | 470 pF | 220 pF |
| C3 = C5 | 820 pF | 390 pF |
| L2 = L6 | 22 Wdg. (ca. 1,45 µH) | 15 Wdg. (ca. 0,68 µH) |
| L4 | 23 Wdg. (ca. 1,59 µH) | 16 Wdg. (ca. 0,77 µH) |
| Grenzfrequenz (−3 dB) | ca. 8,5 MHz | ca. 17,9 MHz |
| Verlust im Band (Spulengüte 60) | ca. 0,7 dB | ca. 0,5 dB |
| Dämpfung 2. Oberwelle | ca. 48 dB (14 MHz) | ca. 44 dB (28 MHz) |
| Dämpfung 3. Oberwelle | ca. 76 dB (21 MHz) | ca. 73 dB (42 MHz) |

Alle Kondensatorwerte sind Standardwerte (E12), die Spulen sind auf ganze Windungen gerundet. Die Abweichung von den idealen Werten liegt unter 5 % und ist in der Simulation berücksichtigt.

## Aufbau der Filter

Baue jedes Filter auf einer eigenen kleinen Platine mit durchgehender Massefläche, am einfachsten aus kupferkaschiertem Material. Jedes Filter bekommt ein eigenes Gehäuse aus Weißblech oder Alu, Eingang und Ausgang an den gegenüberliegenden Seiten.

1. **Spulen:** Kupferlackdraht 0,4 mm auf T37-6 wickeln. Jede Durchführung durch das Loch zählt als eine Windung. Die Windungen gleichmäßig über den Umfang verteilen. Pro Spule etwa 35 bis 40 cm Draht einplanen, inklusive Anschlüsse. Lack an den Enden abschaben und verzinnen.
2. **Kondensatoren:** Nur C0G/NP0 (Keramik, temperaturstabil), mindestens 100 V. Bei 5 W an 50 Ω liegen etwa 16 V Effektivwert und 22 V Spitze an.
3. **Reihenfolge:** Eingang, C1 nach Masse, L2, C3 nach Masse, L4, C5 nach Masse, L6, C7 nach Masse, Ausgang. Die Kondensatoren mit kürzesten Anschlüssen direkt an die Massefläche löten.
4. **Spulen-Lage:** Die drei Ringkerne nicht dicht nebeneinander legen und die Achsen um 90° drehen, damit sie sich nicht koppeln.
5. **Buchsen:** Eingang mit SMA-Buchse (passt direkt zum Ausgang der Radioberry-Platine), Ausgang mit BNC-Buchse für das Antennenkabel. Der Dummy Load bekommt eine BNC-Buchse.

Die beiden Filter werden von Hand getauscht. Ein Umschalter lohnt sich erst, wenn du häufig zwischen den Bändern wechselst.

## Prüfen und Abgleichen

Bevor ein Filter an eine Antenne kommt, sollte seine Kurve gemessen werden. Das geht am besten mit einem NanoVNA oder LiteVNA, den du dir oft im Ortsverband ausleihen kannst.

1. **Mit VNA:** Durchlassdämpfung (S21) im Band messen, sie sollte unter etwa 1 dB liegen. Danach die Dämpfung bei der 2. Oberwelle messen, Richtwert über 40 dB. Zusätzlich die Anpassung (S11) prüfen, ein SWR unter etwa 1,5 im Band ist ein gutes Ergebnis.
2. **Abgleich:** Den Grenzbereich verschiebst du über die Spulen. Windungen enger zusammenschieben senkt die Grenzfrequenz, auseinanderziehen hebt sie.
3. **Ohne VNA:** Oberwellen nur mit einem zweiten Empfänger hinter einem Dämpfungsglied von 30 bis 40 dB messen. Niemals 5 W direkt an einen SDR-Eingang legen.
4. **Erster Sendetest:** Filter zwischen PA und Dummy Load schalten, mit wenig Leistung beginnen, schrittweise erhöhen und Spulen und Kondensatoren auf Erwärmung prüfen.
5. **Antenne:** Erst wenn Messung und Dummy-Load-Test in Ordnung sind, kommt die Antenne an die Reihe.

## Dummy Load

Vier Metalloxid-Widerstände mit 200 Ω und 5 W, parallel geschaltet, ergeben 50 Ω. Bei 5 W Sendeleistung trägt jeder Widerstand etwa 1,25 W, es bleibt also reichlich Reserve. Keine drahtgewickelten Widerstände (Zement- oder Keramikgehäuse) verwenden, sie sind für Hochfrequenz zu induktiv.

1. Eine Buchse (SMA oder BNC, passend zu deinen Kabeln) an einer Seite einer kleinen Platine oder Blechbox montieren.
2. Die vier Widerstände sternförmig anordnen: ein Anschluss jedes Widerstands an den Mittelstift der Buchse, der andere an die Massefläche. Die Anschlüsse möglichst kurz halten.
3. Widerstand mit dem Multimeter prüfen, er sollte zwischen 47 und 53 Ω liegen.
4. Das SWR mit SWR-Meter oder VNA im Bereich 1 bis 30 MHz kontrollieren. Mit kurzen Anschlüssen bleibt es auf Kurzwelle in der Regel niedrig.

Bei längeren Tests dürfen die Widerstände handwarm werden, aber nicht heiß.

## Einkaufsliste

Die Mengen reichen für beide Filter und den Dummy Load, jeweils mit etwas Reserve für Fehlversuche.

| Teil | Menge | Hinweis |
| --- | --- | --- |
| Ringkern T37-6 (gelb) | 8 | 6 benötigt, 2 Reserve |
| Kupferlackdraht 0,4 mm | ca. 3 m | etwa 40 cm pro Spule |
| Kondensator 470 pF C0G/NP0, ≥ 100 V | 3 | 40 m: C1, C7 |
| Kondensator 820 pF C0G/NP0, ≥ 100 V | 3 | 40 m: C3, C5 |
| Kondensator 220 pF C0G/NP0, ≥ 100 V | 3 | 20 m: C1, C7 |
| Kondensator 390 pF C0G/NP0, ≥ 100 V | 3 | 20 m: C3, C5 |
| Widerstand 200 Ω, 5 W, Metalloxid, axial | 4 | Dummy Load |
| Buchsen SMA und BNC (Einbau) | 3 SMA, 4 BNC | SMA am Eingang jedes Filters, BNC am Ausgang und am Dummy Load, je 1 Reserve |
| Kupferkaschiertes Material | 1 Platte | Massefläche, etwa 10 × 15 cm |
| Gehäuse Weißblech oder Alu | 3 | 2 Filter, 1 Dummy Load |

### Preise und Bezugsquellen

Preise vom 12.10.2026, ohne Gewähr, inklusive MwSt., zuzüglich Versand. Wer es genau wissen will, schaut im jeweiligen Warenkorb nach.

| Teil | Quelle | Preis | Hinweis |
| --- | --- | --- | --- |
| Ringkern T-37-6 | WiMo [2] | 0,95 € | sofort lieferbar |
| SMA-Einbaubuchse | WiMo [3] | 3,95 € | sofort lieferbar |
| BNC-Buchse UG-1094, Einloch | WiMo [4] | 3,45 € | sofort lieferbar |
| Widerstand 200 Ω, 5 W (ROX5SSJ200R) | RS [5] | 7,50 € pro 20er-Pack | nur Restbestände |
| Kondensator 470 pF C0G, 100 V (SR211A471JAR) | RS [6] | 10,35 € pro 25er-Pack | gilt je Wert, Mindestmenge ein Pack |
| Kupferlackdraht 0,4 mm | RS [7] | 32,95 € pro 345-m-Spule | für 3 m unverhältnismäßig, besser Reststück |

Zum Versand: WiMo liefert nach Österreich, die Versandkosten liegen laut Abfrage im Warenkorb je nach Bestellung bei etwa 11,40 € bis 28 €. Eine Sammelbestellung im Ortsverband teilt Porto und Mindestmengen. Bei den Kondensatoren lohnt es sich, nach Kleinmengen oder Sortimenten zu suchen, statt ganze Packs zu kaufen. Beim Kauf auf C0G/NP0 achten, X7R oder Y5V sind für Filter ungeeignet.

### Fertigfilter als Alternative

Ein Angebot bei AliExpress (Hochleistungs-Tiefpassfilter 20/30/40 m, BNC, laut Händler 100 W und über 50 dB Oberwellendämpfung) kostet etwa 14,44 € pro Band plus 4,82 € Versand und Zoll. Die Angaben sind ungeprüft: Für ein 5-poliges Filter sind 50 dB optimistisch, die Kondensatorsorte (C0G?) ist nicht angegeben, und der Artikel hat erst wenige Bewertungen. Der Selbstbau ist nicht billiger, bietet aber bekannte Bauteile und nachvollziehbare Werte. Gemessen werden muss in beiden Fällen.

## Quellen

Siehe [README](../README.md#quellen).
