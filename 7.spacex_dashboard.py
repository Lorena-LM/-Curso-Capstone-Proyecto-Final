import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

launch_sites = [{'label': 'All Sites', 'value': 'All Sites'}]
all_launch_sites = spacex_df['Launch Site'].unique().tolist()
for launch_site in all_launch_sites:
    launch_sites.append({'label': launch_site, 'value': launch_site})

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    dcc.Dropdown(
        id='site-dropdown',
        options=launch_sites,
        placeholder='Select a Launch Site',
        searchable=True,
        clearable=False,
        value='All Sites'
    ),
    
    html.Br(),
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: f'{i} Kg' for i in range(0, 11000, 1000)},
        value=[min_payload, max_payload]
    ),
    
    html.Br(),
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

@app.callback(
    Output('success-pie-chart', 'figure'),
    [Input('site-dropdown', 'value')]
)
def update_piegraph(site_dropdown):
    if site_dropdown == 'All Sites':
        data = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            data, names='Launch Site', title='Total Success Launches by All Sites'
        )
    else:
        data = spacex_df[spacex_df['Launch Site'] == site_dropdown]
        fig = px.pie(
            data, names='class', title=f'Total Success Launches for Site → {site_dropdown}'
        )
    return fig

@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]
)
def update_scattergraph(site_dropdown, payload_slider):
    low, high = payload_slider
    filtered_data = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                              (spacex_df['Payload Mass (kg)'] <= high)]
    
    if site_dropdown != 'All Sites':
        filtered_data = filtered_data[filtered_data['Launch Site'] == site_dropdown]
    
    fig = px.scatter(
        filtered_data,
        x="Payload Mass (kg)",
        y="class",
        title=f'Correlation Between Payload and Success for {site_dropdown}',
        color="Booster Version Category",
        size='Payload Mass (kg)',
        hover_data=['Payload Mass (kg)']
    )
    return fig

if __name__ == '__main__':
    app.run_server()