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
    rotation_value = 0
    alphabet = list(ascii_uppercase)
    for i in half:
        rotation_value += alphabet.index(i)
        rotation_value = rotation_value % len(alphabet)
    rotated = ""
    for i in half:
        pos = alphabet.index(i)
        pos = (pos+rotation_value) % len(alphabet)
        rotated += alphabet[pos]
    return rotated


def merge(half_1, half_2):
    alphabet = list(ascii_uppercase)
    final = ""
    for i in range(len(half_1)):
        position = alphabet.index(half_1[i])
        rotation_value = alphabet.index(half_2[i])
        position = (position+rotation_value) % len(alphabet)
        final += alphabet[position]
    return final


drm = input()
half_1, half_2 = divide(drm)
half_1 = rotate(half_1)
half_2 = rotate(half_2)
print(merge(half_1, half_2))
