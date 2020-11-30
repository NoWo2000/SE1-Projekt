### GUI Gruppe 

Aus dem Pflichtenheft:

Stellt SKS-F eine Abweichung in einem Datensystemen fest, so soll eine Korrelation mit den anderen Datensystemen durchgeführt werden. Wird dabei festgestellt, dass ein Angriff mit 75% Wahrscheinlichkeit vorliegt, ist ein entsprechender Alarm auszulösen. Der Alarm muss mindestens den Zeitpunkt der Detektion, die betroffenen Systeme, den vermuteten Angriffstyp und die Wahrscheinlichkeit für einen vorsätzlichen digitalen Angriff beinhalten. Der Alarm muss auf einer zu erstellenden grafischen Oberfläche angezeigt werden. Diese grafische Oberfläche muss sowohl von unseren Mitarbeitern in den Büros und Verkehrszentralen, wie auch unseren Sicherheitskräften im Terminal und dem Flughafengelände aufrufbar sein.

Wir empfangen von Alarmierungsgruppe ein Objekt Alarm mit Parametern:   vorzugsweise JSON
- Zeitpunkt der Detektion
- betroffene Systeme
- vermuteter Angriffstyp
- Wahrscheinlichkeit eines Angriffs
- ob automatische Reaktion stattgefunden hat, und welche
- Checkliste

WICHTIG: Es werden alle potenziellen Alarme ab einer Wahrscheinlichkeit von 10% weitergeleitet, unsere GUI wird zwischen <75% und >75% entscheiden

Das erwartete JSON:
```
var event = {
        "id": id,                                   // Zahl (Auto-Inkrement)
        "time": time,                               // String
        "date": date,                               // String
        "affectedSystems": affectedSystems,         // Array von Strings
        "suspectedAttackType": suspectedAttackType, // String
        "probability": probability,                 // Zahl (10-100) (Zusendung von jedem Event ab 10% Probability)
        "automaticReaction": automaticReaction,     // Array von Strings
        "checklist": checklist                      // Array von Strings
    };
```

Implementierung der simplen grafischen Oberfläche in native CSS mithilfe von bootstrap o.ä. 

Alarm Darstellung
- Farbkodierung der Eintrittswahrscheinlichkeit, Deaktiviert -> grau
- 7-Tage Verlauf Ansicht (Angriffswahrscheinlichkeiten, die keinen Alarm ausgelöst haben)
