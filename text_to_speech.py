import pyttsx3 

def speak_text(command): 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait()
    
if __name__ == "__main__":
    speak_text('not again. fine. hello world.')