import turtle
import time
import random

delay = 0.1
skor = 0
yuksek_skor = 0

# ekran
ekran = turtle.Screen()
ekran.title("Yılan Oyunu @Ceaser")
ekran.bgcolor("#052419")
ekran.setup(width=600, height=600)
ekran.tracer(0)

# kafa
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("#ff0000")
kafa.penup()
kafa.goto(0, 0)
kafa.direction = "stop"

# yemek
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("#DE3163")
yemek.penup()
yemek.goto(0, 100)

# vücut parçaları listesi
evreler = []

# skor yazısı
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Skor: 0  Yüksek Skor: 0", align="center", font=("Courier", 24, "normal"))

# yön fonksiyonları
def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"

def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"

def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"

# hareket fonksiyonu
def move():
    if kafa.direction == "up":
        kafa.sety(kafa.ycor() + 20)
    if kafa.direction == "down":
        kafa.sety(kafa.ycor() - 20)
    if kafa.direction == "left":
        kafa.setx(kafa.xcor() - 20)
    if kafa.direction == "right":
        kafa.setx(kafa.xcor() + 20)

# klavye kontrolleri
ekran.listen()
ekran.onkey(go_up, "w")
ekran.onkey(go_down, "s")
ekran.onkey(go_left, "a")
ekran.onkey(go_right, "d")

# oyun döngüsü
while True:
    ekran.update()

    # sınır kontrolü
    if abs(kafa.xcor()) > 290 or abs(kafa.ycor()) > 290:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for evre in evreler:
            evre.goto(1000, 1000)
        evreler.clear()

        skor = 0
        pen.clear()
        pen.write("Skor: {}  Yüksek Skor: {}".format(skor, yuksek_skor), align="center", font=("Courier", 24, "normal"))

    # yemek yeme kontrolü
    if kafa.distance(yemek) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yemek.goto(x, y)

        yeni_ekle = turtle.Turtle()
        yeni_ekle.speed(0)
        yeni_ekle.shape("square")
        yeni_ekle.color("gray")
        yeni_ekle.penup()
        evreler.append(yeni_ekle)

        skor += 1
        if skor > yuksek_skor:
            yuksek_skor = skor

        pen.clear()
        pen.write("Skor: {}  Yüksek Skor: {}".format(skor, yuksek_skor), align="center", font=("Courier", 24, "normal"))

    # vücut hareketi
    for i in range(len(evreler) - 1, 0, -1):
        x = evreler[i - 1].xcor()
        y = evreler[i - 1].ycor()
        evreler[i].goto(x, y)

    if len(evreler) > 0:
        evreler[0].goto(kafa.xcor(), kafa.ycor())

    move()

    # kendine çarpma kontrolü
    for evre in evreler:
        if kafa.distance(evre) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"

            for evre in evreler:
                evre.goto(1000, 1000)
            evreler.clear()

            skor = 0
            pen.clear()
            pen.write("Skor: {}  Yüksek Skor: {}".format(skor, yuksek_skor), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
