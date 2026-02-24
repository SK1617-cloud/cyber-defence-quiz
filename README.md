# Cyber Defence Quiz
## Introduction 
I currently work within the automotive manufacturing industry, which relies heavily on advanced machinery and digital technologies. The organisation depends on secure IT systems to support daily operations such as internal communication, manufacturing processes, and data management. As modern automotive environments become increasingly digitised, the protection of sensitive data and systems has become essential. 

Due to the rapid growth of digitalisation within the industry, cyber security has become a critical factor in maintaining operational integrity and protecting company information. Employees must understand common cyber threats such as phishing, data breaches, and social engineering attacks. However, the training currently provided by the organisation often relies on static materials, which do not actively assess employee understanding or engagement. 

To address this issue, I decided to develop a Cyber Defence Quiz Minimum Viable Product (MVP). The application will allow users to select relevant cyber security topics, answer multiple-choice questions, and receive immediate feedback on their responses. The system will calculate scores automatically and store results in a CSV file to enable basic performance tracking and analysis. 

This MVP is relevant to the workplace as it provides an interactive and measurable approach to improving cyber security awareness among employees. By encouraging active participation and tracking individual performance, the application supports continuous digital skills development in a cost-effective and scalable manner.

## Design Section
### GUI Design 
 the GUI was made using Figma to demonstarte the user interface and layout of the application before the development begins. the design focuses on making it relevent to organisations gudeline and layouts. The application will be using blue grey colour scheme as it matches the BMW brand style. The application will also be using calvice font formate as it best matches the organisations policies. The design focuses on simplicity, clarity, and ease of navigation to ensure an accessible user experience.

The user Journey can be seen in the image below:

![alt text](image.png)

you can clearly see the user journey in the image attched. 
the application will start off with asking you to enter your name so that app will understand who is using it and easier to store the results. on the second screen you allows users to select the topic they would like to learn about. on the next screen asper the topic it will display the multiple choice questions for users to answer. on the last screen they can see thier results.

 ## Functional and Non-functional Requirements 

### Functional Requirement 

| ID | Requirement Description |
|----|--------------------------|
| FR1 | The application must allow the user to enter their name before starting the quiz. |
| FR2 | The appplication must allow the user to select a quiz topic. |
| FR3 | The appplication must load quiz questions from a CSV file based on the selected topic. |
| FR4 | The appplication must display one question at a time. |
| FR5 | The appplication must display four multiple-choice answer options for each question. |
| FR6 | The appplication must allow the user to select one answer using radio buttons. |
| FR7 | The appplication must validate whether the selected answer is correct. |
| FR8 | The appplication must calculate and track the user’s score. |
| FR9 | The appplication must display the final score and percentage at the end of the quiz. |
| FR10 | The appplication must save the user’s name, score, and percentage to a results CSV file. |
| FR11 | The appplication must prevent progression without selecting an answer. |
| FR12 | The appplication must display an error message if the question file is missing or invalid. |
| FR13 | The appplication must allow the user to exit the application safely. |

### Non-functional Requirement

| ID   | Requirement Description |
|------|--------------------------|
| NFR1 | The interface must be simple and easy to navigate. |
| NFR2 | The application must use clear fonts and readable colours. |
| NFR3 | The layout must remain consistent across all screens. |
| NFR4 | The system must respond to user input within 1 second. |
| NFR5 | The application must load questions without noticeable delay. |
| NFR6 | The system must not crash if invalid input is provided. |
| NFR7 | The system must handle missing or corrupted CSV files gracefully. |
| NFR8 | The quiz must correctly calculate scores without errors. |
| NFR9 | The application must follow object-oriented programming principles. |
| NFR10 | The code must be modular and structured into classes. |
| NFR11 | The system must include unit tests to verify quiz logic. |
| NFR12 | The system must run on Python 3.10 or higher. |
| NFR13 | The application must work on Windows and macOS environments. |

### Tech stack outline 

Python 3 - Programming Language

Tkinter - Graficl user interface 

Pillow (PIL) – for background image handling

CSV – the local data stored in CSV 

unittest – for automated unit testing

CSV files used to - Store quiz questions and store user results

Visual Studio Code - used to develop application in 

Figma - used for UI prototyping

Digram.net - used for class diagram 

### Code Design Document

![alt text](image-1.png)

### Development Section 

### Testing Section 
