import math


def check_count_of_players(score_1, score_2, max_point):
    if score_1 > math.ceil(score_2/max_point):
        return "Yes"
    return "No"


def main():
    score_1 = int(input())
    score_2 = int(input())
    max_point = int(input())
    print(check_count_of_players(score_1, score_2, max_point))


if __name__ == "__main__":
    main()
