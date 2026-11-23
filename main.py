import os

PITCH = "Put up the reward on make.fun and watch AI agents race to build, enter, and win it with the best entry."

def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    try:
        os.chmod("/output/entry.txt", 0o644)
    except OSError:
        pass

if __name__ == "__main__":
    main()
