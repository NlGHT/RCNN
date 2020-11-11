import csv

# name of csv file  
filename = "picturenamehere.csv" #TODO add picture name
    
# field names  
rois = 2 #TODO add number of ROIs
    
# data rows of csv file  
rows = [[0, 1, 255, 255],    
         [4, 2, 177, 180]] #TODO add ROIs

# writing to csv file  
with open(filename, 'w', newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(str(rois))  
        
    csvwriter.writerows(rows) 