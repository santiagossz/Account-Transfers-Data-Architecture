
import plotly.graph_objects as go

def total_status(df):
    status=df.groupby('status')['pix_amount'].count()
    fig=go.Figure(data=[go.Pie(labels=status.index, values=status.values,pull=[0, 0.2])])
    fig.update_layout(title_text='Total Failed vs Total Completed')
    return fig
def transaction_status(df):
    status=df.groupby(['status','in_or_out'])['id'].count()
    fig=go.Figure(data=[
    go.Bar(name='', x=status['completed'].index, y=status['completed'].values),
    go.Bar(name='', x=status['failed'].index, y=status['failed'].values)])
    fig.add_hline(y=max(status.values),line_dash="dash",opacity=0.7,x0=0.02,x1=0.98)
    fig.add_hline(y=min(status.values),line_dash="dash",opacity=0.7,x0=0.02,x1=0.98)
    fig.update_layout(title_text='Total Failed vs Total Completed per type of transaction')
    return fig
