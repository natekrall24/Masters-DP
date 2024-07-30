# A Dynamic Programming Approach to the 0-1 Knapsack Problem

I used this approach to win a 2024 Masters Tournament pool.

## Pool Details

Every entrant in the pool had $50,000 to choose 6 players. Each golfer in the 2024 Masters field was assigned a cost by DraftKings Sportsbook. Better golfers, like Scottie Scheffler, were more expensive ($12,100), while more average golfers, like Harris English, were less expensive ($7,000).

As you may notice, this is a variant of the classic 0-1 Knapsack problem: you have a budget \(B\) to choose 6 players of cost \(C\) and value \(V\). How can you maximize value?

I learned in my algorithms class that dynamic programming is an elegant approach to the Knapsack problem. So, I implemented a 3D-DP algorithm to choose my team for me!

I used a mix of [odds to win and odds to make the cut](https://docs.google.com/spreadsheets/d/1ymUrt8fDtR63FEUxqXPjQkjDtADuj_a6ysMEdsL70p8/edit?gid=0#gid=0) to assign a value to each player. Even with his massive price tag, Scheffler found his way onto my final team due to his insanely high odds to win. And boy was I glad he made it.
