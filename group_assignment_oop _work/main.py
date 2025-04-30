from pet import Pet

def main():
    buddy = Pet("Buddy")

    buddy.get_status()
    buddy.eat()
    buddy.sleep()
    buddy.play()
    buddy.train("roll over")
    buddy.train("shake paw")
    buddy.show_tricks()
    buddy.get_status()

if __name__ == "__main__":
    main()
