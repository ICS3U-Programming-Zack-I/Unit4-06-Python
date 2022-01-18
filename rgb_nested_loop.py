def main():
    print("welcome ")
    red = 0
    green = 0
    blue = 0

    for blue in range(1, 51, 1):
        print(" RGB:( {}, {}, {}) ".format(blue, green, red))
        for green in range(1, 51, 1):
            print("RGB: ( {}, {}, {}) ".format(blue, green, red))
            for red in range(1, 51, 1):
                print("RGB: ({}, {}, {} ) ".format(blue, green, red))


if __name__ == "__main__":
    main()
