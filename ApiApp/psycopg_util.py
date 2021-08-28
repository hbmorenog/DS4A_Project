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
                    where de."Fecha"<=to_date(%s, 'yyyy-mm-dd')
                    order by de."Fecha" desc
                    limit %s
            '''
            params=(date,chunk_size*14)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=pd.DataFrame()
            for row in raw:
                serie=pd.Series({'Demanda':row[1],'Generacion':row[2]},name=row[0].strftime('%Y-%m-%d'))
                data=data.append(serie)
            means=pd.DataFrame()
            for start in range(0, data.shape[0], chunk_size):
                df_subset = data.iloc[start:start + chunk_size]
                mean=df_subset.mean()
                mean.name=data.index.values[start]
                means=means.append(mean)
            means=means.reindex(index=means.index[::-1])
            return means
        except Exception as e:
            print("Error while querying to Postgres")
            self.print_pyscopg_exception(e)
        finally:
            if self.connection is not None:
                cur.close()
    def select_demanda_energia_forecast(self,date,chunk_size):
        try:
            query='''select pbn."fecha", pbn."promedio" from public."precio_bolsa_nacional" pbn
                    where pbn."fecha"<=to_date(%s, 'yyyy-mm-dd')
                    order by pbn."fecha" desc
                    limit %s
            '''
            params=(date,chunk_size*28)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=pd.DataFrame()
            for row in raw:
                serie=pd.Series({'promedio':row[1]},name=row[0].strftime('%Y-%m-%d'))
                data=data.append(serie)
            means=pd.DataFrame()
            for start in range(0, data.shape[0], chunk_size):
                df_subset = data.iloc[start:start + chunk_size]
                mean=df_subset.mean()
                mean.name=data.index.values[start]
                means=means.append(mean)
            means=means.reindex(index=means.index[::-1])
            return means
        except Exception as e:
            print("Error while querying to Postgres")
            self.print_pyscopg_exception(e)
        finally:
            if self.connection is not None:
                cur.close()
    def select_informacion(self,date,chunk_size):
        try:
            #precio_medio
            query='''select  pbn."promedio" from public."precio_bolsa_nacional" pbn
                    where de."Fecha"<=to_date(%s, 'yyyy-mm-dd')
                    order by de."Fecha" desc
                    limit %s
            '''
            params=(date,chunk_size)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=list()
            for row in raw:
                data.append(row[0])
            precio_medio=data.mean()
            #nivel_reservas_medio
            query='''select  rd."vol" from public."reserva_diaria" rd
                    where rd."fecha"<=to_date(%s, 'yyyy-mm-dd')
                    order by de."fecha" desc
                    limit %s
            '''
            params=(date,chunk_size)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=list()
            for row in raw:
                data.append(row[0])
            nivel_reservas_medio=data.mean()            
            
            #enso_medio
            query='''select  enso."prom_anual" from public."enso" enso
                    where enso."year"=%s
            '''
            params=(date.split('-')[0])
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            enso_medio=row[0]           
            
            #tipo_generacion_medio
            query='''select g."tipo_generacion",g."fecha", avg(h0+h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20+h21+h22+h23) from public."generacion" g
                    group by g."fecha",tipo_generacion
                    where g."fecha"<=to_date(%s, 'yyyy-mm-dd')
                    order by g."Fecha" desc
                    limit %s
            
            '''
            params=(date,chunk_size)
            cur = self.connection.cursor()
            cur.execute(query,params)
            raw=cur.fetchall()
            data=pd.DataFrame()
            for row in raw:
                serie=pd.Series({"cantidad":row[2]},name=row[0])
                data=data.append(serie)
            tipo_generacion_medio=data.means()
            return {"mean_price":precio_medio,"enso":enso_medio,"reserves_level":nivel_reservas_medio,"contribution":tipo_generacion_medio}
        except Exception as e:
            print("Error while querying to Postgres")
            self.print_pyscopg_exception(e)
        finally:
            if self.connection is not None:
                cur.close()