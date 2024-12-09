# Dictionary to store each team's treasures (using sets to avoid duplicates)
teams = {}

# 1. Add a treasure to a team's collection
def add_treasure(team_name, treasure):
    if team_name not in teams:
        teams[team_name] = set()
    if treasure not in teams[team_name]:
        teams[team_name].add(treasure)
        print(f"Added treasure '{treasure}' to {team_name}'s collection.")
    else:
        print(f"{team_name} already has the treasure '{treasure}'.")

# 2. Remove a treasure from a team's collection
def remove_treasure(team_name, treasure):
    if team_name in teams and treasure in teams[team_name]:
        teams[team_name].remove(treasure)
        print(f"Removed treasure '{treasure}' from {team_name}'s collection.")
    else:
        print(f"{team_name} does not have the treasure '{treasure}'.")

# 3. View all treasures of a team
def view_treasures(team_name):
    if team_name in teams:
        print(f"{team_name}'s treasures: {teams[team_name]}")
    else:
        print(f"{team_name} has no treasures.")

# 4. Find total number of treasures collected by a team
def total_treasures(team_name):
    if team_name in teams:
        print(f"{team_name} has collected {len(teams[team_name])} treasures.")
    else:
        print(f"{team_name} has no treasures.")

# 5. Check if a specific treasure is collected by a team
def check_treasure(team_name, treasure):
    if team_name in teams and treasure in teams[team_name]:
        print(f"Yes, {team_name} has collected the treasure '{treasure}'.")
    else:
        print(f"No, {team_name} has not collected the treasure '{treasure}'.")

# 6. Find common treasures between two teams
def common_treasures(team1, team2):
    if team1 in teams and team2 in teams:
        common = teams[team1].intersection(teams[team2])
        print(f"Common treasures between {team1} and {team2}: {common}")
    else:
        print(f"One or both teams have no treasures.")

# 7. Find all treasures collected across all teams
def all_treasures():
    all_treasures = set()
    for treasures in teams.values():
        all_treasures.update(treasures)
    print(f"All treasures collected by any team: {all_treasures}")

# 8. Find which team has collected the most treasures
def team_with_most_treasures():
    if not teams:
        print("No teams have collected any treasures.")
        return
    most_treasures_team = max(teams, key=lambda team: len(teams[team]))
    print(f"The team with the most treasures is {most_treasures_team} with {len(teams[most_treasures_team])} treasures.")
# Adding treasures
add_treasure("Team A", "Golden Crown")
add_treasure("Team A", "Silver Sword")
add_treasure("Team B", "Silver Sword")
add_treasure("Team B", "Emerald Ring")

# Viewing treasures
view_treasures("Team A")
view_treasures("Team B")

# Removing treasures
remove_treasure("Team A", "Golden Crown")

# Checking for a specific treasure
check_treasure("Team A", "Golden Crown")

# Finding common treasures between two teams
common_treasures("Team A", "Team B")

# Finding all treasures across all teams
all_treasures()

# Finding the team with the most treasures
team_with_most_treasures()
