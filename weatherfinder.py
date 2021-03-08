import tkinter as tk
import requests
Height = 400
Width = 500
def test(entry):
    print('test input :',entry)
    label ['text'] = str(entry)
    return entry

#weatherstack password
#*******
# API acesss key
# c7136ca6c9cf56b61c94480ec83418fa
#url http://api.weatherstack.com/
def response(api_response):
    try:
        description = api_response['current']['temperature']
        name =api_response['location']['name']
        des =api_response['current']['weather_descriptions'][0]
        feel_like =api_response['current']['feelslike']
        val ='City: %s \nTemperature(°F): %s \nFeel Like: %s \nDescrption: %s' % (name,description,feel_like,des)
    except:
        temp = 'no location found'
    return val

def get_weather(city):

    params = {
    'access_key': 'c7136ca6c9cf56b61c94480ec83418fa',
    'query': city,
    'units': 'f'
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    label['text'] = response(api_response)

# root is the main code han be thought of as a tree where root is the parent
#and all that is called is its children
root = tk.Tk()
#change the icon in tab
root.iconbitmap('favicon.ico')
root.title('Weather App')

#set  default scren ratio when open
canvas = tk.Canvas(root,height = Height,width = Width)
# pack() - widget in blocks before placing them
canvas.pack()

background_im = tk.PhotoImage(file ="wallpaper2.png")
background_label = tk.Label(root,image = background_im)
#place() - allows to manually place the widget in a spefic postion
background_label.place(relx = 0,relwidth = 1,relheight = 1)

# bg = color ,bd = border
frame = tk.Frame(root,bg = '#80c1ff',bd = 5)
# anchor tells what placment to start from
frame.place (relx = 0.5,rely = 0.1,relwidth = 0.75,relheight = 0.1,anchor ='n')

#Entry - accept siginle line string from useer
entry = tk.Entry(frame, font = ('Courier',8))
#reletive widh to the frame
entry.place(relwidth = 0.65,relheight = 1)

#allows the Enter button to be used on keypad
entry.bind("<Return>",(lambda event: get_weather(entry.get())))
button= tk.Button(frame,text="get weather",command = lambda: get_weather(entry.get()))
#relx - reletive x asxis to the frame
button.place(relx =0.7, relwidth = 0.3,relheight = 1)

lower_frame = tk.Frame(root,bg = '#80c1ff',bd = 5)
lower_frame.place(relx =.5,rely =.25,relwidth  = .75,relheight = 0.65, anchor = 'n')

#instead of calling for root we put label in lowerframe
label = tk.Label(lower_frame,font = ('Courier',8))
label.place(relwidth  = 1,relheight = 1)


root.mainloop()
