import sys
import importlib
from typing import Any


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready",
}


def check_dependencies() -> dict[str, Any]:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    loaded: dict[str, Any] = {}
    missing: list[str] = []

    for pkg, desc in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {desc}")
            loaded[pkg] = module
        except ImportError:
            print(f"[MISSING] {pkg} - not installed")
            missing.append(pkg)

    if missing:
        print("\nMissing dependencies detected!\n")

        print("Install with pip:")
        print("pip install -r requirements.txt\n")

        print("Or with Poetry:")
        print("poetry install")

        sys.exit(1)

    return loaded


def analyze_data(mods: dict[str, Any]) -> None:
    print("\nAnalyzing Matrix data...")

    np = mods["numpy"]
    pd = mods["pandas"]

    import matplotlib.pyplot as plt

    data = np.random.normal(loc=50, scale=15, size=1000)

    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame({"signal": data})

    mean = df["signal"].mean()
    std = df["signal"].std()

    print(f"Mean: {mean:.2f}, Std: {std:.2f}")

    print("Generating visualization...")

    plt.figure()
    plt.hist(df["signal"], bins=30)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    modules = check_dependencies()
    analyze_data(modules)


if __name__ == "__main__":
    main()
