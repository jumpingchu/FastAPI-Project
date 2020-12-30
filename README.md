# FastAPI-Project

## 基本操作

### 官網
* https://fastapi.tiangolo.com

### 安裝
	$ pip install fastapi
	$ pip install uvicorn

### 執行
* 創建 `main.py` 後，執行以下指令
```bash
$ uvicorn main:app --reload
```

### 特色
* 可 Query item：`http://127.0.0.1:8000/items/5?q=somequery`
* 返回物件為 {"item_id": 5, "q": "somequery"}
* 支援 Swagger UI 測試介面：`http://127.0.0.1:8000/docs`
* 支援異步調用

---

## 使用 Templates
### 參考資料: 
* https://fastapi.tiangolo.com/advanced/templates/

### 安裝 Jinja2
	$ pip install jinja2

### 需另外匯入模組
```python 
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
```

### 注意事項

```python
# path operation 要加入 Request 參數
response_class=HTMLResponse
```
```python
# 返回的是 TemplateResponse
return templates.TemplateResponse("template_file", context)
```
* context 為 `key : value` 形式
* HTML Templates 的變數要用 Jinja2 的 `{{ context_key }}` 來表示

---

## 功能

### ver 0.1 (2020/12/30)
* 根目錄有前往各功能的按鈕
* 點擊後會出現該分類的最新一篇文章

---
