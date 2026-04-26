def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    test_values = ["25", "abc"]

    for value in test_values:
        print(f"\nInput data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")

        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print()

    print("\nAll tests completed –– program didn't crash!")


def ft_first_exception():
    print("=== Garden Temperature ===")
    test_temperature()


ft_first_exception()
