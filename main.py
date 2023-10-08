from fastapi import FastAPI, File, UploadFile
from nudenet import NudeDetector

app = FastAPI(
    title="Image Recognition Project",
    description="This is a Image Recognition Api ,with auto docs .",
    version="2.5.0",
)



@app.post("/files")
async def UploadImage(file: bytes = File(...)):
    with open('image.jpg','wb') as image:
        image.write(file)
        image.close()
    nude_detector = NudeDetector()
    res=nude_detector.detect('image.jpg') # Returns list of detectionres)
    if len(res)<1:
        return {"Result":"Image Not look either male or female"}
    elif len(res)==5:
        str1="Pics may be adultry.pls recheck it.",res
        return {"Result":str1}

    elif len(res)==1:
         return {"Result":"Seems ok"}
    elif len(res)>1 and len(res)!=5:
         return {"Result":"More than one faces are possible.Pls recheck it"}
    