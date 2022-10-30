def colide(xb1, xb2):
    if (xb1.x <= xb2.x <= xb1.topright[0] and
            xb1.y <= xb2.y <= xb1.bottom):
        return True
    return False