from PIL import Image

# Load map image
img = Image.open("b9ce34b2-09dd-421d-8d88-1daf4ab7be75.png")

# Grid size based on visible tile size (adjust as needed)
TILE_SIZE = 32  # Dungeon tiles appear around 32x32 px

width, height = img.size
cols = width // TILE_SIZE
rows = height // TILE_SIZE

# Convert image to RGB
img = img.convert("RGB")

# Convert tiles to game format
map_grid = []

for y in range(rows):
    row = []
    for x in range(cols):
        # Get average color of tile
        tile_img = img.crop((x*TILE_SIZE, y*TILE_SIZE, (x+1)*TILE_SIZE, (y+1)*TILE_SIZE))
        avg_color = tile_img.resize((1, 1)).getpixel((0, 0))
        brightness = sum(avg_color) / 3    
        # Heuristic: black = wall, blue-ish = floor
        if brightness < 30:
            row.append("#")  # Wall
        else:
            row.append(".")  # Floor
    map_grid.append(row)

# Print or save result
for row in map_grid:
    print("".join(row))
