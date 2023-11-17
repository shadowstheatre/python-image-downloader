import os
import requests

# Funzione per scaricare immagini da URL
def download_images_from_file(file_path):
    with open(file_path, "r") as file:
        image_urls = file.readlines()

        for index, url in enumerate(image_urls):
            url = url.strip()  # Rimuovi spazi e caratteri di nuova riga

            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    # Estrai il nome del file e la struttura delle cartelle dall'URL
                    url_parts = url.split("/")
                    year_index = next((i for i, part in enumerate(url_parts) if part.isdigit() and len(part) == 4), None)
                    if year_index is not None:
                        folder_structure = "/".join(url_parts[year_index:-1])
                        file_name = url_parts[-1].strip()
                        os.makedirs(folder_structure, exist_ok=True)

                        # Salva l'immagine con il nome preso dall'URL
                        with open(f"{folder_structure}/{file_name}", "wb") as image_file:
                            for chunk in response.iter_content(chunk_size=1024):
                                image_file.write(chunk)
                        print(f"Immagine {index + 1} scaricata con successo.")
                    else:
                        print(f"Non è stato possibile trovare l'anno nell'URL dell'immagine {index + 1}.")
                else:
                    print(
                        f"Errore nello scaricare l'immagine {index + 1}. Status Code: {response.status_code}"
                    )
            except Exception as e:
                print(
                    f"Si è verificato un errore nello scaricare l'immagine {index + 1}: {str(e)}"
                )

# Passa il percorso del file contenente gli URL delle immagini
file_path = "url.txt"
download_images_from_file(file_path)