from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_betting_odds(home_team, away_team):
    # Set up Selenium options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    # Specify the path to your ChromeDriver
    chrome_driver_path = 'path/to/chromedriver'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Load the Bet365 website
        url = f'https://www.bet365.it/?_h=5AIPoo_5STISLFEnCIzlHQ%3D%3D#/AC/B1/C1/D1002/G40/J99/I1/Q1/F^24/'  # Placeholder URL
        driver.get(url)

        # Wait for the necessary elements to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'match-container')))

        # Find all match containers
        match_containers = driver.find_elements(By.CLASS_NAME, 'match-container')  # Example class name

        for match in match_containers:
            teams = match.find_elements(By.CLASS_NAME, 'team-name')  # Example class name
            if home_team in teams[0].text and away_team in teams[1].text:
                odds = match.find_elements(By.CLASS_NAME, 'odds')  # Example class name
                home_odds = odds[0].text
                draw_odds = odds[1].text
                away_odds = odds[2].text
                return {
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_odds': home_odds,
                    'draw_odds': draw_odds,
                    'away_odds': away_odds
                }

        return "Match not found"
    except Exception as e:
        return str(e)
    finally:
        driver.quit()

# Example usage
home_team = "Almeria"
away_team = "Cadiz"
print(get_betting_odds(home_team, away_team))
