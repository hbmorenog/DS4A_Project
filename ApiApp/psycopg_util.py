# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:29:54 2021

@author: dusty
"""
import psycopg2
import sys
from psycopg2 import __version__ as psycopg2_version
from psycopg2 import connect
from psycopg2 import OperationalError, errorcodes, errors
import datetime
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
            
    def select_demanda_energia(self,date):
        try:
            query='''select de."Fecha", de."DemandaEnergiakwh",de."Generacionkwh" from public."Demanda_energia" de
                    where de."Fecha">to_date(%s, 'dd-mm-yyyy')
            '''
            params=(date,)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=dict()
            for row in raw:
                data[row[0].strftime('%d/%m/%Y')]={'Demanda':row[1],'Generacion':row[2]}
            return data
        except Exception as e:
            print("Error while querying to Postgres")
            self.print_pyscopg_exception(e)
        finally:
            if self.connection is not None:
                cur.close()