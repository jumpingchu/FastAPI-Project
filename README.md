# FastAPI-Project
【FastAPI】實作測試

## 基本操作
### 官網
* https://fastapi.tiangolo.com

### 安裝

	$ pip install fastapi
	$ pip install uvicorn

### 執行
* 創建 `main.py` 後，執行以下指令
	
		$ uvicorn main:app --reload



## 特色
* 可 Query item：`http://127.0.0.1:8000/items/5?q=somequery`
> {"item_id": 5, "q": "somequery"}
* 支援 Swagger UI 測試介面：`http://127.0.0.1:8000/docs`
* 支援異步調用
