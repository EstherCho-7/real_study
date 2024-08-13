import numpy as np

# 기본 설정
games_played = 20  # 현재까지 경기 수
games_left = 38 - games_played  # 남은 경기 수
current_points = 35  # 현재 승점 (예시)
avg_goals_scored = 1.6  # 경기당 평균 득점
avg_goals_conceded = 1.2  # 경기당 평균 실점

# Poisson 분포를 사용한 득점 예측
expected_points_per_game = 2.0  # 예측된 경기당 평균 승점 (승리=3, 무=1, 패=0)

# 남은 경기에서 얻을 수 있는 승점 예상
points_from_remaining_games = expected_points_per_game * games_left
total_expected_points = current_points + points_from_remaining_games

# 가정: 우승을 위해 필요한 승점 (대략 85점으로 가정)
points_to_win_league = 85
win_probability = total_expected_points / points_to_win_league

# 우승 확률 (0에서 1 사이의 값)
win_probability = min(win_probability, 1)  # 1을 초과하지 않도록 제한
win_probability * 100  # 퍼센트로 변환

