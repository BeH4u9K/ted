cat > main.py << 'EOF'
import qrcode
import base64
from flask import Flask
from flask import request
from io import BytesIO

app = Flask(__name__)

@app.route("/qr")
def qr():
    msg = request.args.get('msg')
    if not msg:
        return "Ошибка: укажите параметр msg (например, /qr?msg=Hello)", 400
    img = qrcode.make(msg)
    
    buffer = BytesIO()
    img.save(buffer, format="png")
    
    img64 = base64.b64encode(buffer.getvalue())
    return f'<img src="data:image/png;base64,{img64.decode()}" alt="qrcode" />'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
EOF