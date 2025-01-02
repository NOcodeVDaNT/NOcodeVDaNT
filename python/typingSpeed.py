from time import *
import random as r

def mistake(testpara,userinp):
    error=0
    for i in range(len(testpara)):
        try:
            if testpara[i]!=userinp[i]:
              error+=1
        except Exception as e:
            error+=1
    return error
            
        
            
            
def speed_time(timestart,timend,userinput):
    time_delay=timend-timestart
    time_roundoff=round(time_delay,2)
    speed=len(userinput)/time_roundoff
    return round(speed)
    
    
           
    
    
test = [
    "Sigma males are independent, self-reliant, and introspective individuals who thrive outside traditional social hierarchies. They prioritize personal freedom, value meaningful connections, and avoid unnecessary drama. Quiet yet confident, they focus on achieving goals with determination. Their adaptability, resourcefulness, and authenticity make them intriguing figures who lead by example, challenging societal norms with their unique perspectives.",
    
    "Artificial Intelligence is revolutionizing the world by enabling machines to perform tasks requiring human intelligence. From automation to personalized recommendations, AI simplifies complex processes. It drives innovation in healthcare, education, and technology, improving efficiency and accuracy. However, ethical concerns like bias, privacy, and job displacement highlight the importance of responsible AI development, ensuring its benefits align with humanity's values."
    ,
    "Health is wealth emphasizes the value of physical and mental well-being over material possessions. A healthy lifestyle fosters happiness, productivity, and resilience. Proper nutrition, regular exercise, and sufficient rest form its foundation. Ignoring health can lead to chronic illnesses, impairing quality of life. Investing in health ensures not just longevity but also the vitality to enjoy lifes true riches."
    

]

test1=r.choice(test)
print("____________typing speed test_____________")
print(test1)
print()
print()
time_1=time()
test_input=input("enter the test paragraph here :")
time_2=time()

print("your typing speed is : ",speed_time(time_1,time_2,test_input),"word/sec")
print("your mistake count is : ",mistake(test1,test_input))




