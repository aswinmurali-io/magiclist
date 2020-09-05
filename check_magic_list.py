from magiclist import MagicList


def main():
    t = MagicList()
    t.append_all({str(i): "test" for i in range(2)})
    t.print()


if __name__ == "__main__":
    main()
