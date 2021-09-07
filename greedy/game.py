# 캐릭터가 있는 장소는 1*1크기의 정사각형으로 이뤄진 N * M 크기의 직사각형이다.
# 각각의 칸은 육지 또는 바다이며 캐릭터는 동서남북 중 한 곳을 바라본다.
# 맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
# 매뉴얼)
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 
# 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
#
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 
# 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
#
# 입력조건: 첫째 줄에 맵의 세로크기와 가로크기를 공백으로 구분하여 입력한다 ( 3<= N,M <=50 )
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
# 방향 d의 값은 다음과 같이 4가지가 존재한다.
#   1) 0: 북쪽
#   2) 1: 동쪽
#   3) 2: 남쪽
#   4) 3: 서쪽
# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어있다.
#   1) 0:육지
#   2) 1:바다
# 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
# 출력조건 : 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
#
# ex) 4 4
#     1 1 0
#     1 1 1 1
#     1 0 0 1
#     1 1 0 1
#     1 1 1 1
#
# 출력 : 3

inputN,inputM = map(int,input().split())

mapd = [[0]* inputM for _ in range(inputN)]
x,y,direction = map(int,input().split())
mapd[x][y] = 1


array = []
for i in range(inputN) :
    array.append(list(map(int,input().split())))

# for i in range(inputN) :
#     for j in range(inputM) :
#         print(array[i][j],end="")
#     print()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnLeft() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

count = 1
turnTime = 0
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if mapd[nx][ny] == 0 and array[nx][ny] == 0 :
        mapd[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turnTime = 0
        continue
    else:
        turnTime += 1
    if turnTime == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]

        if array[nx][ny] == 0 :
            x = nx
            y = ny
        else :
            break
        turnTime = 0
print(count)

