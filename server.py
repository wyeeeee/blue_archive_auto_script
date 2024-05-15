from server.main import app
import uvicorn
import logging
logging.basicConfig(level=logging.DEBUG,format='%(name)s:   %(levelname)s - %(message)s')
if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000)