import turtle
import math
from PIL import Image, ImageTk


WIDTH = 1920
HEIGHT = 1040
IMAGEPATH = "" # path to the image


def set_background_image(image_path):
    canvas = turtle.getcanvas()

    def draw_image():
        # Force update to get real size
        canvas.update_idletasks()
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        if width <= 1 or height <= 1:
            # Still not ready, try again shortly
            canvas.after(100, draw_image)
            return

        # Load and resize the image
        img = Image.open(image_path)
        resized = img.resize((width, height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized)

        # Prevent garbage collection
        canvas.bg_img = photo

        # Remove previous backgrounds
        canvas.delete("bg")

        # Draw at top-left of canvas
        canvas.create_image(0, 0, image=photo, tags="bg")

    draw_image()

screen = turtle.Screen()
screen.title("Follow Mouse Cursor While Right-Click Held")
screen.bgcolor("white")
screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT)
set_background_image(IMAGEPATH)

arrow = turtle.Turtle()
arrow.shape("triangle")
arrow.hideturtle()
arrow.shapesize(0.6, 1.8, 1)
arrow.width(5)
arrow.color("red")
arrow.penup()
arrow.hideturtle()
arrow.speed(0)

drawing = False
need_jump = False
target_x, target_y = 0, 0
speed = 120  # pixels per frame for smooth movement

def right_click_start(x, y):
    global drawing, need_jump, target_x, target_y
    drawing = True
    need_jump = True
    target_x, target_y = x, y

def right_click_stop(x, y):
    global drawing
    drawing = False
    arrow.penup()
    arrow.hideturtle()

def get_mouse_pos():
    canvas = screen.getcanvas()
    root_x = canvas.winfo_rootx()
    root_y = canvas.winfo_rooty()
    pointer_x = canvas.winfo_pointerx() - root_x
    pointer_y = canvas.winfo_pointery() - root_y
    return pointer_x, pointer_y

def update_target():
    global target_x, target_y
    if drawing:
        pointer_x, pointer_y = get_mouse_pos()
        canvas = screen.getcanvas()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        target_x = pointer_x - width / 2
        target_y = height / 2 - pointer_y
    screen.ontimer(update_target, 10)

def follow_mouse():
    global need_jump
    if drawing:
        if need_jump:
            # Teleport pen up, then pendown once at starting pos
            arrow.penup()
            arrow.goto(target_x, target_y)
            arrow.pendown()
            need_jump = False
        else:
            # Move smoothly toward target with pen down
            current_x, current_y = arrow.position()
            dx = target_x - current_x
            dy = target_y - current_y
            dist = math.hypot(dx, dy)
            if dist > speed:
                # Move only 'speed' pixels toward target
                new_x = current_x + dx / dist * speed
                new_y = current_y + dy / dist * speed
                arrow.goto(new_x, new_y)
            else:
                # Close enough, snap to target
                arrow.goto(target_x, target_y)

        # Rotate arrow toward target
        dx = target_x - arrow.xcor()
        dy = target_y - arrow.ycor()
        angle = math.degrees(math.atan2(dy, dx))
        arrow.setheading(angle)

    screen.update()
    screen.ontimer(follow_mouse, 16)

screen.onclick(right_click_start, btn=3)
screen.getcanvas().bind("<ButtonRelease-3>", lambda e: right_click_stop(0, 0))

update_target()
follow_mouse()
screen.mainloop()
