def likes(names):
    MAX_NAMES = 2
    size = len(names)

    match(size):
        case 0:
            message = "no one likes this"

        case 1:
            message = (f"{names[0]} likes this")

        case 2:
            message = (f"{names[0]} and {names[1]} like this")

        case 3:
            message = (f"{names[0]}, {names[1]} and {names[2]} like this")

        case __:
            others = size-MAX_NAMES
            message = (f"{names[0]}, {names[1]} and {others} others like this")

    return message
