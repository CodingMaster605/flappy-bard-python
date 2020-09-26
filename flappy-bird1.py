import random

WIDTH = 395
HEIGHT = 708

# Title for game:

TITLE = "Flappy Bird"

# Postures for the bird flapping

postures = ['bird0', 'bird1', 'bird2']

# Actor for bird

bird = Actor("bird0", (WIDTH/2 - 100, HEIGHT/2 - 80))

# Actor for top poll

top = Actor("flappybird_top", anchor=("left","bottom"))

# Actor for bottom poll

bottom = Actor("flappybird_bottom", anchor=("left","top"))

# Position for top poll

top.x -= 100

# Position for bottom poll

bottom.x -= 200

FLY = -10

# Gap in between both polls

GAP = 200

level = 1

bird.fly=0
bird.dead = False

FALL = .6

start_message = 'Click the "Space" key to start'

game_status = 0

score = 0

x = 0

def draw():
    global game_status,score,level, GAP

    if game_status == 0:
        screen.clear()
        screen.blit("flappybird_background", (0,0))
        screen.draw.text(start_message, (WIDTH/2 - 120, HEIGHT/2 + 10), fontname="futura", fontsize=20, color="white")
        bird.draw()
        top.draw()
        bottom.draw()

    if game_status == 1:
        screen.clear()
        screen.blit("flappybird_background", (0,0))
        bird.draw()
        top.draw()
        bottom.draw()
        screen.draw.text(f"Level: {level}", center=(WIDTH/2-110, 45), fontname = "futura", fontsize = 31, color = "black")
        screen.draw.text(f"Score: {score}", center=(WIDTH/2+110, 45), fontname="futura", fontsize=30, color="black")

    if game_status == 2:
        screen.draw.text("GAME OVER", (WIDTH/2 - 115, HEIGHT/2 + 10), fontname="wacky", fontsize=40, color="black")

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

def update():
    global x,game_status,score, postures, GAP, level

    if game_status == 1:
        bird.fly += FALL
        bird.y += bird.fly

        top.left -= 4
        bottom.left -= 4

        if top.right < 0:
            reset_pipes()
            if bird.dead == False:
                score += 1

    frames_per_image = 5


    bird.image = postures[x // frames_per_image]
    x += 1
    if x // frames_per_image >= len(postures):
        x = 0

    if bird.y >= HEIGHT-50:
        bird.y = HEIGHT-50
        bird.dead = True
        game_status = 2

    if bird.colliderect(top) or bird.colliderect(bottom):
        bird.dead = True
        game_status = 2

    if score == 5:
        level = 2
        GAP = 190
        print(f"Gap is {GAP}")

    elif score == 10:
        level = 3
        GAP = 180
        print(f"Gap is {GAP}")

    elif score == 15:
        level = 4
        GAP = 170
        print(f"Gap is {GAP}")

    elif score == 20:
        level = 5
        GAP = 160
        print(f"Gap is {GAP}")

    elif score == 25:
        level = 6
        GAP = 150
        print(f"Gap is {GAP}")

    elif score == 30:
        level = 7
        GAP = 140
        print(f"Gap is {GAP}")

    elif score == 35:
        level = 8
        GAP = 130
        print(f"Gap is {GAP}")

    elif score == 40:
        level = 9
        GAP = 120
        print(f"Gap is {GAP}")

    elif score == 45:
        level = 10
        GAP = 110
        print(f"Gap is {GAP}")


def on_key_down():
    global start_message, game_status, GAP
    if bird.dead == False:
        if keyboard.SPACE:
            start_message = ""
            game_status = 1
            bird.fly = FLY
