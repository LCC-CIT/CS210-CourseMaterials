---
title: Lab 1, Group B
description: Group B assignment to translate and write Python apps
keywords: python, programming, AI, challenge, selection statements
material: Lab Instructions
generator: Typora
author: Brian Bird
---

<h1>Lab 1, Python and AI Warm-Up</h1>

<h2>Group B</h2>

**CS 210, Intro to AI Programming**



### 1. Translate a Program into Python

#### Simple Medical Diagnostic System

Design a simplified diagnostic system for a fictional clinic. The system should take two binary inputs (`True`/`False`): whether the patient has a *Fever* and whether the patient has a *Persistent Cough*. Based on the combination of these symptoms, the system provides a preliminary diagnosis.

| Fever | Persistent Cough | Diagnosis                                                    |
| ----- | ---------------- | ------------------------------------------------------------ |
| True  | True             | Flu - Recommend rest and hydration.                          |
| True  | False            | Possible Infection - Recommend primary care physician visit. |
| False | True             | Cold/Allergies - Recommend over-the-counter medication.      |
| False | False            | General Check-up - Patient appears healthy.                  |

Translate the program from either [JavaScript](medicalDiagnosis.js) or [C#](medicalDiagnosis.cs) into Python



### 2. Write a Python Program

#### Server Status and Priority Alert

Create a simplified system for monitoring a server cluster. The system uses a *Health Code* (1=Critical, 2=Warning, 3=Optimal) and the *Time Since Last Check* (in hours) to determine the required response priority.

| Health Code  | Time Since Last Check (H) | Alert Priority |
| ------------ | ------------------------- | -------------- |
| 1 (Critical) | Any                       | **HIGH**       |
| 2 (Warning)  | >4 Hours                  | **HIGH**       |
| 2 (Warning)  | ≤4 Hours                  | **MEDIUM**     |
| 3 (Optimal)  | >10 Hours                 | **LOW**        |
| 3 (Optimal)  | ≤10 Hours                 | **CLEAR**      |



## Submitting your lab work on Moodle

### Beta Version

- Post the beta version of both programs to your team channel in Discord.

### Code Review

- Review one of your lab partners' code and post the review in your team channel on Discord.
- Submit a copy of the code review <u>you did</u> on Moodle.

### Production Version

 Based on the code review and helpful advice from your lab partners, you may revise your code. On the code review from your lab partner, complete the “Prod.” column to show what you revised. Upload the following to the *Lab Production Version* assignment on Moodle:

1. The two Python (.py) files
3. The code review <u>from your lab partner</u> with the “Prod.” column filled out by you.

This will be a total of 3 files.

### Grading Criteria

The main focus of grading will be on correct coding and problem solving skills.

