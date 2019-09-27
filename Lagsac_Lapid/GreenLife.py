import PySimpleGUI as sg #import of PySimpleGUI library to python

def insertion_sort(A): #creation of insertion sort for sorting array elements
    int_array = [int(x) for x in A] #conversion of elements of array from string to int
    for i in range(1, len(int_array)): #start of insertion sort algorithm
        key = int_array[i] 
        j = i-1
        while j >= 0 and key < int_array[j] : 
                int_array[j+1] = int_array[j] 
                j -= 1
        int_array[j+1] = key
    return int_array #return of sorted array or list

def display_number(A,key): #creation of function for displaying numbers that has been sorted in the designated tabs
    new_array = insertion_sort(A) #calling the function insertion_sort to sort the array
    s = '\n' .join([str(i) for i in new_array]) #for loop for joining of elements in array and converting it to string
    insert_page.Element('INPUT').Update('') #removing of input in the window
    return insert_page.Element(key).Update(s) #returning the display of numbers in the tab

def point_add(values,key,points): #creation of function for adding of points
    if values['Glass1'] == True: #the condition to check if the radio button for glass is true and formula for adding points
        points = (int(values['INPUT']) * 7)
        total.append(points) #the computed points will be appended to the list or array designated
    if values['Metal1'] == True: #the condition to check if the radio button for metal is true and formula for adding points
        points = int(values['INPUT']) * 7
        total.append(points) #the computed points will be appended to the list or array designated
    if values['Organic1'] == True: #the condition to check if the radio button for organic is true and formula for adding points
        points = int(values['INPUT']) * 7
        total.append(points) #the computed points will be appended to the list or array designated
    if values['Paper1'] == True: #the condition to check if the radio button for paper is true and formula for adding points
        points = int(values['INPUT']) * 7
        total.append(points) #the computed points will be appended to the list or array designated
    if values['Plastic1'] == True: #the condition to check if the radio button for plastic is true and formula for adding points
        points = int(values['INPUT']) * 10
        total.append(points) #the computed points will be appended to the list or array designated
    if values['Styro1'] == True: #the condition to check if the radio button for styro is true and formula for adding points
        points = int(values['INPUT']) * 10
        total.append(points) #the computed points will be appended to the list or array designated
    if len(new_total_array) > 0: #this will check if the array has element inside it
        del new_total_array[0]
    sum_array = sum(total) #initialization of sum_array to the sum of the elements in the total list
    new_total_array.append(sum_array) #appending of sum_array to the new_total_array list
    
    return insert_page.Element(key).Update(sum_array) # updating of points in the redeem page

def claim_item(values,key,input_key,current_points): #creation of fuction for redeeming points
    if values['Pencil1'] == True: #checking if the radio button pencil is True
        if int(values[input_key]) * 50 > current_points: #formula for checking if points is sufficient
            sg.Popup("You have insufficient Points.",background_color="#343434")
        else:
            dif = (int(values[input_key]) * 50) #formula for subtraction of points
            temp.append(dif) #appending the value to a temp array
    elif values['Ballpen1'] == True: #checking if the radio button ballpen is True 
        if int(values[input_key]) * 70 > current_points: #formula for checking if points is sufficient
            sg.Popup("You have insufficient Points.",background_color="#343434")
        else:
            dif = (int(values[input_key]) * 70) #formula for subtraction of points
            temp.append(dif) #appending the value to a temp array
    elif values['Pad_Paper1'] == True: #checking if the pad_paper button ballpen is True 
        if int(values[input_key]) * 150 > current_points: #formula for checking if points is sufficient
            sg.Popup("You have insufficient Points.",background_color="#343434")
        else:
            dif = (int(values[input_key]) * 150) #formula for subtraction of points
            temp.append(dif) #appending the value to a temp array
    else: #condition if the first 3 conditions are not true so it will go to the notebook condition
        if int(values[input_key]) * 300 > current_points: #formula for checking if points is sufficient
            sg.Popup("You have insufficient Points.",background_color="#343434")
        else:
            dif = (int(values[input_key]) * 300) #formula for subtraction of points
            temp.append(dif) #appending the value to a temp array
    new_sum = sum(total) - sum(temp) #subtraction of total list and the temp list
    if len(new_total_array) > 0: #checking if there is no element in the list
        new_total_array.append(new_sum) #appending of the new_sum variable
        del new_total_array[0]
    
    return redeem_page.Element(key).Update(new_sum) #updating of points display in the redeem page

sg.SetOptions(text_color="#e4e4e4", font='opensans 11') #options setting of color and font style

#initialization of the application's homepage with design
homepage_layout = [[sg.Text(' GreenLife', background_color="#343434")],
           [sg.T(' ' * 0,  background_color="#343434"),sg.Button('  Insert  ', button_color=('white', 'black'))],
           [sg.T(' ' * 0,  background_color="#343434"),sg.Button('Redeem', button_color=('white','black'))]]

home_page = sg.Window('Home Page', homepage_layout, background_color="#343434", font='sfprodisplay 25') #declaration of home_page
insert_page_active=False #setting of insert_page to false
redeem_page_active=False #setting of redeem_page to false

glass,metal,organic,paper,plastic,styro,total,temp,new_total_array = [],[],[],[],[],[],[],[],[] #initialization of lists to be used
points = 0 #initialization of points

while True:
    
    home_page_event, home_page_values = home_page.Read() #reading of activities of events and values inside the home page
    
    if home_page_event is None: #condition of the button 'x' is pressed in the home page 
        break
        
    if home_page_event == '  Insert  ' and not insert_page_active and not insert_page_active: #condition of if the insert page is clicked
        
        insert_page_active = True #the window insert_page_will be active and will be displayed in the screen
        home_page.Hide() #the home page will be hidden from the screen
        
        #initialization of the different trash categories tab for the insert layout with design
        glass_layout = [[sg.T('This is the Record for Glass Input', background_color="#343434")],
                       [sg.T('User Inputs:', background_color="#343434")],
                      [sg.Text('',key='Glass2',size=(20,10), background_color="#343434")]]
        metal_layout = [[sg.T('This is the Record for Metal Input', background_color="#343434")],
                       [sg.T('User Inputs:', background_color="#343434")],
                      [sg.Text('',key='Metal2',size=(20,10), background_color="#343434")]]
        organic_layout = [[sg.T('This is the Record for Organic Input', background_color="#343434")],
                       [sg.T('User Inputs:', background_color="#343434")],
                      [sg.Text('',key='Organic2',size=(20,10), background_color="#343434")]]
        paper_layout = [[sg.T('This is the Record for Paper Input', background_color="#343434")],
                       [sg.T('User Inputs:', background_color="#343434")],
                      [sg.Text('',key='Paper2',size=(20,10), background_color="#343434")]]
        plastic_layout = [[sg.T('This is the Record for Plastic Input', background_color="#343434")],
                       [sg.T('User Inputs:', background_color="#343434")],
                      [sg.Text('',key='Plastic2',size=(20,10), background_color="#343434")]]
        styro_layout = [[sg.T('This is the Record for Styro Input', background_color="#343434")],
                       [sg.T('User Inputs:', background_color="#343434")],
                      [sg.Text('',key='Styro2',size=(20,10), background_color="#343434")]]
        
        #initialization of insert page with different buttons and inputs and designs of each functions
        insert_page_layout = [[sg.Button('Exit', button_color=('white', 'black'))],
                    [sg.TabGroup([[sg.Tab(' Glass ', glass_layout, background_color="#343434",),
                    sg.Tab(' Metal ', metal_layout, background_color="#343434"),
                    sg.Tab(' Organic ', organic_layout, background_color="#343434"),
                    sg.Tab(' Paper ', paper_layout, background_color="#343434"),
                    sg.Tab(' Plastic ', plastic_layout, background_color="#343434"),
                    sg.Tab(' Styro ', styro_layout, background_color="#343434")]])],
                  [sg.Text('Points:', background_color="#343434"),
                    sg.Text(sum(new_total_array),key='Points1',size=(10,0), background_color="#343434")],
                  [sg.Radio('Glass - 7points','RADIO1',key='Glass1',background_color="#343434"),
                    sg.Radio('Metal - 7points','RADIO1',key='Metal1',background_color="#343434"),
                    sg.Radio('Organic - 7points','RADIO1',key='Organic1',background_color="#343434"),
                    sg.Radio('Paper - 7points','RADIO1',key='Paper1',background_color="#343434"),
                    sg.Radio('Plastic - 10points','RADIO1',key='Plastic1',background_color="#343434"),
                    sg.Radio('Styro - 10points','RADIO1',key='Styro1',background_color="#343434")],
                  [sg.Text('Please Enter the amount of trash you want to put: ',background_color="#343434"),
                    sg.Input(size=(5,1),key='INPUT',pad=(0,0))],
                  [sg.Button('Submit',button_color=('white', 'black'))]]
        
        
        insert_page = sg.Window('Insert',insert_page_layout, background_color="#343434") #declaration of the insert page 
        while True:
            
            insert_page_event , insert_page_values = insert_page.Read() #reading the event and values that is done inside the insert page
            
            if insert_page_event == 'Submit': #condition if the event in insert page is equal to Sumbit button
                if insert_page_values['Glass1'] == True: #condition if the radio button is clicked on glass
                    glass.append(insert_page_values['INPUT']) #appending of input value to glass array
                    display_number(glass,'Glass2') #calling of display number function
                    point_add(insert_page_values,'Points1',points) #calling of adding points function
                elif insert_page_values['Metal1'] == True: #condition if the radio button is clicked on metal
                    metal.append(insert_page_values['INPUT']) #appending of input value to metal array
                    display_number(metal,'Metal2') #calling of display number function
                    point_add(insert_page_values,'Points1',points) #calling of adding points function
                elif insert_page_values['Organic1'] == True: #condition if the radio button is clicked on organic
                    organic.append(insert_page_values['INPUT']) #appending of input value to organic array
                    display_number(organic,'Organic2') #calling of display number function
                    point_add(insert_page_values,'Points1',points) #calling of adding points function
                elif insert_page_values['Paper1'] == True: #condition if the radio button is clicked on paper
                    paper.append(insert_page_values['INPUT']) #appending of input value to paper array
                    display_number(paper,'Paper2') #calling of display number function
                    point_add(insert_page_values,'Points1',points) #calling of adding points function
                elif insert_page_values['Plastic1'] == True: #condition if the radio button is clicked on plastic
                    plastic.append(insert_page_values['INPUT']) #appending of input value to plastic array
                    display_number(plastic,'Plastic2') #calling of display number function
                    point_add(insert_page_values,'Points1',points) #calling of adding points function
                else: #condition if the first conditions is not met, which means the styro button is clicked
                    styro.append(insert_page_values['INPUT']) #appending of input value to styro array
                    display_number(styro,'Styro2') #calling of display number function
                    point_add(insert_page_values,'Points1',points) #calling of adding points function

            if insert_page_event is None or insert_page_event == 'Exit': #condition if the Exit button is clicked on the insert page
                insert_page.Close() #closing of insert page
                insert_page_active = False 
                break
                
    if home_page_event == 'Redeem' and not insert_page_active and not redeem_page_active: #condition if the redeem button is clicked in the home page
        redeem_page_active = True #the redeem page will be set to active
        home_page.Hide() #the home page will be hidden

        #initialization of the redeem page layout with design
        redeem_page_layout = [[sg.Button('Exit', button_color=('white','black'))],
                   [sg.Text('Redeem Points', background_color="#343434")],
                   [sg.Text('Current Points:', background_color="#343434"),
                    sg.Text(sum(new_total_array),key='Points2',size=(8,0), background_color="#343434"),
                    sg.Text('Quantity', background_color="#343434")],
                   [sg.Radio('Pencil(50pts)','RADIO1',size=(15,1),key="Pencil1", background_color="#343434"),
                    sg.Input(size=(5,1),key='INPUT_PENCIL',pad=(30,0))],
                   [sg.Radio('Ballpen(70pts)','RADIO1',size=(15,1),key="Ballpen1", background_color="#343434"),
                    sg.Input(size=(5,1),key='INPUT_BALLPEN',pad=(30,0))],
                   [sg.Radio('Pad Paper(150pts)','RADIO1',size=(15,1),key="Pad_Paper1", background_color="#343434"),
                    sg.Input(size=(5,1),key='INPUT_PAPER',pad=(30,0))],
                   [sg.Radio('Notebook(300pts)','RADIO1',size=(15,1),key="Notebook1", background_color="#343434"),
                    sg.Input(size=(5,1),key='INPUT_NOTEBOOK',pad=(30,0))],
                   [sg.Button('Submit', button_color=('white','black'))]]

        
        redeem_page = sg.Window('Redeem',redeem_page_layout, background_color="#343434") #declaration of the redeem page window
        while True:
            
            redeem_page_event,redeem_page_values = redeem_page.Read() #reading of events and values in the redeem page
            
            if redeem_page_event == 'Submit': #condition if the event button is equal to submit
                if sum(new_total_array) == 0 and sum(new_total_array) < 50: #condition if the sum of the array is less than 50
                    sg.Popup("You have insufficient Points.",background_color="#343434")
                elif redeem_page_values['Pencil1'] == True: #condition if the radio button clicked is pencil
                    claim_item(redeem_page_values,'Points2','INPUT_PENCIL',sum(new_total_array)) #calling of function claim item
                    redeem_page.Element('INPUT_PENCIL').Update('') #updating of input in the pencil row
                elif redeem_page_values['Ballpen1'] == True: #condition if the radio button clicked is ballpen
                    claim_item(redeem_page_values,'Points2','INPUT_BALLPEN',sum(new_total_array)) #calling of function claim item
                    redeem_page.Element('INPUT_BALLPEN').Update('') #updating of input in the ballpen row
                elif redeem_page_values['Pad_Paper1'] == True: #condition if the radio button clicked is pad paper
                    claim_item(redeem_page_values,'Points2','INPUT_PAPER',sum(new_total_array)) #calling of function claim item
                    redeem_page.Element('INPUT_PAPER').Update('') #updating of input in the pad paper row
                else: #condition if the first conditions are not met it will automatically go to notebook
                    claim_item(redeem_page_values,'Points2','INPUT_NOTEBOOK',sum(new_total_array)) #calling of function claim item
                    redeem_page.Element('INPUT_NOTEBOOK').Update('') #updating of input in the notebook row
                    
            if redeem_page_event is None or redeem_page_event == 'Exit': #condition if the exit button is clicked in the redeem page
                redeem_page.Close() #redeem page will be closed
                redeem_page_active = False
                break
                
    home_page.UnHide() #the home page will be unhided and will be shown again