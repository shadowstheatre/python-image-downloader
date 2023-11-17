# Descrizione dello script di download immagini

Lo script script.py è progettato per scaricare immagini da un file di testo contenente gli URL delle immagini.

# Funzione download_images_from_file

La funzione download_images_from_file prende in input il percorso del file contenente gli URL delle immagini.

1. Apre il file e legge gli URL delle immagini.
2. Per ogni URL, effettua le seguenti operazioni:
- Rimuove spazi e caratteri di nuova riga dall'URL.
- Effettua una richiesta GET all'URL per ottenere la risposta.
- Se la risposta ha uno status code 200 (OK), procede con il download dell'immagine.
- Estrae l'anno dalla struttura dell'URL e crea una struttura di cartelle corrispondente.
- Salva l'immagine con il nome preso dall'URL nella cartella corrispondente.
- Stampa un messaggio di successo.
- Se non è possibile trovare l'anno nell'URL, stampa un messaggio di errore.
- Se la richiesta ha uno status code diverso da 200, stampa un messaggio di errore.
- Se si verifica un'eccezione durante il download dell'immagine, stampa un messaggio di errore.
Utilizzo dello script

Per utilizzare lo script, è necessario specificare il percorso del file contenente gli URL delle immagini. In questo caso, il percorso del file è "url.txt".

Esempio di utilizzo:
`file_path = "url.txt"
download_images_from_file(file_path)`

Lo script scaricherà le immagini dagli URL specificati nel file e le salverà nella struttura di cartelle corrispondente.
