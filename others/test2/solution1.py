import numpy as np


def solution(monsters, bullets):
    monsters = np.array(monsters)
    bullets = np.array(bullets)

    m = np.linalg.norm(monsters, ord=2, axis=1).reshape(-1, 1)
    b = np.linalg.norm(bullets, ord=2, axis=1).reshape(1, -1)

    print(m)
    print(b)
    ab_norm = np.dot(m, b)
    cross_product = np.divide(np.dot(monsters, bullets.T), ab_norm, dtype=np.float16).T

    print(ab_norm)
    print(cross_product)
    theta = np.where(cross_product == 1, 1, 0)
    answer = 0

    for t in theta:
        if 1 in t:
            answer += 1
            continue

    if answer:
        if answer < len(monsters):
            return answer
        else:
            return len(monsters)
    else:
        return -1


a = [[2, 3], [4, 5], [3, -3], [2, -4], [3, -6], [-4, -4], [-3, -3], [-5, 0], [-4, 4]]
b = [[4, 1], [4, 6], [1, -2], [-4, -4], [-3, 0], [-4, 4]]


print(solution(a, b))
