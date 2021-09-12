# GuestRecorder-Python
A Guest Recorder system complete with web-based GUI built using Python + Flask.

## Initial Setup & Running the Program
To clone the repository as well as install all of its dependencies:
```
git clone https://github.com/gabrieljames01/GuestRecorder-Python.git
cd GuestRecorder-Python/
pip install -r requirements.txt
```
There are two python files included in this repository:
 - app.py<br>Main Script with GUI included.
 - src/source.py<br> Source Script without GUI, with complete functionality. 

Both of these files can be run individually by running the default python launch command `python3 FILENAME.py`

## Functionalities
Record the identification of the guest, the destination, as well as purpose of visit. These records can be accessed by opening excel files, which are labeled by dates (If the program is **first** executed on a particular date, a new excel file will be generated).<br>
Destination list (dropdown) can be changed by modifying `/db/db.txt` file (Destinations are seperated by newline, "\n").

