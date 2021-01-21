# Snake-Game
The classic snake game. Made with pygame.

You can check out my video tutorial series on how to create this game: https://www.youtube.com/watch?v=5tvER0MT14s&t=2s

# Requirements
- Python 3.x
- pygame

# Run in Gitpod

You can also run Snake-Game in Gitpod, a free online dev environment for GitHub:

If you're intersted in a paid subscription with GitPod use the coupon code: **TECHWITHTIM19**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/techwithtim/Snake-Game/blob/master/snake.py)



------------------------------------------




1. 게임 속도 조절
기존에 빠르게 움직이던 뱀의 속도를 늦추고 5레벨씩 달성 시 
뱀의 속도를 전의 속도보다 1.5배 빨라지게 설정했습니다.

pygame을 모듈내장함수 init함수로 초기화하고
clock변수에 게임의 시간을 받았습니다.

기존 코드 속 class snake 에 있는 move함수를 수정해
level변수에 5단계 단위로 정수를 저장하고
최초 속도를 6으로 하고 5단계 단위로 속도를 1.5배 해 fps 변수에 넣었습니다.
그리고 내장함수 tick 이용해 조절한 속도를 적용하였습니다. 


2.최종 레벨 25로 달성 시 종료
-class snake안에 end_game함수 생성, sys.exit(0)에 의해 게임 종료
-기존 main함수에서 최종 레벨 25달성시, 게임을 종료하는 end_함수를 실행하는 코드 추가


3. Tk()를 이용하여 window라는 윈도우를 생성하고 타이틀은 "NEW Snake Game"으로 정한다. window.geometry 명령어를 통해 사이즈 설정과 윈도우 창이 뜨는 위치를 설정해 주었습니다. 
label1을 라벨 객체로 생성하고 “Game Start \n Let’s go”를 텍스트에 넣어 윈도우 창에 뜨웁니다. 글씨의 색상은 파란색으로 정했습니다.  relief는 라벨의 테두리 모양을 저지정하는 함수로 “sunken”을 써서 오목하게 보여줬습니다.
b1을 버튼 객체로 생성하고  command=window.destroy 코드를 통해 window 윈도우창을 닫고 메인 보드 게임으로 들어갑니다.
라벨과 버튼 둘 다 pack()을 통해 윈도우창에 띄웠습니다.


4. 게임판에 레벨 출력
메인 게임판 위에 뱀의 길이에 따른 레벨이 담긴 정보를 보여줍니다.

기존 코드 속 class snake 에 show_info함수를 정의하였습니다.
font 변수로 폰트의 정보를 지정하고 
내장함수 render로 뱀의 길이에 따른 레벨을 출력합니다.
출력 내용을 게임보드의 위치를 왼쪽 상단으로 지정합니다.

게임판을 출력하는 redrawWindow 함수에서
스네이크 객체 s를 이용해 show_info를 호출합니다.


5. finish_game함수를 정의해줍니다.
fin 윈도우를 만들고 label2객체를 생성하여 “!! SUCCESS !!”를 출력해줍니다.
b2 객체를 생성하여 “끝내기”버튼을 생성하고 버튼을 클릭시 command = fin.destroy 코드를 통해 윈도우를 종료 시켜줍니다.


6. 메인 게임 보드 설정 조절
메인 게임 보드 속 사소한 부분의 설정을 조절하였습니다.

win.full으로 배경 색을 바꾸고 
게임보드의 크기를 500제곱에서 700제곱으로 변경합니다.
rows도 20 줄에서 25줄로 격자의 양을 늘립니다.
class cube 내의 설정을 위한 변수의 크기도 변경 시킵니다.
gird 의 라인 색상도 변경합니다.
늘어난 메인 게임 보드의 크기만큼 뱀이 보들를 벗어 날 시 
발생하는 충돌 reset에 대한 설정도 20에서 25로 넓힙니다.


7.종료시 게임 total time 출력
- start_ticks객체는 main함수가 호출된 시점의 시작시간을 tick를 통해 받아옴(start_tick=고정값)
-while문 안에서  pygame이 호출된 이후 증가하며 흐르는 시간을 리턴하는 함수를 이용해 경과 시간을 구하기 위해 seconds객체 생성
경과 시간 계산은 밀리세컨들 출력되므로 1000으로 나눠 1초로 표시
-finish_game함수에서 게임이 종료되면 뜨는 윈도우창에 경과시간를 나타낸 객체 seconds를 출력


8. 점수가 있는 큐브 생성

뱀과 충돌시 점수를 내는 변수 버그와 스낵을 선언하고
메인 게임 보드에 정보를 출력합니다.

랜덤큐브를 생성하는 bug를 main에서 선언합니다.

if문을 이용해 스낵과 뱀의 머리가 충돌하면
뱀의 바디를 늘리는 함수를 addcube를 객체 호출하고
다음 레벨에서 다시 랜덤 큐브를 생성시킵니다.
그리고 score 변수에 점수를 +10으로 계산합니다.

같은 방법으로 if문을 이용해 버그와 뱀의 머리가 충돌하면
다음 레벨에서 랜덤큐브를 생성하고 점수를 -10으로 계산합니다.

redrawWindow 안에서 호출한 show_info로 
계산한 점수를 게임 메인 모드에 출력합니다.


9. main 함수 안에 Sound 객체인 eatsnack, eatbug, gameoversound를 생성하여
gameoversound는 뱀이 메인 게임보드 밖에 나갔을 때 play되도록 gameoversound.play()를 넣어줍니다.(243줄)
eatsnack 사운드는 뱀이 snack을 먹었을 때 나오도록 eatsnack.play()를 넣어줍니다.(248줄)
eatbug 사운드는 뱀이 bug를 먹었을 때 나오도록 eatbug.play()를 넣어줍니다.(256줄)
