def latest(scores):
    scores.remove(0)
    return min(scores)


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
