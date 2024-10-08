def main():
    N, M = map(int, input().split())

    rank_l = []
    for i in range(M):
        rank = list(map(int, input().split()))
        rank_l.append(rank)
    
    check = [{f'{i + 1}_f': [], f'{i + 1}_b': []} for i in range(N)]
    for i in range(M):
        check[rank_l[i][0] - 1][f'{rank_l[i][0]}_f'].append(rank_l[i][1])
        check[rank_l[i][1] - 1][f'{rank_l[i][1]}_b'].append(rank_l[i][0])

    answer = [[1, 6] for _ in range(N)]

    def find_answer(dict, num, f, b):

        print(dict, num, f, b)
        if len(dict[f'{num}_f']) != 0:
            for i in range(len(dict[f'{num}_f'])):
                print('진입')
                find_answer(check[dict[f'{num}_f'][i] - 1], dict[f'{num}_f'][i], f, b)
        else:
            f += len(dict[f'{num}_f'])
            return

        answer[num][1] -= f

        if len(dict[f'{num}_b']) != 0:
            for i in range(len(dict[f'{num}_b'])):
                find_answer(check[dict[f'{num}_b'][i] - 1], dict[f'{num}_f'][i], f, b)
        else:
            b += len(dict[f'{num}_b'])
            return

        answer[num][0] += b
        return

    for i in range(len(check)):
        f = 0
        b = 0
        find_answer(check[i], i + 1, f, b)

    print(answer)

if __name__=="__main__":
    main()