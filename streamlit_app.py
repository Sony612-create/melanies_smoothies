# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import requests
import pandas

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """)


name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))
#st.dataframe(data=my_dataframe, use_container_width=True)
#st.stop()

pd_df=my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()


ingredients_list = st.multiselect(
    'Choose up to 5 ingredients' 
    , my_dataframe
    , max_selections=5)

if ingredients_list:
   ingredients_string =''
   
   
    Import python packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

df_calculate_hash(df):
   concatenated_values = df.astype(str).values.sum()
   hash_value = hash(concatenated_values)
   return hash_value
   
   
# Write directly to the app
st.title(":cup_with_straw: Pending Smoothie Orders :cup_with_straw:")
st.write("""Orders that need to filled.""")

#Get the active session
session = get_active_session()
my_dataframe = session.table("Smoothies.public.orders").to_pandas()

if not my_dataframe empty:
    editable_df =st.data_editor(my_dataframe)
    submitted = st.button('Submit')
	
	if submitted:
	    try:
		  
		    hash_before_update = calculate_hash(my_dataframe)
			
			for index, row in editable_df.iterrows():
			    order_uid = row['ORDER_UID']
				order_filled =row['ORDER_FILLED']
				
				if pd.isna(order_uid) or pd.isna(order_filled):
				     continue
					 
				if pd.isna(order_uid) or pd.isna(order_filled):
				     continue
                order_filled = 'TRUE' if order_filled else 'FALSE'

                session.sql(f"""
                    UPDATE smoothies.public.orders
                    SET order_filled = {order_filled}
                    WHERE order_uid	= {order_uid}
                """).collect()


            updated_dataframe = session.table("smoothies.public.orders").to_pandas()

            hash_after_update = calculate_hash(updated_dataframe)

            if hash_before_update == hash_after_update:
                st.success("Order(s) Updated!" ,icon="👍")
            else:
                 st.error("Hash values mismatch. Data integrety may have been compromised.")
        except Exception as e:
            st.write(f'Something went wrong: {e}')
    else:
         st.success('There are no pending orders right now',icon="👍")	
