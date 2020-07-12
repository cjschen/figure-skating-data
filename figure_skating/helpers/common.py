
def is_number(num: str) -> bool: 
    try:
        float(num)
        return True
    except ValueError:
        return False

def stored_score(str: float):
    return int(float(str) * 100)
