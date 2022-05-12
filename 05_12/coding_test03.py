def solution(times, scores):
    m_list = sorted(list(zip(scores, times)))
    count_times = 0
    count_scores = 0
    answer = []
    time_time = []
    for i in range(len(m_list)):
        if m_list[-1][1] > m_list[-2][1] and m_list[-1][0] <= m_list[-2][0] and count_times > 16:
            m_list[-1], m_list[-2] = m_list[-2], m_list[-1]
            continue
        if count_times <= 16:
            time_time.append(m_list[-1][1])
            if sum(time_time) <= 16:
                count_scores += m_list[-1][0]
                count_times += m_list[-1][1]
                m_list.pop()
    answer.append(count_scores)
    time_time.clear()

    count_scores = 0
    count_times = 0
    for i in range(len(m_list)):
        if m_list[-1][1] > m_list[-2][1] and m_list[-1][0] <= m_list[-2][0] and count_times > 16:
            m_list[-1], m_list[-2] = m_list[-2], m_list[-1]
            continue
        if count_times <= 16:
            time_time.append(m_list[-1][1])
            if sum(time_time) <= 16:
                count_scores += m_list[-1][0]
                count_times += m_list[-1][1]
                m_list.pop()
    answer.append(count_scores)
    return sum(answer)

times = [4, 6, 2, 1, 4, 6, 11, 7]
scores = [3, 5, 2, 10, 6, 2, 3, 4]
print(solution(times, scores))
# list = sorted(list(zip(scores, times)))
# print(list)
# print(list[-1][0])
# print(list.pop())
# print(list)