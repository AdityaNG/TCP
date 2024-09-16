import json

def calculate_average_scores(file_path):
    with open(file_path, 'r') as file:
        file_data = json.load(file)
    
    total_composed = 0
    total_penalty = 0
    total_route = 0
    count = 0
    data = file_data['_checkpoint']
    
    for record in data.get('records', []):
        scores = record.get('scores', {})
        total_composed += scores.get('score_composed', 0)
        total_penalty += scores.get('score_penalty', 0)
        total_route += scores.get('score_route', 0)
        count += 1
    
    if count > 0:
        avg_composed = total_composed / count
        avg_penalty = total_penalty / count
        avg_route = total_route / count
        
        print(f"Average Score Composed: {avg_composed:.2f}")
        print(f"Average Score Penalty: {avg_penalty:.2f}")
        print(f"Average Score Route: {avg_route:.2f}")
    else:
        print("No records found in the file.")

# Usage
file_path = 'results_TCP.json'
calculate_average_scores(file_path)
