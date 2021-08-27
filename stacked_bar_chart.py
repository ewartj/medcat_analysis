from altair.vegalite.v4.schema.channels import Y2
import pandas as pd
import altair as alt

alt.renderers.enable('mimetype')

df = pd.read_csv("Aug_all_resukts.csv", index_col="index")
df.drop(["counts"], axis = 1, inplace = True)
df.drop(['address', 'date', "gmc number", "national insurance","url"], axis=0,inplace = True)
df.reset_index(inplace=True)
print(df.head())

df2 = pd.melt(df, id_vars=['index'], value_vars=['Patient','Relative','Healthcare professional'])
print(df2.head())

import plotly.express as px

# wide_df = px.data.medals_wide()

fig = px.bar(df2, x="value", y="index", color='variable', title="Wide-Form Input")
fig.show()

# test = df2.to_dict('index')

# chart = alt.Chart(df2).mark_bar().transform_calculate(
#     x="split(datum.index, ' ')"
#     ).encode(
#     y=alt.X('sum(value)', axis=alt.Axis(title='total annotations')),
#     x=alt.Y('index', axis=alt.Axis(title='')),
#     color=alt.Color('variable', legend=alt.Legend(orient="top",title="", symbolLimit=2))
# ).configure_axis(
#     labelFontSize=20,
#     titleFontSize=20
# ).configure_legend(
# titleFontSize=18,
# labelFontSize=18
# ) 

# text = chart.mark_text(align='left',baseline='middle', lineBreak='\n').encode(text='df:index')
# (chart + text).properties(width=500)
# chart.show()

# chart.save('filename.html')


# df = pd.DataFrame({
#     'y': ['label one', 'label two'],
#     'x': [100, 200],
# })

# chart = alt.Chart(df).mark_bar().transform_calculate(
#     y="split(datum.y, ' ')"
# ).encode(
#     x='x:Q',
#     y='y:N',
# ).properties(
#     height=300
# )

# chart.show()