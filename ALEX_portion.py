
#Alex's portion

#loading packages
import re

#printing intro text welcoming user
print('\n\nHi! Please answer these questions to get a personalized probability of death if hospitalized for COVID-19.\n\n')


#Gathering user data for sex

while True:
    Sex = input('\nWhat is your sex? M or F      ')
    
    #Text Sanitization
    Sex = Sex.strip().capitalize()
    
    if Sex == "F" or Sex == "M":
        if Sex == "Y":
            Sex = 1
        else:  
            Sex = 0
        break
        
    print("\n\nPlease enter 'M' or 'F' to proceed.\n\n")
    

#Gathering user data for age

while True:
    Age = input('\nWhat is your age? Please enter a number:      ')
    
    #Text Sanitization
    Age = Age.strip()
    
    #Text Checking
    valid_age = bool(re.search('^[0-9]{1,2}$', Age))
    
    if valid_age:
        Age = int(Age)
        break
        
    print("\n\nPlease enter a number from 0 to 99.\n\n")


#Gathering user data for diabetes

while True:
    diabetes = input('\nDo you have diabetes? Y or N      ')
    
    #Text Sanitization
    diabetes = diabetes.strip().capitalize()
    
    if diabetes == "Y" or diabetes == "N":
        if diabetes == "Y":
            diabetes = 1
        else:  
            diabetes = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")

    
#Gathering user data for athsma

while True:
    athsma = input('\nDo you have athsma? Y or N      ')
    
    #Text Sanitization
    athsma = athsma.strip().capitalize()
    
    if athsma == "Y" or athsma == "N":
        if athsma == "Y":
            athsma = 1
        else:  
            athsma = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")
    
    
#Gathering user data for hypertension

while True:
    hypertension = input('\nDo you have hypertension? Y or N      ')
    
    #Text Sanitization
    hypertension = hypertension.strip().capitalize()
    
    if hypertension == "Y" or hypertension == "N":
        if hypertension == "Y":
            hypertension = 1
        else:  
            hypertension = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")


    
#Gathering user data for tobacco

while True:
    tobacco = input('\nDo you have a smoking habit? Y or N      ')
    
    #Text Sanitization
    tobacco = tobacco.strip().capitalize()
    
    if tobacco == "Y" or tobacco == "N":
        if tobacco == "Y":
            tobacco = 1
        else:  
            tobacco = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")

    
    
#Gathering user data for covid19 contact

while True:
    contact = input('\nHave you had contact with another person with COVID-19? Y or N      ')
    
    #Text Sanitization
    contact = contact.strip().capitalize()
    
    if contact == "Y" or contact == "N":
        if contact == "Y":
            contact = 1
        else:  
            contact = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")

    
    
#Gathering user data for Obesity

while True:
    obese = input('\nAre you obese? Y or N      ')
    
    #Text Sanitization
    obese = obese.strip().capitalize()
    
    if obese == "Y" or obese == "N":
        if obese == "Y":
            obese = 1
        else:  
            obese = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")


#Gathering user data for Pneumonia

while True:
    pneumonia = input('\nDo you have pneumonia? Y or N      ')
    
    #Text Sanitization
    pneumonia = pneumonia.strip().capitalize()
    
    if pneumonia == "Y" or pneumonia == "N":
        if pneumonia == "Y":
            pneumonia = 1
        else:  
            pneumonia = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")



#Gathering user data for copd

while True:
    copd = input('\nDo you have chronic obstructive pulmonary disease(COPD)? Y or N      ')
    
    #Text Sanitization
    copd = copd.strip().capitalize()
    
    if copd == "Y" or copd == "N":
        if copd == "Y":
            copd = 1
        else:  
            copd = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")


#Gathering user data for cardiovascular disease

while True:
    cardiovascular = input('\nDo you have cardiovascular disease? Y or N      ')
    
    #Text Sanitization
    cardiovascular = cardiovascular.strip().capitalize()
    
    if cardiovascular == "Y" or cardiovascular == "N":
        if cardiovascular == "Y":
            cardiovascular = 1
        else:  
            cardiovascular = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")


#Gathering user data for chronic kidney failure

while True:
    renal_chronic = input('\nDo you have chronic kidney failure? Y or N      ')
    
    #Text Sanitization
    renal_chronic = renal_chronic.strip().capitalize()
    
    if renal_chronic == "Y" or renal_chronic == "N":
        if renal_chronic == "Y":
            renal_chronic = 1
        else:  
            renal_chronic = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")    

    
#Gathering user data for Other Diseases

while True:
    other_disease = input('\nDo you have another disease not mentioned here? Y or N      ')
    
    #Text Sanitization
    other_disease = other_disease.strip().capitalize()
    
    if other_disease == "Y" or other_disease == "N":
        if other_disease == "Y":
            other_disease = 1
        else:  
            other_disease = 0
        break
        
    print("\n\nPlease enter 'Y' for YES or 'N' for NO to proceed.\n\n")
    

#compiling user data into a dictionary

User_data = {
    "sex" : Sex,
    "age" : Age,
    "diabetes" : diabetes,
    "athsma" : athsma,
    "hypertension" : hypertension,
    "tobacco" : tobacco,
    "contact_other_covid" : contact,
    "obesity" : obese,
    "pneumonia" : pneumonia,
    "other_disease" : other_disease,
    "copd" : copd,
    "cardiovascular" : cardiovascular,
    "renal_chronic" : renal_chronic,
    "other_disease" : other_disease
}
    

print("\nHere is the user's data...\n", User_data)

# Could someone help me find meta data about these variables??...

# covid_res