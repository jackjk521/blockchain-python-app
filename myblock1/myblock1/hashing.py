import hashlib

input = b"Hello World"
output = hashlib.sha256(input)

print(output.hexdigest())


# images hashing
file = open("image.jpg", "rb")
hash = hashlib.sha256(file.read().hexdigest())
file.close()

print(f"The hash is: {hash}")

# message hashing

secret = "secretphrase"

def hash_with_secret(input, secret):
    combined = input + secret
    return hashlib.sha256(combined.encode()).hexdigest()

message = "Hey Bob"

print(hash_with_secret(message, secret))