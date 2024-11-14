#Daniel Tugendhaft 318465291
#Program_9 - OOP.py:



####Q1:

class MiniBar:

    def __init__(self,drinks,snacks):
        self.Set_drinks(drinks)
        self.Set_snacks(snacks)
        self.Set_bill()
        
    def Set_drinks(self,drinks):
        self.drinks = drinks
        
    def Set_snacks(self,snacks):
        self.snacks = snacks

    def Set_bill(self):
        self.bill = 0
        
    def Get_drinks(self):
        return self.drinks
    
    def Get_snacks(self):
        return self.snacks
    
    def add_bill(self,bill):
        self.bill += int(bill)

    def print_bill(self):
        print('Your bill is',self.bill,'₪')

    def drink_drink(self,drink):
        if drink in self.drinks:
            drinked_drink = (self.drinks).pop(drink)
            self.add_bill(drinked_drink)
        else:
            raise ValueError('There is no such drink \''+drink+'\' in the mini bar')

    def eat_snack(self,snack):
        if snack in self.snacks:
            eated_snack = (self.snacks).pop(snack)
            self.add_bill(eated_snack)
        else:
            raise ValueError('There is no such snack \''+snack+'\' in the mini bar')
    
    def __repr__(self): 
        return 'The MiniBar have:\n    '+'drinks:'+str(minibar_item_to_str(self.Get_drinks()))+'\n    '+'snacks:'+str(minibar_item_to_str(self.Get_snacks()))+'\n    '+'The bill is '+str(self.bill)+'₪'
    

def minibar_item_to_str(Dict):
    Str = ''
    for k, v in Dict.items():
        Str += ' '+k+'('+str(v)+'₪),'
    return Str.strip(',')

#####checking_code:        
##drinks_Classic = {'pepsi':20,'vodka':90,'soda':20,'water':15}
##snacks_Classic = {'m&m':15,'cookies':45,'doritos':20,'nature_valley':5}
##MiniBarClassic = MiniBar(drinks_Classic,snacks_Classic)
##
##MiniBar305.eat_snack('m&m')
##MiniBar305.drink_drink('pepsi')
##MiniBar305.print_bill()
##
#####exceptions:
####MiniBar305.eat_snack('bamba')
####MiniBar305.drink_drink('coca_cola')





####Q2:

class Room:

    def __init__(self,miniBar,floor,number,guests,clean_level,rank,satisfaction=1.0):
        self.Set_miniBar(miniBar)
        self.Set_floor(floor)
        self.Set_number(number)
        self.Set_guests(guests)
        self.Set_clean_level(clean_level)
        self.Set_rank(rank)
        self.Set_satisfaction(satisfaction)
        
        
    def Set_miniBar(self,miniBar):
        if not isinstance(miniBar,MiniBar):
            raise TypeError('The miniBar must be: \'MiniBar\' class')
        self.miniBar = miniBar
        
    def Set_floor(self,floor):
        check_int(floor,'room floor')
        if 0 <= floor:
            self.floor = floor
        else:
            raise ValueError('The room floor must be: zero or bigger than zero')

            
    def Set_number(self,number):
        check_int(number,'room number')
        if 0 < number:
            self.number = number
        else:
            raise ValueError('The room number must be: bigger than zero')

    def Set_guests(self,guests):
        if not isinstance(guests,list):
            raise TypeError('The item guests must be list')
        if not all((character.isalpha() or character.isspace()) for item in guests for character in item):
            raise ValueError('The guest list of the room must be written in letters and spaces only')
        if guests == []:
            self.guests = 'Empty'
        else:
            self.guests = ''
            for guest in guests:
                self.guests += guest+', '
            self.guests = (self.guests).strip(', ')
        
    def Set_clean_level(self,clean_level):
        check_int(clean_level,'room clean level')
        if 0 <= clean_level <= 10:
            self.clean_level = clean_level
        else:
            raise ValueError('The room clean level must be: between 0 and 10.')

    def Set_rank(self,rank):
        check_int(rank,'room rank')
        if 0 <= rank <= 3:
            self.rank = rank
        else:
            raise ValueError('The room rank must be: 0/1/2/3')

        
    
    def Set_satisfaction(self,satisfaction):
        if not isinstance(satisfaction,float):
            raise TypeError('The item satisfaction must be float')
        if 1.0 <= satisfaction <= 5.0:
            self.satisfaction = satisfaction
        elif satisfaction > 5.0:
            self.satisfaction = 5.0
        else:
            raise ValueError('The room satisfaction must be: between 1.0 and 5.0')


    def Get_guests(self):
        return self.guests

    def __repr__(self): 
        return 'This room details:\n '+'MiniBar:\n  '+str(self.miniBar)+'\n '+'floor: '+str(self.floor)+'\n '+'room number: '+str(self.number)+'\n '+'guests names: '+str(self.guests)+'\n '+'clean_level: '+str(self.clean_level)+'\n '+'rank: '+str(self.rank)+'\n '+'satisfaction: '+str(self.satisfaction)

    def Is_occupied(self):
        if self.guests == 'Empty':
            return False
        else:
            return True

    def Better_than(self,other):
        if self.rank > other.rank or (self.rank == other.rank and self.clean_level > other.clean_level)  :
            return True
        else:
            return False
        if not isinstance(other,Room):
            raise TypeError('The Type of', other, 'is not a Room in the hotel')  

    def Check_in(self,guests):
        if self.guests == 'Empty' :
            self.Set_guests(guests)
            self.Set_satisfaction(1.0)
        else:
            raise RoomError('This room have guests already!')
        
    def Check_out(self):
        if self.guests == 'Empty' :
            raise RoomError('No guests in this room!')
        else:
            self.Set_guests([])

    def Move_to(self,other):
        other.Check_in((self.guests).split(', '))
        self.Check_out()
        if other.Better_than(self):
            other.Set_satisfaction(other.satisfaction+1.2)
            
class RoomError(Exception):
    pass

def check_int(x,item):
    if not isinstance(x,int):
        raise TypeError('The '+item+' must be int')




###checking_code:
##guests305 = ['David david','sara']
##guests304 = ['dana','asaf']
##MiniBar305 = MiniBar(drinks_Classic,snacks_Classic)
##MiniBar304 = MiniBar(drinks_Classic,snacks_Classic)
##Room305 = Room(MiniBar305,3,305,guests305,8,2)
##Room304 = Room(MiniBar305,20,304,guests304,9,2)








