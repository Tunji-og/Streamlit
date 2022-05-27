import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import altair as alt

print("Ready")

# get dataset


# display the result using streamlit


with st.container():
    st.title("Nigerian Foods Prices App")
    st.write("""
        ##### This App Contains a dataset of the costs of nigerian foods from 2002 to 2021
    """)
    def get_data():
        url = './datasets/nigeria_food_prices.csv'
        df = pd.read_csv(url)
        cols_to_drop = ['adm0_id', 'adm1_id', 'mkt_id','cm_id', 'cur_id','pt_id','um_id', 'mp_commoditysource']
        df = df.drop(columns = cols_to_drop)
        new_names = {
            'adm0_name': 'Country',
            'adm1_name':"State",
            'mkt_name': "Market",
            'cm_name':'Produce', 
            'cur_name':'Currency',
            'pt_name':'Market_Type',
            'um_name':'Quantity',
            'mp_month':'Month',
            'mp_year':'Year',
            'mp_price':'Prices'
        }
        df =df.rename(columns=new_names)
        df = df.drop(columns=df.columns[0])
        return df
    # display the result using python
    df = get_data()
with st.container():
        try:
            st.sidebar.header("Controls")
            df = get_data()
            states = st.sidebar.multiselect("Choose State",df.State.unique())
            product = st.sidebar.selectbox("Choose Product",df.Produce.unique())
            if not states:
                st.sidebar.error("Please select at least one State")
            else:
                for i, indx in enumerate(states):
                    data = df[df.State == states[i]]
                    st.write("## Prices of goods in",states[i])
                    st.write(data.head(60))
                    pvt = pd.pivot_table(data,index=["State","Market","Produce","Year"],values=['Prices'],aggfunc= 'mean')
                    pvt_df = pvt.reset_index()
                    #selected state
                    selected_state = states[i]
                    pvt_df = pvt_df[pvt_df['State'] == selected_state]
                    #selected state
                    selected_product = product
                    pvt_df = pvt_df[pvt_df['Produce'] == selected_product]
                    
                    # line chart
                    
                    chart = alt.Chart(pvt_df).mark_line().encode(x='Year',y='Prices',tooltip =['Market','Prices']).interactive()
                    st.write(f"### Price Chart {selected_product} in {selected_state}")
                    st.altair_chart(chart, use_container_width= True)
                    # Area chart
                    chart = alt.Chart(pvt_df).mark_area().encode(x='Year',y='Prices',tooltip =['Market','Prices']).interactive()
                    st.write(f"### Price Chart {selected_product} in {selected_state}")
                    st.altair_chart(chart, use_container_width= True)
                    #area chart in market
                    chart = alt.Chart(pvt_df).mark_area().encode(x='Year',y='Prices',color ='Market',tooltip =['Market','Prices']).interactive()
                    st.write(f"### Price Chart {selected_product} in {selected_state}")
                    st.altair_chart(chart, use_container_width= True)
                    
                    
                    st.write("---")
        except RuntimeError as e:
            st.error(e.reason)
