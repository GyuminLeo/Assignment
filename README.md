# Dungeon Exploration Game using Python Turtle Graphics

A basic dungeon exploration game implemented using Python's `turtle` graphics module. Players navigate a grid-based dungeon, collect items, open doors, defeat enemies, and track their progress in real-time.

---

# Table of Contents

- [Overview](#overview)
- [Execution](#execution)
- [Controls](#controls)
- [Game Elements](#game-elements)
- [Status Display](#status-display)
- [Applied Python Concepts](#applied-python-concepts)
- [한국어 설명](#한국어-설명)
- [개요](#개요)
- [실행 방법](#실행-방법)
- [조작 방법](#조작-방법)
- [게임 요소 설명](#게임-요소-설명)
- [상태 표시](#상태-표시)
- [사용된 파이썬 강의 내용](#사용된-파이썬-강의-내용)
- [스크린샷](#스크린샷)

---

# Overview

This project demonstrates a turn-based dungeon game where the player explores a map, interacts with environmental elements, and applies key Python programming concepts covered in class.

---

# Execution

To run the game:

1. Save the provided Python file as `main.py`.
2. Open a terminal and run the following command:

```bash
python main.py
```

---

# Controls

Use the arrow keys to move:

    ↑ Up
    
    ↓ Down

    ← Left

    → Right

---

# Game Elements

| Symbol | Description                                   | Visual       |
| ------ | --------------------------------------------- | ------------ |
| `#`    | Wall – impassable terrain                     | Black square |
| `.`    | Floor – traversable area                      | Green square |
| `P`    | Player – the controlled character             | Blue turtle  |
| `E`    | Enemy – moves randomly, defeated on collision | Red circle   |
| `C`    | Chest – grants points when collected          | Gold square  |
| `K`    | Key – required to open doors                  | Gold circle  |
| `D`    | Door – opened only if the player has a key    | Brown square |

---

# Status Display

Game statistics are shown at the bottom-left of the screen:

    Enemies defeated

    Points collected

    Number of keys held


---

# Applied Python Concepts

The following Python programming topics are implemented in the game:
🔹 Python Basics and Core Syntax

    Functions (def): Modular code structure with functions like draw_map(), move_player(), etc.

    Print Statements: Console feedback for debugging or messages.

🔹 Variables, Collections, and Operations

    Variables: Used for defining game parameters and state (TILE_SIZE, game_state, etc.).

    Lists: WORLD_MAP is stored as a list of strings.

    Tuples: Used for coordinates (x, y) and directions.

🔹 Strings and Conditionals

    Parsing map symbols to determine tile behavior.

    if/elif/else statements drive interaction logic.

🔹 Lists and For Loops

    for loops iterate through map rows and objects.

🔹 While Loop and Turtle Graphics

    Turtle handles all graphics (map rendering, characters).

    screen.mainloop() and screen.ontimer() maintain game state.

🔹 Random Module

    random.shuffle() adds unpredictability to enemy movement.

🔹 Tuples and String Formatting

    Tuple unpacking and f-strings for clean stat display:

    f"Enemies defeated: {game_state['defeated_enemies']}"

🔹 Function Arguments and Lambda Functions

    Dynamic function inputs for drawing and movement.

    Lambda functions map keypresses to movement directions.

🔹 Dictionaries and Sets

    game_state dictionary stores all dynamic game data.

    Sets optimize storage for positions (enemies, obstacles, etc.).


---
# 한국어 설명


# 개요

이 프로젝트는 Python의 turtle 그래픽 모듈을 활용하여 기본적인 던전 탐험 게임을 구현합니다. 플레이어는 정의된 던전 지도를 탐색하고, 아이템을 수집하며, 환경 요소와 상호작용하고, 적과 교전합니다.

---

# 실행 방법

제공된 Python 소스를 main.py로 저장하세요.

터미널에서 아래 명령어로 실행하세요:
```bash
    python main.py
```

---
# 조작 방법

방향키를 이용해서 플레이어를 움직입니다:

    ↑ 위
    
    ↓ 아래

    ← 왼쪽

    → 오른쪽

---
# 게임 요소 설명

| 기호  | 설명                  | 시각 표현   |
| --- | ------------------- | ------- |
| `#` | 벽 – 이동 불가 지형        | 검은 사각형  |
| `.` | 바닥 – 이동 가능 지형       | 초록 사각형  |
| `P` | 플레이어 – 조작 대상 캐릭터    | 파란색 거북이 |
| `E` | 적 – 무작위 이동, 충돌 시 제거 | 빨간 원    |
| `C` | 상자 – 포인트 제공         | 금색 사각형  |
| `K` | 열쇠 – 문을 열기 위해 필요    | 금색 원    |
| `D` | 문 – 열쇠가 있어야 열 수 있음  | 갈색 사각형  |


---
# 상태 표시

격퇴한 적 수, 획득한 포인트, 보유한 열쇠 수가 화면 좌측 하단에 표시됩니다

    처치한 적 수

    획득한 점수

    소지중인 열쇠 개수

---
# 사용된 파이썬 강의 내용


다음은 게임에 구현된 파이썬 프로그래밍 주제입니다:

🔹 파이썬 지가 및 기본 문법

    함수 (def): draw_map(), move_player() 등과 같은 함수를 통해 모듈화된 코드 구조를 사용합니다.

    출력문 (print): 디버깅 및 메시지 출력을 위한 콘솔 피드백을 제공합니다.

🔹 컬렉션자료와 변수 및 연산

    변수: TILE_SIZE, game_state 등 게임의 상태와 설정 값을 정의하는 데 사용됩니다.

    리스트 (List): WORLD_MAP은 문자열 리스트 형태로 저장됩니다.

    튜플 (Tuple): 좌표 (x, y) 및 방향을 나타내는 데 사용됩니다.

🔹 문자열과 조건문

    맵의 기호를 분석하여 각 타일의 동작을 결정합니다.

    if, elif, else 조건문을 통해 상호작용 로직을 제어합니다.

🔹 리스트연산과 for 반복문

    for 반복문을 사용하여 맵의 행 및 객체들을 순회합니다.

🔹 while반복과 거북이 그래픽

    turtle 모듈을 활용하여 맵 렌더링 및 캐릭터 등의 그래픽을 처리합니다.

    screen.mainloop()와 screen.ontimer()로 게임 상태를 지속적으로 유지합니다.

🔹 random 모듈

    random.shuffle()을 사용하여 적의 움직임에 예측 불가능성을 추가합니다.

🔹 튜플과 문자열 포매팅

    튜플 언패킹 및 f-string을 사용하여 통계를 깔끔하게 표시합니다:
    f"Enemies defeated: {game_state['defeated_enemies']}"

🔹 함수 인자 및 람다 함수

    그리기 및 이동과 관련된 동작에 동적 함수 인자를 사용합니다.

    lambda 함수를 통해 키 입력과 이동 방향을 연결합니다.

🔹 딕셔너리와 집합 (set)

    game_state 딕셔너리는 게임의 동적인 상태 데이터를 저장합니다.

    집합(set)은 적, 장애물 등의 좌표를 효율적으로 저장하고 검색합니다.

# 스크린샷
![1](250614_15h36m24s_screenshot.png?raw=true)
![2](250614_15h36m38s_screenshot.png?raw=true)
![3](250614_15h36m54s_screenshot.png?raw=true)
![4](250614_15h37m19s_screenshot.png?raw=true)
