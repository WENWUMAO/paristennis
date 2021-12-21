## CONTRIBUTOR
wmao

## WHY RUNNING THIS SCRIPT 
reserve one-hour(only）tennis session from https://tennis.paris.fr/

réserver une heure (une session) sur le site [PARIS TENNIS](https://tennis.paris.fr/)

## HOW TO RUN THIS SCRIPT
- install python > 3.0.0 to launch this script.
- install following imported modules (https://docs.python.org/fr/3.9/installing/index.html#basic-usage).
- vscode (and its plugin Python) might help. 

## BEFORE RUNNING THIS SCRIPT 
- an account (login/password) is mandatory.
- this script validates payment by one-ticket. You MUST already possessed tickets(for example, a package of 10 tickets).
- only one hour per account is allowed by Paris tennis. This script will not work if you have already a validated session.
- complete mandatory parameters in variable section.
- sport center and court's technical identifiers MUST be specified.

## HOW TO FIND SPORT CENTER AND COURT ID
- they are hidden under the 'Reserver' button in courts' list page when you are reserving normally.
- login to paris.tennis.com
- find an available session of your wished sport center and court
- inspect html element of the button 'Reserver' by F12 or right-click the element and select Inspect. you shall see the equipmentId and courtId.

## CONSEILS TO AUTOMATE RESERVATION SCRIPT
- crontab -> https://www.jcchouinard.com/python-automation-with-cron-on-mac/
- Python module 'pause': Currently this part is commented as follwing.
- crontab or pause does not work when pc is in mode sleep ou shutup. https://support.apple.com/fr-fr/guide/mac-help/mchlp2266/mac

## VERSION
- 0.0.0. Quite simple, this script does not handle any error. Make sure that all variables are correctly set. 
