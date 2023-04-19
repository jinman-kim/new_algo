import heapq

# 1. 무기버리기
# 2. 무기바꾸기
# 3. 싸우기
# 4. 이긴사람, 진사람
# 5. 진사람 움직이기

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
player = [0] + [list(map(int, input().split())) for _ in range(m)] # 1번부터 플레이어번호
for i in range(len(player)): #헷갈려서 x,y  1씩 까줌
    try:
        player[i][0] -= 1
        player[i][1] -= 1
        player[i].append(0) # 총은 4번 인덱스로 01234
    except:
        pass
player_board = [[0]*n for _ in range(n)]
for i in range(len(player)):
    try:
        player_board[player[i][0]][player[i][1]] = i # 플레이어 있는 칸에 번호 i 초기화
    except:
        pass
guns = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        guns[i][j].append(-board[i][j])
scores = [0]*(m+1)
dx, dy = [0, 1, 0 ,-1] , [-1 , 0 , 1 , 0]
for i in range(1,5):
    player[i][0], player[i][1] = player[i][0] + dx[player[i][2]], player[i][1] + dy[player[i][2]]
    if player[i][0] >= n or player[i][0] <0  or player[i][1] < 0 or player[i][1] >= n:
        player[i][2] = (player[i][2] + 2) % 4 #격자 밖으로 나가면 뒤돌고 2칸 돌아옴
        player[i][0] += 2*dx[player[i][2]]
        player[i][1] += 2*dy[player[i][2]]
    a, b = player[i][0], player[i][1] #임시로 a,b로 간략하게
    #사람을 만나면 스코어 갱신, 진 사람 총 버리고 90도 회전하면서 사람없는데 가기
    if player_board[a][b]:
        if player[i][2] + player[i][4] > player[player_board[a][b]][2] + player[player_board[a][b]][4]:
            scores[i] += player[i][2] + player[i][4] - \
                         player[player_board[a][b]][2] + player[player_board[a][b]][4]
            guns[a][b].append(-player[player_board[a][b]][4]) #땅에 총추가
            player[player_board[a][b]] = 0 # 총뺏김 ㅠㅠ
            player[i][4] = heapq.heappushpop(guns[a][b], player[i][4])
            for d in range(4):
                board[player[player_board[a][b]][0] + dx[d]
                player[player_board[a][b]][1] + dy[d]

def loser(idx, x, y):
    throw_weapon(idx,x,y)
    l_dir = w[idx][2]
    for _ in range(4):
        nx, ny = x + dir[l_dir][0] , y + dir[l_dir][1]
        if 0 <= nx < n and 0 <= ny < n and not w_board[nx][ny]:
            change_weapon(idx, nx, ny)
            w[idx][x], w[idx][y] = nx, ny
            w_board[x][y] = idx
            w[idx][2] = l_dir
            return
        l_dir = (l_dir+1) %4
    return
# 탐색할 보드
# 총 정보 보드 ( 최대힙 -메소드로)
# 플레이어 위치 보드
# 점수판
#
