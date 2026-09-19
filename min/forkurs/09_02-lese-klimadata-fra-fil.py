#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9.2 — Lese klimadata fra fil

Opphav   : min egen
Status   : PÅBEGYNT. Åpner og leser fila, ikke mer
Merk     : leser vaerdata.txt fra dag 2 — oppgaven ber om klima.txt fra techteach.no
Notat    : Master_brain/…/BTS4210-…/02_assignments/Forkurs-python-numpy/09.02-lese-klimadata-fra-fil.md

Created on Tue Sep  1 09:26:18 2026   (Spyder-stempel. @author er fjernet — det sto "mine"
                             på alle filer, også dem som er LEOs)
"""

import numpy as np

STI = "vaerdata.txt"

content = open(STI).read()
# print("  type :", type(content).__name__)

