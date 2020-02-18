from flask import Flask, render_template
from chembl_webresource_client.new_client import new_client
import json

app = Flask(__name__)

targets = ["CHEMBL325", "CHEMBL1937", "CHEMBL1829", "CHEMBL3524", "CHEMBL2563", "CHEMBL1865", "CHEMBL2716", "CHEMBL3192", "CHEMBL4145", "CHEMBL5103", "CHEMBL3310"]

molecules = ["CHEMBL98", "CHEMBL99", "CHEMBL27759", "CHEMBL2018302", "CHEMBL483254", "CHEMBL1213490", "CHEMBL356769", "CHEMBL272980", "CHEMBL430060", "CHEMBL1173445", "CHEMBL356066", "CHEMBL1914702"]

# In case we want to create a python dictio nary for passing the heatmap data as JSON
heatmap_data = []

@app.route("/")
def index():

  # We will obtain all the activity objects for every pair of 
  # compound and target in the above list and then take the 
  # average of their pChEMBL values then the data as a python
  # dictionary to be passed to the html template as JSON
  
  for target in targets:

    total_entries = 0
    avg_pchembl_value = 0
    pchembl_value_sum = 0

    for molecule in molecules:
      filtered_acts = new_client.activity.filter(molecule_chembl_id=molecule, target_chembl_id=target, pchembl_value__isnull=False)
      # then the pchembl_value of every activity object is extracted and the average of all is taken
      for act in filtered_acts:
        total_entries += 1
        pchembl_value_sum += float(act['pchembl_value'])
        #print("result: " + str(total_entries) + target + ', ' + molecule + ": " + str(act['pchembl_value'])) # DEBUG
      avg_pchembl_value = round(pchembl_value_sum / total_entries, 2)
      #print("average pchembl_value for " + target + ' and ' + molecule + " is: " + str(avg_pchembl_value)) #DEBUG

      data_row = {'group' : target, 'variable': molecule, 'value' : avg_pchembl_value}
      #data_row = {'target' : target, 'molecule': molecule, 'pchembl_value' : str(avg_pchembl_value)}

      print(data_row)
      # In case we use the data dictionary we append values here 
      heatmap_data.append(data_row)

  print(heatmap_data) # DEBUG
  
  # Finally we pass the data to our template, this data will pased as 
  # JSON and then parsed in the D3.js script to render the Heatmap
  return render_template('index.html', heatmap_data=heatmap_data) 

if __name__ == "__main__":
  app.run()

