class Esrtructura:
    def __init__(self):
        self.dict={}
        
    def pedirDatos(self):
        dict2={}
        listfeatures_seasons=[]
        listepisodes=[]
        dict3={}
        listActors=[]
        cont=0
        bandera=True
        while bandera:
            try:
                serie=input("ingrese la serie de la pelicula")
                self.dict["serie"]=serie
                number_seasons=int(input("ingrese el numero de sesiones"))
                self.dict["number_seasons"]=number_seasons
                original_lenguage= input("ingrese el lengiaje original")
                self.dict["original_lenguage"]=original_lenguage
                season_number=int(input("ingrese el numero de sesiones"))
                dict2["season_number"]=season_number
                season_name=input("ingrese el nombre de sesion")
                dict2["season_name"]=season_name
                premier_date=input("ingrese la fecha de estreno")
                dict2["premier_date"]=premier_date
                num_actors=int(input("ingrese el numero de los actores"))
                for i in range(num_actors):
                    actor=input("ingrese el nombre del actor: "+ i+1)
                    listActors.append(actor)
                dict2["cast"]= listActors
                episode_name=input("ingrese el nombre del episodio")
                dict3["episode_name"]=episode_name
                time_duration=int(input("ingrese el tiempo de duracion de la pelicula"))
                dict3["ime_duration"]=time_duration
                
                listepisodes=[dict3]
                dict2["episodes"]=listepisodes
                listfeatures_seasons=[dict2]
                self.dict["features_seasons"]=listfeatures_seasons
                
               
                
                cont+1
                if cont==3:
                    bandera=False    
            except: 
                print("ingrese un numero")
    def buscar_serie_por_actor(numdict,name,self):
        for clve,valor in self.dict:
            lista1=self.dict["features_seasons"][0]["cast"]
        cont=0
        lista_agregar=[]
        for i in lista1.len():
            if i==name:
                lista_agregar.append(self.dict["serie"])
                
                
                
            
        
                
        # dict={
        #     "serie": "String",
        #     "number_seasons": 1,
        #     "original_lenguage": "String",
        #     "features_seasons": [
        #         {
        #             "season_number": 1,
        #             "season_name": "String",
        #             "premier_date": "Date",
        #             "cast": ["Actor1", "Actor2"],
        #             "episodes": [
        #                 {"episode_name": "String",
        #                  "time_duration": 1

        #                 }       ]
        #         }               ] 
        # }
  

    


        
        
