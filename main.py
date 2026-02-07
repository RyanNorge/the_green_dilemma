import subprocess

from src.game import run


def main():

    subprocess.run(["uv", "run", "ruff", "format"])
    run()


if __name__ == "__main__":
    main()
