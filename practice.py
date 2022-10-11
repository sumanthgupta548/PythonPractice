import logging
import sys

logging.basicConfig(filename = "list.log", level = logging.DEBUG, format= "%(asctime)s %(levelname)s %(message)s")

#List tasks is based on the logging and exception
class list_l:
    """This is the class list"""
    logging.info("Accessing the list_l class")

    """def extract_list(self,l):
        #Extracting the list entity from the collection
        logging.info("We are extracting the list from the collection")

        try:
            self.l = l
            if len(self.l)== 0:
                #raise ValueError("List is empty")
                logging.error("List is empty")

            else:
                for i in self.l:
                    if type(i) == list:
                        logging.info("Extracted list %s" , i)
        except Exception as e:
            logging.exception(e)

        finally:
            logging.info("Hurray you have moved to next level ")"""

    def extract_ineuron(self,m):
        """Extracting "ineuron" from the collection of list"""
        logging.info("A task is to extract ineuron from the collection of the list")
        try:
            self.m = m
            if len(self.m) == 0:
                logging.error("List is empty")
            else :
                for i in self.m:
                    if type(i)  == list or type(i)  == tuple or  type(i)  == set:
                        for j in i:
                            if j == "ineuron":
                                logging.info(j)

                    if type(i) == dict :
                        for k,v in i.items():
                            #for g in t:
                                logging.info(v)
                                return v
        except Exception as e:
            logging.exception(e)
        finally:
            logging.info("Hurray you have jumped into next level")

#m = [3,4,5,6,"ineuron", [23,456,"ineuron" ,8,78,78] , [345,56,87,8,98,9] , (234,"ineuron",6) , {"key1" :"ineuron" , 234:[23,45,656]}]
m= 0
list_var = list_l()
#print(list_var.extract_list(l))
print(list_var.extract_ineuron(m))





