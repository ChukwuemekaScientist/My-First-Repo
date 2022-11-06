# Chukwuemeka Agu
# 1871765

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0.0
        self.team_losses = 0.0

    def get_win_percentage(self):
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


student_team = Team()
student_team.team_name = input()
student_team.team_wins = float(input())
student_team.team_losses = float(input())

if student_team.get_win_percentage() >= 0.5:
    print(f"Congratulations, Team {student_team.team_name} has a winning average!")
else:
    print(f"Team {student_team.team_name} has a losing average.")