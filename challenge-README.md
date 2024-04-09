Goal
Harvest odds from Draftkings sportsbook. Make sure the odds are from one of the following major sports: MLB, NBA, NFL, or NHL. The odds you need to grab are the three basic markets only: Moneylines, Spreads, and Totals. After harvesting, write the resulting data to a csv file.

The following information should be present with each harvested odd within the csv file:
Sportsbook we are getting data from
Sport & League information
Game information (data, time, participants)
Market name (ex. Moneyline, Spread, etc..)
Bet selection name (ex. New York Knicks +1.5, Under 7.5, etc..)
Price of selection (-115, +200, etc..)
Timestamp of when odd was retrieved
Whether or not the bet is available or not (locked)

Feel free to use any technology/language/libraries required to execute the task. We use Python and Golang mostly; but not a requirement.

Extra Credit:
If multiple spreads / totals exist for a game, indicate which odds are considered main line vs. alternate line
Run harvesting task on a 10 second interval and update the csv on each iteration by appending data
Handle potential network request errors so the process fails gracefully
Unit testing
Timing
We expect the challenge to take between 1 and 2 hours max. We don't expect an entirely perfect solution. Please email the solution you have completed within the permitted time window. Please reach out with questions/clarification if you have any.
End Result
Please provide a csv of the resulting odds along with the code used to generate the file. The code you share should be able to run on a mac machine. If there are steps to create a runnable environment on any machine please share the steps as well.
