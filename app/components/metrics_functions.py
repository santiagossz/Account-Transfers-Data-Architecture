
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_status(df):
    status=df.groupby('status')['pix_amount'].count()
    failed_status=df.groupby(['status','in_or_out'])['pix_amount'].count()
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "domain"}, {"type": "bar"}]],
                    subplot_titles=("Total Failed vs Total Completed", "Total Failed per type of transaction"),
                    horizontal_spacing=0.25)
    fig.add_trace(
        go.Pie(labels=status.index, values=status.values,pull=[0, 0.2]),row=1, col=1)
    fig.add_trace(
        go.Bar(x=failed_status['failed'].index,y=failed_status['failed'].values, showlegend=False),row=1, col=2)
    fig.layout.margin.t=20
    fig.update_layout(title_text='<b>PIX Transaction Status Metrics 2020<b>', title_x=0.5,
     width=600, height=300)
    fig.update_annotations(font_size=12)
    return fig

def plot_comparisson(pix_df,tr_df):
    pix=pix_df[pix_df['status']=='failed']['is_business_hour'].value_counts()
    tr=tr_df['is_business_hour'].value_counts()
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
    subplot_titles=("Pix Transactions", "Regular Transactions"))
    colors=['rgb(18, 36, 37)','rgb(56, 75, 126)' ]
    fig.add_trace(go.Pie(labels=pix.index, values=pix.values,pull=[0, 0.2], marker_colors=colors),
                1, 1)
    fig.add_trace(go.Pie(labels=tr.index, values=tr.values,pull=[0, 0.2]),
              1, 2)
    fig.update_layout(title_text='<b>Failed Transactions across Time<b>', title_x=0.5,
     width=600, height=300)
    fig.update_annotations(font_size=12)
    return fig
