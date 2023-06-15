from datetime import date, datetime
import streamlit as st
import json

layout = {
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
}

log_query = '''
with max_exe_id
as
(
select max(execution_id) as max_id from config.dbingestion_audit_logs
)
select replace(replace(split_part(details,':',1	),'"',''),'{','') as data_layer,replace(replace(split_part(details,':',2),'"',''),'}','') as record_count 
from config.dbingestion_audit_logs where execution_id = (select max_id from max_exe_id)
and replace(replace(split_part(details,':',1	),'"',''),'{','') not in ('Errorneous_Records');
'''

log_query_for_pie_chart = '''
with max_exe_id
as
(
select max(execution_id) as max_id from config.dbingestion_audit_logs
)
select replace(replace(split_part(details,':',1	),'"',''),'{','') as data_layer,replace(replace(split_part(details,':',2),'"',''),'}','') as record_count 
from config.dbingestion_audit_logs where execution_id = (select max_id from max_exe_id) 
and replace(replace(split_part(details,':',1	),'"',''),'{','') in ('Target_Filtered_Records','Errorneous_Records');
'''


def age(born):
    born = datetime.strptime(str(born), "%Y-%m-%d").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def blanklines(n):
    for i in range(n):
        st.write('')


def key_operations(data, operation, key_name, key_value, table_name):
    data = json.loads(str(data))
    if operation.lower() == "add":
        data[key_name] = key_value
    elif operation.lower() == "delete":
        data = {key.replace(table_name + '_', ''): data[key] for key in data if key not in ['updated_at', 'created_at']}
    return json.dumps(data)
