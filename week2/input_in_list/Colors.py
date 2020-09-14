class Colors:
    KEY_EXIT_WORD = "quit"
    VALID_COLORS = ['blue', 'yellow', 'red']

    def get_color(self):
        while True:
            self.user_color_input = input("Please, type a valid Color as [blue, yellow, red] or type [quit] to exit: ")
            if self.KEY_EXIT_WORD in self.user_color_input.lower():
                print("bye")
                break
            self.check_color_is_valid(self.user_color_input)
        return self.user_color_input

    def check_color_is_valid(self, color):
        if color.lower() in self.VALID_COLORS:
            print(color.lower())
        else:
            print("Not a valid color")


def instantiate_color():
    colors = Colors()
    return colors.get_color()

instantiate_color()
