import subprocess


def main():

    # Format code with ruff
    subprocess.run(["uv", "run", "ruff", "format"])

    # Run the game with environment loaded
    subprocess.run(["uv", "run", "src/game.py"])


if __name__ == "__main__":
    main()
