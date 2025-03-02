from flask import Flask, jsonify

app = Flask(__name__)

# Function to calculate combinations
def calculate_combinations():
    combinations = {}
    for a in range(1, 7):
        for b in range(1, 7):
            sum_value = a + b
            if sum_value not in combinations:
                combinations[sum_value] = 0
            combinations[sum_value] += 1
    return combinations

# Function to calculate probability
def probability(combinations):
    total = 36
    probabilities = {k: v / total for k, v in combinations.items()}
    return probabilities

# Function to undoom dice with Loki's rule
def undoom_dice():
    # Die A with max spots 4
    new_die_a = [1, 1, 2, 2, 3, 4] 
    # Die B with normal spots
    new_die_b = [1, 2, 3, 4, 5, 6]  
    return new_die_a, new_die_b

@app.route('/combinations', methods=['GET'])
def get_combinations():
    combinations = calculate_combinations()
    return jsonify(combinations)

@app.route('/probability', methods=['GET'])
def get_probability():
    combinations = calculate_combinations()
    probabilities = probability(combinations)
    return jsonify(probabilities)

@app.route('/undoom', methods=['GET'])
def get_undoom():
    new_die_a, new_die_b = undoom_dice()
    return jsonify({"New_Die_A": new_die_a, "New_Die_B": new_die_b})

if __name__ == '__main__':
    app.run(debug=True)
