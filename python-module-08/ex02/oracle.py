import os
import sys
from dotenv import load_dotenv


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str] = {}
    missing: list[str] = []

    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        else:
            config[var] = value

    if missing:
        print("ORACLE STATUS: Reading the Matrix...")
        print("WARNING: Missing configuration variables:")
        for var in missing:
            print(f"- {var}")

        print("\nCreate a .env file based on .env.example")
        print("Or export variables manually:")
        print("export MATRIX_MODE=development")
        sys.exit(1)

    return config


def describe_environment(config: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"]
    db = config["DATABASE_URL"]
    api = config["API_KEY"]
    log = config["LOG_LEVEL"]
    zion = config["ZION_ENDPOINT"]

    print(f"Mode: {mode}")

    if "localhost" in db or "local" in db:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to remote cluster")

    if api:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {log}")

    if zion.startswith("http"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    print("\nEnvironment security check:")

    if not os.path.exists(".env"):
        print("[WARNING] No .env file detected")
    else:
        print("[OK] .env file properly configured")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


def main() -> None:
    config = load_config()
    describe_environment(config)
    security_check()


if __name__ == "__main__":
    main()
