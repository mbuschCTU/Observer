########################################################################
class Subject(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.observers = []
        self.data = 23
        
    #----------------------------------------------------------------------
    def subscribe(self, observer):
        """"""
        self.observers.append(observer)
        print("subscribed " + observer.name)
        
    #----------------------------------------------------------------------
    def unsubscribe(self, observer):
        """"""
        self.observers.remove(observer)
        print("unsubscribed " + observer.name)
    #----------------------------------------------------------------------
    def notify_observers(self, value):
        """"""
        for observer in self.observers:
            observer.notify(value)
        
    #----------------------------------------------------------------------
    def change_data(self, new_value):
        """"""
        self.data = new_value
        self.notify_observers(self.data)
        
        
        
########################################################################
class Observer(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self,name):
        """Constructor"""
        super().__init__()
        self.name = name
    #----------------------------------------------------------------------
    def notify(self, value):
        """"""
        print(self.name + " Observer changed - new value = " + str(value))
        
        
#----------------------------------------------------------------------
def main():
    """"""
    subject = Subject()
    look1 = Observer("look1")
    look2 = Observer("look2")
    
    subject.subscribe(look1)
    subject.subscribe(look2)
    
    subject.change_data(11)
    subject.change_data(21)
    

    
if __name__=='__main__':
    main()
    