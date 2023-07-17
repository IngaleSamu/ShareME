import base64


def encodePassword(password):
    passwordBytes = password.encode("ascii")
    base64_bytes = base64.b64encode(passwordBytes)
    encodedPassword = base64_bytes.decode("ascii")
    return encodedPassword