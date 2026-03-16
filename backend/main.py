# import matplotlib.pyplot as plt
# import io
# import base64
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from model import generate_perfume

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class RequestData(BaseModel):
#     ingredients: list
#     category: str


# @app.post("/generate")
# def generate(data: RequestData):

#     result = generate_perfume(
#         data.ingredients,
#         data.category
#     )

#     # create pie chart
#     chart = generate_chart(result["formula"])

#     # add chart to response
#     result["chart"] = chart

#     return result

# def generate_chart(formula):
#     labels = [item["ingredient"] for item in formula]
#     sizes = [item["percentage"] for item in formula]

#     fig, ax = plt.subplots()

#     ax.pie(
#         sizes,
#         labels=labels,
#         autopct="%1.1f%%",
#         startangle=90
#     )

#     ax.axis("equal")

#     buf = io.BytesIO()
#     plt.savefig(buf, format="png")
#     plt.close()

#     buf.seek(0)

#     chart_base64 = base64.b64encode(buf.read()).decode("utf-8")

#     return chart_base64

import matplotlib
matplotlib.use("Agg")  # MUST be before pyplot import

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import matplotlib.pyplot as plt
import io
import base64

from model import generate_perfume


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestData(BaseModel):
    ingredients: list[str]
    category: str


# -------------------------------
# PIE CHART GENERATOR
# -------------------------------
def generate_chart(formula):
    try:
        labels = [item["ingredient"] for item in formula]
        sizes = [item["percentage"] for item in formula]

        if not labels or sum(sizes) == 0:
            print("Chart skipped: empty labels or zero sizes")
            return None

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        fig.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)
        buf.seek(0)

        chart_base64 = base64.b64encode(buf.read()).decode("utf-8")
        print(f"Chart generated OK. Base64 length: {len(chart_base64)}")
        return chart_base64

    except Exception as e:
        print(f"Chart generation ERROR: {e}")
        return None


# -------------------------------
# TEST ENDPOINT
# Open in browser: http://localhost:8000/test-chart
# -------------------------------
@app.get("/test-chart", response_class=HTMLResponse)
def test_chart():
    dummy_formula = [
        {"ingredient": "Rose", "percentage": 40},
        {"ingredient": "Jasmine", "percentage": 35},
        {"ingredient": "Musk", "percentage": 25},
    ]
    chart = generate_chart(dummy_formula)

    if chart:
        return f"""
        <html><body>
        <h2>Chart Test — SUCCESS ✅</h2>
        <img src="data:image/png;base64,{chart}" />
        </body></html>
        """
    else:
        return "<html><body><h2>Chart Test — FAILED ❌ (check terminal)</h2></body></html>"


# -------------------------------
# MAIN ENDPOINT
# -------------------------------
@app.post("/generate")
def generate(data: RequestData):
    result = generate_perfume(data.ingredients, data.category)

    print(f"Formula: {result.get('formula')}")

    chart = generate_chart(result["formula"])
    result["chart"] = chart

    print(f"Chart: {'YES length=' + str(len(chart)) if chart else 'NO (None)'}")

    return result