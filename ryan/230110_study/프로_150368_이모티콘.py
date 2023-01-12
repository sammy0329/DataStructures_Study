def solution(users, emoticons):
    from itertools import product

    samples = product([10, 20, 30, 40], repeat=len(emoticons))
    result_list = []

    for sample in samples:
        sample_sum_membership = 0
        sample_sum_price = 0

        for user in users:
            user_sum_price = 0
            for i, price in enumerate(emoticons):
                if user[0] <= sample[i]:
                    user_sum_price += int((100-sample[i])*0.01*price)

            if user_sum_price >= user[1]:
                sample_sum_membership += 1

            else:
                sample_sum_price += user_sum_price

        result_list.append([sample_sum_membership, sample_sum_price])

    return max(result_list)