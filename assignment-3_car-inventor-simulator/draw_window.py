def main():
    screen = Screen()

    drawcar()
    canvas = screen.getcanvas()

    button_car = Button(canvas.master, text="CAR",
                        command=open_car_window, bg="orange")
    button_suv = Button(canvas.master, text="SUV",
                        command=open_suv_window, bg="orange")
    button_truck = Button(canvas.master, text="TRUCK",
                          command=open_truck_window, bg="orange")

    button_car.pack()
    button_car.place(x=50, y=300)
    button_suv.pack()
    button_suv.place(x=50, y=350)
    button_truck.pack()
    button_truck.place(x=50, y=400)

    # Use random car
    car = generate_random_car()

    boldfont = ("Times", 14, "bold")
    regfont = ("Times", 12, "normal")
    turtle.penup()
    turtle.goto(-235, 325)
    turtle.right(90)
    turtle.write("USED CAR INVENTORY", font=boldfont)
    turtle.goto(-235, 315)
    turtle.write('----------------------------------------', font=boldfont)
    turtle.goto(-235, 305)
    turtle.write('The following car is in inventory:', font=regfont)
    turtle.goto(-235, 285)
    turtle.write('Make:', font=boldfont)
    turtle.goto(-170, 285)
    turtle.write(f'{car.get_make()}', font=regfont)
    turtle.goto(-235, 265)
    turtle.write('Model:', font=boldfont)
    turtle.goto(-170, 265)
    turtle.write(f'{car.get_model()}', font=regfont)
    turtle.goto(-235, 245)
    turtle.write('Mileage:', font=boldfont)
    turtle.goto(-140, 245)
    turtle.write(f'{car.get_mileage()}', font=regfont)
    turtle.goto(-235, 225)
    turtle.write('Price:', font=boldfont)
    turtle.goto(-170, 225)
    turtle.write(f'{car.get_price()}', font=regfont)
    turtle.goto(-235, 205)
    turtle.write('Number of doors:', font=boldfont)
    turtle.goto(-70, 205)
    turtle.write(f'{car.get_doors()}', font=regfont)

    turtle.done()
    screen.mainloop()
