import harvest_data_helpers
import csv

test_get_market_data = {
        "id": "c5e653a024326e1ae72231bb1c005328",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-04-09T23:10:00Z",
        "home_team": "Charlotte Hornets",
        "away_team": "Dallas Mavericks",
        "bookmakers": [{
            "key": "draftkings",
            "title": "DraftKings",
            "last_update": "2024-04-08T21:57:08Z",
            "markets": [{
                    "key": "h2h",
                    "last_update": "2024-04-08T21:57:08Z",
                    "outcomes": [{
                            "name": "Charlotte Hornets",
                            "price": 5.25
                        },
                        {
                            "name": "Dallas Mavericks",
                            "price": 1.17
                        }
                    ]
                },
                {
                    "key": "spreads",
                    "last_update": "2024-04-08T21:57:08Z",
                    "outcomes": [{
                            "name": "Charlotte Hornets",
                            "price": 1.91,
                            "point": 10.5
                        },
                        {
                            "name": "Dallas Mavericks",
                            "price": 1.91,
                            "point": -10.5
                        }
                    ]
                },
                {
                    "key": "totals",
                    "last_update": "2024-04-08T21:57:08Z",
                    "outcomes": [{
                            "name": "Over",
                            "price": 1.93,
                            "point": 221.5
                        },
                        {
                            "name": "Under",
                            "price": 1.89,
                            "point": 221.5
                        }
                    ]
                }
            ]
        }]
    }
get_market_data_list = harvest_data_helpers.get_markets(test_get_market_data, "basketball_nba", "Charlotte Hornets", "Dallas Mavericks", "2024-04-09T23:10:00Z")
assert len(get_market_data_list) == 6


test_write_to_file = harvest_data_helpers.write_to_file(get_market_data_list)
reader = csv.reader(open("final_odds.csv"))
assert len(list(reader)) > 2