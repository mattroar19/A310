"""draw_picture.py
Reads a drawing-command text file (Lee & Hubbard Ch.1 format) and draws it with turtle.

Usage:
  python draw_picture.py my_picture.txt
If no filename is given, it defaults to 'my_picture.txt'.
"""

import sys
import turtle


def draw_from_file(filename: str) -> None:
    screen = turtle.Screen()
    screen.title(f"Drawing: {filename}")
    t = turtle.Turtle()
    t.speed(0)

    # Read and execute commands
    with open(filename, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            parts = [p.strip() for p in line.split(",")]
            command = parts[0].lower()

            if command == "goto":
                # goto, x, y, width, color
                x = float(parts[1])
                y = float(parts[2])
                width = float(parts[3])
                color = parts[4]
                t.width(width)
                t.pencolor(color)
                t.goto(x, y)

            elif command == "circle":
                # circle, radius, width, color
                radius = float(parts[1])
                width = float(parts[2])
                color = parts[3]
                t.width(width)
                t.pencolor(color)
                t.circle(radius)

            elif command == "beginfill":
                # beginfill, color
                color = parts[1]
                t.fillcolor(color)
                t.begin_fill()

            elif command == "endfill":
                t.end_fill()

            elif command == "penup":
                t.penup()

            elif command == "pendown":
                t.pendown()

            else:
                print(f"Unknown command: {command} (line: {raw_line!r})")

    t.hideturtle()
    screen.exitonclick()


def main() -> None:
    filename = sys.argv[1] if len(sys.argv) > 1 else "my_picture.txt"
    draw_from_file(filename)
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
