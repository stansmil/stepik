def mean(vals: list) -> float:
    return round(sum(vals) / len(vals), 2)


def total_mean(groups: list) -> float:
    return round(sum(mean(g) for g in groups) / len(groups), 2)
