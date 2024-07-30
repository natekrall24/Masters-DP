**A dynamic programming approach to the 0-1 Knapsack problem that I used to win a 2024 Masters Tournament pool.**

## Pool Details:
Every entrant in the pool had $50,000 to choose 6 players. Each golfer in the 2024 Masters field was assigned a cost by DraftKings Sportsbook. Better golfers, like Scottie Scheffler, were more expensive ($12,100), while more average golfers, like Harris English, were less ($7,000).
As you may notice, this is a variant of the classic 0-1 Knapsack problem: you have a budget B to choose 6 players of cost C and value V. How can you maximize value?
I learned in my algorithms class that elegant approach to the Knapsack problem is a dynamic programming algorithm. So, I implemented a 3D-DP algorithm to choose my team for me!
