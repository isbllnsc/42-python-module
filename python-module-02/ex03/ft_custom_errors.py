class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===.\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for error in [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


test_custom_errors()
