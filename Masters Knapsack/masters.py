import pandas

#hard coded player pool with value calculated using odds to win, odds to make cut, and a few other factors
players = [
    {"name": "Scottie Scheffler", "cost": 12100, "value": 11.85498674},
    {"name": "Jon Rahm", "cost": 11200, "value": 7.203654941},
    {"name": "Rory McIlroy", "cost": 10800, "value": 7.464695545},
    {"name": "Brooks Koepka", "cost": 10200, "value": 5.22624849},
    {"name": "Wyndham Clark", "cost": 10000, "value": 4.283009448},
    {"name": "Xander Schauffele", "cost": 9900, "value": 6.450148792},
    {"name": "Joaquin Niemann", "cost": 9600, "value": 4.928942348},
    {"name": "Viktor Hovland", "cost": 9500, "value": 4.463283997},
    {"name": "Patrick Cantlay", "cost": 9400, "value": 4.333021767},
    {"name": "Jordan Spieth", "cost": 9300, "value": 5.067021118},
    {"name": "Will Zalatoris", "cost": 9200, "value": 3.850902467},
    {"name": "Ludvig Aberg", "cost": 9100, "value": 4.733945338},
    {"name": "Hideki Matsuyama", "cost": 9000, "value": 5.552254718},
    {"name": "Cameron Smith", "cost": 8900, "value": 4.002419345},
    {"name": "Dustin Johnson", "cost": 8800, "value": 4.144578119},
    {"name": "Justin Thomas", "cost": 8700, "value": 4.062622854},
    {"name": "Tony Finau", "cost": 8600, "value": 4.300275606},
    {"name": "Cameron Young", "cost": 8500, "value": 3.884242087},
    {"name": "Collin Morikawa", "cost": 8400, "value": 4.040058139},
    {"name": "Max Homa", "cost": 8300, "value": 3.636219574},
    {"name": "Bryson DeChambeau", "cost": 8200, "value": 4.248692132},
    {"name": "Sam Burns", "cost": 8100, "value": 3.60498711},
    {"name": "Shane Lowry", "cost": 8000, "value": 4.04905559},
    {"name": "Matt Fitzpatrick", "cost": 7900, "value": 4.430537836},
    {"name": "Brian Harman", "cost": 7800, "value": 3.636219574},
    {"name": "Jason Day", "cost": 7700, "value": 3.678847896},
    {"name": "Sahith Theegala", "cost": 7700, "value": 4.062622854},
    {"name": "Sungjae Im", "cost": 7600, "value": 3.23035548},
    {"name": "Tyrrell Hatton", "cost": 7600, "value": 3.686022611},
    {"name": "Tommy Fleetwood", "cost": 7500, "value": 4.198331251},
    {"name": "Corey Conners", "cost": 7500, "value": 3.418524626},
    {"name": "Tom Kim", "cost": 7400, "value": 2.949444269},
    {"name": "Patrick Reed", "cost": 7400, "value": 3.267337802},
    {"name": "Min Woo Lee", "cost": 7300, "value": 3.23035548},
    {"name": "Rickie Fowler", "cost": 7300, "value": 2.610096855},
    {"name": "Justin Rose", "cost": 7200, "value": 2.703114937},
    {"name": "Russell Henley", "cost": 7200, "value": 3.64534254},
    {"name": "Akshay Bhatia", "cost": 7200, "value": 3.25898582},
    {"name": "Adam Scott", "cost": 7100, "value": 3.293285535},
    {"name": "Si Woo Kim", "cost": 7100, "value": 3.597586193},
    {"name": "Stephan Jaeger", "cost": 7100, "value": 2.651092666},
    {"name": "Nick Taylor", "cost": 7000, "value": 2.682111863},
    {"name": "Phil Mickelson", "cost": 7000, "value": 1.597970334},
    {"name": "Harris English", "cost": 7000, "value": 2.848653431},
    {"name": "Cameron Davis", "cost": 6900, "value": 2.393534942},
    {"name": "Matthieu Pavon", "cost": 6900, "value": 2.450841989},
    {"name": "Chris Kirk", "cost": 6900, "value": 3.017478085},
    {"name": "Tiger Woods", "cost": 6800, "value": 1.9598333},
    {"name": "Sergio Garcia", "cost": 6800, "value": 2.941576467},
    {"name": "J.T. Poston", "cost": 6800, "value": 2.586695154},
    {"name": "Sepp Straka", "cost": 6700, "value": 2.48895165},
    {"name": "Ryan Fox", "cost": 6700, "value": 2.407195026},
    {"name": "Keegan Bradley", "cost": 6700, "value": 2.82415587},
    {"name": "Nicolai Hojgaard", "cost": 6700, "value": 2.469601103},
    {"name": "Byeong Hun An", "cost": 6700, "value": 3.042367305},
    {"name": "Eric Cole", "cost": 6600, "value": 2.407195026},
    {"name": "Adam Hadwin", "cost": 6600, "value": 2.765674189},
    {"name": "Erik Van Rooyen", "cost": 6600, "value": 2.618553557},
    {"name": "Jake Knapp", "cost": 6600, "value": 2.205756519},
    {"name": "Adrian Meronk", "cost": 6500, "value": 2.63144203},
    {"name": "Luke List", "cost": 6500, "value": 2.076615802},
    {"name": "Thorbjorn Olesen", "cost": 6500, "value": 2.274422123},
    {"name": "Nick Dunlap", "cost": 6500, "value": 2.03569255},
    {"name": "Emiliano Grillo", "cost": 6400, "value": 2.771619525},
    {"name": "Kurt Kitayama", "cost": 6400, "value": 2.538423948},
    {"name": "Bubba Watson", "cost": 6400, "value": 1.926753337},
    {"name": "Gary Woodland", "cost": 6400, "value": 2.192096435},
    {"name": "Taylor Moore", "cost": 6400, "value": 2.37153549},
    {"name": "Austin Eckroat", "cost": 6300, "value": 2.329470246},
    {"name": "Ryo Hisatsune", "cost": 6300, "value": 1.980523652},
    {"name": "Charl Schwartzel", "cost": 6300, "value": 1.980523652},
    {"name": "Lucas Glover", "cost": 6300, "value": 2.600355239},
    {"name": "Danny Willett", "cost": 6300, "value": 1.285844538},
    {"name": "Denny McCarthy", "cost": 6200, "value": 3.03649848},
    {"name": "Lee Hodges", "cost": 6200, "value": 1.980523652},
    {"name": "Adam Schenk", "cost": 6200, "value": 2.297611843},
    {"name": "Peter Malnati", "cost": 6200, "value": 1.867529078},
    {"name": "Grayson Murray", "cost": 6200, "value": 0.4319321501},
    {"name": "Christo Lamprecht", "cost": 6100, "value": 0.4319321501},
    {"name": "Camilo Villegas", "cost": 6100, "value": 0.4319321501},
    {"name": "Jasper Stubbs", "cost": 6100, "value": 0.4319321501},
    {"name": "Zach Johnson", "cost": 6100, "value": 0.4319321501},
    {"name": "Santiago De la Fuente", "cost": 6100, "value": 0.4319321501},
    {"name": "Stewart Hagestad", "cost": 6000, "value": 0.4319321501},
    {"name": "Neal Shipley", "cost": 6000, "value": 0.4319321501},
    {"name": "Fred Couples", "cost": 6000, "value": 0.4319321501},
    {"name": "Mike Weir", "cost": 6000, "value": 0.4319321501},
    {"name": "Vijay Singh", "cost": 6000, "value": 0.4319321501},
    {"name": "Jose Maria Olazabal", "cost": 6000, "value": 0.4319321501}]

# Code below to pull data from mastersdata.csv
'''
file_path = 'mastersdata.csv'
df = pd.read_csv(file_path)
players = df[["Player", "Cost", "makeCut"]].rename(columns={"Player": "name", "Cost": "cost", "makeCut": "value"}).to_dict(orient="records")
'''

budget = 50000
n = len(players)
max_players = 6

dp = [[[None for _ in range(max_players + 1)] for _ in range(budget + 1)] for _ in range(n + 1)]

#dp algo

for j in range(budget + 1):
    dp[0][j][0] = 0

for i in range(1, n + 1):
    for j in range(budget + 1):
        for k in range(1, max_players + 1):
            dp[i][j][k] = dp[i-1][j][k]
            if players[i-1]["cost"] <= j and dp[i-1][j-players[i-1]["cost"]][k-1] is not None:
                if not dp[i][j][k]:
                    dp[i][j][k] = dp[i-1][j-players[i-1]["cost"]][k-1] + players[i-1]["value"]
                else:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-players[i-1]["cost"]][k-1] + players[i-1]["value"])

chosen_players = []
j = budget
k = max_players

if not dp[n][j][k]:
    print("It's not possible to choose 6 players within the given budget")
else:
    for i in range(n, 0, -1):
        if dp[i][j][k] is not None and (not dp[i-1][j][k] or dp[i][j][k] != dp[i-1][j][k]):
            chosen_players.append(players[i-1]["name"])
            j -= players[i-1]["cost"]
            k -= 1

    chosen_players.reverse()
    print("Chosen players:", chosen_players)