# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:29:54 2021

@author: dusty
"""
import psycopg2
import sys
import pandas as pd
class Pyscopg_util():
    def __init__(self):
        self.connection=None
        self.endpoint='ds4a-demo-instance.cganmkarjo24.us-east-2.rds.amazonaws.com'
        self.database='energia'
        self.user='postgres'
        self.password='Laclave.'
        
    def print_pyscopg_exception(self,err):
            # get details about the exception
            err_type, err_obj, traceback = sys.exc_info()
        
            # get the line number when exception occured
            line_num = traceback.tb_lineno
            # print the connect() error
            print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
            print ("psycopg2 traceback:", traceback, "-- type:", err_type)
        
            # psycopg2 extensions.Diagnostics object attribute
            print ("\nextensions.Diagnostics:", err.diag)
        
            # print the pgcode and pgerror exceptions
            print ("pgerror:", err.pgerror)
            print ("pgcode:", err.pgcode, "\n")
    def connect_to_db(self):    
        try:
            conn = psycopg2.connect(host=self.endpoint,
                                 database=self.database,
                                 user=self.user,
                                 password=self.password)
    
            if conn is not None:
                # create a cursor
                cur = conn.cursor()
                # execute a statement
                cur.execute('SELECT current_database()')
                # display the PostgreSQL database server version
                db = cur.fetchone()
                print('Connected to ',db)   
                self.connection= conn
        except Exception as e:
            print("Error while connecting to Postgres")
            self.print_pyscopg_exception(e)
        finally:
            if self.connection is not None:
                cur.close()
                
    def close_connection(self):
        try:
            self.connection.close()
            print("Conection closed")
        except Exception as e:
            print("Exception while closing connection: ")
            self.print_pyscopg_exception(e)
            
    def select_demanda_energia(self,date,chunk_size):
        try:
            query='''select de."Fecha", de."DemandaEnergiakwh",de."Generacionkwh" from public."Demanda_energia" de
                    where de."Fecha"<=to_date(%s, 'dd-mm-yyyy')
                    order by de."Fecha" desc
                    limit %s
            '''
            params=(date,chunk_size*12)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=pd.DataFrame()
            for row in raw:
                serie=pd.Series({'Demanda':row[1],'Generacion':row[2]},name=row[0].strftime('%d/%m/%Y'))
                data=data.append(serie)
            means=pd.DataFrame()
            for start in range(0, data.shape[0], chunk_size):
                df_subset = data.iloc[start:start + chunk_size]
                mean=df_subset.mean()
                mean.name=data.index.values[start]
                means=means.append(mean)
            return means
        except Exception as e:
            print("Error while querying to Postgres")
            self.print_pyscopg_exception(e)
        finally:
            if self.connection is not None:
                cur.close()