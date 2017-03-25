"""This is the entry point of the program."""


def create_box(height, width, character):
    if height >= 1 and width >= 1:
        return (width * character + '\n') * height
    return 'Height and width must be greater or equal to 1'

def create_outer_border(height, width, character):
    if height >= 1 and width >= 1:
        top_and_bottom_lines = width * character + '\n'
        middle_lines = character + ((width - 2) * ' ') + character + '\n'
        return top_and_bottom_lines + (middle_lines * (height - 2)) + top_and_bottom_lines
    return 'Height and width must be greater or equal to 1'


if __name__ == '__main__':
    create_box(3, 4, '*')

