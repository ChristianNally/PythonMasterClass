from fastapi import FastAPI, File, HTTPException, status, UploadFile
from fastapi.responses import HTMLResponse
import aiofiles

from typing import Annotated

app = FastAPI()

@app.post('/upload')
async def upload(file: UploadFile):
	try:
		contents = await file.read()
		async with aiofiles.open(file.filename, 'wb') as f:
				await f.write(contents)
	except Exception:
		raise HTTPException(
				status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
				detail='There was an error uploading the file',
		)
	finally:
		await file.close()

	return {'message': f'Successfuly uploaded {file.filename}'}

@app.get('/')
def main():
	content = '''
	<body>
	<form action='/upload' enctype='multipart/form-data' method='post'>
	<input name='file' type='file'>
	<input type='submit'>
	</form>
	</body>
	'''
	return HTMLResponse(content=content)

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
	return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
	return {"filename": file.filename}
