# python_course_project2# Gestione Studenti - Esercitazione Finale Python

Questo repository contiene l'esercitazione finale del corso di Python. Il progetto consiste in un semplice script che utilizza i principi della Programmazione Orientata agli Oggetti (OOP) per simulare la gestione dei dati e delle attività di uno studente universitario.

## Descrizione del Funzionamento

Il file principale definisce la classe `Studente`. Attraverso il costruttore della classe (`__init__`), ogni volta che viene creato un nuovo studente è possibile assegnargli delle informazioni personali uniche (stato dell'oggetto).

### Attributi della Classe
Ogni istanza della classe `Studente` memorizza i seguenti dati:
* **Nome:** Il nome dello studente.
* **Cognome:** Il cognome dello studente.
* **Età:** L'età dello studente.
* **Matricola:** Il numero di matricola universitario.
* **Voti:** Una lista inizialmente vuota che raccoglie i voti degli esami superati.

### Metodi della Classe
Lo script implementa le seguenti funzionalità per interagire con l'oggetto studente:
* `presentati()`: Stampa a schermo un messaggio formale con i dati anagrafici e la matricola dello studente.
* `aggiungi_voto(voto)`: Riceve un voto in input. Verifica che sia valido (compreso tra 18 e 30) e, in caso affermativo, lo aggiunge alla lista dei voti dello studente. Gestisce le eccezioni stampando messaggi di errore in caso di insufficienza o voto oltre il massimo consentito.
* `calcola_media()`: Calcola e stampa la media matematica dei voti presenti nella lista dello studente. Se la lista è vuota, gestisce il caso restituendo 0.
* `studia(ore)`: Stampa un messaggio che indica quante ore di studio ha completato lo studente.

### Simulazione
Alla fine dello script, vengono istanziati due oggetti separati di tipo `Studente` (es. "Angelica" ed "Erika"). Per dimostrare il corretto funzionamento dei metodi e l'indipendenza degli oggetti, il codice esegue una serie di operazioni dirette sul primo studente (presentazione, registrazione dei voti, calcolo della media e simulazione dello studio), generando i relativi output a schermo.

## Autore
* Bruno Zollino