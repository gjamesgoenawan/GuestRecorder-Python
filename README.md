# GuestRecorder-Python
A Guest Recorder system complete with web-based GUI built using Python + Flask.

## Initial Setup & Running the Program
To clone the repository as well as install all of its dependencies:
```
git clone
cd GuestRecorder-Python/
pip install -r requirements.txt
```
Theere are two python files included in this repository:
1. app.py<br>
   Main Script with GUI included.
3. src/source.py
   Source Script without GUI, with complete functionality.



## Functionalities and Features
Record the identification of the guest, the destination, as well as purpose of visit. These records can be accessed by opening excel files, which are labeled by dates (If the program is **first** executed on a particular date, a new excel file will be generated).<br>
Destination list (dropdown) can be changed by modifying `/db/db.txt` file (Destinations are seperated by newline, "\n").

