import uvicorn, aiofiles
from os import system
from time import time
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI(
    title = 'Fast file upload to device by network',
    version = '0.5.0',
    docs_url = None,
    redoc_url = None
)

@app.post('/send', response_class=PlainTextResponse)
async def recive(request:Request):
    mb = lambda b: round(b / 1024 / 1024, 1)
    try:
        filename = request.headers.get(
            'filename',
            f'stream-{int(time()*1000)}.part'
        )
        file_len = int(request.headers.get('content-length', 0))
        writed = 0
        async with aiofiles.open(f'./uploads/{filename}', 'wb') as file:
            print(f'Created {filename}')

            async for chunk in request.stream():
                await file.write(chunk)
                writed += len(chunk)
                print(f'Saved {mb(writed)}/{mb(file_len)} MB', end='\r')

            print('\nDone')
    except Exception as e:
        print('\nERROR:')
        print(e)
        raise HTTPException(status_code=409, detail='Uploading false')

    return 'JD'

@app.get('/', response_class=HTMLResponse)
async def index():
    async with aiofiles.open('./index.html') as file:
        return await file.read()

if __name__ == '__main__':
    system('(ip a || ifconfig) | grep "inet 192"')
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
