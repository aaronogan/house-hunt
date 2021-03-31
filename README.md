# house-hunt

## intro
this is a project to help automate a complicated house hunt

### general workflow
1. gather listings
    1. spark pipeline to call a real estate api based on a saved search
    1. optionally save api result to file for iterative development
    1. save data to mongodb
1. TODO "code" listings
    1. TODO simple web app to browse listings from mongodb
    1. TODO user can classify each listing as "ideal" or "not ideal"
1. TODO train machine learning model
1. TODO send suggested listings to user on some regular interval

## getting started
1. if not already installed, ensure you have `python3` and `python3-pip`
1. `make init`

