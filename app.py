from weasyprint import HTML
from flask import Flask
import os

html = HTML('invoice.html')
html.write_pdf('invoice.pdf')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

