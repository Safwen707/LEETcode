class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1=[]
        stack2=[]
        
        for i in range(len(s)):
            print("s[i]")
            print(s[i])
            if s[i]=="(":
                stack1.append(i)
            if s[i]=="*":
                stack2.append(i)
            if s[i]==")":
                print ("condirtion if s[i]=="')'":")
                print("stack1")      
                print(stack1)  
                
                if stack1:
                    stack1.pop() # matché 
                else:
                    if stack2:
                        k=stack2.pop()

                    else:
                        return False
                
        print("stack1")      
        print(stack1)   
        if stack1:
            if not stack2:
                return False
            else:
                while stack1 and stack2:
                    k1=stack1.pop() 
                    k2=stack2.pop() 
                    if k1>k2:
                        return False  
            if stack1:
                return False
        
        return True
            


      
 


        