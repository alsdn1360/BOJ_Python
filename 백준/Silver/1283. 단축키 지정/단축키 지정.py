def find_shortcut(cmds, short_cut):
    # 1. 첫 글자 단축키 확인
    for w in range(len(cmds)):
        if cmds[w][0].upper() not in short_cut:
            short_cut.add(cmds[w][0].upper())
            return w, 0

    # 2. 첫 글자 제외 단축키 확인
    for w in range(len(cmds)):
        for c in range(1, len(cmds[w])):
            if cmds[w][c].upper() not in short_cut:
                short_cut.add(cmds[w][c].upper())
                return w, c

    return None  # 단축키를 지정할 수 없으면 None 반환


# main
n = int(input())
short_cut = set()

for _ in range(n):
    cmds = input().split()

    short_cut_pos = find_shortcut(cmds, short_cut)

    if short_cut_pos:
        w, c = short_cut_pos
        cmds[w] = cmds[w][:c] + "[" + cmds[w][c] + "]" + cmds[w][c + 1 :]
        print(" ".join(cmds))
    else:
        # 3. 단축키가 하나도 안되면 그냥 출력
        print(" ".join(cmds))
