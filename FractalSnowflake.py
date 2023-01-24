import turtle
import random

def fractal_snowflake(t, branch_len, branch_factor, angle, angle_factor):
    if branch_len > 5:
        for i in range(6):
            t.forward(branch_len)
            t.right(angle)
            fractal_snowflake(t, branch_len * branch_factor, branch_factor, angle + angle_factor, angle_factor)
            t.left(angle * 2)
            fractal_snowflake(t, branch_len * branch_factor, branch_factor, angle + angle_factor, angle_factor)
            t.right(angle)
            t.backward(branch_len)
            t.left(60)

def generate_snowflake():
    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(0, 0)
    t.down()

    # Generate random parameters for the fractal snowflake
    branch_len = random.randint(50, 100)
    branch_factor = random.uniform(0.5, 0.8)
    angle = random.randint(15, 45)
    angle_factor = random.uniform(1, 2)

    fractal_snowflake(t, branch_len, branch_factor, angle, angle_factor)
