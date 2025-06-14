import turtle
import random

# --- Constants ---
TILE_SIZE = 40  # Size of each tile in pixels
MAP_WIDTH = 30  # Number of tiles horizontally
MAP_HEIGHT = 50  # Number of tiles vertically

# --- Game State ---
game_state = {
    # Stores the current position of the player
    "player_pos": (0, 0),
    # Set of enemy positions
    "enemy_positions": set(),
    # Set of obstacle positions (walls)
    "obstacles": set(),
    # Camera offset for scrolling
    "camera_x": 0,
    "camera_y": 0,
    # Number of defeated enemies
    "defeated_enemies": 0,
    # Set of chest locations
    "chest_location": set(),
    # Player's points
    "points": 0,
    # Set of door positions
    "doors": set(),
    # Number of keys the player has
    "keys": 0,
    # Set of key positions
    "key_positions": set(),
}

WORLD_MAP = [
    "###############################",
    "#########..P.##################",
    "#########....##################",
    "#########....##################",
    "######.......##################",
    "#K...........##################",
    "#............##################",
    "#...........###################",
    "#...........###################",
    "#...........###################",
    "#....E......###################",
    "#............##################",
    "#......E.....##################",
    "#............##################",
    "#............##################",
    "#............##################",
    "#######D#############K.....####",
    "####.......##########......####",
    "#..............######...E..####",
    "#..............######......####",
    "#....E.........######..E...####",
    "####.......##..#####.......####",
    "####.......##CC#..##........###",
    "######...#######..##.....E..###",
    "######...#######.......##....##",
    "######.................##....##",
    "######.................##..E.##",
    "######...#....######.........##",
    "######...###..######........###",
    "######...###..#########...#####",
    "######...###...#######.......##",
    "######...###........#........##",
    "######...###.................##",
    "#######D#########...#........##",
    "####.......######...##....#..##",
    "###.........#######D.###CC#####",
    "###.........#####...###########",
    "###.........#####...###########",
    "###...E.....#####...###########",
    "###.........######..###########",
    "###.........######..###########",
    "###.........######..###########",
    "#####CCCCCC#####....C##########",
    "################.....##########",
    "################..E..##########",
    "################K....##########",
    "###############################",
]

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Dungeon Explorer")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

# --- Utility Functions ---
def world_to_screen(x, y):
    # Converts world (tile) coordinates to screen (pixel) coordinates
    screen_x = (x * TILE_SIZE) - game_state["camera_x"] - (screen.window_width() // 2) + TILE_SIZE // 2
    screen_y = ((MAP_HEIGHT - 1 - y) * TILE_SIZE) - game_state["camera_y"] - (screen.window_height() // 2) + TILE_SIZE // 2
    return screen_x, screen_y

def can_move(x, y):
    # Checks if the player or enemy can move to the given tile
    return (0 <= x < MAP_WIDTH) and (0 <= y < MAP_HEIGHT) and ((x, y) not in game_state["obstacles"])

# --- Drawing Functions ---
def draw_tile(x, y, ch):
    # Draws a single tile (wall, enemy, chest, etc.) at the given coordinates
    screen_x, screen_y = world_to_screen(x, y)
    pen.goto(screen_x, screen_y)
    if ch == "#":
        pen.color("black")
        pen.shape("square")
        pen.shapesize(stretch_wid=2, stretch_len=2)
    elif ch == "E":
        pen.color("red")
        pen.shape("circle")
        pen.shapesize(stretch_wid=1.5, stretch_len=1.5)
    elif ch == 'C':
        pen.color("gold")
        pen.shape("square")
        pen.shapesize(stretch_wid=1.5, stretch_len=1.5)
    elif ch == 'K':
        pen.color("gold")
        pen.shape("circle")
        pen.shapesize(1.5, 1.5)
    elif ch == 'D':
        pen.color("brown")
        pen.shape("square")
        pen.shapesize(2, 2)
    elif ch == ".":
        pen.color("lightgreen")
        pen.shape("square")
        pen.shapesize(stretch_wid=2, stretch_len=2)
    pen.stamp()

def draw_map():
    """Draws only the visible portion of the game map, including static tiles, enemies, chests, keys, and doors."""
    pen.clear()
    px, py = game_state["player_pos"]
    # Calculate visible area based on player position
    tiles_x = screen.window_width() // TILE_SIZE + 2
    tiles_y = screen.window_height() // TILE_SIZE + 2
    start_x = max(0, px - tiles_x // 2)
    end_x = min(MAP_WIDTH, px + tiles_x // 2 + 1)
    start_y = max(0, py - tiles_y // 2)
    end_y = min(MAP_HEIGHT, py + tiles_y // 2 + 1)
    # Draw static map tiles
    for y in range(start_y, end_y):
        if y >= len(WORLD_MAP):
            continue
        row = WORLD_MAP[y]
        for x in range(start_x, end_x):
            if x >= len(row):
                continue
            ch = row[x]
            if ch != "P" and ch != "E":
                draw_tile(x, y, ch)
    # Draw dynamic objects (enemies, chests, keys, doors)
    for (x, y) in game_state["enemy_positions"]:
        if start_x <= x < end_x and start_y <= y < end_y:
            draw_tile(x, y, "E")
    for (x, y) in game_state["chest_location"]:
        if start_x <= x < end_x and start_y <= y < end_y:
            draw_tile(x, y, "C")
    for (x, y) in game_state.get("key_positions", set()):
        if start_x <= x < end_x and start_y <= y < end_y:
            draw_tile(x, y, "K")
    for (x, y) in game_state["doors"]:
        if start_x <= x < end_x and start_y <= y < end_y:
            draw_tile(x, y, "D")

def draw_player():
    # Draws the player turtle at the correct screen position
    x, y = game_state["player_pos"]
    screen_x, screen_y = world_to_screen(x, y)
    player.goto(screen_x, screen_y)

def draw_status():
    # Displays the status bar with enemies defeated, points, and keys
    pen.goto(-screen.window_width() // 2 + 10, -screen.window_height() // 2 + 10)
    pen.color("black")
    pen.write(
        f"Enemies defeated: {game_state['defeated_enemies']} | Points: {game_state['points']} | Keys: {game_state['keys']}",
        font=("Arial", 16, "normal")
    )

def redraw_all():
    """Redraws the map, player, and status bar."""
    draw_map()
    draw_player()
    draw_status()
    screen.update()

# --- Game Logic Functions ---
def find_objects():
    """Scans the WORLD_MAP and populates game_state with positions of obstacles, enemies, player, chests, keys, and doors."""
    for y, row in enumerate(WORLD_MAP):
        for x, ch in enumerate(row):
            # Identify and store obstacles, enemies, player, chests, keys, and doors
            if ch == "#":
                game_state["obstacles"].add((x, y))
            elif ch == "E":
                game_state["enemy_positions"].add((x, y))
            elif ch == "P":
                game_state["player_pos"] = (x, y)
            elif ch == "C":
                game_state["chest_location"].add((x, y))
            elif ch == 'K':
                game_state["key_positions"] = game_state.get("key_positions", set())
                game_state["key_positions"].add((x, y))
            elif ch == 'D':
                game_state["doors"].add((x, y))

def move_player(dx, dy):
    """Handles player movement, interaction with doors, keys, enemies, and chests, and updates camera position."""
    x, y = game_state["player_pos"]
    new_x, new_y = x + dx, y + dy
    # Door interaction
    if (new_x, new_y) in game_state["doors"]:
        if game_state["keys"] > 0:
            print("Used a key to open the door!")
            game_state["keys"] -= 1
            game_state["doors"].remove((new_x, new_y))
        else:
            print("You need a key to open this door!")
            return
    # Key pickup
    if (new_x, new_y) in game_state.get("key_positions", set()):
        game_state["key_positions"].remove((new_x, new_y))
        game_state["keys"] += 1
        print("Picked up a key! 🔑")
    # Move if possible
    if can_move(new_x, new_y):
        game_state["player_pos"] = (new_x, new_y)
        # Update camera position
        game_state["camera_x"] = new_x * TILE_SIZE - screen.window_width() // 2 + TILE_SIZE // 2
        game_state["camera_y"] = (MAP_HEIGHT - 1 - new_y) * TILE_SIZE - screen.window_height() // 2 + TILE_SIZE // 2
        # Enemy encounter
        if (new_x, new_y) in game_state["enemy_positions"]:
            game_state["enemy_positions"].remove((new_x, new_y))
            game_state["defeated_enemies"] += 1
            print("Defeated an enemy!")
        # Chest pickup
        if (new_x, new_y) in game_state["chest_location"]:
            game_state["chest_location"].remove((new_x, new_y))
            game_state["points"] += 1
            print("Found a chest! +1 Point!")
        redraw_all()

def enemy_move():
    """Moves all enemies randomly, avoiding obstacles and the player, and schedules the next move."""
    new_positions = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Move each enemy in a random direction if possible
    for (ex, ey) in game_state["enemy_positions"]:
        random.shuffle(directions)
        moved = False
        for dx, dy in directions:
            nx, ny = ex + dx, ey + dy
            if can_move(nx, ny) and (nx, ny) != game_state["player_pos"] and (nx, ny) not in game_state["enemy_positions"]:
                new_positions.add((nx, ny))
                moved = True
                break
        if not moved:
            new_positions.add((ex, ey))
    game_state["enemy_positions"] = new_positions
    redraw_all()
    # Schedule next enemy move
    screen.ontimer(enemy_move, 1000)

# --- Input Handlers ---
# Lambda function to create movement direction tuples
get_direction = lambda key: {
    'Up': (0, -1),
    'Down': (0, 1),
    'Left': (-1, 0),
    'Right': (1, 0)
}.get(key, (0, 0))

def go_up():
    dx, dy = get_direction('Up')
    move_player(dx, dy)
def go_down():
    dx, dy = get_direction('Down')
    move_player(dx, dy)
def go_left():
    dx, dy = get_direction('Left')
    move_player(dx, dy)
def go_right():
    dx, dy = get_direction('Right')
    move_player(dx, dy)

# --- Initialization ---
find_objects()  # Scan the map and initialize game state
# Set initial camera position based on player
game_state["camera_x"] = game_state["player_pos"][0] * TILE_SIZE - screen.window_width() // 2 + TILE_SIZE // 2
game_state["camera_y"] = (MAP_HEIGHT - 1 - game_state["player_pos"][1]) * TILE_SIZE - screen.window_height() // 2 + TILE_SIZE // 2
redraw_all()
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
enemy_move()  # Start enemy movement loop
screen.mainloop()  # Start the main event loop
