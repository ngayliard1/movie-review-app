import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import pandas as pd
import numpy as np

app = dash.Dash(__name__)
model_file = 'movie_review_base_rf_model.sav'
model = pickle.load(open(model_file, 'rb'))

app.layout = html.Div(
    [
        html.I("Enter a Movie Review"),
        html.Br(),
        dcc.Input(id="input1", type="text", placeholder="This movie is the worst.",
                debounce=True, style = {"width" : "60%"}),
        html.Div(id="output"),
    ]
)

@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
)
def update_output(input1, model = model):
    if type(input1) == str:
        valence_array = list(SentimentIntensityAnalyzer().polarity_scores(input1).values())
        prediction = model.predict(np.array(valence_array).reshape(1,-1))
        if prediction[0] == 1:
            return f'Predicted review: Fresh'
        return f'Predicted review: Rotten'
    else:
        return 'enter a string'


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port=8050)
