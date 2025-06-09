# main
n = int(input())
short_cut = set()

for _ in range(n):
    cmds = list(map(str, input().split()))
    short_cut_pos = []

    # 1. 첫 글자 단축키 확인
    for w in range(len(cmds)):
        if cmds[w][0].upper() in short_cut:
            continue

        short_cut.add(cmds[w][0].upper())
        short_cut_pos.extend([w, 0])

        break

    # 2. 첫 글자 제외 단축키 확인
    if not short_cut_pos:
        for w in range(len(cmds)):
            for c in range(len(cmds[w])):
                if cmds[w][c].upper() in short_cut:
                    continue

                short_cut.add(cmds[w][c].upper())
                short_cut_pos.extend([w, c])

                break

            if short_cut_pos:
                break

    if short_cut_pos:
        w = short_cut_pos[0]
        c = short_cut_pos[1]

        cmds[w] = cmds[w][:c] + "[" + cmds[w][c] + "]" + cmds[w][c + 1 :]

        print(" ".join(cmds))
    else:
        # 3. 단축키가 하나도 안되면 그냥 출력
        print(" ".join(cmds))
