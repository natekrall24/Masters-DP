# A Dynamic Programming Approach to the 0-1 Knapsack Problem

I used DP to win a 2024 Masters Tournament pool.

## Pool Details

Every entrant in the pool had 50,000 fake dollars to choose 6 players. DraftKings Sportsbook assigned each golfer in the 2024 Masters field a cost based on their quality. Better golfers, like Scottie Scheffler, were more expensive ($12,100), while more average golfers, like Harris English, were less expensive ($7,000).

As you may notice, this is a variant of the classic 0-1 Knapsack problem: you have a budget \(B\) to choose 6 players of cost \(C\) and value \(V\). How can you maximize value?

I learned in my algorithms class that dynamic programming is an elegant approach to finding a solution the Knapsack problem. So, I implemented a 3D-DP algorithm to choose my team for me!

I used a mix of [odds to win and odds to make the cut](https://docs.google.com/spreadsheets/d/1ymUrt8fDtR63FEUxqXPjQkjDtADuj_a6ysMEdsL70p8/edit?gid=0#gid=0) to assign a value to each player. Even with his massive price tag, the algorithm selected Scheffler to my team due to his impressively high probability to win, and boy was I glad it did.
