import plotly.express as px


fig = px.line(x=data1.keys(),y=data1.values())
fig2 = px.line(x=data2.keys(),y=data2.values())

fig.show()
fig2.show()