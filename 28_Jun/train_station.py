class Bogie(object):
    
    #Sleep seat
    COUNT_SLEEP_TYPE=0
    #Sit Seat
    COUNT_SEAT_TYPE=0
    
    #Genarate method
    def __init__(self,_type="SIT",max_seat=10):
        self.type=_type
        self.max_seat=max_seat
        self.sales=0
        self.code="ST1"
        
    #Buy seat method
    def buy_ticket(self,quantity):
        #Check if it has enough seat for sale
        if (quantity+self.sales>self.max_seat):
            #Seat not enough
            return False
        else:
            #Seat is avalble for sale and increase sold seat number
            self.sales=quantity+self.sales
            return True
        
    # return remain seat
    def remain(self):
        return self.max_seat-self.sales
    
    # display Bogie's code
    def dis(self):
        return self.code