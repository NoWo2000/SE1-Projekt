# Software Engineering - Datenverarbeitung & Alarm

## 🤓 Aufsetzen der Entwicklungs-Umgebung
In diesem Abschnitt findest du Informationen, wie du deine Umgebung zum Entwickeln einrichten kannst. Dafür kannst du dich entweder zwischen der Methode mittels Docker, oder der manuellen Installation entscheiden.

### 1. Mittels Docker 🐳
Hierfür benötigst du nur: *Docker*! Anleitungen zum Installieren findest du am einfachsten online. Ebenfalls benötigst du *docker-compose*, welche aber in der Regel mit installiert wird -> Sonst nachinstallieren

Um mit dem Programmieren anzufangen, kannst du einfach mit dem Befehl `cd .devcontainer && docker-compose up -d` alles starten, was du zum Programmieren benötigst.

Solltest du **VS Code** zum Programmieren nutzten, kannst du alles was du benötigst mithilfe der Erweiterung `ms-vscode-remote.vscode-remote-extensionpack` aufsetzten. Öffne dazu einfach direkt den Ordner `Datenverarbeitung`, öffne die Kommando-Eingabe (`Strg + P` in der Regel) und führe den Befehl `Remote-Containers: Reopen in Container` aus! Das war's 😄!

### 2. Manuelles Setup 🗿
Solltest du dir nicht Docker installieren wollen, benötigst du folgende Software zum Programmieren:

- Python 3.9 (vllt geht auch 3.8)
- Postgres SQL

Suche online einfach nach verfügbaren Anleitungen und installiere die entsprechende Software!

## 💻 Programmieren
> In diesem Abschnitt findest du alle wichtigen Angaben für's Programmieren!

### config.ini anlegen
Diese Datei wird nicht in git getrackt und dient dazu Konfigurationen und Passwörter zu speichern. Kopiere dafür die Datei `config.ini.example` an die Stelle `[...]/Datenübertragung/ config.ini` und passe die Werte an.

Ob die Config richtig gelesen wurde, kanns du jederzeit mit `python3 -m blueprint.resources.utils.config` (working-dir: `Datenübertragung/`) überprüfen. 

> *Achtung*: Wer die Docker-Remote-Development-Methode verwendet muss `postgres` als DB-Host angeben

### Datenverarbeitung
Für die Datenverarbeitung steht die Klasse `ApiRequest` in `resources/api.py` bereit. Diese kann beliebig importiert werden.

Um zu Überprüfen, ob die Abfrage funktionert: `python3 -m blueprint.resources.utils.api` (working-dir: `Datenübertragung/`)