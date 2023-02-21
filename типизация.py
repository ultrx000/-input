text = "я люблю динамическую типизацию"

# cp1251 кодировка
encoded_text = text.encode("cp1251")
print("cp1251:", len(encoded_text), "bytes")

# utf-8 кодировка
encoded_text = text.encode("utf-8")
print("utf-8:", len(encoded_text), "bytes")

# utf-16 кодировка
encoded_text = text.encode("utf-16")
print("utf-16:", len(encoded_text), "bytes")

# utf-32 кодировка
encoded_text = text.encode("utf-32")
print("utf-32:", len(encoded_text), "bytes")
