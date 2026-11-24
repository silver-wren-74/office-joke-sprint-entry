import os

LINE = "Our meeting about reducing meetings ran long, so the only action item was a follow-up meeting to discuss why we keep needing follow-ups."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
