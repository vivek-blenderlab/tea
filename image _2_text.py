
import easyocr


reader = easyocr.Reader(["en"])
result = reader.readtext("photos\shayri.jpeg")

print(result)