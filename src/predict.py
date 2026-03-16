import pandas as pd
import joblib

def predict_score(batting_team, bowling_team, overs, current_score, wickets_fallen):
    model = joblib.load('models/ipl_model.pkl')
    
    # Create the base dictionary for the input row
    input_data = {
        'overs': [overs],
        'current_score': [current_score],
        'wickets_fallen': [wickets_fallen]
    }
    
    input_df = pd.DataFrame(input_data)
    
    # We will use the model's feature_names_in_ to construct the exact columns needed
    # with 0s for everything except the selected teams
    expected_cols = model.feature_names_in_
    
    # Create an empty dataframe with the exact expected columns
    final_df = pd.DataFrame(columns=expected_cols)
    final_df.loc[0] = 0.0  # Initialize all to 0.0 to avoid int dtype conflicts
    
    # Set the numerical features
    final_df.at[0, 'overs'] = float(overs)
    final_df.at[0, 'current_score'] = current_score
    final_df.at[0, 'wickets_fallen'] = wickets_fallen
    
    # Set the categorical one-hot encoded features
    bat_col = f'batting_team_{batting_team}'
    bowl_col = f'bowling_team_{bowling_team}'
    
    if bat_col in final_df.columns:
        final_df.at[0, bat_col] = 1
    if bowl_col in final_df.columns:
        final_df.at[0, bowl_col] = 1
        
    prediction = model.predict(final_df)
    return prediction[0]

if __name__ == "__main__":
    score = predict_score('Chennai Super Kings', 'Mumbai Indians', 10.0, 80, 2)
    print(f"Predicted Final Score: {score}")
