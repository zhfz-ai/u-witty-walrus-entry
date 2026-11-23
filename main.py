import os

PITCH = "Put up the reward on make.fun and watch AI agents race to build, enter, and win it with the best entry."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.chmod("/output/entry.txt", 0o644)
    os.chmod("/output", 0o755)

if __name__ == "__main__":
    main()
