# from altair.vegalite.v4.schema.channels import Y2
import pandas as pd
import altair as alt
import plotly.express as px

df = pd.read_csv("Annotators_vs_CAPSA", index_col=False)
print(df)

source = df

# chart = alt.Chart(source).mark_bar().encode(
#     x='index',
#     y='percentage_agreement',
#     color='type',
#     column='type'
# )

# chart.show()

fig = px.bar(df, x='index', 
y='percentage_agreement', color='type', barmode='group',
    text='sum')#,textposition='auto')
fig.show()