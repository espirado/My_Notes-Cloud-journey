#!/usr/bin/env python3.6

def gather_information():
    height = float(inpit("what is your height?(inches or meters)"))
    weight =  float(input("what is your weight(pounds or kilograms)"))
    system =  input("are your measurements in metrics or imperial unit?").lower().strip()
    return (height,weight,system)
    