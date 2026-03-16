import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Filter only 1st Inning to avoid 300+ scores
    df = df[df['inning'] == 1]
    
    consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                        'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                        'Delhi Capitals', 'Sunrisers Hyderabad', 'Lucknow Super Giants', 'Gujarat Titans']
    
    df = df[(df['batting_team'].isin(consistent_teams)) & (df['bowling_team'].isin(consistent_teams))]
    
    # 2. Sort to ensure cumsum is correct
    df = df.sort_values(by=['match_id', 'over', 'ball'])
    
    # 3. Running calculations
    df['overs'] = df['over'] + (df['ball'] / 6)
    df['current_score'] = df.groupby('match_id')['total_runs'].cumsum()
    df['wickets_fallen'] = df.groupby('match_id')['is_wicket'].cumsum()
    
    # 4. Correct Final Score Calculation
    total_runs = df.groupby('match_id')['total_runs'].sum().reset_index()
    total_runs.rename(columns={'total_runs': 'final_score'}, inplace=True)
    df = df.merge(total_runs, on='match_id')
    
    # 5. Filter for 5+ overs
    df = df[df['overs'] >= 5.0]
    
    print(f"Average Final Score in Data: {df['final_score'].mean():.2f}")
    
    return df[['batting_team', 'bowling_team', 'overs', 'current_score', 'wickets_fallen', 'final_score']]