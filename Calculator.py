
# coding: utf-8

# In[139]:


import re
#input the string

Str=input()
#Str="(20 * (30 +10)/(10*2))"

 

########################################################

#step 1 

# first, replace the numbers in the string to the character 
# EG: (20 * (30 + 10) / (10 * 2))  ---->>>   (a*(b+d)/(d*e))

k=97
q=""
inf={}
for i in Str.split(): 
    ss=re.search(r"\d+(\.\d+)?", i)
    #p=i
    if(ss):
        inf[ss.group(0)]=chr(k)
        k=k+1
    
for i in Str.split(): 
    ss=re.search(r"\d+(\.\d+)?", i)
    p=i
    if(ss):       
        p=i.replace(ss.group(0),inf[ss.group(0)])       
        
    q=q+p
exp=q

################################################
##step 2:
# Second, given expression will need to convert into postfix or prefix to get rid of parenthesis
# we are converting to postfix

#EG: (a*(b+d)/(d*e)) ------>>>>>>> abd+*de*/
class Conversion: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1 
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
        # Precedence setting 
        self.output = [] 
        self.precedence = {'+':1, '-':1, '*':2, '/':2} 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
    # A utility function to check is the given character 
    # is operand  
    def isOperand(self, ch): 
        return ch.isalpha() 
  
    # Check if the precedence of operator is strictly 
    # less than top of stack or not 
    def notGreater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
              
    def Postfix(self, exp): 
          
        # Iterate over the expression for conversion 
        for i in exp: 
            # If the character is an operand,  
            # add it to output 
            if self.isOperand(i): 
                self.output.append(i) 
              
            # If the character is an '(', push it to stack 
            elif i  == '(': 
                self.push(i) 
  
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif i == ')': 
                while( (not self.isEmpty()) and self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
  
            # An operator is encountered 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 
  
        # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
        return  ("".join(self.output)) 
  
obj = Conversion(len(exp)) 
PostFixString=obj.Postfix(exp) 
#################################################################################

#replace characters with orignal number

#EG: abd+*de*/ ---->>> 20 30 10 + * 10 2 * /
ww=""
for i in PostFixString:
    p=i+ ' '
    for k,j in inf.items():
        
        if(j==i):
            p=i.replace(i,k+ ' ')
            
            break
    ww=ww+p
newStr=ww[:-1:]
################################################################################
#step 3 
#evaluate the postfix expression
# EG 20 30 10 + * 10 2 * /      ----------->>> 40
class evalpostfix: 
    def __init__(self): 
        self.stack =[] 
        self.top =-1
    def pop(self): 
        if self.top ==-1: 
            return
        else: 
            self.top-= 1
            return self.stack.pop() 
    def push(self, i): 
        self.top+= 1
        self.stack.append(i) 
  
    def centralfunc(self, ab): 
        for i in ab: 
  
            try: 
                self.push(int(i)) 
            except ValueError: 
                val1 = self.pop() 
                val2 = self.pop() 
  
                switcher ={'+':val2 + val1, '-':val2-val1, '*':val2 * val1, '/':val2 / val1, '^':val2**val1} 
                self.push(switcher.get(i)) 
        return int(self.pop()) 


strconv = newStr.split(' ') 
obj = evalpostfix() 
print(obj.centralfunc(strconv)) 

