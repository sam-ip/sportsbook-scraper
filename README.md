### How to run/Verify:
- `pip install requirements.txt`
- `python harvest_data.py`
- look at final_odds.csv for data!

### To test:
- `python harvest_data_test.py` 

### Explanations/Further Improvements:
- Used this API from https://the-odds-api.com/ instead of draftkings api. I couldn't find an official draftkings API documentation website, and while there were unofficial API's, I opted to use this one as it could extend to other sports books and had fairly good documentation.
- The downside of using this API though, is unlike draftking's API response, it doesn't contain availability of the bet (assumption is that posted odds are available/live). Furthermore, I wasn't able to find enough data such that multiple spreads were offered. Though, I'd imagine there'd be metadata from the API response to distinguish main vs: alternate lines for a given game spread.
- Polling implemented, though naive. Using python's main running thread via timer object or the equivalent would have more control over how this program is run, especially when other methods may be called in the future.
- Fail gracefully implemented with some Exception handling, and a moreso naive retry mechanism is established. Alongside the 10 second delay, I figured that would be sufficient to give a minute of requests to configure before failing. Future work using exponential backoff could work depending on usage of harvest_data.
- My solution could be extended to accept different sports, leagues, regions, and books by accepting command-line arguments of these fields and parsing via sys.argv 
- more unit tests could be written (ex. input cleanliness, harvesting different sports, output cleanliness), and the format of data in the csv could be cleaner... especially if we're introducing more sportsbooks, API's to scrape, and different lines in the future. 
- Ran on Windows PC... I was playing video games before this on my PC lol

### Assumptions:
- all game line responses is an available bet you can make 
- 'h2h' means Moneyline, and a spread that's not indicated as negative is assumed positive. A quick mapping to "MoneyLine" would change this data type
