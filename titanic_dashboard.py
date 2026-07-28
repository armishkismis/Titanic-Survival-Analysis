import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Titanic Analytics | Professional Dashboard",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

COLORS = {
    'primary': '#1e3a5f',
    'secondary': '#3d5a80',
    'accent': '#ee6c4d',
    'success': '#2ec4b6',
    'danger': '#e63946',
    'warning': '#f4a261',
    'info': '#4895ef',
    'dark': '#1d3557',
    'light': '#f8f9fa',
    'muted': '#6c757d'
}

CHART_TEMPLATE = {
    'layout': go.Layout(
        font=dict(family='Segoe UI, sans-serif', size=12, color='#2d3748'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=60, r=30, l=60, b=60),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
        xaxis=dict(showgrid=True, gridcolor='#e2e8f0', linewidth=1, linecolor='#e2e8f0'),
        yaxis=dict(showgrid=True, gridcolor='#e2e8f0', linewidth=1, linecolor='#e2e8f0')
    )
}

def style_metric卡片(label, value, delta=None, help_text=None):
    return st.metric(label=label, value=value, delta=delta, help=help_text)

@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "titanic_cleaned.csv")
    return pd.read_csv(csv_path)

def style_sidebar():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e3a5f 0%, #2d4a6f 100%);
        }
        [data-testid="stSidebar"] .stRadio > div {
            background-color: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 10px;
        }
        [data-testid="stSidebar"] label {
            color: white !important;
            font-weight: 600;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: white !important;
        }
        .sidebar-header {
            color: white;
            font-size: 24px;
            font-weight: 700;
            padding: 20px 0;
            text-align: center;
            border-bottom: 2px solid rgba(255,255,255,0.2);
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 14px;
            font-weight: 600;
            color: #6c757d;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .card-header {
            font-size: 18px;
            font-weight: 600;
            color: #1e3a5f;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 2px solid #ee6c4d;
        }
        .kpi-card {
            background: linear-gradient(135deg, #1e3a5f 0%, #3d5a80 100%);
            border-radius: 16px;
            padding: 24px;
            color: white;
            box-shadow: 0 4px 12px rgba(30,58,95,0.3);
        }
        .kpi-value {
            font-size: 36px;
            font-weight: 700;
        }
        .kpi-label {
            font-size: 14px;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        </style>
    """, unsafe_allow_html=True)

def create_header():
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 20px 0; border-bottom: 2px solid #e2e8f0; margin-bottom: 30px;">
            <div>
                <h1 style="margin: 0; color: #1e3a5f; font-size: 32px; font-weight: 700;">🚢 Titanic Analytics</h1>
                <p style="margin: 8px 0 0 0; color: #6c757d; font-size: 14px;">Professional Passenger Survival Analysis Dashboard</p>
            </div>
            <div style="text-align: right;">
                <span style="background: #ee6c4d; color: white; padding: 6px 16px; border-radius: 20px; font-size: 12px; font-weight: 600;">DATASET 1912</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

df = load_data()
style_sidebar()
create_header()

with st.sidebar:
    st.markdown('<div class="sidebar-header">🎯 Navigation</div>', unsafe_allow_html=True)
    page = st.radio("Select Page", ["Executive Overview", "Survival Analysis", "Demographics", "Fare & Economics"])
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    total = len(df)
    survived = df["Survived"].sum()
    st.markdown(f"**Total Passengers:** {total}")
    st.markdown(f"**Survived:** {survived} ({survived/total*100:.1f}%)")
    st.markdown(f"**Avg Fare:** ${df['Fare'].mean():.2f}")

if page == "Executive Overview":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="kpi-card" style="background: linear-gradient(135deg, #1e3a5f 0%, #3d5a80 100%);">
                <div class="kpi-label">Total Passengers</div>
                <div class="kpi-value">{total:,}</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="kpi-card" style="background: linear-gradient(135deg, #2ec4b6 0%, #20a39e 100%);">
                <div class="kpi-label">Survived</div>
                <div class="kpi-value">{survived:,}</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        rate = survived/total*100
        st.markdown(f"""
            <div class="kpi-card" style="background: linear-gradient(135deg, #ee6c4d 0%, #d4573d 100%);">
                <div class="kpi-label">Survival Rate</div>
                <div class="kpi-value">{rate:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div class="kpi-card" style="background: linear-gradient(135deg, #4895ef 0%, #3670d1 100%);">
                <div class="kpi-label">Avg Age</div>
                <div class="kpi-value">{df['Age'].mean():.0f}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><div class="card-header">Passenger Class Distribution</div>', unsafe_allow_html=True)
        class_counts = df['Pclass'].value_counts().sort_index()
        fig = go.Figure()
        fig.add_trace(go.Pie(labels=['1st Class', '2nd Class', '3rd Class'], 
                          values=class_counts.values,
                          marker=dict(colors=['#1e3a5f', '#3d5a80', '#ee6c4d']),
                          hole=0.4,
                          textinfo='percent+label',
                          textposition='outside'))
        fig.update_layout(template=CHART_TEMPLATE, height=350, showlegend=True, legend=dict(orientation='h'))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card"><div class="card-header">Gender Distribution</div>', unsafe_allow_html=True)
        sex_data = df['Sex'].value_counts()
        colors = [COLORS['primary'], COLORS['accent']]
        fig = go.Figure(go.Bar(
            x=sex_data.index.str.title(),
            y=sex_data.values,
            marker_color=colors,
            text=sex_data.values,
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350, showlegend=False,
                       xaxis_title=None, yaxis_title='Count')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><div class="card-header">Age Distribution</div>', unsafe_allow_html=True)
        fig = px.histogram(df, x='Age', nbins=35, color_discrete_sequence=[COLORS['primary']])
        fig.update_layout(template=CHART_TEMPLATE, height=350, 
                       xaxis_title='Age (Years)', yaxis_title='Count')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card"><div class="card-header">Embarkation Ports</div>', unsafe_allow_html=True)
        port_data = df['Embarked'].value_counts()
        port_names = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
        fig = go.Figure(go.Bar(
            x=[port_names.get(p, p) for p in port_data.index],
            y=port_data.values,
            marker_color=[COLORS['primary'], COLORS['secondary'], COLORS['accent']],
            text=port_data.values,
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       xaxis_title=None, yaxis_title='Count')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Survival Analysis":
    st.markdown('<div class="card"><div class="card-header">Survival Rate by Key Factors</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        surv_class = df.groupby('Pclass')['Survived'].mean() * 100
        colors = ['#2ec4b6' if v == max(surv_class.values) else '#1e3a5f' for v in surv_class.values]
        fig = go.Figure(go.Bar(
            x=['1st Class', '2nd Class', '3rd Class'],
            y=surv_class.values,
            marker_color=colors,
            text=[f'{v:.1f}%' for v in surv_class.values],
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       title='By Passenger Class', yaxis_title='Survival Rate (%)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        surv_sex = df.groupby('Sex')['Survived'].mean() * 100
        colors = [COLORS['accent'], COLORS['success']]
        fig = go.Figure(go.Bar(
            x=surv_sex.index.str.title(),
            y=surv_sex.values,
            marker_color=colors,
            text=[f'{v:.1f}%' for v in surv_sex.values],
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       title='By Gender', yaxis_title='Survival Rate (%)')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><div class="card-header">Survival by Age Group</div>', unsafe_allow_html=True)
        df_temp = df.copy()
        df_temp['AgeGroup'] = pd.cut(df_temp['Age'], bins=[0, 12, 18, 35, 50, 80], 
                                labels=['Child (0-12)', 'Teen (13-18)', 'Young (19-35)', 'Middle (36-50)', 'Senior (51+)'])
        surv_age = df_temp.groupby('AgeGroup')['Survived'].mean() * 100
        fig = go.Figure(go.Bar(
            x=surv_age.index.astype(str),
            y=surv_age.values,
            marker_color=COLORS['primary'],
            text=[f'{v:.1f}%' for v in surv_age.values],
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       yaxis_title='Survival Rate (%)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card"><div class="card-header">Survival by Family Size</div>', unsafe_allow_html=True)
        df_temp = df.copy()
        df_temp['FamilyGroup'] = df_temp['FamilySize'].apply(lambda x: 'Solo' if x == 1 else ('Small (2-4)' if x <= 4 else 'Large (5+)'))
        surv_fam = df_temp.groupby('FamilyGroup')['Survived'].mean() * 100
        order = ['Solo', 'Small (2-4)', 'Large (5+)']
        surv_fam = surv_fam.reindex(order)
        fig = go.Figure(go.Bar(
            x=surv_fam.index,
            y=surv_fam.values,
            marker_color=[COLORS['warning'], COLORS['success'], COLORS['danger']],
            text=[f'{v:.1f}%' for v in surv_fam.values],
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       yaxis_title='Survival Rate (%)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><div class="card-header">2D Survival Matrix: Class vs Gender</div>', unsafe_allow_html=True)
    pivot = df.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean') * 100
    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=['Female', 'Male'],
        y=['1st Class', '2nd Class', '3rd Class'],
        colorscale=[[0, '#f8f9fa'], [1, '#2ec4b6']],
        text=[[f'{v:.1f}%' for v in row] for row in pivot.values],
        texttemplate='%{text}',
        textfont=dict(size=14)
    ))
    fig.update_layout(template=CHART_TEMPLATE, height=350, margin=dict(t=30))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Demographics":
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><div class="card-header">Age Distribution by Survival</div>', unsafe_allow_html=True)
        colors = {0: COLORS['danger'], 1: COLORS['success']}
        fig = go.Figure()
        for survived in [0, 1]:
            subset = df[df['Survived'] == survived]['Age']
            fig.add_trace(go.Histogram(
                x=subset,
                name='Survived' if survived else 'Did Not Survive',
                marker_color=colors[survived],
                opacity=0.7,
                nbinsx=30
            ))
        fig.update_layout(template=CHART_TEMPLATE, height=400, barmode='overlay',
                       xaxis_title='Age (Years)', yaxis_title='Count', legend=dict(orientation='h'))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card"><div class="card-header">Family Size Distribution</div>', unsafe_allow_html=True)
        fam = df['FamilySize'].value_counts().sort_index()
        fig = go.Figure(go.Bar(
            x=fam.index,
            y=fam.values,
            marker_color=COLORS['secondary'],
            text=fam.values,
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=400,
                       xaxis_title='Family Size', yaxis_title='Count')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><div class="card-header">Passenger Titles Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        title_counts = df['Title'].value_counts()
        fig = go.Figure(go.Bar(
            x=title_counts.values,
            y=title_counts.index,
            orientation='h',
            marker_color=COLORS['primary'],
            text=title_counts.values,
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       xaxis_title='Count', yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        title_surv = df.groupby('Title')['Survived'].mean() * 100
        title_surv = title_surv.sort_values(ascending=True)
        colors = [COLORS['success'] if v > 50 else COLORS['danger'] for v in title_surv.values]
        fig = go.Figure(go.Bar(
            x=title_surv.values,
            y=title_surv.index,
            orientation='h',
            marker_color=colors,
            text=[f'{v:.0f}%' for v in title_surv.values],
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       xaxis_title='Survival Rate (%)', yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Fare & Economics":
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><div class="card-header">Fare Distribution by Class</div>', unsafe_allow_html=True)
        fig = px.box(df, x='Pclass', y='Fare', color='Pclass',
                    color_discrete_map={1: COLORS['success'], 2: COLORS['warning'], 3: COLORS['danger']})
        fig.update_layout(template=CHART_TEMPLATE, height=400,
                       xaxis_title='Passenger Class', yaxis_title='Fare ($)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card"><div class="card-header">Average Fare by Embarkation Port</div>', unsafe_allow_html=True)
        fare_port = df.groupby('Embarked')['Fare'].mean()
        port_names = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
        fig = go.Figure(go.Bar(
            x=[port_names.get(p, p) for p in fare_port.index],
            y=fare_port.values,
            marker_color=[COLORS['primary'], COLORS['secondary'], COLORS['accent']],
            text=[f'${v:.0f}' for v in fare_port.values],
            textposition='outside'
        ))
        fig.update_layout(template=CHART_TEMPLATE, height=400,
                       xaxis_title='Port', yaxis_title='Average Fare ($)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><div class="card-header">Fare vs Survival Comparison</div>', unsafe_allow_html=True)
    
    fare_surv = df[df['Survived'] == 1]['Fare']
    fare_died = df[df['Survived'] == 0]['Fare']
    
    fig = go.Figure()
    fig.add_trace(go.Violin(y=fare_surv, name='Survived', 
                         marker_color=COLORS['success'], box_visible=True, meanline_visible=True))
    fig.add_trace(go.Violin(y=fare_died, name='Did Not Survive', 
                         marker_color=COLORS['danger'], box_visible=True, meanline_visible=True))
    fig.update_layout(template=CHART_TEMPLATE, height=400,
                    yaxis_title='Fare ($)', legend=dict(orientation='h'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><div class="card-header">Fare Distribution</div>', unsafe_allow_html=True)
        fig = px.histogram(df, x='Fare', nbins=40, color_discrete_sequence=[COLORS['primary']])
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       xaxis_title='Fare ($)', yaxis_title='Count')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card"><div class="card-header">Correlation: Age vs Fare</div>', unsafe_allow_html=True)
        fig = px.scatter(df, x='Age', y='Fare', color='Survived',
                       color_discrete_map={0: COLORS['danger'], 1: COLORS['success']},
                       opacity=0.5)
        fig.update_layout(template=CHART_TEMPLATE, height=350,
                       xaxis_title='Age (Years)', yaxis_title='Fare ($)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px; color: #6c757d; font-size: 12px;">
        <p>📊 Titanic Analytics Dashboard | Built with Streamlit + Plotly | Data: Kaggle Titanic Dataset</p>
    </div>
""", unsafe_allow_html=True)