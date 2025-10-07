def count_senior(node, min_level):
    # Base case: if node is None or invalid, return 0
    if node is None or not isinstance(node, dict):
        return 0

    level = node.get("level", 0)
    reports = node.get("reports", [])

    # Count this person if they meet or exceed min_level
    count = 1 if level >= min_level else 0

    # Recursively count all reports (if any)
    for r in reports:
        count += count_senior(r, min_level)

    return count
