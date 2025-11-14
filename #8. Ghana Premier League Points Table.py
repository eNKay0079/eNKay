teams = [
    {"name": "Kotoko", "points": 25},
    {"name": "Hearts", "points": 23},
    {"name": "Aduana Stars", "points": 18}
]

print("Current League Table:")
for team in teams:
    print(f"- {team['name']}: {team['points']} points")

team_name = input("Enter team name: ").lower()
points_gained = int(input(f"Enter new points for {team_name.title()}: "))

for team in teams:
    if team["name"].lower() == team_name:
        new_points = team["points"] + points_gained
        team["points"] = new_points

print("New League Table:")
for team in teams:
    print(f"- {team['name']}: {team['points']} points")