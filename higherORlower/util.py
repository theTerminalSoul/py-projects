def compare_follower(person1, person2):
    if person1["followers"] < person2["followers"]:
        return "high"
    else:
        return "low"
