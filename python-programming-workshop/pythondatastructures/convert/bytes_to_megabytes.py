

#Python that converts bytes, megabytes

def bytestomegabytes(bytes):
    return (bytes / 1024) / 1024

def kilobytestomegabytes(kilobytes):
    return kilobytes / 1024

# Convert 100000 bytes to megabytes.
megabytes1 = bytestomegabytes(100000)
print(100000, "bytes =", megabytes1, "megabytes")

# 1024 kilobytes to megabytes.
megabytes2 = kilobytestomegabytes(1024)
print(1024, "kilobytes =", megabytes2, "megabytes")
