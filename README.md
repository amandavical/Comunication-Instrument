# Communication Instrument

A Python project that simulates data collection from a virtual instrument using serial communication.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)

## Introduction

Communication Instrument is a Python project that demonstrates the simulation of data collection from a virtual instrument using serial communication. It includes a simulated client for communication and a virtual instrument with attributes like temperature, voltage, and current.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/amandavical/communication-instrument.git
   cd communication-instrument


## Features

#### Here are the main features and functionality available in this project:



`1 - Communication with the Instrument Class.`


| Class    | Type        | Description                                                                                                                                     |
|:---------|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| `Client` | `bytearray` | The application interacts with an instrument using the class, allowing the exchange of commands and the reading of responses in bytearray format.|



  `2 - Temperature Storage and Verification.`

| Function               | Type   | Description                                                                                  |
|:-----------------------|:-------|:---------------------------------------------------------------------------------------------|
| `collect_temperatures` | `int`  | Capable of reading 20 instrument temperatures and storing them in a list.                    |
| `check_temperatures`   | `int`  | Returns an `TemperatureTooHighError` error if a read temperature is greater than 80 degrees. |



  `3 - Voltage Storage and Verification.`

| Function           | Type   | Description                                                                                                                   |
|:-------------------|:-------|:------------------------------------------------------------------------------------------------------------------------------|
| `collect_voltages` | `int`  | Collects a list of 20 voltage values and storing them in a list.                                                              |
| `check_voltages`   | `int`  | If any voltage is equal to zero, a message is displayed. If it exceeds 190 volts, an `VoltageTooHighError` error is returned. |


  `4 - Data Collection and Attributes`

| Function | Type  | Description |
|:---------|:------|:------------|
| `collect_statuses`      | `int` | Collects a list of 5 status values.|



  `5 - Current Monitoring.`

| Function           | Type  | Description                                                                                               |
|:-------------------|:------|:----------------------------------------------------------------------------------------------------------|
| `collect_currents` | `int` | Collects a list of 30 current values **greater than 25mA and less than 800mA** and stores them in a list. |
| `check_current_threshold`    | `int` | If any current is less than 25mA, a `Threshold alert!` error is returned.                                 |
