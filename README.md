# FearTeams

FearTeams is a web application built with Streamlit and Python designed to separate players into two balanced teams based on their game statistics. The application aims to create fair and competitive teams by considering the number of games won and games played by each player.

## Motivation

The motivation behind TeamBalancer is to simplify the process of creating balanced teams for casual sports games. Often, players have varying skill levels, and forming fair teams can be challenging. TeamBalancer addresses this issue by using game statistics to balance teams, ensuring a more enjoyable experience for all participants.

## Goal

The goal of FearTeams is to:
- Upload player statistics from a CSV file.
- Calculate the win ratio for each player.
- Form two balanced teams based on the win ratio.
- Provide visualizations to compare team statistics.
- Allow users to download the team compositions.

## Technical Details

- The application is built using Streamlit for the user interface.
- Players' statistics are uploaded via a CSV file.
- The win ratio is calculated for each player as `games_won / games_played`.
- Players are sorted based on their win ratios and distributed into two balanced teams.
- Visualizations are created using Matplotlib and Seaborn to analyze and compare team statistics.

## Libraries and Tools

- [Streamlit](https://streamlit.io/): For building the web application.
- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [Matplotlib](https://matplotlib.org/): For creating visualizations.
- [Seaborn](https://seaborn.pydata.org/): For enhancing visualizations.

## Workflow

1. **Upload CSV File:**
   - Users upload a CSV file containing player names, games won, and games played.
2. **Data Validation:**
   - The application checks for the presence of required columns ('name', 'games_won', 'games_played').
3. **Calculate Win Ratios:**
   - The win ratio for each player is calculated.
4. **Sort and Distribute Players:**
   - Players are sorted by their win ratios and distributed into two balanced teams.
5. **Display and Download Teams:**
   - The teams are displayed on the app, and users can download the team compositions as CSV files.
6. **Visualizations:**
   - The app provides various visualizations to analyze and compare the statistics of the teams.
## Usage

To use FearTeams, follow these steps:

1. Clone the repository:
2. streamlit run spliting_teams.py --server.enableXsrfProtection false   
