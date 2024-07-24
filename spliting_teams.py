import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Football Team Divider Version 0.0")
# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file with your friends' names, games won, and games played", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Here are your friends and their game statistics:")
    st.write(df)

    # Ensure there are 'name', 'games_won', and 'games_played' columns in the CSV
    if 'name' not in df.columns or 'games_won' not in df.columns or 'games_played' not in df.columns:
        st.error("The CSV file must contain columns named 'name', 'games_won', and 'games_played'")
    else:
        # Get the list of names, games won, and games played
        names = df['name'].tolist()
        games_won = df['games_won'].tolist()
        games_played = df['games_played'].tolist()

        # Calculate win ratio for each player
        win_ratios = [won / played if played > 0 else 0 for won, played in zip(games_won, games_played)]

        # Create a list of tuples (name, games_won, games_played, win_ratio)
        players = list(zip(names, games_won, games_played, win_ratios))

        # Sort players by win_ratio in descending order
        players.sort(key=lambda x: x[3], reverse=True)

        # Create two balanced teams
        team1, team2 = [], []
        total_wins_team1, total_wins_team2 = 0, 0
        total_games_team1, total_games_team2 = 0, 0

        # Distribute players ensuring balanced teams
        for player in players:
            if len(team1) < len(team2):
                team1.append(player)
                total_wins_team1 += player[1]
                total_games_team1 += player[2]
            elif len(team1) > len(team2):
                team2.append(player)
                total_wins_team2 += player[1]
                total_games_team2 += player[2]
            else:  # len(team1) == len(team2)
                if total_wins_team1 / (total_games_team1 + 1) <= total_wins_team2 / (total_games_team2 + 1):
                    team1.append(player)
                    total_wins_team1 += player[1]
                    total_games_team1 += player[2]
                else:
                    team2.append(player)
                    total_wins_team2 += player[1]
                    total_games_team2 += player[2]

        # Extract names for display and download
        team1_df = pd.DataFrame(team1, columns=['name', 'games_won', 'games_played', 'win_ratio'])
        team2_df = pd.DataFrame(team2, columns=['name', 'games_won', 'games_played', 'win_ratio'])

        # Display the teams
        st.write("Team 1:")
        st.write(team1_df)

        st.write("Team 2:")
        st.write(team2_df)

        # Save teams into CSV files for download
        team1_csv = team1_df.to_csv(index=False).encode('utf-8')
        team2_csv = team2_df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="Download Team 1 as CSV",
            data=team1_csv,
            file_name='team1.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Download Team 2 as CSV",
            data=team2_csv,
            file_name='team2.csv',
            mime='text/csv',
        )

        # Visualization
        st.write("### Players Statistics Visualization")


        # Games Won vs Games Played with diagonal line and names next to dots
        fig, ax = plt.subplots()
        sns.scatterplot(x=games_played, y=games_won, hue=names, ax=ax, s=100, legend=False)
        ax.set_xlabel('Games Played')
        ax.set_ylabel('Games Won')
        ax.set_title('Games Won vs Games Played')

        # Add diagonal line
        max_games = max(games_played + games_won)
        ax.plot([0, max_games], [0, max_games], 'r--')

        # Add player names next to dots
        for i, name in enumerate(names):
            ax.text(games_played[i], games_won[i], name)

        st.pyplot(fig)

        # Team 1 and Team 2 Win Ratios
        fig, ax = plt.subplots(1, 2, figsize=(15, 5))
        sns.barplot(x=team1_df['name'], y=team1_df['win_ratio'], ax=ax[0])
        ax[0].set_title('Team 1 Win Ratios')
        ax[0].set_xlabel('Players')
        ax[0].set_ylabel('Win Ratio')
        ax[0].tick_params(axis='x', rotation=90)

        sns.barplot(x=team2_df['name'], y=team2_df['win_ratio'], ax=ax[1])
        ax[1].set_title('Team 2 Win Ratios')
        ax[1].set_xlabel('Players')
        ax[1].set_ylabel('Win Ratio')
        ax[1].tick_params(axis='x', rotation=90)

        st.pyplot(fig)

        # Comparison of Teams Based on Averages
        st.write("### Comparison of Teams Based on Averages")
        avg_team1 = team1_df[['games_won', 'games_played', 'win_ratio']].mean()
        avg_team2 = team2_df[['games_won', 'games_played', 'win_ratio']].mean()
        avg_df = pd.DataFrame({
            'Team': ['Team 1', 'Team 2'],
            'Avg Games Won': [avg_team1['games_won'], avg_team2['games_won']],
            'Avg Games Played': [avg_team1['games_played'], avg_team2['games_played']],
            'Avg Win Ratio': [avg_team1['win_ratio'], avg_team2['win_ratio']]
        })
        fig, ax = plt.subplots(1, 3, figsize=(18, 5))
        sns.barplot(x='Team', y='Avg Games Won', data=avg_df, ax=ax[0])
        sns.barplot(x='Team', y='Avg Games Played', data=avg_df, ax=ax[1])
        sns.barplot(x='Team', y='Avg Win Ratio', data=avg_df, ax=ax[2])
        ax[0].set_title('Average Games Won')
        ax[1].set_title('Average Games Played')
        ax[2].set_title('Average Win Ratio')
        st.pyplot(fig)

        # Box Plot for Games Played Distribution
        st.write("### Distribution of Games Played by Teams")
        combined_df = pd.concat([team1_df.assign(team='Team 1'), team2_df.assign(team='Team 2')])
        fig, ax = plt.subplots()
        sns.boxplot(x='team', y='games_played', data=combined_df, ax=ax)
        ax.set_xlabel('Team')
        ax.set_ylabel('Games Played')
        ax.set_title('Distribution of Games Played by Teams')
        st.pyplot(fig)

