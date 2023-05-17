import module.db_ingestion.insert_queries as queries
import pandas as pd


# function for query generation

# """
# Purpose : it is creating multiple queries for respective db
# input : csv file
# output : sql file having multiple sql queries
# """

def multiQueryGenerator(process_name, path):
    query = ''

    if process_name == 'db_ingestion_config_details':
        # reading data for sf_dq_config_details
        db_ingestion_config_details = pd.read_csv(path)
        for i in range(len(db_ingestion_config_details)):
            db_name = db_ingestion_config_details.loc[i, 'DATABASE_NAME']
            schema_name = db_ingestion_config_details.loc[i, 'SCHEMA_NAME']
            table_name = db_ingestion_config_details.loc[i, 'TABLE_NAME']
            columns_to_select = db_ingestion_config_details.loc[i, 'COLUMNS_TO_SELECT']
            src_path = db_ingestion_config_details.loc[i, 'SRC_PATH']
            raw_bucket_name = db_ingestion_config_details.loc[i, 'RAW_BUCKET_NAME']
            raw_tgt_path = db_ingestion_config_details.loc[i, 'RAW_TGT_PATH']
            curated_bucket_name = db_ingestion_config_details.loc[i, 'CURATED_BUCKET_NAME']
            curated_tgt_path = db_ingestion_config_details.loc[i, 'CURATED_TGT_PATH']
            mode = db_ingestion_config_details.loc[i, 'MODE']
            limitDataCheck = db_ingestion_config_details.loc[i, 'LIMITDATACHECK']
            incr_column_name = db_ingestion_config_details.loc[i, 'INCR_COLUMN_NAME']
            limitDataConstraint = db_ingestion_config_details.loc[i, 'LIMITDATACONSTRAINT']
            incremental_cond_check = db_ingestion_config_details.loc[i, 'INCREMENTAL_COND_CHECK']
            columns_to_select_check = db_ingestion_config_details.loc[i, 'COLUMNS_TO_SELECT_CHECK']
            incr_column_timestamp_format = db_ingestion_config_details.loc[i, 'INCR_COLUMN_TIMESTAMP_FORMAT']
            incr_column_timestamp_cond_check = db_ingestion_config_details.loc[i, 'INCR_COLUMN_TIMESTAMP_COND_CHECK']

            config = queries.db_ingestion_config_details_query.format(db_name=db_name, schema_name=schema_name,
                                                                      table_name=table_name,
                                                                      columns_to_select=columns_to_select,
                                                                      src_path=src_path,
                                                                      raw_bucket_name=raw_bucket_name,
                                                                      raw_tgt_path=raw_tgt_path,
                                                                      curated_bucket_name=curated_bucket_name,
                                                                      curated_tgt_path=curated_tgt_path,
                                                                      mode=mode, limitDataCheck=limitDataCheck,
                                                                      incr_column_name=incr_column_name,
                                                                      limitDataConstraint=limitDataConstraint,
                                                                      incremental_cond_check=incremental_cond_check,
                                                                      columns_to_select_check=columns_to_select_check,
                                                                      incr_column_timestamp_format=incr_column_timestamp_format,
                                                                      incr_column_timestamp_cond_check=incr_column_timestamp_cond_check)

            query = query + config + '\n'

    elif process_name == 'sfload_config_details':
        # reading data for sf_load_config_details
        sf_load_config_details = pd.read_csv(path)
        for i in range(len(sf_load_config_details)):
            db_name = sf_load_config_details.loc[i, 'DATABASE_NAME']
            schema_name = sf_load_config_details.loc[i, 'SCHEMA_NAME']
            table_name = sf_load_config_details.loc[i, 'TABLE_NAME']
            s3_path = sf_load_config_details.loc[i, 'FILE_PREFIX_PATH']
            ext_stage = sf_load_config_details.loc[i, 'SF_EXT_STAGE']
            load_type = sf_load_config_details.loc[i, 'LOAD_TYPE']
            truncate_load = sf_load_config_details.loc[i, 'TRUNCATE_LOAD']
            purge_file = sf_load_config_details.loc[i, 'PURGE_FILES']
            action_on_error = sf_load_config_details.loc[i, 'ACTION_ON_ERROR']

            config = queries.sfload_config_details_query.format(db_name=db_name, schema_name=schema_name,
                                                                table_name=table_name, s3_path=s3_path,
                                                                ext_stage=ext_stage, load_type=load_type,
                                                                truncate_load=truncate_load, purge_file=purge_file,
                                                                action_on_error=action_on_error)

            query = query + config + '\n'

    elif process_name == 'sf_load_stg_config_details':
        # reading data for db_ingestion_config_details
        sf_load_stg_config = pd.read_csv(path)
        for i in range(len(sf_load_stg_config)):
            source_table_schema = sf_load_stg_config.loc[i, 'SOURCE_TABLE_SCHEMA']
            target_table_schema = sf_load_stg_config.loc[i, 'TARGET_TABLE_SCHEMA']
            source_table_name = sf_load_stg_config.loc[i, 'SOURCE_TABLE_NAME']
            target_table_name = sf_load_stg_config.loc[i, 'TARGET_TABLE_NAME']
            source_table_database = sf_load_stg_config.loc[i, 'SOURCE_TABLE_DATABASE']
            target_table_database = sf_load_stg_config.loc[i, 'TARGET_TABLE_DATABASE']
            block_number = sf_load_stg_config.loc[i, 'BLOCK_NUMBER']
            target_schema = sf_load_stg_config.loc[i, 'TARGET_SCHEMA']
            target_table = sf_load_stg_config.loc[i, 'TARGET_TABLE']
            target_database = sf_load_stg_config.loc[i, 'TARGET_DATABASE']

            config = queries.sf_load_stg_config_query.format(source_table_schema=source_table_schema,
                                                             target_table_schema=target_table_schema,
                                                             source_table_name=source_table_name,
                                                             target_table_name=target_table_name,
                                                             source_table_database=source_table_database,
                                                             target_table_database=target_table_database,
                                                             block_number=block_number,
                                                             target_schema=target_schema, target_table=target_table,
                                                             target_database=target_database)

            query = query + config + '\n'

    elif process_name == 'sf_load_curated_config':
        # reading data for db_ingestion_config_details
        sf_load_curated_config = pd.read_csv(path)
        for i in range(len(sf_load_curated_config)):
            source_table_schema = sf_load_curated_config.loc[i, 'SOURCE_TABLE_SCHEMA']
            target_table_schema = sf_load_curated_config.loc[i, 'TARGET_TABLE_SCHEMA']
            source_table_database = sf_load_curated_config.loc[i, 'SOURCE_TABLE_DATABASE']
            target_table_database = sf_load_curated_config.loc[i, 'TARGET_TABLE_DATABASE']
            source_table_name = sf_load_curated_config.loc[i, 'SOURCE_TABLE_NAME']
            target_table_name = sf_load_curated_config.loc[i, 'TARGET_TABLE_NAME']
            dml_type = sf_load_curated_config.loc[i, 'DML_TYPE']
            block_number = sf_load_curated_config.loc[i, 'BLOCK_NUMBER']
            target_schema = sf_load_curated_config.loc[i, 'TARGET_SCHEMA']
            target_table = sf_load_curated_config.loc[i, 'TARGET_TABLE']
            target_database = sf_load_curated_config.loc[i, 'TARGET_DATABASE']

            config = queries.sf_load_curated_config_query.format(source_table_schema=source_table_schema,
                                                                 target_table_schema=target_table_schema,
                                                                 source_table_database=source_table_database,
                                                                 target_table_database=target_table_database,
                                                                 source_table_name=source_table_name,
                                                                 target_table_name=target_table_name,
                                                                 dml_type=dml_type, block_number=block_number,
                                                                 target_schema=target_schema, target_table=target_table,
                                                                 target_database=target_database)
            query = query + config + '\n'

    elif process_name == 'incremental_config_details':
        # reading data for db_ingestion_config_details
        incremental_config_details = pd.read_csv(path)
        for i in range(len(incremental_config_details)):
            db_name = incremental_config_details.loc[i, 'DATABASE_NAME']
            schema_name = incremental_config_details.loc[i, 'SCHEMA_NAME']
            table_name = incremental_config_details.loc[i, 'TABLE_NAME']
            value = incremental_config_details.loc[i, 'VALUE']
            column_name = incremental_config_details.loc[i, 'COLUMN_NAME']
            operator = incremental_config_details.loc[i, 'OPERATOR']

            config = queries.incremental_config_details_query.format(db_name=db_name, schema_name=schema_name,
                                                                     table_name=table_name, value=value,
                                                                     column_name=column_name,
                                                                     operator=operator)
            query = query + config + '\n'

    elif process_name == 'sf_load_block_driver_details':
        # reading data for sf_dq_block_driver
        sf_load_block_driver_details = pd.read_csv(path)
        for i in range(len(sf_load_block_driver_details)):
            sf_db_master = sf_load_block_driver_details.loc[i, 'SNOWFLAKE_DATABASE_MASTER']
            sf_schema_master = sf_load_block_driver_details.loc[i, 'SNOWFLAKE_SCHEMA_MASTER']
            table_master = sf_load_block_driver_details.loc[i, 'TABLE_MASTER']
            block_number = sf_load_block_driver_details.loc[i, 'BLOCK_NUMBER']
            config = queries.sf_load_block_driver_details.format(sf_db_master=sf_db_master,
                                                                 sf_schema_master=sf_schema_master,
                                                                 table_master=table_master, block_number=block_number)

        query = query + config + '\n'


    elif process_name == 'dbingestion_block_driver_details':
        # reading data for db_ingestion_block_driver_details
        dbingestion_block_driver_details = pd.read_csv(path)
        for i in range(len(dbingestion_block_driver_details)):
            sf_db_master = dbingestion_block_driver_details.loc[i, 'SNOWFLAKE_DATABASE_MASTER']
            sf_schema_master = dbingestion_block_driver_details.loc[i, 'SNOWFLAKE_SCHEMA_MASTER']
            table_master = dbingestion_block_driver_details.loc[i, 'TABLE_MASTER']
            block_number = dbingestion_block_driver_details.loc[i, 'BLOCK_NUMBER']

            config = queries.dbingestion_block_driver_details_query.format(sf_db_master=sf_db_master,
                                                                           sf_schema_master=sf_schema_master,
                                                                           table_master=table_master,
                                                                           block_number=block_number)
            query = query + config + '\n'


    elif process_name == 'incremental_tables_list':
        # reading data for sf_dq_block_driver
        incremental_tables_list = pd.read_csv(path)
        for i in range(len(incremental_tables_list)):
            database_name = incremental_tables_list.loc[i, 'DATABASE_NAME']
            schema_name = incremental_tables_list.loc[i, 'SCHEMA_NAME']
            table_name = incremental_tables_list.loc[i, 'TABLE_NAME']
            status = incremental_tables_list.loc[i, 'STATUS']
            config = queries.incremental_table_list_query.format(database_name=database_name.upper(),
                                                                 schema_name=schema_name.upper(),
                                                                 table_name=table_name.upper(), status=status)

            query = query + config + '\n'

    else:
        pass

    return query
