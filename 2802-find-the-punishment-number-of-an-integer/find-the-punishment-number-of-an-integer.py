class Solution: 
    p=[1,10]
    def generate_sums(self,arr:list):
        result = set()  # Utiliser un set pour éviter les doublons
        n = len(arr)
        
        # Générer toutes les positions où on pourrait faire une coupure
        for i in range(1, int(2**(n-1))):  # 2^(n-1) combinaisons possibles de coupures
            sum_parts = []
            current_part = str(arr[0])
            
            # Vérifier chaque bit du nombre i pour savoir où couper
            for j in range(1, n):
                if i & (1 << (j - 1)):  # Si le bit est 1, on fait une coupure
                    sum_parts.append(int(current_part))  # Ajouter le groupe courant à la liste des parties
                    current_part = str(arr[j])  # Commencer une nouvelle partie
                else:
                    current_part += str(arr[j])  # Ajouter à la partie courante
                    
            sum_parts.append(int(current_part))  # Ajouter la dernière partie
            result.add(sum(sum_parts))  # Additionner les parties et ajouter au set
        
        return sorted(result)  # Retourner la liste triée sans doublons



    def decimal(self,a: int):
        l = []
        while a != 0:
            l.append(a % 10)  # Utilisation de % au lieu de "mod"
            a = a // 10  # Utilisation de // pour la division 
        return l[::-1]  # Retourner la liste inversée
    def ispartitionned(self, i:int):
        test=True
        if i in self.p:
            return test
        else:
            d=self.decimal(i*i)
            print("d=")
            
            print(d)
            
            l=len(d)
            
                
            
                
                    
            li=self.generate_sums(d)
            print(li)
            if li:
                for s in li :
                              
                    if s==i:
                        
                        self.p.append(s)
                        
                        return True
                    else:
                        test= False
            else:
                test= False
            return test
        

    def punishmentNumber(self, n: int) -> int:
        s=0
        for i in range(1,n+1):
            if self.ispartitionned(i):
               
                s+=(i*i)
        return s