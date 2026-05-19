import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# הכנת נתוני דוגמא
df = px.data.iris()

# יצירת אפליקציית Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("דשבורד אינטרקטיבי לדוגמה"),
    html.Label("בחר משתנה X:"),
    dcc.Dropdown(
        id='x-axis',
        options=[{'label': i, 'value': i} for i in df.columns if df[i].dtype != 'object'],
        value='sepal_width'
    ),
    html.Label("בחר משתנה Y:"),
    dcc.Dropdown(
        id='y-axis',
        options=[{'label': i, 'value': i} for i in df.columns if df[i].dtype != 'object'],
        value='sepal_length'
    ),
    dcc.Graph(id='scatter-plot'),
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis', 'value'),
     Input('y-axis', 'value')]
)
def update_figure(x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, color="species", title="Scatter plot של נתוני Iris")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)