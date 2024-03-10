# midterm
midtermProject
# TechTimeApp

# TechTime PC Optimizer

## Introduction
TechTime PC Optimizer is a web application designed to enhance the performance of your PC through a series of optimization scripts. Before using these scripts, it is highly recommended to create a system restore point. The application allows users to track performance issues, apply optimizations, and record changes in performance before and after optimizations in the notes section.

## Features
- **Optimization Scripts**: Access to a variety of CMD prompts designed to improve system performance.
- **Performance Tracking**: Users can add notes for before and after applying optimizations to monitor performance changes.
- **Restoration Point Advice**: Guidance on creating system restore points before running any optimization scripts.

## Technologies Used
- **FastAPI**: For building the backend and routing.
- **Static Files**: Serving static files like HTML, CSS, and JS for the frontend.
- **API Routers**: `file_routers` for handling file downloads, and `todo.py` for managing notes about system performance.

## Project Structure
- `main.py`: The entry point for the application, setting up the server and including all routers.
- `todo.py`: Handles the notes functionality, allowing users to track performance before and after optimizations.
- `file_routers.py`: Manages the download of CMD prompt scripts for system optimization.
- `frontend/`: Contains HTML, CSS, and JS files for the user interface.
## Cmd Prompt Usage
- inside each cmd and reg edit prompt is a comment that states what is being changed either in the registry editor or through a command prompt
- In order to see what is in the command prompt, one simply has to download the cmd file or reg edit file and highlight the downloaded file.
- After highlighting click edit file and open it with notepad to see the comments needed to understand each reg edit or cmd file.
## Adding notes , editing notes, deleting notes
-inside the adding and editing notes feature gives a live feedback to whether an individual is actually editing notes or not.
-I used the same front end parts to edit the notes for simplicity.
## Struggles
-The part I struggled with most was being able to use multiple routers in order to achieve the correct type of parsing in my front end files.  Making another another file named file_routers.py helped, but a small mistake regarding the order in which the routers are applied using the app.mount method hung me up for a while
## Things I would do differently
-In the future I would utilize office hours in order to help with my router problems and making sure the debugging for api endpoints using postman is implemented.  Postman saved me a lot of time because I could pinpoint what was wrong with my api endpoints and what was happening down my chain of command.



![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204423.png)
 ![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204447.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204743.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204838.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204936.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204838.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20204936.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20205020.png)
![alt text](https://github.com/micetich/midterm/blob/main/Screenshot%202024-03-09%20205054.png)
