
import easyocr


reader = easyocr.Reader(["en"])
result = reader.readtext("photos\shayri5.jpeg")

print(result)