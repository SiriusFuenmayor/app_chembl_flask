Sample application for fetching the EMBL ChEMBL API
===================================================

Sample application showing the fetching, processing and visualisation of data from the ChEMBL API of the European Molecular Biology Laboratory (https://www.ebi.ac.uk/chembl/) using the Flask web framework and ChEMBL web service client (https://github.com/chembl/chembl_webresource_client). The D3.js JavaScript Library was used for creating the Heatmap for data visualization.

This application will extract all the pchembl_value's in the ChEMBL database relating the activity of a given molecule over a given target for targets and molecules of the following list:

List of targets: CHEMBL325, CHEMBL1937, CHEMBL1829, CHEMBL3524, CHEMBL2563, CHEMBL1865, CHEMBL2716, CHEMBL3192, CHEMBL4145, CHEMBL5103, CHEMBL3310

List of molecules: CHEMBL98, CHEMBL99, CHEMBL27759, CHEMBL2018302, CHEMBL483254, CHEMBL1213490, CHEMBL356769, CHEMBL272980, CHEMBL430060, CHEMBL1173445, CHEMBL356066, CHEMBL1914702

**Please look at the 'chembl_app_flask.py' and 'index.html' files which are commented showing the details of the data fetching and processing**

Installation
------------

Install Flask and ChEMBL web service client:

	pip3 install Flask
	pip3 install chembl_webresource_client

Then from a command line or terminal do the following:

	git clone https://github.com/SiriusFuenmayor/app_chembl_flask.git
	python3 chembl_app_flask.py

it will start the Flask server and the web page will be available on 

	http://localhost:3000



