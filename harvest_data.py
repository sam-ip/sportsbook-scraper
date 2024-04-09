import requests
import time
import os
import harvest_data_helpers

API_KEY = "95e2d43eb60275fd62ab83fae3d186f2"
SPORTS = 'basketball_nba'
MARKETS = 'h2h,spreads,totals'
REGIONS = 'us'
BOOKMAKERS = 'draftkings'
ODDS_FORMAT = 'decimal'
DATE_FORMAT = 'iso'

FAILED_ATTEMPTS = 0
MAX_FAILED_ATTEMPTS = 6
    
def fail_gracefully(status_code, response_text):
    print(f'Failed to get odds for sports: status code {status_code}\n response: {response_text}')
    FAILED_ATTEMPTS += 1
    print(f'request failed {FAILED_ATTEMPTS} times, exiting at threshold {MAX_FAILED_ATTEMPTS}')
    if FAILED_ATTEMPTS == MAX_FAILED_ATTEMPTS:
        os.exit()

# Scrapes current NBA game lines and updates final_odds.csv
class DraftKingsNBAScraper():

    def harvest_data(self):
        url = f'https://api.the-odds-api.com/v4/sports/{SPORTS}/odds'
        draftkings_api_response = None
        try: 
            draftkings_api_response = requests.get(
                url,
                params={
                    'api_key': API_KEY,
                    'regions': REGIONS,
                    'markets': MARKETS,
                    'odds_format': ODDS_FORMAT,
                    'date_format': DATE_FORMAT,
                    'bookmakers': BOOKMAKERS
                },
                timeout=5
            )
        except (requests.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException):
            fail_gracefully(draftkings_api_response.status_code, draftkings_api_response.text)

        if draftkings_api_response.status_code != 200:
            fail_gracefully(draftkings_api_response.status_code, draftkings_api_response.text)
            return
        
        FAILED_ATTEMPTS = 0
        markets = []
        draftkings_api_json = draftkings_api_response.json()
        for game in draftkings_api_json:
            sport_league = game["sport_key"]
            home_team, away_team, commence_time = game["home_team"], game['away_team'], game['commence_time']
            markets = harvest_data_helpers.get_markets(game, sport_league, home_team, away_team, commence_time)

        harvest_data_helpers.write_to_file(markets)

        # Check the usage quota
        print('Remaining requests', draftkings_api_response.headers['x-requests-remaining'])
        print('Used requests', draftkings_api_response.headers['x-requests-used'])

scraper = DraftKingsNBAScraper()
# 
while True:
    scraper.harvest_data()
    time.sleep(10)

# "https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey=95e2d43eb60275fd62ab83fae3d186f2&markets=h2h,spreads,totals&bookmakers=draftkings&commenceTimeFrom=2024-04-08T00:00:00Z"