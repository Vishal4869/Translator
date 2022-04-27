from deep_translator import GoogleTranslator
import pyttsx3
import PySimpleGUI as sg
import pyperclip
layout = [  [sg.Text("Enter the Text: ", size=(30,1))],
            [sg.InputText('', key='input_text',size=(60,2))],
            [sg.Text("Select Language: ", size=(30,1))],
            [sg.Combo(['Afrikaans', 'Arabic', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Finnish', 'French', 'Gujarati', 'Hindi', 'Marathi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian', 'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Malayalam', 'Myanmar (Burmese)', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Chinese'],default_value='English',key='langg'),sg.Checkbox('Speak', default=False, key="tick1")],
            [sg.Button("Convert",size=(15,2))],
            [sg.Text("Translation:", size=(30,1))],
            [sg.InputText('', key='-output-', size=(60,1)),sg.Button("Copy")],
            [sg.Exit("Exit",size=(10,2))]]



window = sg.Window("Text to Speech   (!!! Email: vaumtol@gmail.com !!!)",layout,size=(500,400))
while True:
    event, values = window.Read()
    if event == 'Convert':
        to_translate = values['input_text']
        lang_dict = {'Afrikaans': 'af', 'Arabic': 'ar', 'Bulgarian': 'bg', 'Bengali': 'bn', 'Bosnian': 'bs',
                     'Catalan': 'ca', 'Czech': 'cs', 'Welsh': 'cy', 'Danish': 'da', 'German': 'de', 'Greek': 'el',
                     'English': 'en', 'Esperanto': 'eo', 'Spanish': 'es', 'Estonian': 'et', 'Finnish': 'fi',
                     'French': 'fr', 'Gujarati': 'gu', 'Hindi': 'hi', 'Croatian': 'hr', 'Hungarian': 'hu',
                     'Armenian': 'hy', 'Indonesian': 'id', 'Icelandic': 'is', 'Italian': 'it', 'Japanese': 'ja',
                     'Javanese': 'jw', 'Khmer': 'km', 'Kannada': 'kn', 'Korean': 'ko', 'Latin': 'la', 'Latvian': 'lv',
                     'Macedonian': 'mk', 'Malayalam': 'ml', 'Marathi': 'mr', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne',
                     'Dutch': 'nl', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro',
                     'Russian': 'ru', 'Sinhala': 'si', 'Slovak': 'sk', 'Albanian': 'sq', 'Serbian': 'sr',
                     'Sundanese': 'su', 'Swedish': 'sv', 'Swahili': 'sw', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th',
                     'Filipino': 'tl', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Vietnamese': 'vi',
                     'Chinese': 'zh-CN'}
        lang = values['langg']
        language = lang_dict.get(lang)

        try:
            translated = GoogleTranslator(source='auto', target=language).translate(to_translate)
            window["-output-"].update(translated)
            if values['tick1'] == True:
                translated2 = GoogleTranslator(source='auto', target='en').translate(translated)
                engine = pyttsx3.init()
                rate = engine.getProperty('rate')
                engine.setProperty('rate', 100)
                engine.say(translated2)
                engine.runAndWait()
        except:
            sg.popup('Enter Proper Text',text_color='yellow')
            continue

    if event == 'Copy':
        pyperclip.copy(translated)

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()



