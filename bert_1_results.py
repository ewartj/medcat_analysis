from altair.vegalite.v4.schema.channels import Y2
import pandas as pd
import altair as alt

alt.renderers.enable('mimetype')

df = pd.read_csv("bert_v1.csv", index_col="term")
df.reset_index(inplace=True)
print(df.head())


df2 = pd.melt(df, id_vars=['term'], value_vars=['precision','recall','f1','support'])
# print(df2.head())

chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y('term', axis=alt.Axis(title='')),
    x=alt.X('f1', axis=alt.Axis(title='F1 score')),
    # color=alt.Color('support', legend=alt.Legend(orient="top",title="", symbolLimit=2))
)

text = chart.mark_text(
    align='left',
    baseline='middle',
    color='black'
    # dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='support'
)

# line = alt.Chart(pd.DataFrame({'f1': 0.95})).mark_rule().encode(x='x')

# line = alt.Chart().mark_rule().encode(y=1)

chart = chart #+ text #+ line

chart.show()