""" Programm which returns how many times the person has seen the ball which
was thrown from the h m height with bouncing """

def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        seen = 0
        while h > window:
            h = h * bounce
            seen += 1
            if h > window:
                seen += 1
        return seen
    else:
        return -1


print(bouncing_ball(3, 1/2, 1.5))
