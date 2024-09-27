from collections import defaultdict
from datetime import datetime

transactions = []
payers = defaultdict(int)

def add_points(payer: str, points: int, timestamp: datetime):
    payers[payer] += points
    transactions.append({"payer": payer, "points": points, "timestamp": timestamp})
 
def spend_points(points: int):
    remaining = points # stores the number of points left to spend 
    spent = defaultdict(int) # tracks how much each payer has spent 

    for transaction in transactions:
        if remaining <= 0:
            break

        points_to_spend = min(remaining, transaction["points"]) 
        remaining -= points_to_spend
        transaction["points"] -= points_to_spend
        payers[transaction["payer"]] -= points_to_spend
        spent[transaction["payer"]] -= points_to_spend

    if remaining > 0:
        raise ValueError("Not enough points to spend!")
    
    response = [{"payer": payer, "points": points} for payer, points in spent.items()]
    return response

def retrieve_balance():
    return payers