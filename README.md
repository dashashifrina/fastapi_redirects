# fastapi_redirects


To test:

```
# Start up local ASGI server using Uvicorn
pip install fastapi
pip install uvicorn
uvicorn main:app --reload
```

You can issue a POST request to `localhost/upload_image`. The response is a 307 redirect to `/redirect` and ultimately returns the entire request body originally passed into `/get_image`:
<img width="866" alt="image" src="https://github.com/dashashifrina/fastapi_redirects/assets/109158970/60098550-e908-4cbd-995f-5a4ccd7bbd1e">
