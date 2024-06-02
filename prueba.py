from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()

# Abrir la página web
url = 'https://www.bet365.es/?_h=GoHvveP5Yw8_sCKOqRsYYQ%3D%3D#/AC/B1/C1/D1002/E92494079/G981/I1/'
driver.get(url)

# Esperar un tiempo para que la página cargue completamente
time.sleep(10)  # Puedes ajustar el tiempo según sea necesario

# Obtener el contenido HTML de la página
html = driver.page_source

# Cerrar el navegador
driver.quit()

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extraer los datos de los partidos
matches = []
for match in soup.select('.gl-MarketGroupContainer '):  # Ajusta el selector según la estructura HTML de la página
    local_team = match.select_one('.rcl-ParticipantFixtureDetailsTeam_TeamName').text
    visitor_team = match.select_one('.rcl-ParticipantFixtureDetailsTeam_TeamName').text
    over_2_5 = match.select_one('.sgl-ParticipantOddsOnly80_Odds').text
    under_2_5 = match.select_one('.sgl-ParticipantOddsOnly80_Odds').text
    matches.append([local_team, visitor_team, over_2_5, under_2_5])

# Crear un DataFrame con los datos
df = pd.DataFrame(matches, columns=['Equipo Local', 'Equipo Visitante', 'Piu di 2,5', 'Meno di 2,5'])

# Guardar los datos en un archivo CSV
df.to_csv('./partidos.csv', index=False, sep=';')