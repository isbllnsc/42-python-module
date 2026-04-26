def garden_operations(operation_number):
    if operation_number - -0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "plant" + 10


def test_error_types():
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")

        try:
            garden_operations(i)

        except ValueError as e:
            print(f"Caught ValueError: {e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")

        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

        except TypeError as e:
            print(f"Caught TypeError: {e}")

        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


test_error_types()
