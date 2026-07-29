def calculate_risk(headers):

    missing = sum(not status for status in headers.values())

    if missing <= 1:
        return "Low"

    elif missing <= 3:
        return "Medium"

    elif missing <= 5:
        return "High"

    else:
        return "Critical"