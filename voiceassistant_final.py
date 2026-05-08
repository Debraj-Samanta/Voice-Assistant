import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk

# ==== Class Assistant
class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="images/background.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="images/frame_image.jpg")
        left = Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

        # ==== Start button
        start = Button(self.root, text='START', font=("times new roman", 14), command=self.start_option).place(x=150, y=520)

        # ==== Close button
        close = Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window).place(x=350, y=520)

    # ==== Start assistant
    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        # ==== Default Start
        def start():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello Sir,' + wish + ' I am your voice assistant. Please tell me how may I help you')

        # ==== Take Command
        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker, timeout=10)  # Timeout to avoid infinite waiting
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except sr.UnknownValueError:
                print("Could not understand audio")
                speak("Sorry, I could not understand. Could you please repeat?")
                return None
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service")
                speak("Sorry, there is an issue with the speech recognition service.")
                return None
            except Exception as e:
                print(f"Error: {str(e)}")
                speak("Sorry, I encountered an error. Please try again.")
                return None

        # ==== Run Command
        def run_command():
            instruction = take_command()
            if instruction:
                print(instruction)
                try:
                    if 'who are you' in instruction:
                        speak('I am your personal voice Assistant')

                    elif 'what can you do for me' in instruction:
                        speak('I can play songs, tell time, and help you go with Wikipedia')

                    elif 'current time' in instruction:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        speak('Current time is ' + time)

                    elif 'open google' in instruction:
                        speak('Opening Google')
                        webbrowser.open('https://www.google.com')

                    elif 'open youtube' in instruction:
                        speak('Opening Youtube')
                        webbrowser.open('https://www.youtube.com')

                    elif 'open facebook' in instruction:
                        speak('Opening Facebook')
                        webbrowser.open('https://www.facebook.com')

                    elif 'open linkedin' in instruction:
                        speak('Opening LinkedIn')
                        webbrowser.open('https://www.linkedin.com')

                    elif 'open gmail' in instruction:
                        speak('Opening Gmail')
                        webbrowser.open('https://www.gmail.com')

                    elif 'open stack overflow' in instruction:
                        speak('Opening Stack Overflow')
                        webbrowser.open('https://stackoverflow.com')

                    elif 'open gndec website' in instruction:
                        speak('Opening College Website')
                        webbrowser.open('https://gndecb.ac.in')

                    elif 'shutdown' in instruction:
                        speak('Voice Assistant Signing Off Have a nice day ahead')
                        self.close_window()
                        return False  # Returning False to break the loop

                    else:
                        speak('I did not understand that. Can you please repeat again?')

                except Exception as e:
                    speak('An error occurred: ' + str(e))
            return True  # Return True to continue the loop

        # ==== Default Start calling
        start()

        # ==== To run assistance continuously
        while True:
            if not run_command():  # Break the loop if user says "shutdown"
                break

    # ==== Close window
    def close_window(self):
        self.root.destroy()

# ==== Create tkinter window
root = Tk()

# === Creating object for class
obj = AssistanceGUI(root)

# ==== Start the GUI
root.mainloop()
