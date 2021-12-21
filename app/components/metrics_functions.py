
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def status_comp(pix_df,tr_df):
    status_pix=pix_df.groupby('status')['pix_amount'].count()
    status_tr=tr_df.groupby('status')['amount'].count()
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "domain"}, {"type": "domain"}]],
                    subplot_titles=("<b>PIX Total Failed vs Total Completed<b>", "<b>Regular Total Failed vs Total Completed<b>"),
                    horizontal_spacing=0.25)
    fig.add_trace(
        go.Pie(labels=status_pix.index, values=status_pix.values,pull=[0, 0.2]),row=1, col=1)
    fig.add_trace(
        go.Pie(labels=status_tr.index, values=status_tr.values,pull=[0, 0.2]),row=1, col=2)

    fig.update_layout(width=600, height=400)
    fig.update_annotations(font_size=11)
    
    
    return fig

def failed_transfers(pix_df):
    b_hours=pix_df[pix_df['status']=='failed']['is_business_hour'].value_counts()
    type_tr=pix_df[pix_df['status']=='failed'].groupby('in_or_out')['pix_amount'].count()
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "domain"}]],
                    subplot_titles=("<b>Failed transfers in vs transfers out<b>", 
                    "<b>Failed in business/non-business hours<b>"),
                    horizontal_spacing=0.3)
    colors=['rgb(18, 36, 37)','rgb(56, 75, 126)' ]
    fig.add_trace(
        go.Bar(x=type_tr.index,y=type_tr.values,showlegend=False),row=1, col=1)
    fig.add_trace(
        go.Pie(labels=b_hours.index, values=b_hours.values,pull=[0, 0.2], marker_colors=colors),row=1, col=2)

    fig.update_layout(width=700, height=400)
    fig.update_annotations(font_size=11)


    return fig

