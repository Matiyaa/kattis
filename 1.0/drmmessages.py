from string import ascii_uppercase


def divide(drm):
    n = len(drm)
    half = int(n/2)
    drm_1 = ""
    drm_2 = ""
    i = 0
    for letter in drm:
        if i < half:
            drm_1 += letter
            i += 1
        else:
            drm_2 += letter
            i += 1
    return drm_1, drm_2


def rotate(half):
    rotv = 0
    alph = list(ascii_uppercase)
    for i in half:
        rotv += alph.index(i)
        rotv = rotv % len(alph)
    rotated = ""
    for i in half:
        pos = alph.index(i)
        pos = (pos+rotv) % len(alph)
        rotated += alph[pos]
    return rotated


def merge(half_1, half_2):
    alph = list(ascii_uppercase)
    final = ""
    for i in range(len(half_1)):
        pos = alph.index(half_1[i])
        rotv = alph.index(half_2[i])
        pos = (pos+rotv) % len(alph)
        final += alph[pos]
    return final


drm = input()
half_1, half_2 = divide(drm)
half_1 = rotate(half_1)
half_2 = rotate(half_2)
print(merge(half_1, half_2))
