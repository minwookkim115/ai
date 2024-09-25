def solution(m, musicinfos):
    answer = ''
    music_list = []
    
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].split(',')
        play_time = 0
        music_start = musicinfo[0].split(':')
        music_end = musicinfo[1].split(':')
        
        hour = int(music_end[0]) - int(music_start[0])
        minute = int(music_end[1]) - int(music_start[1])
        
        play_time += (hour * 60) + minute

        music = []
        
        i = 0
        cnt = 0
        while True:
            if cnt >= play_time:
                break
            
            if i % len(musicinfo[3]) == len(musicinfo[3]) - 1: # 마지막이면
                music.append(musicinfo[3][i % len(musicinfo[3])]) # 뮤직에 넣고
                i += 1 # + 1
                cnt += 1
                # print(f'마지막일때 : {music}')
            elif musicinfo[3][i % len(musicinfo[3]) + 1] == '#': # 다음게 #이면
                music.append(musicinfo[3][i % len(musicinfo[3])] + musicinfo[3][i % len(musicinfo[3]) + 1])
                i += 2 # + 2
                cnt += 1
                # print(f'#일때 : {music}')
            else: # 나머지는 그냥 music에
                music.append(musicinfo[3][i % len(musicinfo[3])])
                i += 1
                cnt += 1
                # print(f'그냥 : {music}')
        # print(music)
        music_list.append(music)
    print(music_list)
    
    m_list = []
    i = 0
    while True:
        if i == len(m):
            break
        
        if i == len(m) - 1:
            m_list.append(m[i])
            i += 1
        elif m[i + 1] == '#':
            m_list.append(m[i : i + 2])
            i += 2
        else:
            m_list.append(m[i])
            i += 1
    print(m_list)
    
    answer_list = []
    for i in range(len(music_list)):
        if len(music_list[i]) < len(m_list):
            break
        else:
            for j in range(len(music_list[i]) - len(m_list) + 1):
                if m_list[0] == music_list[i][j]:
                    check = True
                    for k in range(len(m_list)):
                        if m_list[k] != music_list[i][j + k]:
                            check=False
                            break
                    
                    if check == True:
                        answer_list.append([musicinfos[i].split(',')[2], len(music_list[i])]) 
                        break
    
    if len(answer_list) == 1:
        answer = answer_list[0][0]
    elif len(answer_list) == 0:
        answer = '(None)'
    else:
        temp = 0
        temp_ans = ''
        for i in range(len(answer_list)):
            if answer_list[i][1] > temp:
                temp = answer_list[i][1]
                temp_ans = answer_list[i][0]
        answer = temp_ans
    return answer

print(solution("CC#BCC#BCC#", ["03:00,03:08,FOO,C#F#C#"]))