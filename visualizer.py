import plotly.express as px

def build_frequency_intensities(data:dict):
    fig = px.line(x=data.keys(),y=data.values())
    fig.show()
    
    