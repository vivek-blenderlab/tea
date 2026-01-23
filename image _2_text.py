
import easyocr


reader = easyocr.Reader(["en"])
result = reader.readtext("photos\shayri.jpeg")

print(result)



#### edit this
"""
batch_size (int, default = 1) - batch_size>1 will make EasyOCR faster but use more memory

def read_img(sta_path , lang) :
  reader = easyocr.Reader(lang)
  result = reader.readtext(sta_path , details = 0 , gpu = False
  return result , reader 
  
  
# save extracted data into another new dir user_data/exe_data
exe_data:
            img
            pdf
            video transcript
            convo summery
            user_plan(summery as text)


# pdf summery 





            
"""
