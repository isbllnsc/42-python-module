def input_temperature(temp_str):
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature():
    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"\nInput data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed –– program didn't crash!")


def ft_raise_exception():
    print("=== Garden Temperature Checker ===")
    test_temperature()


ft_raise_exception()
