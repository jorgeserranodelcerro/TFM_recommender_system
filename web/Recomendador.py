import pandas as pd
from scipy.spatial import distance


perfiles = pd.read_csv('static/data/uPerfil_Clear.csv')
perfiles.drop('Unnamed: 0',axis=1,inplace=True)
users=perfiles['userID']
perfiles.drop('userID',axis=1,inplace=True)
rating = pd.read_csv('../Data/rating_final.csv')
rInfo=pd.read_csv('static/data/rInfo.csv')
array_norm = perfiles.values



def recomienda_10(_list):
    distancias = []

    for i in range(len(perfiles)):
        distancias.append(10-distance.euclidean(_list, array_norm[i]))
       
    df_dist = pd.DataFrame({'userID':users, 'dist':distancias})
    
    top20Users=df_dist.sort_values('dist', ascending=False).head(10)
    
    ratingtop20=pd.merge(top20Users,rating, how='inner', on='userID')
    
    ratingtop20['rating_final']=2*ratingtop20['dist']*ratingtop20['rating']+ratingtop20['dist']*ratingtop20['food_rating']+ratingtop20['dist']*ratingtop20['service_rating']
    rating_final=ratingtop20[['placeID','rating_final']]
    rTop5=rating_final.sort_values('rating_final', ascending=False).head(5)
    salida=pd.merge(rTop5,rInfo,how='inner',on='placeID')
    return salida[['name','alcohol','smoking_area','price','dress_code','parking_lot']]


def CodeSmoker(TSmoke):
    if TSmoke.upper()=='TRUE':
        return 0
    else:
        return 1
    
def CodeAlcohol(Alcohol):
    if Alcohol.upper()=='ABSTEMIOUS':
        return 1
    else:
        return 0   
    
def CodeDress(Dress):
    if Dress.upper()=='INFORMAL' or Dress.upper()=='?':
        return 0
    elif Dress.upper()=='NO PREFERENCE':
        return 2
    else:
        return 1

def CodeTransport(Transport):
    if Transport.upper()=='CAR OWNER':
        return 0
    else:
        return 1
    
def CodeBudget(Budget):
    if Budget.upper() == 'LOW':
        return 0
    elif Budget.upper() == 'MEDIUM':
        return 1
    elif Budget.upper() == 'HIGH':
        return 2


