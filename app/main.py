def main() -> None:
    text_file = open(f"{input("Enter name of the file: ")}.txt", "a")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        text_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
