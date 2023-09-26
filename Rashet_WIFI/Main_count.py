import math
class Ranges: 
    def __init__(self,dict_parametr:dict) -> None:
        try:
            dict_parametr["losses_to_receiver"]=float(dict_parametr["losses_to_receiver"])*0.23
            dict_parametr["losses_to_transmitter"]=float(dict_parametr["losses_to_transmitter"])*0.23
            for key,val in dict_parametr.items():
                if val!='':
                    self.__setattr__(key,float(val))
            self.FSL=None
            self.length=None
        except:
           self.length='Введены некоректные значения'
    def decision_FSL(self)->float:
        FSL=self.transmitter_power+self.receiver_gain+self.transmitter_gain-self.sensitivity-self.losses_to_receiver-self.losses_to_transmitter-self.SOM
        return FSL
    def decision_distance(self)->str:
        if self.length==None:
           self.length=10**((self.decision_FSL()/20)-(32.44/20)-math.log10(self.frequency))
           self.length=self.length*1000 #перевод в метры
        return str(round(self.length,3))

def leng_out(dict_parametr:dict)->str:
    '''Функция для вывода длины дейстия беспроводного устройства '''
    applain=Ranges(dict_parametr)
    return  applain.decision_distance()

def main():
    pass

if __name__=='__main__':
    main()