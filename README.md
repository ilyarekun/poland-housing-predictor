# Poland Housing Predictor

![Head](frontend/static/pic3.png)


## Table of Contents
1. [Overview](#overview)
2. [Components](#components)
3. [Installation & Setup](#installation--setup)

---

## Overview

**Poland Housing Predictor** is a tool designed to give you a quick estimate of apartment prices in Poland. It uses a pre-trained **RandomForestRegressor** model — built on real housing data from Kaggle — to make predictions based on your input.  
Fill out a form, click on the map to set the location, and see the predicted price instantly.  
The backend and the frontend are in their own Docker container. Both components are managed via Docker Compose.

## Components
### Data and Model
The project is built around a pre-trained **RandomForestRegressor** model, developed using a dataset of Polish apartment prices available on [Kaggle](https://www.kaggle.com/datasets/krzysztofjamroz/apartment-prices-in-poland/data). 

The dataset comprises multiple CSV files — including buying data from January 2024 to June 2024 along with additional historical and rental data. 

These are form inputs, listed in their importance to the prediction:


| **Field Name**          | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| **squareMeters**        | Slider to input apartment size (25 to 150 m²).                                  |
| **rooms**               | Number input for the number of rooms (1 to 6).                                  |
| **latitude** (hidden)   | Hidden field for storing latitude selected on the map.                          |
| **longitude** (hidden)  | Hidden field for storing longitude selected on the map.                         |
| **city**                | Dropdown to select a city (15 Polish cities, e.g., Warszawa, Krakow).            |
| **centreDistance**      | Number input for distance to city center (0.02 to 16.62 km).                    |
| **poiCount**            | Number input for points of interest nearby (0 to 210).                          |
| **type**                | Dropdown to select building type (Block of Flats, Tenement, Apartment Building).|
| **floorCount**          | Number input for total floors in the building (1 to 30).                        |
| **floor**               | Number input for the apartment's floor number (1 to 30).                        |
| **hasElevator**         | Radio buttons to indicate if there’s an elevator (Yes/No).                      |
| **hasBalcony**          | Radio buttons to indicate if there’s a balcony (Yes/No).                        |
| **hasParkingSpace**     | Radio buttons to indicate if there’s a parking space (Yes/No).                  |
| **hasStorageRoom**      | Radio buttons to indicate if there’s a storage room (Yes/No).                   |
| **hasSecurity**         | Radio buttons to indicate if there’s security (Yes/No).                         |


---

 **Notes**
- The **latitude** and **longitude** fields are hidden and auto-filled based on map interaction.


### The model achieved:  
 - MSE of 164285.32
 - MAE of 263.85
 - R-squared of 0.894.

### Application

The backend is implemented in **Flask** and is responsible for processing form submissions, running the prediction with the model, and returning the results. This service runs in its own **Docker container**.  
The frontend is an HTML and CSS interface that allows users to fill out a form, select coordinates on an interactive map, and view the prediction outcome. It is served from a **Docker container** built on **Node 18-alpine**.  
Both containers are managed using **Docker Compose**.

## Installation & Setup
- clone the repo: `git clone https://github.com/ilyarekun/poland-housing-predictor.git`
- create and activate your env:
    - python -m venv venv
    - source venv/bin/activate
- run `pip install -r requirements.txt`
- add venv to kernels:
    - `python -m ipykernel install --user --name=venv --display-name "Python (venv)"`
- run `inspec.ipynb` to get model weights.
- make files executable:
    - `chmod +x prepare-app.sh`
    - `chmod +x start-app.sh`
    - `chmod +x end-app.sh`
- run in your terminal:
    - `sudo ./prepare-app.sh`
    - `./start-app.sh`
- open in your browser:
    - `http://localhost:3000/`
- finish the work:
    - `./end-app.sh`

