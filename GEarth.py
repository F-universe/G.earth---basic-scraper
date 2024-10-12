from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import logging

app = Flask(__name__)

# Percorso del driver di Chrome
chrome_driver_path = r"C:\Users\fabio\OneDrive\Desktop\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"

# Configura il logging per ottenere informazioni dettagliate
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_screenshot', methods=['POST'])
def get_screenshot():
    location = request.form['location']  # Ottieni la posizione dal form HTML
    
    logging.info(f"Ricerca della posizione: {location}")
    
    # Crea l'URL di Google Earth con la parola chiave dal form
    search_url = f"https://earth.google.com/web/search/{location}/"
    
    logging.info(f"Google Earth URL generato: {search_url}")
    
    # Imposta Selenium per aprire il browser
    options = webdriver.ChromeOptions()
    
    # Disabilita la modalità headless per il debug visivo (puoi riabilitarla in seguito se necessario)
    # options.add_argument("--headless")
    
    # Utilizza il Service per specificare il driver
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    screenshot_path = None
    
    try:
        # Apri Google Earth con il link personalizzato
        driver.get(search_url)
        logging.info("Pagina Google Earth caricata.")
        
        # Attendi che la pagina si carichi completamente
        time.sleep(10)  # Attendi il caricamento della mappa
        
        # Iniezione di JavaScript per eseguire lo zoom sulla posizione
        zoom_script = """
        var zoomLevel = 20000;  // Imposta il livello di zoom desiderato
        var flyTo = document.querySelector('earth-view') || window.earth;
        if (flyTo) {
            flyTo.setCamera({ altitude: zoomLevel });
        }
        """
        driver.execute_script(zoom_script)
        logging.info("Zoom eseguito sulla posizione.")
        
        # Attendi che lo zoom sia applicato
        time.sleep(5)
    
        # Effettua lo screenshot e salvalo
        screenshot_path = "static/screenshot.png"
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshoot salvato in: {screenshot_path}")
    
    except Exception as e:
        logging.error(f"Errore durante l'operazione: {e}")
    
    finally:
        driver.quit()
        logging.info("Browser chiuso.")

    # Gestisci il caso in cui lo screenshot non venga creato correttamente
    if not screenshot_path:
        screenshot_path = "static/default_image.png"
        logging.info("Utilizzo dell'immagine di default.")

    return render_template('index.html', screenshot=screenshot_path)

if __name__ == '__main__':
    app.run(debug=True)
