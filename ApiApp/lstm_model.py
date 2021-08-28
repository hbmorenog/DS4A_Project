# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:23:03 2021

@author: dusty
"""
import pandas as pd
import keras as K
import numpy as np

class Lstm_model:
    
    def normalize_precio(self,x):
        '''
        Normalize the energy price
        '''
        meannB=134.33447502138475
        stdnB=135.98355133235674
        return (x-meannB)/stdnB
    
    def normalize_demanda(self,x):
        '''
        Normalize the energy demand
        '''
        meannA=155247922.8975228
        stdnA=27728694.604139626
        return (x-meannA)/stdnA
    
    def desnormalize_precio(self,x):
        '''
        Normalize the energy price
        '''
        meannB=134.33447502138475
        stdnB=135.98355133235674
    
        return (x*stdnB+meannB)

    def smapeLoss(self,true,predicted):
        '''
        loss fuction to be implemented in the neural network
        '''
        epsilon = 0.1
        summ = K.maximum(K.abs(true) + K.abs(predicted) + epsilon, epsilon)
        smape = K.abs(predicted - true) / summ * 2.0
        return smape
    
    def load_model(self):
        new_model = K.models.load_model('LSTM-DNNS_FINAL.h5', custom_objects={'smapeLoss': self.smapeLoss})
        return new_model
    
    def evolve_n_days(self,n,naux,model,X1,X2):
        '''
        evolve the system n days 
        '''
        n_features=1
        dnn_numinputs=14 #n_steps
        dnn_predictions=X2
        for k in range(n):
            aux1=X1[naux+k].reshape(1,n_features)
        
            aux2 = np.reshape(dnn_predictions[-dnn_numinputs:],(1,1,dnn_numinputs))
            new_pred = model.predict([aux1,aux2], verbose=0).flatten()
            new_pred=self.normalize_precio(new_pred)
            dnn_predictions = np.concatenate((dnn_predictions, new_pred.reshape(1,1)))
        return dnn_predictions
    #make demand prediction
    
    def demand_pred(self):
        #defines the previously calculated weekly and anual trends
        week=[1.03915625, 1.04375992, 1.04160141, 1.04018262, 0.97917122, 0.86171919, 0.99440939]
    
        season=[-4.66040387e-01, -4.18483105e-01, -3.61202154e-01, -3.09712463e-01,
           -2.81583974e-01, -2.63323228e-01, -2.36232538e-01, -2.01606735e-01,
           -1.61702652e-01, -1.20530080e-01, -8.53505560e-02, -5.53229846e-02,
           -2.72730843e-02, -9.19098643e-03,  1.58026088e-03,  1.18734305e-02,
            1.97216731e-02,  2.72798892e-02,  3.34327271e-02,  3.98299135e-02,
            4.75680675e-02,  5.35027837e-02,  5.99541343e-02,  6.53432253e-02,
            6.98390950e-02,  7.35354213e-02,  7.46737384e-02,  7.66518302e-02,
            7.79101998e-02,  7.90722637e-02,  7.97984386e-02,  8.19201600e-02,
            8.71533009e-02,  9.28646117e-02,  9.54870737e-02,  9.74510215e-02,
            9.75221965e-02,  9.94786240e-02,  1.00884011e-01,  1.02207159e-01,
            1.03486314e-01,  1.06115224e-01,  1.07620733e-01,  1.07546185e-01,
            1.07687093e-01,  1.09118599e-01,  1.09526386e-01,  1.10114530e-01,
            1.07945607e-01,  1.06351265e-01,  1.03294721e-01,  9.88436887e-02,
            9.38577000e-02,  8.75657795e-02,  7.93161103e-02,  7.34906595e-02,
            6.75337597e-02,  6.60005991e-02,  6.69732733e-02,  6.80890721e-02,
            7.26159763e-02,  8.00061985e-02,  8.48235279e-02,  8.94494708e-02,
            9.32605987e-02,  9.50510463e-02,  9.42750712e-02,  9.20524992e-02,
            8.96585794e-02,  8.30414291e-02,  7.52764854e-02,  6.46628074e-02,
            4.06242759e-02,  7.78326230e-03, -2.20095955e-02, -5.61986332e-02,
           -8.54150836e-02, -9.98023651e-02, -1.25210240e-01, -1.36301876e-01,
           -1.21336244e-01, -1.08874483e-01, -9.63370306e-02, -8.72485747e-02,
           -9.64813424e-02, -9.26395143e-02, -9.07873176e-02, -1.07905984e-01,
           -1.18469909e-01, -1.22410297e-01, -1.23495066e-01, -1.14110109e-01,
           -1.05838472e-01, -1.02014735e-01, -8.98525605e-02, -8.86079803e-02,
           -9.32319278e-02, -8.73591951e-02, -9.01158115e-02, -9.81073193e-02,
           -8.99966043e-02, -8.69939647e-02, -8.56176327e-02, -8.44583486e-02,
           -9.31770523e-02, -9.39817005e-02, -7.94463565e-02, -7.05122533e-02,
           -5.87930793e-02, -4.12708150e-02, -2.03268564e-02,  3.08272003e-03,
            9.05550525e-03,  5.47450265e-04, -1.59529278e-02, -4.99633351e-02,
           -8.09142947e-02, -9.41187559e-02, -1.04521030e-01, -9.13922603e-02,
           -7.33029913e-02, -5.79615359e-02, -2.06300864e-02,  9.81133511e-03,
            1.01574963e-02,  1.77385185e-02,  1.91300748e-02,  1.68812555e-02,
            2.64141192e-02,  1.97521892e-02,  1.57303597e-02,  2.91071298e-02,
            2.97972457e-02,  2.38315438e-02,  2.44780674e-02,  1.39370184e-02,
            1.48303667e-02,  2.04878960e-02,  1.47076896e-02,  7.93626587e-03,
            1.30780326e-02,  9.84268557e-04, -2.58467669e-03, -5.64257353e-03,
           -2.54832905e-02, -4.10660470e-02, -4.92761780e-02, -6.63812555e-02,
           -6.64836405e-02, -7.11168243e-02, -7.60673723e-02, -6.05481608e-02,
           -4.97007844e-02, -4.32186741e-02, -3.48246826e-02, -2.84495560e-02,
           -2.01400960e-02, -2.10829747e-02, -2.52436244e-02, -2.53719165e-02,
           -3.15462711e-02, -3.27371066e-02, -3.53657291e-02, -3.33940491e-02,
           -2.43566208e-02, -2.72892111e-02, -2.73077525e-02, -1.87763696e-02,
           -1.61749544e-02, -1.83316729e-02, -2.37131174e-02, -3.06412608e-02,
           -3.62388431e-02, -4.52504338e-02, -6.35830583e-02, -7.98126635e-02,
           -9.71819272e-02, -1.18512086e-01, -1.34794527e-01, -1.42182866e-01,
           -1.35586260e-01, -1.14326776e-01, -9.01235279e-02, -6.60064238e-02,
           -3.37849196e-02, -5.17669538e-03,  1.98117108e-02,  3.35204686e-02,
            3.69774829e-02,  3.87518728e-02,  3.67654459e-02,  3.28012856e-02,
            1.83766066e-02, -4.90388075e-03, -2.32498360e-02, -3.64235229e-02,
           -5.45084739e-02, -5.10112604e-02, -4.15386049e-02, -2.06903467e-02,
            8.40689946e-03,  3.20795170e-02,  5.00776606e-02,  7.14654120e-02,
            7.24908270e-02,  6.69711467e-02,  6.07594686e-02,  5.34257464e-02,
            4.95470718e-02,  4.81108763e-02,  3.21922653e-02,  1.92033952e-02,
            7.79686853e-03, -8.13344609e-03, -1.74588151e-02, -1.20133442e-02,
           -5.04755998e-03,  1.70683880e-02,  3.86953996e-02,  5.23130035e-02,
            6.46929504e-02,  7.07150818e-02,  5.12393360e-02,  2.85620995e-02,
            9.67383020e-03, -3.70534436e-03, -1.07452261e-02, -2.97622198e-03,
            7.72303057e-03,  3.12326438e-02,  5.52253652e-02,  7.56639940e-02,
            8.65128822e-02,  9.76569152e-02,  1.01395314e-01,  1.04161558e-01,
            1.03189599e-01,  1.01898114e-01,  9.91435115e-02,  9.83400862e-02,
            9.64658328e-02,  9.62965149e-02,  1.00767530e-01,  1.01762512e-01,
            1.02692315e-01,  1.04522428e-01,  1.07954045e-01,  1.15939840e-01,
            1.16254302e-01,  1.12988594e-01,  1.11936271e-01,  1.11201544e-01,
            1.08314145e-01,  1.02442698e-01,  9.19751547e-02,  8.56898923e-02,
            7.99127628e-02,  7.65458131e-02,  7.33551514e-02,  7.13744499e-02,
            6.91091758e-02,  7.33303256e-02,  7.85971755e-02,  8.06895155e-02,
            8.16826039e-02,  8.20304230e-02,  8.48329530e-02,  8.75317610e-02,
            8.27257796e-02,  7.45642636e-02,  6.71651060e-02,  6.10621923e-02,
            5.81717654e-02,  5.49344842e-02,  5.24825803e-02,  5.42621416e-02,
            5.85321094e-02,  5.68050628e-02,  4.61924399e-02,  2.55094770e-02,
            5.92572413e-05, -1.87617806e-02, -4.42674747e-02, -6.80862352e-02,
           -8.18914432e-02, -8.31450379e-02, -6.92683480e-02, -4.86466110e-02,
           -3.09741992e-02, -9.55540670e-03,  8.48787466e-03,  1.97236561e-02,
            2.59390398e-02,  2.59061271e-02,  2.41762324e-02,  2.45045246e-02,
            2.51893105e-02,  1.40485804e-02,  3.19834386e-03, -8.38308321e-03,
           -2.46221437e-02, -4.18775342e-02, -5.54185138e-02, -7.27647886e-02,
           -7.10118939e-02, -6.03844531e-02, -5.17473750e-02, -3.09617697e-02,
           -1.48617367e-02, -7.49211371e-03, -2.46707930e-03, -3.20623034e-03,
           -9.28663511e-03, -9.09826596e-03, -1.81914046e-02, -1.41997403e-02,
           -6.66706059e-04,  2.07443142e-02,  4.30338890e-02,  6.51050145e-02,
            8.25275851e-02,  1.01851525e-01,  1.14594615e-01,  1.20436930e-01,
            1.26849385e-01,  1.33342452e-01,  1.36960757e-01,  1.40961716e-01,
            1.41363410e-01,  1.41915216e-01,  1.42682874e-01,  1.47528076e-01,
            1.52188750e-01,  1.47722714e-01,  1.38179183e-01,  1.24383319e-01,
            1.15665788e-01,  1.10355206e-01,  1.14206289e-01,  1.19442448e-01,
            1.34944866e-01,  1.50099135e-01,  1.67054911e-01,  1.76778212e-01,
            1.82572045e-01,  1.72955143e-01,  1.60582142e-01,  1.47726659e-01,
            1.37811515e-01,  1.21333623e-01,  6.98973326e-02,  5.09901832e-03,
           -7.03739271e-02, -1.56015376e-01, -2.27255321e-01, -2.67827932e-01,
           -3.01524289e-01, -3.29199868e-01, -3.58666264e-01, -3.95047908e-01,
           -4.28309649e-01, -4.63123748e-01, -4.97093367e-01, -5.12664359e-01,
           -4.97765774e-01]
        #calculates the weekly trend for dates greater than 2021-01-01 and save it in newweek
        naux=7668%len(week)
        auxweek=week[naux:]
        auxweek.extend(week[:naux])
    
    
        newweek=pd.DataFrame(auxweek)
        #newweek=newweek.set_index('Fecha')
        #newweek['week_pattern']=week
        #pd.concat([newweek, week[['seasonal']]])
        for i in range(729):
        
            newweek=newweek.append(auxweek,ignore_index=True)
        #auxseason['Fecha'][362].dayofyear#['Fecha'][4]
        idx = pd.date_range("2021-01-01", periods=len(newweek))
        idx
        newweek.index=idx
       
        #calculates the annual trend for dates greater than 2021-01-01 and save it in newseason
        naux=7668%len(season)
    
        auxseason=season[naux:]
        auxseason.extend(season[:naux])
    
        newseason=pd.DataFrame(season)
    
        #pd.concat([newweek, week[['seasonal']]])
        for i in range(13):
        
            newseason=newseason.append(auxseason,ignore_index=True)
        idx = pd.date_range("2021-01-01", periods=len(newseason))
        idx
        newseason.index=idx
        
        
        #calculates the overall trend
        pendiente=0.00141927/5#0.0012197#0.00044111#0.0012197# 0.00335521
        intercepto=6.270164229068847#12.6040394969468#4.376574820564484#12.6040394969468# 5.746820921209072
        trend=pd.DataFrame()
        x=np.array(range(5110)).reshape(-1, 1)
        y_pred = intercepto + np.sum(pendiente * x, axis=1)
        trend['trend']=y_pred
        trend
        idx = pd.date_range("2021-01-01", periods=len(trend))
        idx
        trend.index=idx
        
        
        #add everything to get the prediction
        indexs=newseason.index.isin(trend.index)
        indexw=newweek.index.isin(trend.index)
        caldemand=(newseason[0][indexs]+trend['trend'])*newweek[0][indexw]-2*2.46870088
        return caldemand
    
    
    def organize_input(self,X1,X2):
        '''
        normalize data and add energy demand predictions
        '''
        #******X1*******
        #energy demand from the current date to end of database if initial date<2021-08-25
        #X1=df['DemandaEnergiakwh'].iloc[index_database:]
        
        X1=self.normalize_demanda(X1)
        #calculates future demand and append it to X1
        future_demand=self.demand_pred()
        X1=X1.append(future_demand,ignore_index=True)
        X1=np.asarray(X1)#.reshape(X1.shape[0],1)
        X1=X1.reshape(X1.shape[0],1)
    
    
    
        #******X2*******
        #energy price from the  previous 14 days to initial date 
        #X2=df['precio_bolsa_nacional_ponderado'].iloc[index_database-15:index_database-1]
    
        #X2 SHOULD BE THE normalized 14 days last prices
        X2=self.normalize_precio(X2)
        X2=np.asarray(X2)
        X2=X2.reshape(X2.shape[0],1)
        #X2.shape#[0]
        return X1,X2
    
    
    
    def make_prediction(self,X1,X2,initial_date,final_date):
        
        n=pd.datetime.strptime(final_date,'%Y-%m-%d')-pd.datetime.strptime(initial_date,'%Y-%m-%d')
        n=n.days
        current_date=pd.to_datetime(initial_date,format='%Y-%m-%d')
    
        X1,X2=self.organize_input(X1,X2)
        #loads the trained model
        new_model=self.load_model()
        naux=0
        predictions=self.evolve_n_days(n,naux,new_model,X1,X2)
        #transform to correct units
        predictions=self.desnormalize_precio(predictions)
        predictions
    
        dpred=pd.DataFrame()
        dpred['predicted']=pd.Series(predictions[14:].reshape(len(predictions[14:]),))
        idx = pd.date_range(current_date, periods=len(dpred))
        dpred.index=idx
        return dpred
