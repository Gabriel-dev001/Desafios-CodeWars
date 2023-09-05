def Control_likes(vetor):
    MAX_NAMES = 2
    size = len(vetor)

    match(size):
        case 0:
            message = "No Likes..."

        case 1:
            message = (f"{vetor[0]}, Like your picture")

        case 2:
            message = (f"{vetor[0]} and {vetor[1]}, Like your picture")

        case 3:
            message = (f"{vetor[0]}, {vetor[1]} and {vetor[2]} others Like your picture")

        case __:
            others = size-MAX_NAMES
            message = (f"{vetor[0]}, {vetor[1]} and {others} others Like your picture")

    return message
