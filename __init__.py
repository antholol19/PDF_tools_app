from flask import Flask, redirect, url_for, render_template, request
from PyPDF2 import PdfWriter

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

