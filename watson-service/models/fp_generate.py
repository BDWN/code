"""fp_generate.py"""
from csv import DictWriter
from random import randint

PERSONAS = [1, 3]
AMOUNT_USER_PER_P = 100
AMOUNT_FACT_PER_U = 5
DISLIK = 1
NEUTRL = 2.5
COMMON = 4
LIKE__ = 5

def initial_setup(p_id, u_id):
    """Returns the concept ratings for a persona."""
    records = []
    for f_id in range(50, 61):
        records.append({'userId': u_id, 'factId': f_id, 'rating': concept_rating(p_id, f_id)})

    return records

def concept_rating(p_id, f_id):
    """Returns a concept rating for a persona."""
    scheme = {
        50: {1: LIKE__, 2: DISLIK, 3: DISLIK},
        51: {1: LIKE__, 2: DISLIK, 3: DISLIK},
        52: {1: LIKE__, 2: DISLIK, 3: DISLIK},
        53: {1: LIKE__, 2: DISLIK, 3: DISLIK},
        54: {1: DISLIK, 2: LIKE__, 3: DISLIK},
        55: {1: DISLIK, 2: LIKE__, 3: DISLIK},
        56: {1: DISLIK, 2: LIKE__, 3: DISLIK},
        57: {1: DISLIK, 2: LIKE__, 3: DISLIK},
        58: {1: DISLIK, 2: DISLIK, 3: LIKE__},
        59: {1: DISLIK, 2: DISLIK, 3: LIKE__},
        60: {1: DISLIK, 2: DISLIK, 3: LIKE__}
    }

    return scheme[f_id][p_id]

def fact_rating(p_id, f_id):
    """Returns a fact rating for a persona."""
    scheme = {
        1: {1: COMMON, 2: COMMON, 3: COMMON},
        2: {1: COMMON, 2: COMMON, 3: DISLIK},
        3: {1: DISLIK, 2: DISLIK, 3: LIKE__},
        4: {1: COMMON, 2: COMMON, 3: DISLIK},
        5: {1: DISLIK, 2: NEUTRL, 3: LIKE__},
        6: {1: NEUTRL, 2: LIKE__, 3: DISLIK},
        7: {1: NEUTRL, 2: DISLIK, 3: LIKE__},
        8: {1: COMMON, 2: COMMON, 3: NEUTRL},
        9: {1: NEUTRL, 2: DISLIK, 3: LIKE__},
        10: {1: COMMON, 2: COMMON, 3: DISLIK},
        11: {1: LIKE__, 2: NEUTRL, 3: DISLIK},
        12: {1: DISLIK, 2: LIKE__, 3: DISLIK},
        13: {1: NEUTRL, 2: DISLIK, 3: LIKE__},
        14: {1: LIKE__, 2: DISLIK, 3: NEUTRL},
        15: {1: COMMON, 2: COMMON, 3: NEUTRL},
        16: {1: COMMON, 2: COMMON, 3: DISLIK},
        17: {1: DISLIK, 2: DISLIK, 3: LIKE__},
        18: {1: DISLIK, 2: DISLIK, 3: LIKE__},
        19: {1: COMMON, 2: COMMON, 3: NEUTRL},
        20: {1: LIKE__, 2: NEUTRL, 3: DISLIK}
    }

    return scheme[f_id][p_id]

def generate():
    """Generates a fp dataset."""
    records = []
    for p_id in PERSONAS:
        for i in range(0, AMOUNT_USER_PER_P):
            u_id = i + 100 * p_id
            records = records + initial_setup(p_id, u_id)

            for _ in range(0, AMOUNT_FACT_PER_U):
                f_id = randint(1, 20)
                f_r = fact_rating(p_id, f_id)

                records.append({'userId': u_id, 'factId': f_id, 'rating': f_r})

    return records

def write(records):
    """Writes records to a CSV file."""
    fieldnames = ['userId', 'factId', 'rating']

    with open('fact_ratings.csv', 'w', newline='') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in records:
            if record['rating'] > 0:
                writer.writerow(record)

def personas():
    """Returns records with only initial setup."""
    return initial_setup(1, 1) + initial_setup(2, 3)

if __name__ == "__main__":
    write(generate() + personas())
