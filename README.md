# GuestRecorder-Python
A Guest Recorder system complete with web-based GUI built using Python + Flask.

## Initial Setup & Running the Program
To clone the repository as well as install all of its dependencies:
```
git clone https://github.com/gabrieljames01/GuestRecorder-Python.git
cd GuestRecorder-Python/
pip install -r requirements.txt
```

## Running Flask Server
To server has to serve `127.0.0.1:5000`, hence run:
```
flask run -h 127.0.0.1 -p 5000
```


## Functionalities
Record the identification of the guest, the destination, as well as purpose of visit. These records can be accessed by opening excel files, which are labeled by dates (If the program is **first** executed on a particular date, a new excel file will be generated).<br>
Destination list (dropdown) can be changed by modifying `/db/db.txt` file (Destinations are seperated by newline, "\n").

