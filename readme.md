# Projekt Unfallfrei - Zähler Nestle Werk Osthofen
Gemacht mit python3 für einen Raspberry Pi von Stefan Höhn ![Python application](https://github.com/dewomser/no_injuries_day_counter/workflows/Python%20application/badge.svg)

### Zugang über Wlan ist möglich:
/etc/wpa_supplicant/wpa_supplicant.conf
oder am Desktop (oben rechts)

### SSH ist möglich

### VNC verbindung (Viewer soll von Fa.Real sein)

Möglichkeit 1
Vncserver wird automatisch gestartet (kleines Bild)
Vncviewer (Handy) IP eingeben

Möglichkeit 2
VNCviewer (Desktop) vncviewer in die Konsole tippen
VNCviewer (Handy) IP:1 eingeben

### Zugangsdaten :
user=pi

pw= #####


### USB DCF-Empfänger  deinstalliert
Quelle:https://wiki.ubuntuusers.de/ntpd/ntp_mit_externen_lokalen_Zeitquellen/

### Anleitung rtc ds1392 Datum setzen /Uhrzeit einstellen: (8.JUli 13:32)

sudo date -u 07081332

ds1302_set_utc

Quelle: https://github.com/sourceperl/rpi.rtc

zusätzliche Quelle: Stackoverflow
