import plotly.express as px

def build_frequency_intensities(data):
    fig = px.line(x=data[:,0],y=data[:,1])
    fig.show()
