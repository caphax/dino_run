def colide(xb1, xb2):
    b1_x1 = xb1.x
    b1_x2 = xb1.bottomright[0]
    b1_y1 = xb1.y
    b1_y2 = xb1.bottomright[1]
    b2_x1 = xb2.x
    b2_x2 = xb2.bottomright[0]
    b2_y1 = xb2.y
    b2_y2 = xb2.bottomright[1]
    if ((b1_y1 <= b2_y2 <= b1_y2) or (b1_y1 <= b2_y1 <= b1_y2) and
            (b1_x1 <= b2_x2 <= b1_x2) or (b1_x1 <= b2_x1 <= b1_x2)):
        return True
    return False