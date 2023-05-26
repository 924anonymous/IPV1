# """
# Purpose : input parameters for queryGenerator function
# """

db_ingestion_config_details_query = ''' 
/************************ DBINGESTION_CONFIG_DETAILS ************************/
insert into config.dbingestion_config_details (
 DATABASE_NAME,
 SCHEMA_NAME,
 TABLE_NAME,
 CONFIGURATIONS,
 CREATED_AT,
 STATUS,
 CREATED_USER,
 CONNECTION_ID) VALUES('{db_name}',
'{schema_name}',
'{table_name}',
'{{\"database_name\": \"{db_name}\", 
\"schema_name\": \"{schema_name}\",
\"table_name\": \"{table_name}\",
\"columns_to_select\": \"{columns_to_select}\", 
\"src_path\": \"{src_path}\", 
\"raw_bucket_name\": \"{raw_bucket_name}\",
\"raw_tgt_path\": \"{raw_tgt_path}\",
\"curated_bucket_name\": \"{curated_bucket_name}\",  
\"curated_tgt_path\": \"{curated_tgt_path}\", 
\"mode\": \"{mode}\", 
\"header": \"\", 
\"delimiter\": \"\", 
\"hashcheck\": \"no\", 
\"fileFormat\": \"parquet\", 
\"part_files\": \"NA\", 
\"comp_format\": \"\", 
\"target_type\": \"S3\", 
\"col_name_lb_ub\": \"\", 
\"hashcolumnname\": \"\", 
\"limitDataCheck\": \"{limitDataCheck}\",  
\"rds_config_mode\": \"append\", 
\"compressionCheck\": \"no\",
\"eventDtPartition\": {{\"ipColName\": \"\", \"ipDateFormat\": \"\", \"opDateFormat": \"\", \"partitionFlag\": \"no\", \"partColumnName\": \"\"}},
\"incr_column_name\": \"{incr_column_name}\", 
\"query_contraints\": \"\", 
\"curated_prt_check\": \"no\", 
\"processDtPartition\": {{\"timeZone\": \"Asia/Kolkata\", \"dateFormat\": \"yyyyMMdd\", \"partitionFlag\": \"yes\",\"partColumnName\": \"aws_processed_date\"}}, 
\"processed_tgt_path\": \"\", 
\"additionalPartition\": \"\", 
\"limitDataConstraint\": \" {limitDataConstraint} \", 
\"writePartitionCheck\": \"yes\", 
\"loadDateDirPartition\": {{\"partitionFlag\": \"yes\"}}, 
\"processed_bucket_name\": \"\", 
\"incremental_cond_check\": \"{incremental_cond_check}\", 
\"processed_bucket_check\": \"no\", 
\"query_contraints_check\": \"no\", 
\"columns_to_select_check\": \"{columns_to_select_check}\",
\"target_file_prefix_path\": \"\", 
\"incr_column_timestamp_format\": \"{incr_column_timestamp_format}\",
\"incr_column_timestamp_cond_check\": \"{incr_column_timestamp_cond_check}\"}}',
CURRENT_TIMESTAMP,
'active',
CURRENT_USER,
{connection_id});'''

sfload_config_details_query = '''
/************************ SFLOAD_CONFIG_DETAILS ************************/
insert into config.sfload_config_details(
 DATABASE_NAME,
 SCHEMA_NAME,
 TABLE_NAME,
 CONFIG_DTLS,
 STATUS,
 CREATED_AT,
 CREATED_USER) VALUES('{db_name}',
'{schema_name}',
'{table_name}',
'{{\"database_name\": \"{db_name}\",
\"schema_name\": \"{schema_name}\",
\"table_name\": \"{table_name}\",
\"file_prefix_path\": \"{s3_path}\",
\"sf_ext_stage\": \"{ext_stage}\",
\"load_type\": \"{load_type}\",
\"truncate_load\": \"{truncate_load}\",
\"purge_files\": \"{purge_file}\",
\"action_on_error\":\"{action_on_error}\",
\"column_names_caps\": \"no\",
\"file_prefix_name_case\": \"as_is\",
\"_etl_batch_id\": \"yes\",
\"_etl_insert_date_time\": \"yes\",
\"_etl_update_date_time\": \"yes\",
\"force\":\"FALSE\",
\"partition_cols\": [],
\"validate_errors\":\"no\",
\"error_table_name\" : \"\",
\"error_schema_name\" : \"\",
\"offload\":\"no\",
\"stage_name\": \"\",
\"folder_name\" : \"\",
\"query_columns\" : \"\",
\"condition\" : \"\",
\"limit_value\" : \"\"}}',
'active',
CURRENT_TIMESTAMP,
CURRENT_USER);'''

sf_load_stg_config_query = '''
/************************ SF_LOAD_STG_CONFIG_DETAILS ************************/
insert into config.sf_load_stg_config (
CONFIGURATIONS,
BLOCK_NUMBER,
STATUS,
CREATED_AT,
CREATED_BY,
TARGET_SCHEMA,
TARGET_TABLE,
TARGET_DATABASE) VALUES ('{{\"source_table_schema\": \"{source_table_schema}\",
\"target_table_schema\": \"{target_table_schema}\",
\"source_table_name\": \"{source_table_name}\",
\"target_table_name\": \"{target_table_name}\",
\"source_table_database\": \"{source_table_database}\",
\"target_table_database\": \"{target_table_database}\"}}',
'{block_number}',
'active',
CURRENT_TIMESTAMP,
CURRENT_USER,
'{target_schema}',
'{target_table}',
'{target_database}');'''

sf_load_curated_config_query = ''' 
/************************ SF_LOAD_CURATED_CONFIG ************************/
insert into config.sf_load_curated_config(
 CONFIGURATIONS,
 BLOCK_NUMBER,
 STATUS,
 CREATED_AT,
 CREATED_BY,
 TARGET_SCHEMA,
 TARGET_TABLE,
 TARGET_DATABASE) VALUES('{{\"source_table_schema\": \"{source_table_schema}\",
\"target_table_schema\": \"{target_table_schema}\",
\"source_table_database\": \"{source_table_database}\",
\"target_table_database\": \"{target_table_database}\",
\"source_table_name\": \"{source_table_name}\",
\"target_table_name\": \"{target_table_name}\",
\"dml_type\": \"{dml_type}\"}}',
'{block_number}',
'active',
CURRENT_TIMESTAMP,
CURRENT_USER,
'{target_schema}',
'{target_table}',
'{target_database}');'''

incremental_config_details_query = ''' 
/************************ Incremental_Config_Details ************************/
insert into config.incremental_details(
 DATABASE_NAME,
 SCHEMA_NAME,
 TABLE_NAME,
 VALUE,
 COLUMN_NAME,
 OPERATOR,
 STATUS,
 CREATED_AT,
 CREATED_USER) VALUES('{db_name}',
 '{schema_name}',
 '{table_name}', 
 '{value}', 
 '{column_name}',
 '{operator}',
'active',
CURRENT_TIMESTAMP,
CURRENT_USER);'''

sf_load_block_driver_details = '''
 /************************ SF_BLOCK_DRIVER_DETAILS ************************/

INSERT INTO edo_contextdb_snowflake_prod.SF_LOAD_BLOCK_DRIVER_DETAILS (SNOWFLAKE_DATABASE_MASTER,
SNOWFLAKE_SCHEMA_MASTER,
TABLE_MASTER,
 BLOCK_NUMBER,
 CREATE_DATE,
 CREATED_BY) VALUES ('{sf_db_master}',
 '{sf_schema_master}',
 '{table_master}',
 '{block_number}',
 CURRENT_TIMESTAMP,
 CURRENT_USER);'''

dbingestion_block_driver_details_query = '''
 /************************ DBINGESTION_BLOCK_DRIVER_DETAILS_TABLE ************************/

INSERT INTO edo_contextdb_snowflake_prod.DBINGESTION_BLOCK_DRIVER_DETAILS(SNOWFLAKE_DATABASE_MASTER,
 SNOWFLAKE_SCHEMA_MASTER,
 TABLE_MASTER,
 BLOCK_NUMBER,
 CREATE_DATE,
 CREATED_BY) VALUES('{sf_db_master}',
 '{sf_schema_master}',
 '{table_master}',
 '{block_number}',
 CURRENT_TIMESTAMP,
 CURRENT_USER);'''

incremental_table_list_query = '''
INSERT INTO dev_code_repo.COM.INCREMENTAL_TABLES_LIST(
DATABASE_NAME,
SCHEMA_NAME,
TABLE_NAME,
STATUS) VALUES(
'{database_name}',
 '{schema_name}',
 '{table_name}',
 '{status}'); '''

update_incremental_details = '''
update config.incremental_details 
set status='inactive' 
where database_name = '{database_name}'
and schema_name = '{schema_name}'
and table_name = '{table_name}' and status = 'active'; '''

update_dbingestion_config_details = '''
update config.dbingestion_config_details
set status = 'inactive'
where database_name = '{database_name}'
and schema_name = '{schema_name}'
and table_name = '{table_name}' and status = 'active'; '''
