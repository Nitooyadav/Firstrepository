# main.py
import mysql.connector
from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import matplotlib.pyplot as plt
import io, base64
from collections import Counter
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

def get_launchdata():
    mydb = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM launchdata")
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows


# Home page with links to other pages
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Raw data page with HTML table
@app.get("/rawdata", response_class=HTMLResponse)
def rawdata(request: Request):
    try:
        launches = get_launchdata()
        return templates.TemplateResponse("rawdata.html", {"request": request, "launches": launches})
    except Exception as e:
        return templates.TemplateResponse("rawdata.html", {"request": request, "launches": [], "error": str(e)})

# Flight info search page
@app.get("/flightinfo", response_class=HTMLResponse)
def flightinfo(request: Request, flight_number: int = Query(None)):
    try:
        launches = get_launchdata()
        result = None
        if flight_number is not None:
            for launch in launches:
                if launch.get("flight_number") == flight_number:
                    result = launch
                    break
        return templates.TemplateResponse("flightinfo.html", {
            "request": request,
            "result": result,
            "flight_number": flight_number
        })
    except Exception as e:
        return templates.TemplateResponse("flightinfo.html", {
            "request": request,
            "result": None,
            "flight_number": flight_number,
            "error": str(e)
        })

# Statistics page with pie and bar charts
@app.get("/statistics", response_class=HTMLResponse)
def statistics(request: Request):
    try:
        launches = get_launchdata()

        success = sum(1 for l in launches if l.get("success") == 1)
        failure = sum(1 for l in launches if l.get("success") == 0)

        
        fig, ax = plt.subplots()
        ax.pie([success, failure], labels=["Success", "Failure"], autopct="%1.1f%%", colors=["green", "red"])
        pie_img = io.BytesIO()
        plt.savefig(pie_img, format="png" , transparent=True)
        pie_img.seek(0)
        pie_base64 = base64.b64encode(pie_img.getvalue()).decode("utf-8")
        plt.close(fig)

        
        years = [str(l["date_utc"].year) for l in launches if l.get("date_utc")]
        year_counts = Counter(years)

        fig, ax = plt.subplots()
        ax.bar(year_counts.keys(), year_counts.values(), color="blue")
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Launches")
        ax.set_title("Launches Per Year")
        bar_img = io.BytesIO()
        plt.savefig(bar_img, format="png", transparent=True)
        bar_img.seek(0)
        bar_base64 = base64.b64encode(bar_img.getvalue()).decode("utf-8")
        plt.close(fig)

        return templates.TemplateResponse("statistics.html", {
            "request": request,
            "pie_chart": pie_base64,
            "bar_chart": bar_base64
        })

    except Exception as e:
        return templates.TemplateResponse("statistics.html", {
            "request": request,
            "pie_chart": "",
            "bar_chart": "",
            "error": str(e)
        })
