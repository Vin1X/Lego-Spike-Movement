from lego_spike import Lego_Spike


# Main function to call
def main():
    # Init Lego Spike
    spike = Lego_Spike()
    while True:
        spike.follow_line()


if __name__ == "__main__":
    main()
