def solution(today, terms, privacies):
    year, month, day = map(int, today.split("."))
    today = year * 336 + month * 28 + day
    term_dic = dict()
    for term in terms:
        name, month = term.split()
        term_dic[name] = int(month) * 28

    print(term_dic)
    print(today)
    answer = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        p_year, p_month, p_day = map(int, date.split("."))
        p_date = p_year * 336 + p_month * 28 + p_day

        if term_dic[term] + p_date <= today:
            answer.append(i+1)


    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
