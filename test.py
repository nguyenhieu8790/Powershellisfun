import json, csv
  
# reading the data from the file 
with open('file.tmp') as f: 
    data = f.read() 
  
      
logon_log = json.loads(data)   
with open('report-win.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
    for element in logon_log:
        w = csv.DictWriter(f, element.keys())
    #    w.writeheader()
        w.writerow(element)
