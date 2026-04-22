def ft_water_reminder() -> None:
    last_wtr = int(input("Days since last watering: "))
    if last_wtr > 2:
        print("Water needs plants!")
    else:
        print("Plants are fine.")
