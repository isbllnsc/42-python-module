import sys
import os
import site


def in_virtualenv() -> bool:
    """
    Detecta se está em um virtual environment
    """
    return (
        hasattr(sys, "base_prefix")
        and sys.prefix != sys.base_prefix
    ) or hasattr(sys, "real_prefix")


def main() -> None:
    python_path: str = sys.executable

    if not in_virtualenv():
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")
        return

    # Dentro do venv
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path)

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")

    # Caminho dos packages
    site_packages: list[str] = site.getsitepackages()
    if site_packages:
        print("\nPackage installation path:")
        print(site_packages[0])


if __name__ == "__main__":
    main()
