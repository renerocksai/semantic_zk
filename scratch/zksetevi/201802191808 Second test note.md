# 201802191808 Pandoc gives us tables!
tags = #second #plain #oneandtwo

## Matchings und Matching Score

Gegeben *eine* Grundwahrheit, generiert der Algorithmus 3 binäre Matching-Ergebnisse:

* Subjekt gefunden (_true_ | _false_)
* Prädikat gefunden (_true_ | _false_)
* Objekt gefunden (_true_ | _false_)

### Matching Score
Die drei Ergebnisse werden zur weiteren Verarbeitung zu einem  Tupel _(subject_match, predicate_match, object_match)_ zusammengefasst, aber zwecks einfacher relativer Vergleichbarkeit (besser, schlechter) auch in einen numerischen Wert umgewandelt, analog einer 3-bit Binärzahl, wobei das höchstwertige Bit (MSB) dem Prädikat zukommt und das niederwertigste Bit (LSB) dem Objekt, wie die nachfolgende Funktionstabelle veranschaulicht:

 predicate_match   subject_match   object_match   **matching_score**
----------------- --------------- -------------- --------------------
        0               0                0               0
        0               0                1               1
        0               1                0               2
        0               1                1               3
        1               0                0               4
        1               0                1               5
        1               1                0               6
        1               1                1               7

In dieser numerischen Repräsentation ist also eine Wertung der Satzglieder enthalten: Prädikat (_interaction_) zählt am meisten, gefolgt von Subjekt (_interactor_) und Objekt (_interactee_). Möglicherweise kann das später von Vorteil sein, sofern diese Wertung für richtig gehalten wird.

Alternativ betrachtet, ergibt sich folgende Punkte-Zählweise:

Satzglied   Wertung
---------   -----------------------
Prädikat    **4** Punkte
Subjekt     **2** Punkte
Objekt      **1** Punkt

Der Matching Score ist nur relevant, um zwei Matching-Ergebnisse mit einander zu vergleichen; zum Beispiel den gleichen generierten Satz gegen 2 verschiedene Grundwahrheiten. Zur Beurteilung eines ganzen Datensatzes ist der Matching Score hingegen nicht besonders gut geeignet. Wird er gemittelt, verliert er seine Aussagekraft bezüglich der einzelnen Bewertungen bzw. Satzglieder. Beispiel:

* Ein Satz hat ein _predicate_match_, _subject_match_ und _object_match_ = 111 entspricht 7
* Ein Satz hat nur ein _object_match_ = 001 entspricht 1
* Die Mittelung entspricht nun dem Wert 4 = 100, was bedeuten würde, dass beide Sätze im Mittel das **Prädikat** treffen.

Statt des Matching Scores werden zur Datensatzbewertung Accuracies auf Basis von Matchings errechnet, wie weiter unten beschrieben.
